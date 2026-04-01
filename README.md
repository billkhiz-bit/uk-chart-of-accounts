# uk-chart-of-accounts

Machine-readable UK Chart of Accounts for Python. 166 standard nominal codes with account types, VAT treatments, and HMRC box mappings.

## Install

```bash
pip install uk-chart-of-accounts
```

## Quick start

```python
from uk_coa import ChartOfAccounts, AccountType, VatRate

coa = ChartOfAccounts()

# Look up by code
account = coa.get(7602)
account.name          # "Accountancy Fees"
account.type          # AccountType.OVERHEAD
account.vat           # VatRate.STANDARD
account.vat_rate_pct  # 0.20
account.debit_increase  # True (expenses increase on debit side)

# Search
coa.search("insurance")           # All accounts with "insurance" in the name
coa.by_type(AccountType.INCOME)   # All income accounts
coa.by_vat(VatRate.EXEMPT)        # All VAT-exempt accounts
coa.by_tag("motor")               # All motor-related accounts
coa.code_range(7000, 7012)        # Payroll overheads

# Convenience
coa.expenses()                    # Direct expenses + overheads
coa.income_accounts()             # All income codes
coa.balance_sheet_accounts()      # Assets, liabilities, equity
coa.profit_and_loss_accounts()    # Income, expenses

# Export for LLM prompts
context = coa.to_prompt_context()
# or filter: coa.to_prompt_context(types=[AccountType.OVERHEAD])

# Export as dict (JSON-serialisable)
data = coa.to_dict()
```

## What's included

- **166 nominal codes** - the standard UK chart (Fixed Assets through Control accounts)
- **10 account types** - with double-entry rules (debit/credit increase direction)
- **VAT treatments** - Standard (20%), Reduced (5%), Zero-rated, Exempt, Outside Scope
- **HMRC box mappings** - CT600, VAT Return, FPS/RTI references where applicable
- **Tags** - searchable labels (motor, payroll, premises, insurance, etc.)
- **LLM export** - `to_prompt_context()` formats the chart for AI/LLM prompts
- **Zero dependencies** - pure Python, stdlib only

## Account types

| Type | Debit increases? | Statement |
|------|-----------------|-----------|
| Fixed Asset | Yes | Balance Sheet |
| Current Asset | Yes | Balance Sheet |
| Current Liability | No | Balance Sheet |
| Long-Term Liability | No | Balance Sheet |
| Equity | No | Balance Sheet |
| Income | No | Profit & Loss |
| Direct Expense | Yes | Profit & Loss |
| Overhead | Yes | Profit & Loss |
| Tax | Yes | Profit & Loss |
| Control | Yes | Balance Sheet |

## VAT treatments

| Treatment | Rate | Example codes |
|-----------|------|---------------|
| Standard | 20% | Most expenses, sales |
| Reduced | 5% | Domestic fuel/power |
| Zero-rated | 0% | Books, postage |
| Exempt | - | Insurance, bank charges, rent |
| Outside Scope | - | Wages, taxes, depreciation |

## Contributing

PRs welcome - particularly for:
- Additional HMRC box mappings
- VAT treatment corrections
- Industry-specific code extensions

## Licence

MIT
