def send_mail(message, recipient, sender = "university.help@gmail.com"):

    if ("@" and (".com" or ".ru" or ".net")) not in (recipient or sender) or ("@" or (".com" or ".ru" or ".net")) not in (recipient or sender):
        print(f'невозможно отправить письмо с адреса {sender} на адрес {recipient}')

    elif sender == recipient:
        print('Нельзя отправить письмо')

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")

send_mail('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_mail('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_mail('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_mail('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')