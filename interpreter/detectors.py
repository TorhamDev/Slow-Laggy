import re


def is_a_endif(token: str) -> bool:
    if "endif" == token[:5]:
        return True
    return False


def is_a_if(token: str) -> bool:
    if "if" == token[:2]:
        return True
    return False


def is_a_println(token: str) -> bool:
    if "println" == token[:7]:
        return True

    return False


def check_if_condition(if_token: str) -> bool:
    if is_a_if(if_token):
        condition = re.match(r"if.(.*):", if_token).group(1)
        result = eval(condition)
        return result
    return False
