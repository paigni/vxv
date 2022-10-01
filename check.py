
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


def check_hero_hp(hero) -> bool:
    """
    Проверка жив ли герой
    Args:
        hero: текущий монстр
    Returns:
        Статус проверки
    """
    if hero.current_hp >= 0:
        return True
    return False


def check_max_count(count, team_list):
    if len(team_list) >= count:
        return True
    return False