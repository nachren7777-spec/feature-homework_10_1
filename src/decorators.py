import logging
import sys
from functools import wraps
from time import time
from typing import Optional
from typing import Callable


def log(filename: Optional[str] = None):
    def decorator(func: Callable) -> Callable:
        logger = logging.getLogger(f"{func.__module__}.{func.__name__}")
        logger.setLevel(logging.INFO)

        # Очищаем старые handlers
        for handler in logger.handlers[:]:
            handler.close()
            logger.removeHandler(handler)

        # Добавляем новый handler
        if filename:
            handler = logging.FileHandler(filename, encoding='utf-8')
        else:
            handler = logging.StreamHandler(sys.stdout)  # ← явно в stdout

        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"Вызов функции {func.__name__} с аргументами args={args}, kwargs={kwargs}")
            start_time = time()

            try:
                result = func(*args, **kwargs)
                end_time = time()
                elapsed = end_time - start_time
                logger.info(f"Функция {func.__name__} ok. Результат: {result}. Время: {elapsed:.4f} сек")
                return result
            except Exception as e:
                end_time = time()
                elapsed = end_time - start_time
                logger.error(
                    f"Ошибка в функции {func.__name__}: {e}. "
                    f"Аргументы: args={args}, kwargs={kwargs}. "
                    f"Время до ошибки: {elapsed:.4f} сек"
                )
                raise

        return wrapper

    if callable(filename):
        func = filename
        filename = None
        return decorator(func)

    return decorator
