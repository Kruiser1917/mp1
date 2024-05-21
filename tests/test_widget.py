from src.widget import universal_masking, format_datetime_to_date

def test_format_datetime_to_date():
    assert format_datetime_to_date('2018-07-11T02:26:18.671407') == '11.07.2018'

def test_universal_masking():
    assert universal_masking('Visa Platinum 1234567812345678') == 'Visa Platinum 1234 56** **** 5678'
    assert universal_masking('Счет 12345678') == 'Счет **5678'