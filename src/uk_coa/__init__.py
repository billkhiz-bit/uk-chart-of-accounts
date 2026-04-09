"""uk-chart-of-accounts - Machine-readable UK Chart of Accounts for Python.

Usage::

    from uk_coa import ChartOfAccounts, AccountType, VatRate

    coa = ChartOfAccounts()

    # Look up by code
    account = coa.get(7602)
    account.name          # "Accountancy Fees"
    account.vat           # VatRate.STANDARD
    account.vat_rate_pct  # 0.20

    # Search
    coa.search("insurance")   # All accounts with "insurance" in the name
    coa.by_tag("motor")       # All motor-related accounts
    coa.by_vat(VatRate.EXEMPT)  # All VAT-exempt accounts

    # Export for LLM prompts
    context = coa.to_prompt_context()
"""

__version__ = "0.1.2"

from .chart import ChartOfAccounts
from .enums import AccountType, FinancialStatement, VatRate
from .models import Account

__all__ = [
    "ChartOfAccounts",
    "Account",
    "AccountType",
    "VatRate",
    "FinancialStatement",
]
