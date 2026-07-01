import pytest
import time
import re
from src.decorators import log


class TestLogDecorator:
    """Минимальный набор тестов для декоратора @log."""

    def test_log_to_console(self, capsys) -> None:
        """1. Логирование в консоль при успешном вызове."""

        @log
        def add(a: int, b: int) -> int:
            return a + b

        result = add(2, 3)
        assert result == 5

        captured = capsys.readouterr()

        assert "Вызов функции add" in captured.out
        assert "Функция add ok" in captured.out
        assert "Результат: 5" in captured.out

    def test_log_to_file(self, tmp_path) -> None:
        """2. Логирование в файл."""

        log_file = tmp_path / "test.log"

        @log(filename=str(log_file))
        def multiply(a: int, b: int) -> int:
            return a * b

        result = multiply(4, 5)
        assert result == 20

        content = log_file.read_text(encoding='utf-8')
        assert "Вызов функции multiply" in content
        assert "Результат: 20" in content

    def test_log_exception(self, capsys) -> None:
        """3. Логирование исключений."""

        @log
        def divide(a: int, b: int) -> float:
            return a / b

        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

        captured = capsys.readouterr()

        assert "Ошибка в функции divide" in captured.out
        assert "division by zero" in captured.out

    def test_preserves_metadata(self) -> None:
        """4. Декоратор сохраняет имя и докстринг функции."""

        @log
        def my_function() -> int:
            """Test docstring."""
            return 42

        assert my_function.__name__ == "my_function"
        assert my_function.__doc__ == "Test docstring."

    def test_timing_works(self, capsys) -> None:
        """5. Замер времени выполнения работает."""

        @log
        def slow_function() -> int:
            time.sleep(0.05)
            return 42

        slow_function()

        captured = capsys.readouterr()

        match = re.search(r"Время:\s*([\d.]+)\s*сек", captured.out)
        assert match is not None
        assert float(match.group(1)) >= 0.05
