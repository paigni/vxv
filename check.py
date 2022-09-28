from hero_class import Hero


def check_hero_choice(inp: int) -> bool:
    """
    Проверка корректности выбора пользователя
    Args:
        inp: ввод пользователя
    Returns:
        Статус проверки
    """
    if 1 >= inp >= 7:
        return True
    return False



def check_choice(inp: str) -> bool:
    """
    Проверка корректности выбора пользователя
    Args:
        inp: ввод пользователя
    Returns:
        Статус проверки
    """
    if 0 < int(inp) < 3:
        return True
    return False