from hero_class import Hero


def check_hero_choice(inp: str) -> bool:
    """
    Проверка корректности выбора пользователя
    Args:
        inp: ввод пользователя
    Returns:
        Статус проверки
    """
    if 1 <= int(inp) <= 6:
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
    if 1 <= int(inp) <= 3:
        return True
    return False