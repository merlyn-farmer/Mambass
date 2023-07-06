import re


def user_command():
    command = input('Ожидаю команду...\n')

    pattern_skip = re.compile(r"skip", re.IGNORECASE).search(command)
    pattern_next = re.compile(r"next", re.IGNORECASE).search(command)
    pattern_re = re.compile(r"re", re.IGNORECASE).search(command)
    pattern_ky = re.compile(r"ку", re.IGNORECASE).search(command)
    pattern_exit = re.compile(r"exit", re.IGNORECASE).search(command)

