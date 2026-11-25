# import pytest


# @pytest.fixture
# def program(request):
#     return request.param

# @pytest.mark.parametrize("program, result", [
#     ("anydesk", "anydesk start"),
#     ("virus",   "virus start"),
# ], indirect=["program"])
# def test_get_start_indirect(program, result):
#     assert get_start(program) == result

# def get_start(program: str):
#     return f'{program} start'

# @pytest.mark.smoke
# @pytest.mark.parametrize("program, result", [
#     pytest.param("anydesk", 'anydesk start', id='anydesk start'),
#     pytest.param("virus", 'virus start', id='virus start'),
#     pytest.param("browser", 'browser start', id='browser start'),
# ])
# def test_get_start(program, result):
#     assert get_start(program) == result
    

# @pytest.mark.skip(reason="not released")
# def test_program_name_start_qe():
#     assert get_start('program_name_qe') == False

# @pytest.mark.xfail(reason="BAG-019", strict=True)
# def test_program_name_start():
#     assert get_start('program_name') == False

# import pytest

# def validate_nickname(nickname: str) -> bool:
#     if not (3 <= len(nickname) <= 16):
#         return False
#     if not nickname[0].isalpha() or not nickname[0].isascii():
#         return False
#     for ch in nickname:
#         if not (ch.isalnum() or ch == "_"):
#             return False
#         if ch.isalpha() and not ch.isascii():
#             return False
#     return True

# import pytest

# @pytest.mark.parametrize("nickname, expected", [
#     # --- границы длины ---
#     pytest.param("ab", False, id="2 символа — ниже минимума"),
#     pytest.param("abc", True, id="3 символа — нижняя граница"),
#     pytest.param("abcd", True, id="4 символа — чуть выше нижней"),
#     pytest.param("a" * 15, True, id="15 символов — чуть ниже верхней"),
#     pytest.param("a" * 16, True, id="16 символов — верхняя граница"),
#     pytest.param("a" * 17, False, id="17 символов — выше максимума"),

#     # --- первый символ не буква ---
#     pytest.param("1ab", False, id="начинается с цифры"),
#     pytest.param("_ab", False, id="начинается с подчёркивания"),

#     # --- недопустимые символы ---
#     pytest.param("ab c", False, id="пробел"),
#     pytest.param("ab-c", False, id="дефис"),
#     pytest.param("ab.c", False, id="точка"),
#     pytest.param("$$$", False, id="символы"),

#     # --- не-ASCII ---
#     pytest.param("йван", False, id="кириллица — не ASCII"),

#     # --- пустое / None-подобное ---
#     pytest.param("", False, id="пустая строка"),

#     # --- позитив ---
#     pytest.param("abc", True, id="просто буквы"),
#     pytest.param("User_123", True, id="буквы + цифры + подчёркивание"),
# ])
# def test_validate_nickname(nickname, expected):
#     assert validate_nickname(nickname) == expected


# import pytest


# def divide(a: float, b: float) -> float:
#     if b == 0:
#         raise ZeroDivisionError("Cannot divide by zero")
#     return a / b

# @pytest.fixture
# def test_data():
#     data = [1.2, 3.1]
#     yield data
#     print("teardown!")

# @pytest.mark.parametrize("data, result", [
#     pytest.param([1.2, 3.1], 0.3870967741935484, id="test_data 1.2, 3.1"),
#     pytest.param([3, 3], 1, id="data 3, 3"),
# ])
# def test_divide_positive(data, result):
#     i, b = data
#     assert divide(i, b) == result

# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError) as err:
#         divide(2, 0)
#     assert "Cannot divide by zero" in str(err.value)

# import pytest
# import os

# @pytest.fixture
# def temp_file():
#     path = "test_data.txt"
#     with open(path, "w") as f:
#         f.write("test")
#     yield path          # отдаём тесту путь
#     os.remove(path)     # уборка после теста

# @pytest.mark.parametrize("num, result", [
#     pytest.param(7, False, id="7"),
#     pytest.param(8, True, id="8"),
#     pytest.param(20, True, id="20"),
#     pytest.param(21, False, id="21")
# ])
# def test_is_valid_password(num, result):
#     assert num == result
 

import httpx
import pytest


@pytest.mark.asyncio
async def test_timeout():
    async with httpx.AsyncClient() as client:
        with pytest.raises(httpx.TimeoutException):
            await client.get("https://httpbin.org/delay/2", timeout=1.0)

