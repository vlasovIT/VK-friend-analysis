from settings import *


def log_action(text):
    if SHOW_PROGRESS:
        print(text)


def log_user(text):
    if SHOW_PARSING_USER:
        print(text)
