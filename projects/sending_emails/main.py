import smtplib
import os


login = os.getenv('LOGIN')
password = os.getenv("PASSWORD")

mailing_text = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
'''

website_link = 'dvmn.org'
recipient_name = 'Такеши Ковач'
sender_name = 'Иван'
letterhead = '''From: devman.test@yandex.ru\nTo: devman.test@yandex.ru\nSubject: Invite\nContent-Type: text/plain; charset="UTF-8";\n\n
'''

mailing_message = (letterhead + mailing_text.replace('%website%', website_link).replace('%friend_name%', recipient_name).replace('%my_name%', sender_name)).encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail('devman.test@yandex.ru', 'devman.test@yandex.ru', mailing_message)
server.quit()
