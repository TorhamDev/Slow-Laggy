
def is_a_println(token: str) -> bool:
    if "println" == token[:7]:
        return True

    return False
