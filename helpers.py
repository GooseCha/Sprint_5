import random as r


def generate_email():
    return str(r.randint(100, 999999999)) + "@mail.ru"
