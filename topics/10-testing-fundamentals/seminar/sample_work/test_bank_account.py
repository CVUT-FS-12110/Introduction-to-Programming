"""Testy stavu objektu s použitím fixture."""

import pytest

from bank_account import BankAccount


@pytest.fixture
def funded_account():
    """Každý test dostane nový účet se zůstatkem 100."""
    return BankAccount("Alice", balance=100)


def test_deposit_increases_balance(funded_account):
    funded_account.deposit(50)
    assert funded_account.balance == 150


def test_withdraw_decreases_balance(funded_account):
    funded_account.withdraw(30)
    assert funded_account.balance == 70


def test_withdraw_entire_balance_leaves_zero(funded_account):
    funded_account.withdraw(100)
    assert funded_account.balance == 0


def test_withdraw_more_than_balance_raises(funded_account):
    with pytest.raises(ValueError, match="insufficient"):
        funded_account.withdraw(100.01)
    assert funded_account.balance == 100  # stav se po chybě nezměnil
