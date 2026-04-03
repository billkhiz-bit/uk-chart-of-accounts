"""Tests for uk-chart-of-accounts."""

import json

from uk_coa import AccountType, ChartOfAccounts, VatRate
from uk_coa import __version__


class TestChartOfAccounts:
    """Core functionality tests."""

    def setup_method(self):
        self.coa = ChartOfAccounts()

    def test_total_accounts(self):
        """Should have 166 nominal codes."""
        assert len(self.coa) == 166

    def test_get_by_code(self):
        account = self.coa.get(7602)
        assert account is not None
        assert account.name == "Accountancy Fees"
        assert account.type == AccountType.OVERHEAD

    def test_get_unknown_code_returns_none(self):
        assert self.coa.get(99999) is None

    def test_get_by_name(self):
        account = self.coa.get_by_name("Accountancy Fees")
        assert account is not None
        assert account.code == 7602

    def test_get_by_name_case_insensitive(self):
        account = self.coa.get_by_name("accountancy fees")
        assert account is not None
        assert account.code == 7602

    def test_search(self):
        results = self.coa.search("insurance")
        assert len(results) >= 3  # Premises, Vehicle, general Insurance
        assert all("insurance" in a.name.lower() for a in results)

    def test_search_empty(self):
        results = self.coa.search("xyznonexistent")
        assert results == []

    def test_by_type(self):
        fixed = self.coa.by_type(AccountType.FIXED_ASSET)
        assert len(fixed) == 10
        assert all(a.type == AccountType.FIXED_ASSET for a in fixed)

    def test_by_vat(self):
        exempt = self.coa.by_vat(VatRate.EXEMPT)
        assert len(exempt) > 0
        assert all(a.vat == VatRate.EXEMPT for a in exempt)

    def test_by_tag(self):
        motor = self.coa.by_tag("motor")
        assert len(motor) >= 2
        assert all("motor" in a.tags for a in motor)

    def test_code_range(self):
        overheads = self.coa.code_range(7000, 7012)
        assert all(7000 <= a.code <= 7012 for a in overheads)
        assert len(overheads) == 13  # 7000-7012 inclusive

    def test_expenses(self):
        expenses = self.coa.expenses()
        assert all(
            a.type in (AccountType.DIRECT_EXPENSE, AccountType.OVERHEAD)
            for a in expenses
        )

    def test_income_accounts(self):
        income = self.coa.income_accounts()
        assert all(a.type == AccountType.INCOME for a in income)

    def test_balance_sheet_vs_pnl_no_overlap(self):
        bs = set(a.code for a in self.coa.balance_sheet_accounts())
        pnl = set(a.code for a in self.coa.profit_and_loss_accounts())
        assert bs.isdisjoint(pnl), "No account should appear on both statements"

    def test_all_accounts_on_a_statement(self):
        bs = self.coa.balance_sheet_accounts()
        pnl = self.coa.profit_and_loss_accounts()
        assert len(bs) + len(pnl) == len(self.coa)

    def test_iterator_sorted_by_code(self):
        codes = [a.code for a in self.coa]
        assert codes == sorted(codes)

    def test_descriptions_coverage(self):
        """At least 50% of accounts should have descriptions."""
        with_desc = sum(1 for a in self.coa if a.description is not None)
        assert with_desc >= 83, f"Only {with_desc}/166 accounts have descriptions"


class TestAccountModel:
    """Test the Account dataclass properties."""

    def setup_method(self):
        self.coa = ChartOfAccounts()

    def test_debit_increase_for_assets(self):
        bank = self.coa.get(1200)
        assert bank.debit_increase is True

    def test_credit_increase_for_liabilities(self):
        creditors = self.coa.get(2100)
        assert creditors.debit_increase is False

    def test_credit_increase_for_income(self):
        sales = self.coa.get(4000)
        assert sales.debit_increase is False

    def test_debit_increase_for_expenses(self):
        rent = self.coa.get(7100)
        assert rent.debit_increase is True

    def test_vat_rate_pct_standard(self):
        stationery = self.coa.get(7502)
        assert stationery.vat == VatRate.STANDARD
        assert stationery.vat_rate_pct == 0.20

    def test_vat_rate_pct_exempt(self):
        insurance = self.coa.get(8204)
        assert insurance.vat == VatRate.EXEMPT
        assert insurance.vat_rate_pct is None

    def test_vat_rate_pct_outside_scope(self):
        wages = self.coa.get(7003)
        assert wages.vat == VatRate.OUTSIDE_SCOPE
        assert wages.vat_rate_pct is None

    def test_hmrc_box_set(self):
        corp_tax = self.coa.get(2110)
        assert corp_tax.hmrc_box == "CT600 Box 86"

    def test_hmrc_box_not_set(self):
        stationery = self.coa.get(7502)
        assert stationery.hmrc_box is None

    def test_frozen(self):
        account = self.coa.get(7602)
        try:
            account.name = "Something else"
            assert False, "Should not be able to mutate frozen dataclass"
        except AttributeError:
            pass


class TestExport:
    """Test export functionality."""

    def setup_method(self):
        self.coa = ChartOfAccounts()

    def test_to_prompt_context_returns_string(self):
        context = self.coa.to_prompt_context()
        assert isinstance(context, str)
        assert "UK Chart of Accounts" in context
        assert "7602" in context

    def test_to_prompt_context_filtered(self):
        context = self.coa.to_prompt_context(types=[AccountType.INCOME])
        assert "4000" in context
        assert "7602" not in context  # Overhead, should be excluded

    def test_to_dict_serialisable(self):
        d = self.coa.to_dict()
        json_str = json.dumps(d)  # Should not raise
        assert '"7602"' in json_str

    def test_to_dict_structure(self):
        d = self.coa.to_dict()
        assert d["version"] == __version__
        assert "accounts" in d
        assert "7602" in d["accounts"]
        assert d["accounts"]["7602"]["name"] == "Accountancy Fees"
