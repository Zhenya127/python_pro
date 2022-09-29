import numpy as np


predict_number = np.random.randint(1, 100) # Загаданное число


def compare(predict_number: int, compare_number: int) -> bool:
    """Сравнение числа с искомым

    Args:
        predict_number (int): загаданное число
        compare_number (int): сравниваемое число

    Returns:
        bool: True -- загаданное число меньше, False -- загаданное число больше
    """
    return predict_number < compare_number


def score_game(compare) -> int:
    """Поиск загаданного числа

    Args:
        compare ([type]): функция сравнения

    Returns:
        int: угаданное число
    """
    compare_number = 50
    attempt_amount = 0
    delta_size = 50
    while predict_number != compare_number:
        attempt_amount += 1
        compare_type = compare(predict_number, compare_number)
        delta_size = delta_size // 2 + delta_size % 2
        if compare_type == True:
            compare_number = compare_number - delta_size
        else:
            compare_number = compare_number + delta_size
    print(f"Загаданное число {predict_number}")
    print(f"Алгоритм угадал число {compare_number} за:{attempt_amount} попыток")
    return


if __name__ == "__main__":
    # RUN
    score_game(compare) 