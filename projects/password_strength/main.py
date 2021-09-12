import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)


def doesnt_consist_of_symbols(password):
    return not all(not symbol.isdigit() and not symbol.isalpha() for symbol in password)


def show_the_rating(rating_forming_functions, edit, password):
    rating_points = 0
    for function in rating_forming_functions:
        if function(password):
            rating_points += 2
    reply.set_text("Рейтинг этого пароля: %s" % rating_points)


if __name__ == '__main__':
    rating_forming_functions = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
        doesnt_consist_of_symbols,
    ]
    ask = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', show_the_rating, user_args=[rating_forming_functions])
    urwid.MainLoop(menu).run()
