import random
from faker import Faker
import file_operations


last_form = 10
first_form = 1
min_level_of_character = 8
max_level_of_character = 14
total_character_skills = 3
charsheet_path = 'charsheet.svg'
fake = Faker("ru_RU")
runic_skills = []
skills = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]
letters_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '  
}

for skill in skills:
    runic_word = ''
    for letter in skill:
        runic_word += letters_mapping[letter]
    runic_skills.append(runic_word)

for number_of_form in range(first_form, last_form + 1):
    random_skills = random.sample(runic_skills, total_character_skills)
    male_name = (fake.first_name_male(), fake.last_name_male())
    female_name = (fake.first_name_female(), fake.last_name_female())
    character_first_name, character_last_name = random.choice((male_name, female_name))           
    context = {
        'first_name': character_first_name,
        'last_name': character_last_name,
        'job': fake.job(),
        'town': fake.city(),
        'strength': random.randint(min_level_of_character, max_level_of_character),
        'agility': random.randint(min_level_of_character, max_level_of_character),
        'endurance': random.randint(min_level_of_character, max_level_of_character),
        'intelligence': random.randint(min_level_of_character, max_level_of_character),
        'luck': random.randint(min_level_of_character, max_level_of_character),
        'skill_1': random_skills[0],
        'skill_2': random_skills[1],
        'skill_3': random_skills[2]
    }
    file_operations.render_template(charsheet_path, 'new_charsheets/new_charsheet_{}.svg'.format(number_of_form), context)
