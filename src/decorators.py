import functools
import logging
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функций и их результатов.

    Args:
        filename (Optional[str]): Имя файла для логов. Если не задано, логи выводятся в консоль.

    Returns:
        Callable: Декорированная функция.
    """
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO)
    else:
        logging.basicConfig(level=logging.INFO)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                logging.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logging.error(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator
