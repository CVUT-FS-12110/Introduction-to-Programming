"""Bankovní účet — objekt se stavem (převzato z výkladového notebooku)."""


class BankAccount:
    """A bank account with deposits and withdrawals."""

    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("initial balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """Add amount to the balance. Raises ValueError if amount is not positive."""
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Remove amount from the balance.

        Raises ValueError if amount is not positive or exceeds the balance.
        """
        if amount <= 0:
            raise ValueError("withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
