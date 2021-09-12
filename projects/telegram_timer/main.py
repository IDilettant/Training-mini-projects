import os
import ptbot
from pytimeparse import parse


TOKEN = os.getenv('TOKEN')
CHAT_ID = '1359737821'


def reply(text):
    total_secs = parse(text)
    message_id = bot.send_message(CHAT_ID, 'Таймер запущен на {} секунд'.format(total_secs))
    bot.create_countdown(total_secs, notify_progress, message_id=message_id, total_secs=total_secs)
    bot.create_timer(total_secs, notify)


def notify():
    bot.send_message(CHAT_ID, 'Время вышло')


def notify_progress(secs_left, message_id, total_secs):
    bot.update_message(CHAT_ID, message_id, "Осталось секунд: {}\n{}".format(secs_left, render_progressbar(total_secs, secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    bot = ptbot.Bot(TOKEN)
    bot.send_message(CHAT_ID, 'На сколько запустить таймер?')
    bot.reply_on_message(reply) 
    bot.run_bot()
