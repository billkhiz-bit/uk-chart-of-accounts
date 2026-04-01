"""
UK Chart of Accounts - nominal code data.

Written from scratch based on the standard UK nominal code structure
used by Sage, Xero, FreeAgent, and other UK accounting software.
This is publicly available reference data, not proprietary.

VAT treatments verified against HMRC guidance. HMRC box mappings
reference CT600, VAT Return, FPS/RTI, EPS, CIS, and P11D forms.
"""

from .enums import AccountType as T, VatRate as V
from .models import Account

# fmt: off
ACCOUNTS: tuple[Account, ...] = (

    # ── Fixed Assets (10-51) ─────────────────────────────────────────
    Account(10,   "Freehold Property",              T.FIXED_ASSET,  V.STANDARD,      tags=("property",),
            description="New commercial property (under 3 years) is standard rated. Older property is exempt unless the seller has opted to tax. Residential property is exempt."),
    Account(11,   "Leasehold Property",             T.FIXED_ASSET,  V.STANDARD,      tags=("property",),
            description="Commercial lease premiums are standard rated. Residential leases are exempt. The grant of a new commercial lease is a standard-rated supply."),
    Account(20,   "Plant and Machinery",            T.FIXED_ASSET,  V.STANDARD,      tags=("capital",)),
    Account(21,   "Plant/Machinery Depreciation",   T.FIXED_ASSET,  V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",)),
    Account(30,   "Office Equipment",               T.FIXED_ASSET,  V.STANDARD,      tags=("capital",)),
    Account(31,   "Office Equipment Depreciation",  T.FIXED_ASSET,  V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",)),
    Account(40,   "Furniture and Fixtures",         T.FIXED_ASSET,  V.STANDARD,      tags=("capital",)),
    Account(41,   "Furniture/Fixture Depreciation",  T.FIXED_ASSET,  V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",)),
    Account(50,   "Motor Vehicles",                 T.FIXED_ASSET,  V.STANDARD,      tags=("capital", "motor"),
            description="Company cars are a reportable benefit in kind on form P11D Section A-F."),
    Account(51,   "Motor Vehicles Depreciation",    T.FIXED_ASSET,  V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation", "motor")),

    # ── Current Assets (1001-1250) ───────────────────────────────────
    Account(1001, "Stock",                          T.CURRENT_ASSET, V.STANDARD),
    Account(1002, "Work in Progress",               T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1003, "Finished Goods",                 T.CURRENT_ASSET, V.STANDARD),
    Account(1004, "Raw Materials",                  T.CURRENT_ASSET, V.STANDARD),
    Account(1100, "Debtors Control Account",        T.CURRENT_ASSET, V.OUTSIDE_SCOPE, tags=("control",)),
    Account(1101, "Sundry Debtors",                 T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1102, "Other Debtors",                  T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1103, "Prepayments",                    T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1104, "Inter-company Debtors",          T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1105, "Provision for Credit Notes",     T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1106, "Provision for Doubtful Debts",   T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1200, "Bank Current Account",           T.CURRENT_ASSET, V.OUTSIDE_SCOPE, tags=("bank",)),
    Account(1210, "Bank Deposit Account",           T.CURRENT_ASSET, V.OUTSIDE_SCOPE, tags=("bank",)),
    Account(1220, "Euro Bank Account",              T.CURRENT_ASSET, V.OUTSIDE_SCOPE, tags=("bank",)),
    Account(1230, "Petty Cash",                     T.CURRENT_ASSET, V.OUTSIDE_SCOPE, tags=("cash",)),
    Account(1235, "Cash Register",                  T.CURRENT_ASSET, V.OUTSIDE_SCOPE, tags=("cash",)),
    Account(1240, "Company Credit Card",            T.CURRENT_ASSET, V.OUTSIDE_SCOPE),
    Account(1250, "Credit Card Receipts",           T.CURRENT_ASSET, V.OUTSIDE_SCOPE),

    # ── Current Liabilities (2100-2230) ──────────────────────────────
    Account(2100, "Creditors Control Account",      T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, tags=("control",)),
    Account(2101, "Sundry Creditors",               T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE),
    Account(2102, "Other Creditors",                T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE),
    Account(2109, "Accruals",                       T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE),
    Account(2110, "Corporation Tax",                T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 86", tags=("tax", "hmrc")),
    Account(2200, "Sales Tax Control Account",      T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="VAT Return Box 1", tags=("vat", "control")),
    Account(2201, "Purchase Tax Control Account",   T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="VAT Return Box 4", tags=("vat", "control")),
    Account(2202, "VAT Liability",                  T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="VAT Return Box 5", tags=("vat", "hmrc")),
    Account(2204, "Manual Adjustments",             T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE),
    Account(2210, "P.A.Y.E.",                       T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll", "hmrc")),
    Account(2211, "National Insurance",             T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll", "hmrc")),
    Account(2220, "Net Wages",                      T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(2230, "Pension Fund",                   T.CURRENT_LIABILITY, V.OUTSIDE_SCOPE, tags=("payroll",)),

    # ── Long-Term Liabilities (2300-2330) ────────────────────────────
    Account(2300, "Loans",                          T.LONG_TERM_LIABILITY, V.OUTSIDE_SCOPE),
    Account(2301, "Directors Loan Account (Director 1)", T.LONG_TERM_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 79", tags=("directors",)),
    Account(2302, "Directors Loan Account (Director 2)", T.LONG_TERM_LIABILITY, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 79", tags=("directors",)),
    Account(2310, "Hire Purchase",                  T.LONG_TERM_LIABILITY, V.OUTSIDE_SCOPE),
    Account(2330, "Mortgages",                      T.LONG_TERM_LIABILITY, V.OUTSIDE_SCOPE),

    # ── Equity (3000-3200) ───────────────────────────────────────────
    Account(3000, "Ordinary Shares",                T.EQUITY, V.OUTSIDE_SCOPE),
    Account(3010, "Preference Shares",              T.EQUITY, V.OUTSIDE_SCOPE),
    Account(3100, "Reserves",                       T.EQUITY, V.OUTSIDE_SCOPE),
    Account(3101, "Undistributed Reserves",         T.EQUITY, V.OUTSIDE_SCOPE),
    Account(3200, "Profit and Loss Account",        T.EQUITY, V.OUTSIDE_SCOPE),

    # ── Income (4000-4905) ───────────────────────────────────────────
    Account(4000, "Sales Type A",                   T.INCOME, V.STANDARD, hmrc_box="CT600 Box 42; VAT Return Box 1, Box 6", tags=("sales",)),
    Account(4001, "Sales Type B",                   T.INCOME, V.STANDARD, hmrc_box="CT600 Box 42; VAT Return Box 1, Box 6", tags=("sales",)),
    Account(4002, "Sales Type C",                   T.INCOME, V.STANDARD, hmrc_box="CT600 Box 42; VAT Return Box 1, Box 6", tags=("sales",)),
    Account(4009, "Discounts Allowed",              T.INCOME, V.OUTSIDE_SCOPE, tags=("sales",)),
    Account(4010, "Management Charges Receivable",  T.INCOME, V.STANDARD, hmrc_box="CT600 Box 42"),
    Account(4099, "Flat Rate - Benefit/Cost",       T.INCOME, V.OUTSIDE_SCOPE, tags=("vat",)),
    Account(4100, "Sales Type D",                   T.INCOME, V.STANDARD, hmrc_box="CT600 Box 42; VAT Return Box 1, Box 6", tags=("sales",)),
    Account(4101, "Sales Type E",                   T.INCOME, V.STANDARD, hmrc_box="CT600 Box 42; VAT Return Box 1, Box 6", tags=("sales",)),
    Account(4200, "Sales of Assets",                T.INCOME, V.STANDARD, tags=("capital",)),
    Account(4400, "Credit Charges (Late Payments)", T.INCOME, V.OUTSIDE_SCOPE,
            description="Statutory late payment interest under the Late Payment of Commercial Debts Act is compensatory damages, not a supply of finance. Outside the scope of VAT."),
    Account(4900, "Miscellaneous Income",           T.INCOME, V.STANDARD, hmrc_box="CT600 Box 43"),
    Account(4901, "Royalties Received",             T.INCOME, V.STANDARD, hmrc_box="CT600 Box 43"),
    Account(4902, "Commissions Received",           T.INCOME, V.STANDARD, hmrc_box="CT600 Box 43"),
    Account(4903, "Insurance Claims",               T.INCOME, V.OUTSIDE_SCOPE),
    Account(4904, "Rent Income",                    T.INCOME, V.EXEMPT,  hmrc_box="CT600 Box 43; SA105", tags=("property",),
            description="Residential rental income is exempt. Commercial rental income is standard rated (20%) if the landlord has opted to tax the property."),
    Account(4905, "Distribution and Carriage",      T.INCOME, V.STANDARD),

    # ── Direct Expenses (5000-6900) ──────────────────────────────────
    Account(5000, "Materials Purchased",            T.DIRECT_EXPENSE, V.STANDARD, hmrc_box="VAT Return Box 4, Box 7", tags=("purchases",)),
    Account(5001, "Materials Imported",             T.DIRECT_EXPENSE, V.STANDARD, hmrc_box="VAT Return Box 2, Box 4, Box 9", tags=("purchases",),
            description="EU acquisitions: VAT Return Box 2 (VAT due) and Box 9 (total value). Non-EU imports: postponed VAT accounting uses Box 1 and Box 4."),
    Account(5002, "Miscellaneous Purchases",        T.DIRECT_EXPENSE, V.STANDARD, hmrc_box="VAT Return Box 4, Box 7", tags=("purchases",)),
    Account(5003, "Packaging",                      T.DIRECT_EXPENSE, V.STANDARD, tags=("purchases",)),
    Account(5009, "Discounts Taken",                T.DIRECT_EXPENSE, V.OUTSIDE_SCOPE),
    Account(6000, "Productive Labour",              T.DIRECT_EXPENSE, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(6001, "Cost of Sales Labour",           T.DIRECT_EXPENSE, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(6002, "Sub-Contractors",                T.DIRECT_EXPENSE, V.STANDARD, hmrc_box="CIS Monthly Return", tags=("cis",),
            description="Construction industry subcontractors: domestic reverse charge applies since March 2021. Customer accounts for VAT on qualifying CIS supplies."),
    Account(6100, "Sales Commissions",              T.DIRECT_EXPENSE, V.STANDARD),
    Account(6200, "Sales Promotions",               T.DIRECT_EXPENSE, V.STANDARD, tags=("marketing",)),
    Account(6201, "Advertising",                    T.DIRECT_EXPENSE, V.STANDARD, tags=("marketing",)),
    Account(6202, "Gifts and Samples",              T.DIRECT_EXPENSE, V.STANDARD, tags=("marketing",)),
    Account(6203, "P.R. (Literature & Brochures)",  T.DIRECT_EXPENSE, V.STANDARD, tags=("marketing",)),
    Account(6900, "Miscellaneous Expenses",         T.DIRECT_EXPENSE, V.STANDARD),

    # ── Overheads (7000-8250) ────────────────────────────────────────
    # Payroll
    Account(7000, "Gross Wages",                    T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(7001, "Directors Salaries",             T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll", "directors")),
    Account(7002, "Directors Remuneration",         T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll", "directors")),
    Account(7003, "Staff Salaries",                 T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(7004, "Wages - Regular",                T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(7005, "Wages - Casual",                 T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll",)),
    Account(7006, "Employers N.I. (Non-Directors)", T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI; EPS", tags=("payroll",)),
    Account(7007, "Employers Pensions",             T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI", tags=("payroll", "pension")),
    Account(7008, "Recruitment Expenses",           T.OVERHEAD, V.STANDARD, tags=("payroll",)),
    Account(7009, "Adjustments",                    T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("payroll",)),
    Account(7010, "SSP Reclaimed",                  T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="EPS", tags=("payroll",)),
    Account(7011, "SMP Reclaimed",                  T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="EPS", tags=("payroll",)),
    Account(7012, "Employers N.I. (Directors)",     T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="FPS/RTI; EPS", tags=("payroll", "directors")),

    # Premises
    Account(7100, "Rent",                           T.OVERHEAD, V.EXEMPT,   tags=("premises",),
            description="Residential rent is exempt. Commercial rent on opted-in properties is standard rated (20%)."),
    Account(7102, "Water Rates",                    T.OVERHEAD, V.ZERO,     tags=("premises", "utilities")),
    Account(7103, "General Rates",                  T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("premises",)),
    Account(7104, "Premises Insurance",             T.OVERHEAD, V.EXEMPT,   tags=("premises", "insurance")),

    # Utilities
    Account(7200, "Electricity",                    T.OVERHEAD, V.STANDARD, tags=("utilities",),
            description="Business use is standard rated (20%). Domestic and charity use qualifies for the reduced rate (5%) with a supplier declaration."),
    Account(7201, "Gas",                            T.OVERHEAD, V.STANDARD, tags=("utilities",),
            description="Same VAT treatment as electricity. Business use at 20%, domestic/charity at 5% with supplier declaration."),
    Account(7202, "Oil",                            T.OVERHEAD, V.STANDARD, tags=("utilities",),
            description="Heating oil for business use is standard rated. Domestic/charity use qualifies for reduced rate (5%)."),
    Account(7203, "Other Heating Costs",            T.OVERHEAD, V.STANDARD, tags=("utilities",)),

    # Motor
    Account(7300, "Vehicle Fuel",                   T.OVERHEAD, V.STANDARD, tags=("motor",),
            description="Company car fuel is a reportable benefit in kind (P11D Section M)."),
    Account(7301, "Vehicle Repairs and Servicing",  T.OVERHEAD, V.STANDARD, tags=("motor",)),
    Account(7302, "Vehicle Licences",               T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("motor",)),
    Account(7303, "Vehicle Insurance",              T.OVERHEAD, V.EXEMPT,   tags=("motor", "insurance")),
    Account(7304, "Miscellaneous Motor Expenses",   T.OVERHEAD, V.STANDARD, tags=("motor",)),
    Account(7305, "Congestion Charges",             T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("motor",)),
    Account(7306, "Mileage Claims",                 T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("motor",),
            description="Mileage allowances are outside scope, but businesses can reclaim VAT on the fuel element using HMRC advisory fuel rates via a separate VAT-only journal."),

    # Travel & Entertainment
    Account(7400, "Travelling",                     T.OVERHEAD, V.STANDARD, tags=("travel",)),
    Account(7401, "Car Hire",                       T.OVERHEAD, V.STANDARD, tags=("travel",)),
    Account(7402, "Hotels",                         T.OVERHEAD, V.STANDARD, tags=("travel",)),
    Account(7403, "U.K. Entertainment",             T.OVERHEAD, V.STANDARD, hmrc_box="CT600 Box 46", tags=("entertainment",),
            description="VAT on business entertainment is blocked from input tax recovery (HMRC VAT Notice 700/65). Disallowable for corporation tax - must be added back on CT600."),
    Account(7404, "Overseas Entertainment",         T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("entertainment",),
            description="Disallowable for corporation tax - must be added back on CT600."),
    Account(7405, "Overseas Travelling",            T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("travel",)),
    Account(7406, "Subsistence",                    T.OVERHEAD, V.STANDARD, tags=("travel",)),

    # Office & Admin
    Account(7500, "Printing",                       T.OVERHEAD, V.STANDARD, tags=("admin",)),
    Account(7501, "Postage and Carriage",           T.OVERHEAD, V.EXEMPT,   tags=("admin",),
            description="Royal Mail universal service is VAT exempt. Private couriers (DHL, DPD, Hermes) are standard rated (20%). Default set to exempt as Royal Mail is most common; adjust per supplier."),
    Account(7502, "Office Stationery",              T.OVERHEAD, V.STANDARD, tags=("admin",)),
    Account(7503, "Books etc.",                     T.OVERHEAD, V.ZERO,     tags=("admin",)),
    Account(7550, "Telephone and Fax",              T.OVERHEAD, V.STANDARD, tags=("comms",)),
    Account(7551, "Internet Charges",               T.OVERHEAD, V.STANDARD, tags=("comms",)),
    Account(7552, "Computers & Software",           T.OVERHEAD, V.STANDARD, tags=("tech",)),
    Account(7553, "Mobile Charges",                 T.OVERHEAD, V.STANDARD, tags=("comms",)),

    # Professional Fees
    Account(7600, "Legal Fees",                     T.OVERHEAD, V.STANDARD, tags=("professional",)),
    Account(7601, "Audit Fees",                     T.OVERHEAD, V.STANDARD, tags=("professional",)),
    Account(7602, "Accountancy Fees",               T.OVERHEAD, V.STANDARD, tags=("professional",)),
    Account(7603, "Consultancy Fees",               T.OVERHEAD, V.STANDARD, tags=("professional",)),
    Account(7604, "Professional Fees",              T.OVERHEAD, V.STANDARD, tags=("professional",)),
    Account(7605, "Management Charges Payable",     T.OVERHEAD, V.STANDARD),
    Account(7606, "Software Subscriptions",         T.OVERHEAD, V.STANDARD, tags=("tech",)),

    # Equipment
    Account(7700, "Equipment Hire",                 T.OVERHEAD, V.STANDARD),
    Account(7701, "Office Machine Maintenance",     T.OVERHEAD, V.STANDARD),
    Account(7702, "Equipment Leasing",              T.OVERHEAD, V.STANDARD),
    Account(7703, "Leasing Costs",                  T.OVERHEAD, V.STANDARD),

    # Premises Maintenance
    Account(7800, "Repairs and Renewals",           T.OVERHEAD, V.STANDARD, tags=("premises",)),
    Account(7801, "Cleaning",                       T.OVERHEAD, V.STANDARD, tags=("premises",)),
    Account(7802, "Laundry",                        T.OVERHEAD, V.STANDARD),
    Account(7803, "Premises Expenses",              T.OVERHEAD, V.STANDARD, tags=("premises",)),

    # Finance Costs
    Account(7900, "Bank Interest Paid",             T.OVERHEAD, V.EXEMPT,   hmrc_box="CT600 Box 44", tags=("finance",)),
    Account(7901, "Bank Charges",                   T.OVERHEAD, V.EXEMPT,   tags=("finance",)),
    Account(7902, "Currency Charges",               T.OVERHEAD, V.EXEMPT,   tags=("finance",)),
    Account(7903, "Loan Interest Paid",             T.OVERHEAD, V.EXEMPT,   hmrc_box="CT600 Box 44", tags=("finance",)),
    Account(7904, "H.P. Interest",                  T.OVERHEAD, V.EXEMPT,   hmrc_box="CT600 Box 44", tags=("finance",)),
    Account(7905, "Credit Charges",                 T.OVERHEAD, V.EXEMPT,   tags=("finance",)),
    Account(7906, "Exchange Rate Variance",         T.OVERHEAD, V.OUTSIDE_SCOPE, tags=("finance",)),
    Account(7907, "Other Interest Charges",         T.OVERHEAD, V.EXEMPT,   hmrc_box="CT600 Box 44", tags=("finance",)),
    Account(7908, "Factoring Charges",              T.OVERHEAD, V.EXEMPT,   tags=("finance",)),

    # Depreciation
    Account(8000, "Depreciation",                   T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",),
            description="Disallowable for corporation tax. Must be added back on CT600 - capital allowances are claimed instead."),
    Account(8001, "Plant/Machinery Depreciation",   T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",)),
    Account(8002, "Furniture/Fitting Depreciation",  T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",)),
    Account(8003, "Vehicle Depreciation",           T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation", "motor")),
    Account(8004, "Office Equipment Depreciation",  T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 46", tags=("depreciation",)),

    # Other Overheads
    Account(8100, "Bad Debt Write Off",             T.OVERHEAD, V.OUTSIDE_SCOPE),
    Account(8102, "Bad Debt Provision",             T.OVERHEAD, V.OUTSIDE_SCOPE),
    Account(8200, "Donations",                      T.OVERHEAD, V.OUTSIDE_SCOPE, hmrc_box="CT600 Box 47", tags=("charity",),
            description="Qualifying charitable donations are eligible for corporation tax relief under CT600 Box 47."),
    Account(8201, "Subscriptions",                  T.OVERHEAD, V.STANDARD),
    Account(8202, "Clothing Costs",                 T.OVERHEAD, V.STANDARD),
    Account(8203, "Training Costs",                 T.OVERHEAD, V.STANDARD),
    Account(8204, "Insurance",                      T.OVERHEAD, V.EXEMPT,   tags=("insurance",)),
    Account(8205, "Refreshments",                   T.OVERHEAD, V.STANDARD),
    Account(8206, "Cash Register Discrepancies",    T.OVERHEAD, V.OUTSIDE_SCOPE),
    Account(8250, "Sundry Expenses",                T.OVERHEAD, V.STANDARD),

    # ── Tax & Control (9001-9999) ────────────────────────────────────
    Account(9001, "Taxation",                       T.TAX,     V.OUTSIDE_SCOPE, tags=("tax",)),
    Account(9998, "Suspense Account",               T.CONTROL, V.OUTSIDE_SCOPE, tags=("control",)),
    Account(9999, "Mispostings Account",            T.CONTROL, V.OUTSIDE_SCOPE, tags=("control",)),
)
# fmt: on
