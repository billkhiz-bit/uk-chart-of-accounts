"""Main ChartOfAccounts class - the public API."""

from typing import Optional

from . import __version__
from .data import ACCOUNTS
from .enums import AccountType, VatRate
from .models import Account


class ChartOfAccounts:
    """UK Chart of Accounts - lookup, search, and export.

    Usage::

        from uk_coa import ChartOfAccounts

        coa = ChartOfAccounts()
        account = coa.get(7602)
        account.name       # "Accountancy Fees"
        account.vat        # VatRate.STANDARD
        account.vat_rate_pct  # 0.20
    """

    def __init__(self) -> None:
        self._by_code: dict[int, Account] = {a.code: a for a in ACCOUNTS}
        self._by_name: dict[str, Account] = {a.name.lower(): a for a in ACCOUNTS}

    def __len__(self) -> int:
        return len(self._by_code)

    def __iter__(self):
        return iter(sorted(self._by_code.values(), key=lambda a: a.code))

    def get(self, code: int) -> Optional[Account]:
        """Look up an account by nominal code. Returns None if not found."""
        return self._by_code.get(code)

    def get_by_name(self, name: str) -> Optional[Account]:
        """Look up an account by exact name (case-insensitive)."""
        return self._by_name.get(name.lower())

    def search(self, query: str) -> list[Account]:
        """Search accounts by partial name match (case-insensitive)."""
        q = query.lower()
        return sorted(
            [a for a in ACCOUNTS if q in a.name.lower()],
            key=lambda a: a.code,
        )

    def by_type(self, account_type: AccountType) -> list[Account]:
        """Get all accounts of a given type."""
        return sorted(
            [a for a in ACCOUNTS if a.type == account_type],
            key=lambda a: a.code,
        )

    def by_vat(self, vat: VatRate) -> list[Account]:
        """Get all accounts with a specific VAT treatment."""
        return sorted(
            [a for a in ACCOUNTS if a.vat == vat],
            key=lambda a: a.code,
        )

    def by_tag(self, tag: str) -> list[Account]:
        """Get all accounts with a specific tag."""
        return sorted(
            [a for a in ACCOUNTS if tag in a.tags],
            key=lambda a: a.code,
        )

    def code_range(self, start: int, end: int) -> list[Account]:
        """Get all accounts within a code range (inclusive)."""
        return sorted(
            [a for a in ACCOUNTS if start <= a.code <= end],
            key=lambda a: a.code,
        )

    def expenses(self) -> list[Account]:
        """All expense accounts (direct expenses + overheads)."""
        return self.by_type(AccountType.DIRECT_EXPENSE) + self.by_type(AccountType.OVERHEAD)

    def income_accounts(self) -> list[Account]:
        """All income accounts."""
        return self.by_type(AccountType.INCOME)

    def balance_sheet_accounts(self) -> list[Account]:
        """All accounts that appear on the balance sheet."""
        return sorted(
            [a for a in ACCOUNTS if a.is_balance_sheet],
            key=lambda a: a.code,
        )

    def profit_and_loss_accounts(self) -> list[Account]:
        """All accounts that appear on the profit and loss."""
        return sorted(
            [a for a in ACCOUNTS if a.is_profit_and_loss],
            key=lambda a: a.code,
        )

    def to_prompt_context(self, types: Optional[list[AccountType]] = None) -> str:
        """Export the chart as formatted text for LLM prompts.

        Args:
            types: Optional filter - only include these account types.
                   Defaults to all types.

        Returns:
            A formatted string listing codes, names, and types.
        """
        accounts = list(self) if types is None else [
            a for a in self if a.type in types
        ]
        lines = ["UK Chart of Accounts", "=" * 40, ""]
        current_type = None
        for a in accounts:
            if a.type != current_type:
                current_type = a.type
                lines.append(f"\n## {current_type.value.replace('_', ' ').title()}")
            vat_str = f" [{a.vat.value}]" if a.vat != VatRate.NOT_SET else ""
            lines.append(f"  {a.code}: {a.name}{vat_str}")
        return "\n".join(lines)

    def to_dict(self) -> dict:
        """Export full chart as a dictionary (for JSON serialisation)."""
        return {
            "version": __version__,
            "description": "UK Chart of Accounts - standard nominal codes",
            "accounts": {
                str(a.code): {
                    "name": a.name,
                    "type": a.type.value,
                    "vat": a.vat.value,
                    "hmrc_box": a.hmrc_box,
                    "tags": list(a.tags),
                }
                for a in self
            },
        }
