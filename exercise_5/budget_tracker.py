import calendar
from datetime import datetime
from collections import defaultdict

class BudgetTracker:
    def __init__(self):
        self.data = {}
        self.budget_limits = {}
    
    def _initialize_month(self, month_key):
        """Initialize data structure for a new month if it doesn't exist"""
        if month_key not in self.data:
            self.data[month_key] = {"income": {}, "expenses": {}}
    
    def add_transaction(self, date_str, category, amount, transaction_type):
        """Add an income or expense transaction"""
        try:
            date = datetime.strptime(date_str, "%Y-%m")
            month_key = date.strftime("%Y-%m")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM.")
            return False
        
        if transaction_type.lower() not in ["income", "expenses"]:
            print("Invalid transaction type. Use 'income' or 'expenses'.")
            return False
        
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Amount must be a positive number.")
            return False
        
        # Initialize month if it doesn't exist
        self._initialize_month(month_key)
        
        # Normalize transaction type
        trans_type = "expenses" if transaction_type.lower().startswith("expens") else "income"
        
        # Add the transaction
        if category in self.data[month_key][trans_type]:
            self.data[month_key][trans_type][category] += amount
        else:
            self.data[month_key][trans_type][category] = amount
        
        return True
    
    def set_budget_limit(self, category, limit):
        """Set monthly budget limit for a category"""
        if not isinstance(limit, (int, float)) or limit <= 0:
            print("Limit must be a positive number.")
            return False
        
        self.budget_limits[category] = limit
        return True
    
    def get_monthly_summary(self, month_key):
        """Generate summary for a specific month"""
        if month_key not in self.data:
            print(f"No data available for {month_key}")
            return None
        
        month_data = self.data[month_key]
        total_income = sum(month_data["income"].values())
        total_expenses = sum(month_data["expenses"].values())
        net_savings = total_income - total_expenses
        savings_percentage = (net_savings / total_income * 100) if total_income > 0 else 0
        
        # Format month name for display
        year, month = map(int, month_key.split('-'))
        month_name = calendar.month_name[month]
        
        summary = {
            "month": f"{month_name} {year}",
            "total_income": total_income,
            "total_expenses": total_expenses,
            "net_savings": net_savings,
            "savings_percentage": savings_percentage,
            "income_breakdown": month_data["income"],
            "expense_breakdown": month_data["expenses"]
        }
        
        return summary
    
    def display_summary(self, month_key):
        """Display formatted monthly summary"""
        summary = self.get_monthly_summary(month_key)
        if not summary:
            return
        
        print(f"=== PERSONAL BUDGET TRACKER ===")
        print(f"Month: {summary['month']}\n")
        print("💰 FINANCIAL SUMMARY")
        print(f"Total Income: ${summary['total_income']:,.2f}")
        print(f"Total Expenses: ${summary['total_expenses']:,.2f}")
        print(f"Net Savings: ${summary['net_savings']:,.2f} ({summary['savings_percentage']:.1f}%)\n")
        
        # Display budget warnings
        self._display_budget_warnings(month_key)
        
        # Display text charts
        self._display_income_chart(summary['income_breakdown'])
        self._display_expense_chart(summary['expense_breakdown'])
    
    def _display_budget_warnings(self, month_key):
        """Display budget limit warnings"""
        if month_key not in self.data or not self.budget_limits:
            return
        
        print("⚠️ BUDGET WARNINGS")
        warnings = []
        
        for category, spent in self.data[month_key]["expenses"].items():
            if category in self.budget_limits:
                limit = self.budget_limits[category]
                if spent > limit:
                    over_percent = (spent - limit) / limit * 100
                    warnings.append(
                        f"- {category}: ${spent:,.2f} spent (${limit:,.2f} limit, {over_percent:.1f}% over)"
                    )
        
        if warnings:
            print("\n".join(warnings))
        else:
            print("No budget limits exceeded.")
        print()
    
    def _display_income_chart(self, income_data):
        """Display income breakdown as text chart"""
        if not income_data:
            return
        
        print("📈 INCOME BREAKDOWN")
        total = sum(income_data.values())
        
        for category, amount in income_data.items():
            percentage = amount / total * 100
            bar = '█' * int(percentage / 5)  # Each █ represents 5%
            print(f"{category.title():<15} {bar} {percentage:.1f}% (${amount:,.2f})")
        print()
    
    def _display_expense_chart(self, expense_data):
        """Display expense breakdown as text chart"""
        if not expense_data:
            return
        
        print("📉 EXPENSE BREAKDOWN")
        total = sum(expense_data.values())
        
        for category, amount in expense_data.items():
            percentage = amount / total * 100
            bar = '█' * int(percentage / 5)  # Each █ represents 5%
            print(f"{category.title():<15} {bar} {percentage:.1f}% (${amount:,.2f})")
        print()
    
    def analyze_spending_trends(self, category, num_months=3):
        """Analyze spending trends for a category"""
        sorted_months = sorted(self.data.keys(), reverse=True)
        relevant_months = sorted_months[:num_months]
        
        if not relevant_months:
            print("No data available for trend analysis.")
            return
        
        amounts = []
        for month in relevant_months:
            amount = self.data[month]["expenses"].get(category, 0)
            amounts.append(amount)
        
        if len(amounts) < 2:
            print("Not enough data to analyze trends.")
            return
        
        # Calculate trend
        trend = amounts[0] - amounts[-1]
        trend_percent = (trend / amounts[-1] * 100) if amounts[-1] > 0 else 0
        
        print(f"📊 SPENDING TREND ANALYSIS FOR '{category.upper()}'")
        for i, month in enumerate(relevant_months):
            year, month_num = map(int, month.split('-'))
            month_name = calendar.month_name[month_num]
            print(f"{month_name} {year}: ${amounts[i]:,.2f}")
        
        if trend > 0:
            print(f"\nTrend: Increasing by ${trend:,.2f} ({trend_percent:.1f}%) over period")
        elif trend < 0:
            print(f"\nTrend: Decreasing by ${abs(trend):,.2f} ({abs(trend_percent):.1f}%) over period")
        else:
            print("\nTrend: No significant change")
    
    def export_monthly_summary(self, month_key, filename="budget_summary.txt"):
        """Export monthly summary to a text file"""
        summary = self.get_monthly_summary(month_key)
        if not summary:
            return False
        
        with open(filename, 'w') as f:
            f.write(f"=== PERSONAL BUDGET TRACKER ===\n")
            f.write(f"Month: {summary['month']}\n\n")
            f.write("💰 FINANCIAL SUMMARY\n")
            f.write(f"Total Income: ${summary['total_income']:,.2f}\n")
            f.write(f"Total Expenses: ${summary['total_expenses']:,.2f}\n")
            f.write(f"Net Savings: ${summary['net_savings']:,.2f} ({summary['savings_percentage']:.1f}%)\n\n")
            
            f.write("📈 INCOME BREAKDOWN\n")
            for category, amount in summary['income_breakdown'].items():
                percentage = amount / summary['total_income'] * 100 if summary['total_income'] > 0 else 0
                f.write(f"{category.title():<15} {percentage:.1f}% (${amount:,.2f})\n")
            
            f.write("\n📉 EXPENSE BREAKDOWN\n")
            for category, amount in summary['expense_breakdown'].items():
                percentage = amount / summary['total_expenses'] * 100 if summary['total_expenses'] > 0 else 0
                f.write(f"{category.title():<15} {percentage:.1f}% (${amount:,.2f})\n")
        
        print(f"Summary exported to {filename}")
        return True


# Example usage
if __name__ == "__main__":
    tracker = BudgetTracker()
    
    # Add sample data
    tracker.add_transaction("2024-01", "salary", 3000, "income")
    tracker.add_transaction("2024-01", "bonus", 200, "income")
    tracker.add_transaction("2024-01", "food", 400, "expenses")
    tracker.add_transaction("2024-01", "rent", 1200, "expenses")
    tracker.add_transaction("2024-01", "entertainment", 150, "expenses")
    tracker.add_transaction("2024-01", "transport", 200, "expenses")
    
    tracker.add_transaction("2024-02", "salary", 3000, "income")
    tracker.add_transaction("2024-02", "food", 450, "expenses")
    tracker.add_transaction("2024-02", "rent", 1200, "expenses")
    tracker.add_transaction("2024-02", "entertainment", 300, "expenses")
    
    # Set budget limits
    tracker.set_budget_limit("food", 350)
    tracker.set_budget_limit("entertainment", 200)
    
    # Display summary
    tracker.display_summary("2024-01")
    
    # Analyze trends
    tracker.analyze_spending_trends("entertainment")
    
    # Export summary
    tracker.export_monthly_summary("2024-01")