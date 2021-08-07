import pytest
import time

from src.Account import Account


@pytest.fixture()
def account():
    return Account("Eva", 500)


def test_account_create(account):
    assert account.balance == 500
