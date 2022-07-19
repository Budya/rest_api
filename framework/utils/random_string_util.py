import random
from framework.config import Config


def randstring(length=Config.RANDOM_STRING_UTIL_LENGTH.value):
    random_string_chars = Config.RANDOM_STRING_UTIL_LINE.value
    return ''.join((random.choice(random_string_chars) for i in range(length)))
