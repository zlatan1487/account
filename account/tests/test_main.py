from account import main


def test_up_first():
    assert main.up_first('skypro') == 'Skypro'


def test_up_first_for_empty():
    assert main.up_first('') == ''