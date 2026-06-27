from sfos.account import Account, Ownership
from sfos.enums import AccountType
from sfos.institution import Institution


def test_create_account():
    chase = Institution(name="Chase")

    account = Account(
        institution=chase,
        account_type=AccountType.CREDIT_CARD,
        official_name="Marriott Bonvoy Visa",
        nickname="Marriott Card",
        ownership=Ownership.JOINT,
    )

    assert account.nickname == "Marriott Card"
    assert account.ownership == Ownership.JOINT
    assert account.balance == 0.0