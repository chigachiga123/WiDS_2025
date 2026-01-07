import pandas as pd

# ---------- CompanyFinancials Class ----------
class CompanyFinancials:
    def __init__(self, row):
        self.r = row

    def ebitda_margin(self):
        return self.r.EBITDA / self.r.Revenue

    def pat_margin(self):
        return self.r.PAT / self.r.Revenue

    def gross_profit_margin(self):
        return self.r["Gross Profit"] / self.r.Revenue

    def roe(self):
        return self.r.PAT / self.r.Equity

    def roa(self):
        return self.r.PAT / self.r["Total Assets"]

    def roce(self):
        return self.r.EBIT / (self.r.Equity + self.r.Debt)

    def debt_equity(self):
        return self.r.Debt / self.r.Equity

    def interest_coverage(self):
        return self.r.EBIT / self.r.Interest

    def fixed_asset_turnover(self):
        return self.r.Revenue / self.r["Fixed Assets"]

    def total_asset_turnover(self):
        return self.r.Revenue / self.r["Total Assets"]

    def inventory_turnover(self):
        return self.r.Revenue / self.r.Inventory

    def inventory_days(self):
        return 365 / self.inventory_turnover()

    def receivables_turnover(self):
        return self.r.Revenue / self.r.Receivables

    def dso(self):
        return 365 / self.receivables_turnover()

    def pe_ratio(self):
        return self.r["Market Price"] / self.r.EPS

    def book_value_per_share(self):
        return self.r.Equity / self.r.Shares

    def pb_ratio(self):
        return self.r["Market Price"] / self.book_value_per_share()

    def ps_ratio(self):
        return self.r["Market Price"] / (self.r.Revenue / self.r.Shares)


# ---------- Read Input ----------
df = pd.read_excel("company_input.xlsx", sheet_name="Financials")

results = []

for _, row in df.iterrows():
    c = CompanyFinancials(row)

    results.append({
        "Year": row.Year,
        "EBITDA Margin": c.ebitda_margin(),
        "PAT Margin": c.pat_margin(),
        "Gross Profit Margin": c.gross_profit_margin(),
        "ROE": c.roe(),
        "ROA": c.roa(),
        "ROCE": c.roce(),
        "Debt/Equity": c.debt_equity(),
        "Interest Coverage": c.interest_coverage(),
        "Fixed Asset Turnover": c.fixed_asset_turnover(),
        "Total Asset Turnover": c.total_asset_turnover(),
        "Inventory Turnover": c.inventory_turnover(),
        "Inventory Days": c.inventory_days(),
        "Receivables Turnover": c.receivables_turnover(),
        "DSO": c.dso(),
        "P/E Ratio": c.pe_ratio(),
        "P/B Ratio": c.pb_ratio(),
        "P/S Ratio": c.ps_ratio(),
        "EPS": row.EPS,
        "Book Value / Share": c.book_value_per_share()
    })

# ---------- Export to Excel ----------
output = pd.DataFrame(results)
output.to_excel("company_valuations_output.xlsx", index=False)

print("Good work soldier")
