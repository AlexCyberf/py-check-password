from app.main import check_password


def test_password_has_less_than_8_characters() -> None:
    assert check_password("A5@bc") == False


def test_password_has_more_than_16_characters() -> None:
    assert check_password("A5@bcdefghijklmnop") == False


def test_password_has_no_uppercase() -> None:
    assert check_password("abc5_efgh") == False


def test_password_has_no_digit() -> None:
    assert check_password("Alexcyberf@") == False


def test_password_has_no_special_symbol() -> None:
    assert check_password("Alexcyberf5") == False


def test_password_has_all_needed_rules() -> None:
    assert check_password("Abcdefg5!") == True
