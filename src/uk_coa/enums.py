"""Enumerations for UK Chart of Accounts."""

from enum import Enum


class AccountType(str, Enum):
    """Standard UK nominal account types."""

    FIXED_ASSET = "fixed_asset"
    CURRENT_ASSET = "current_asset"
    CURRENT_LIABILITY = "current_liability"
    LONG_TERM_LIABILITY = "long_term_liability"
    EQUITY = "equity"
    INCOME = "income"
    DIRECT_EXPENSE = "direct_expense"
    OVERHEAD = "overhead"
    TAX = "tax"
    CONTROL = "control"


class VatRate(str, Enum):
    """UK VAT treatment codes."""

    STANDARD = "standard"          # 20%
    REDUCED = "reduced"            # 5%
    ZERO = "zero"                  # 0% (zero-rated, still VAT-registered)
    EXEMPT = "exempt"              # Outside VAT system (insurance, finance)
    OUTSIDE_SCOPE = "outside_scope"  # Not a VAT supply (wages, taxes, dividends)
    MIXED = "mixed"                # Depends on context (e.g. food can be standard or zero)
    NOT_SET = "not_set"            # Awaiting classification


class FinancialStatement(str, Enum):
    """Which financial statement this account appears on."""

    BALANCE_SHEET = "balance_sheet"
    PROFIT_AND_LOSS = "profit_and_loss"
