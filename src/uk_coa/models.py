"""Data models for UK Chart of Accounts."""

from dataclasses import dataclass, field
from typing import Optional

from .enums import AccountType, FinancialStatement, VatRate


# Standard double-entry rules per account type.
# debit_increase: True means debits increase the balance (assets, expenses).
# False means credits increase the balance (liabilities, equity, income).
ACCOUNT_TYPE_RULES: dict[AccountType, dict] = {
    AccountType.FIXED_ASSET:        {"debit_increase": True,  "statement": FinancialStatement.BALANCE_SHEET},
    AccountType.CURRENT_ASSET:      {"debit_increase": True,  "statement": FinancialStatement.BALANCE_SHEET},
    AccountType.CURRENT_LIABILITY:  {"debit_increase": False, "statement": FinancialStatement.BALANCE_SHEET},
    AccountType.LONG_TERM_LIABILITY:{"debit_increase": False, "statement": FinancialStatement.BALANCE_SHEET},
    AccountType.EQUITY:             {"debit_increase": False, "statement": FinancialStatement.BALANCE_SHEET},
    AccountType.INCOME:             {"debit_increase": False, "statement": FinancialStatement.PROFIT_AND_LOSS},
    AccountType.DIRECT_EXPENSE:     {"debit_increase": True,  "statement": FinancialStatement.PROFIT_AND_LOSS},
    AccountType.OVERHEAD:           {"debit_increase": True,  "statement": FinancialStatement.PROFIT_AND_LOSS},
    AccountType.TAX:                {"debit_increase": True,  "statement": FinancialStatement.PROFIT_AND_LOSS},
    AccountType.CONTROL:            {"debit_increase": True,  "statement": FinancialStatement.BALANCE_SHEET},
}


@dataclass(frozen=True)
class Account:
    """A single nominal account in the UK Chart of Accounts."""

    code: int
    name: str
    type: AccountType
    vat: VatRate = VatRate.NOT_SET
    hmrc_box: Optional[str] = None
    description: Optional[str] = None
    tags: tuple[str, ...] = field(default_factory=tuple)

    @property
    def debit_increase(self) -> bool:
        """Whether debits increase this account's balance."""
        return ACCOUNT_TYPE_RULES[self.type]["debit_increase"]

    @property
    def statement(self) -> FinancialStatement:
        """Which financial statement this account appears on."""
        return ACCOUNT_TYPE_RULES[self.type]["statement"]

    @property
    def is_balance_sheet(self) -> bool:
        return self.statement == FinancialStatement.BALANCE_SHEET

    @property
    def is_profit_and_loss(self) -> bool:
        return self.statement == FinancialStatement.PROFIT_AND_LOSS

    @property
    def vat_rate_pct(self) -> Optional[float]:
        """Numeric VAT rate, or None if not applicable."""
        return {
            VatRate.STANDARD: 0.20,
            VatRate.REDUCED: 0.05,
            VatRate.ZERO: 0.0,
        }.get(self.vat)
