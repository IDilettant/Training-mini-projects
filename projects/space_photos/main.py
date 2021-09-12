import os
from urllib.parse import urlparse, urlunparse

import requests


def get_response(url, payload=None):
    try:
        response = requests.get(url, params=payload)
    except requests.exceptions.SSLError:
        response = requests.get(
            url,
            params=payload,
            verify=False,  # noqa: S501
        )
    response.raise_for_status()
    return response


def load_image(url, file_path):
    response = get_response(url)
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)
    with open(file_path, 'wb') as image:
        image.write(response.content)


def get_image_urls(launches):
    for launch in launches:
        image_urls = launch.get('links').get('flickr').get('original')
        if image_urls:
            return image_urls


def fetch_spacex_last_launch(directory):  # noqa: WPS210
    url = 'https://api.spacexdata.com/v4/launches'
    response = get_response(url)
    launches = sorted(
        response.json(),
        key=lambda flight: flight['flight_number'],
        reverse=True,
    )
    image_urls = get_image_urls(launches)
    for num, image_url in enumerate(image_urls):
        file_path = os.path.join(directory, 'spacex{0}.jpg'.format(num))
        load_image(image_url, file_path)


def get_file_extension(file_name):
    return file_name.split('.')[-1]


def fetch_hubble_photo(image_id, directory):
    url = 'https://hubblesite.org//api/v3/image/{0}'.format(image_id)
    response = get_response(url)
    image_file = response.json()['image_files'][-1]
    image_url = urlunparse(
        urlparse(  # noqa: WPS437
            image_file['file_url'],
        )._replace(scheme='https'),
    )
    file_path = os.path.join(
        directory,
        '{0}.{1}'.format(image_id, get_file_extension(image_url)),
    )
    load_image(image_url, file_path)


def fetch_hubble_gallery(collection_name, directory):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {'page': 'all', 'collection_name': collection_name}
    response = get_response(url, payload=payload)
    image_files = response.json()
    for image in image_files:
        fetch_hubble_photo(image['id'], directory)


def main():
    directory = '../images'
    fetch_spacex_last_launch(os.path.join(directory, 'spacex'))
    fetch_hubble_gallery(
        'stsci_gallery',
        os.path.join(directory, 'hubble'),
    )


if __name__ == '__main__':
    main()
