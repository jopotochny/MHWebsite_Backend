import re


def get_regex_count(string, str_pattern):
    return len(re.compile(str_pattern, re.IGNORECASE).findall(string))
