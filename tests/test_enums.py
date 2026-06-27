from sfos.enums import AccountType


def test_account_type():
    assert AccountType.CHECKING.value == "checking"