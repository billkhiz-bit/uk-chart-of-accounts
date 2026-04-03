# Contributing to uk-chart-of-accounts

Thanks for your interest in improving the UK Chart of Accounts! This library aims to be the most accurate, machine-readable UK nominal code reference on PyPI.

## Getting started

```bash
git clone https://github.com/billkhiz-bit/uk-chart-of-accounts.git
cd uk-chart-of-accounts
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]" 2>/dev/null || pip install -e .
pip install pytest
```

## Running tests

```bash
python -m pytest tests/ -v
```

All 30 tests must pass before submitting a PR.

## What we're looking for

**High priority:**
- HMRC box mapping corrections or additions (CT600, VAT Return, FPS/RTI, CIS, P11D)
- VAT treatment corrections (especially edge cases like opted-to-tax properties, reverse charge)
- Descriptions for accounts that lack them (148 of 166 accounts could use one)

**Welcome:**
- Industry-specific nominal code extensions (construction, medical, property)
- Additional tags for better searchability
- Documentation improvements

**Out of scope:**
- Non-UK charts of accounts (this library is specifically for UK/HMRC)
- Runtime dependencies (the library must remain zero-dependency, pure Python)

## How to add or correct accounts

All account data lives in `src/uk_coa/data.py`. Each account follows this structure:

```python
Account(
    code=7602,
    name="Accountancy Fees",
    type=AccountType.OVERHEAD,
    vat=VatRate.STANDARD,
    hmrc_box="CT600 Box 46",          # optional
    tags=("professional",),           # optional, for searchability
    description="Explanation of VAT treatment or HMRC rules.",  # optional
)
```

When adding or correcting VAT treatments, please cite the relevant HMRC guidance (e.g. VAT Notice 701/1, HMRC manual reference).

## Code style

- Pure Python, no external dependencies
- Type hints throughout
- British English in descriptions and documentation (colour, categorise, organisation)
- Run `pytest` before submitting

## Submitting a PR

1. Fork the repo and create a feature branch
2. Make your changes
3. Run `python -m pytest tests/ -v` and ensure all tests pass
4. If adding new accounts, add corresponding tests in `tests/test_chart.py`
5. Open a PR with a clear description of what changed and why

## Questions?

Open an issue on GitHub if anything is unclear.
