import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("=" * 60)
print("GREENGROCER BUSINESS ANALYTICS")
print("=" * 60)

np.random.seed(42)

stores = ["Tampa", "Orlando", "Miami", "Jacksonville", "Gainesville"]
store_data = {
    "Store": stores,
    "SquareFootage": [15000, 12000, 18000, 10000, 8000],
    "StaffCount": [45, 35, 55, 30, 25],
    "YearsOpen": [5, 3, 7, 2, 1],
    "WeeklyMarketingSpend": [2500, 2000, 3000, 1800, 1500]
}

store_df = pd.DataFrame(store_data)

departments = ["Produce", "Dairy", "Bakery", "Grocery", "Prepared Foods"]
categories = {
    "Produce": ["Organic Vegetables", "Organic Fruits", "Fresh Herbs"],
    "Dairy": ["Milk & Cream", "Cheese", "Yogurt"],
    "Bakery": ["Bread", "Pastries", "Cakes"],
    "Grocery": ["Grains", "Canned Goods", "Snacks"],
    "Prepared Foods": ["Hot Bar", "Salad Bar", "Sandwiches"]
}

sales_data = []
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq="D")

store_performance = {
    "Tampa": 1.0,
    "Orlando": 0.85,
    "Miami": 1.2,
    "Jacksonville": 0.75,
    "Gainesville": 0.65
}

dept_performance = {
    "Produce": 1.2,
    "Dairy": 1.0,
    "Bakery": 0.85,
    "Grocery": 0.95,
    "Prepared Foods": 1.1
}

for date in dates:
    month = date.month
    seasonal_factor = 1.0
    if month in [6, 7, 8]:
        seasonal_factor = 1.15
    elif month == 12:
        seasonal_factor = 1.25
    elif month in [1, 2]:
        seasonal_factor = 0.9

    dow_factor = 1.3 if date.dayofweek >= 5 else 1.0

    for store in stores:
        store_factor = store_performance[store]

        for dept in departments:
            dept_factor = dept_performance[dept]

            for category in categories[dept]:
                base_sales = np.random.normal(loc=500, scale=100)
                sales_amount = base_sales * store_factor * dept_factor * seasonal_factor * dow_factor
                sales_amount = sales_amount * np.random.normal(loc=1.0, scale=0.1)

                base_margin = {
                    "Produce": 0.25,
                    "Dairy": 0.22,
                    "Bakery": 0.35,
                    "Grocery": 0.20,
                    "Prepared Foods": 0.40
                }[dept]

                profit_margin = base_margin * np.random.normal(loc=1.0, scale=0.05)
                profit_margin = max(min(profit_margin, 0.5), 0.15)

                profit = sales_amount * profit_margin

                sales_data.append({
                    "Date": date,
                    "Store": store,
                    "Department": dept,
                    "Category": category,
                    "Sales": round(sales_amount, 2),
                    "ProfitMargin": round(profit_margin, 4),
                    "Profit": round(profit, 2)
                })

sales_df = pd.DataFrame(sales_data)

customer_data = []
total_customers = 5000

age_mean, age_std = 42, 15
income_mean, income_std = 85, 30

segments = ["Health Enthusiast", "Gourmet Cook", "Family Shopper", "Budget Organic", "Occasional Visitor"]
segment_probabilities = [0.25, 0.20, 0.30, 0.15, 0.10]

store_probs = {
    "Tampa": 0.25,
    "Orlando": 0.20,
    "Miami": 0.30,
    "Jacksonville": 0.15,
    "Gainesville": 0.10
}

for i in range(total_customers):
    age = int(np.random.normal(loc=age_mean, scale=age_std))
    age = max(min(age, 85), 18)

    gender = np.random.choice(["M", "F"], p=[0.48, 0.52])

    income = int(np.random.normal(loc=income_mean, scale=income_std))
    income = max(income, 20)

    segment = np.random.choice(segments, p=segment_probabilities)
    preferred_store = np.random.choice(stores, p=list(store_probs.values()))

    if segment == "Health Enthusiast":
        visit_frequency = np.random.randint(8, 15)
        avg_basket = np.random.normal(loc=75, scale=15)
    elif segment == "Gourmet Cook":
        visit_frequency = np.random.randint(4, 10)
        avg_basket = np.random.normal(loc=120, scale=25)
    elif segment == "Family Shopper":
        visit_frequency = np.random.randint(5, 12)
        avg_basket = np.random.normal(loc=150, scale=30)
    elif segment == "Budget Organic":
        visit_frequency = np.random.randint(6, 10)
        avg_basket = np.random.normal(loc=60, scale=10)
    else:
        visit_frequency = np.random.randint(1, 5)
        avg_basket = np.random.normal(loc=45, scale=15)

    visit_frequency = max(min(visit_frequency, 30), 1)
    avg_basket = max(avg_basket, 15)

    monthly_spend = visit_frequency * avg_basket
    if monthly_spend > 1000:
        loyalty_tier = "Platinum"
    elif monthly_spend > 500:
        loyalty_tier = "Gold"
    elif monthly_spend > 200:
        loyalty_tier = "Silver"
    else:
        loyalty_tier = "Bronze"

    customer_data.append({
        "CustomerID": f"C{i+1:04d}",
        "Age": age,
        "Gender": gender,
        "Income": income * 1000,
        "Segment": segment,
        "PreferredStore": preferred_store,
        "VisitsPerMonth": visit_frequency,
        "AvgBasketSize": round(avg_basket, 2),
        "MonthlySpend": round(visit_frequency * avg_basket, 2),
        "LoyaltyTier": loyalty_tier
    })

customer_df = pd.DataFrame(customer_data)

operational_data = []

for store in stores:
    store_row = store_df[store_df["Store"] == store].iloc[0]
    square_footage = store_row["SquareFootage"]
    staff_count = store_row["StaffCount"]

    store_sales = sales_df[sales_df["Store"] == store]["Sales"].sum()
    store_profit = sales_df[sales_df["Store"] == store]["Profit"].sum()

    sales_per_sqft = store_sales / square_footage
    profit_per_sqft = store_profit / square_footage
    sales_per_staff = store_sales / staff_count
    inventory_turnover = np.random.uniform(12, 18) * store_performance[store]
    customer_satisfaction = min(
        5,
        np.random.normal(loc=4.0, scale=0.3) * (store_performance[store] ** 0.5)
    )

    operational_data.append({
        "Store": store,
        "AnnualSales": round(store_sales, 2),
        "AnnualProfit": round(store_profit, 2),
        "SalesPerSqFt": round(sales_per_sqft, 2),
        "ProfitPerSqFt": round(profit_per_sqft, 2),
        "SalesPerStaff": round(sales_per_staff, 2),
        "InventoryTurnover": round(inventory_turnover, 2),
        "CustomerSatisfaction": round(customer_satisfaction, 2)
    })

operational_df = pd.DataFrame(operational_data)

print("\nDataframes created successfully. Ready for analysis!")
print(f"Sales data shape: {sales_df.shape}")
print(f"Customer data shape: {customer_df.shape}")
print(f"Store data shape: {store_df.shape}")
print(f"Operational data shape: {operational_df.shape}")

print("\nSales Data Sample:")
print(sales_df.head(3))
print("\nCustomer Data Sample:")
print(customer_df.head(3))
print("\nStore Data Sample:")
print(store_df)
print("\nOperational Data Sample:")
print(operational_df)

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"

def analyze_sales_performance():
    total_sales = float(sales_df["Sales"].sum())
    total_profit = float(sales_df["Profit"].sum())
    avg_profit_margin = float(sales_df["ProfitMargin"].mean())
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)

    print("\nSales Performance Statistics")
    print("-" * 40)
    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Average Profit Margin: {avg_profit_margin:.2%}")
    print(f"Mean Transaction Sales: ${sales_df['Sales'].mean():.2f}")
    print(f"Median Transaction Sales: ${sales_df['Sales'].median():.2f}")
    print(f"Sales Std Dev: ${sales_df['Sales'].std():.2f}")
    print(f"Mean Transaction Profit: ${sales_df['Profit'].mean():.2f}")
    print(f"Median Transaction Profit: ${sales_df['Profit'].median():.2f}")
    print(f"Profit Std Dev: ${sales_df['Profit'].std():.2f}")

    print("\nSales by Store:")
    print(sales_by_store.round(2))

    print("\nSales by Department:")
    print(sales_by_dept.round(2))

    return {
        "total_sales": total_sales,
        "total_profit": total_profit,
        "avg_profit_margin": avg_profit_margin,
        "sales_by_store": sales_by_store,
        "sales_by_dept": sales_by_dept
    }

def visualize_sales_distribution():
    sales_by_store = sales_df.groupby("Store")["Sales"].sum().sort_values(ascending=False)
    sales_by_dept = sales_df.groupby("Department")["Sales"].sum().sort_values(ascending=False)

    monthly_sales = sales_df.groupby(sales_df["Date"].dt.to_period("M"))["Sales"].sum()
    monthly_sales.index = monthly_sales.index.astype(str)

    store_fig, ax1 = plt.subplots(figsize=(8, 5))
    sales_by_store.plot(kind="bar", ax=ax1)
    ax1.set_title("Annual Sales by Store")
    ax1.set_xlabel("Store")
    ax1.set_ylabel("Sales ($)")
    ax1.tick_params(axis="x", rotation=45)
    store_fig.tight_layout()

    dept_fig, ax2 = plt.subplots(figsize=(8, 5))
    sales_by_dept.plot(kind="bar", ax=ax2)
    ax2.set_title("Annual Sales by Department")
    ax2.set_xlabel("Department")
    ax2.set_ylabel("Sales ($)")
    ax2.tick_params(axis="x", rotation=45)
    dept_fig.tight_layout()

    time_fig, ax3 = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind="line", marker="o", ax=ax3)
    ax3.set_title("Monthly Sales Trend")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Sales ($)")
    ax3.tick_params(axis="x", rotation=45)
    time_fig.tight_layout()

    return store_fig, dept_fig, time_fig

def analyze_customer_segments():
    segment_counts = customer_df["Segment"].value_counts()
    segment_avg_spend = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    segment_loyalty = pd.crosstab(customer_df["Segment"], customer_df["LoyaltyTier"])

    fig1, ax1 = plt.subplots(figsize=(8, 5))
    segment_counts.plot(kind="bar", ax=ax1)
    ax1.set_title("Customer Segment Distribution")
    ax1.set_xlabel("Segment")
    ax1.set_ylabel("Customer Count")
    ax1.tick_params(axis="x", rotation=45)
    fig1.tight_layout()

    fig2, ax2 = plt.subplots(figsize=(8, 5))
    segment_avg_spend.plot(kind="bar", ax=ax2)
    ax2.set_title("Average Monthly Spend by Segment")
    ax2.set_xlabel("Segment")
    ax2.set_ylabel("Average Monthly Spend ($)")
    ax2.tick_params(axis="x", rotation=45)
    fig2.tight_layout()

    print("\nCustomer Segment Analysis")
    print("-" * 40)
    print("Segment Counts:")
    print(segment_counts)
    print("\nAverage Monthly Spend by Segment:")
    print(segment_avg_spend.round(2))
    print("\nSegment vs Loyalty Tier:")
    print(segment_loyalty)

    return {
        "segment_counts": segment_counts,
        "segment_avg_spend": segment_avg_spend,
        "segment_loyalty": segment_loyalty
    }

def analyze_sales_correlations():
    merged = pd.merge(store_df, operational_df, on="Store")

    numeric_cols = [
        "SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend",
        "AnnualSales", "AnnualProfit", "SalesPerSqFt", "ProfitPerSqFt",
        "SalesPerStaff", "InventoryTurnover", "CustomerSatisfaction"
    ]

    store_correlations = merged[numeric_cols].corr()

    sales_corr = store_correlations["AnnualSales"].drop("AnnualSales").sort_values(ascending=False)
    top_correlations = list(sales_corr.items())

    fig, ax = plt.subplots(figsize=(8, 6))
    sales_corr.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Correlation of Operational Factors with Annual Sales")
    ax.set_xlabel("Correlation Coefficient")
    ax.set_ylabel("Factor")
    fig.tight_layout()

    print("\nCorrelation Analysis")
    print("-" * 40)
    print(store_correlations.round(3))
    print("\nTop Correlations with Annual Sales:")
    for factor, corr in top_correlations:
        print(f"{factor}: {corr:.3f}")

    return {
        "store_correlations": store_correlations,
        "top_correlations": top_correlations,
        "correlation_fig": fig
    }

def compare_store_performance():
    efficiency_metrics = operational_df.set_index("Store")[["SalesPerSqFt", "SalesPerStaff"]]
    performance_ranking = operational_df.set_index("Store")["AnnualProfit"].sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    operational_df.plot(
        x="Store",
        y=["AnnualSales", "AnnualProfit"],
        kind="bar",
        ax=ax
    )
    ax.set_title("Store Performance Comparison")
    ax.set_ylabel("Amount ($)")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()

    print("\nStore Performance Comparison")
    print("-" * 40)
    print("\nEfficiency Metrics:")
    print(efficiency_metrics.round(2))
    print("\nStore Ranking by Annual Profit:")
    print(performance_ranking.round(2))

    return {
        "efficiency_metrics": efficiency_metrics,
        "performance_ranking": performance_ranking,
        "comparison_fig": fig
    }

def analyze_seasonal_patterns():
    seasonal_df = sales_df.copy()
    seasonal_df["Month"] = seasonal_df["Date"].dt.month
    seasonal_df["DayName"] = seasonal_df["Date"].dt.day_name()
    seasonal_df["Season"] = seasonal_df["Month"].apply(get_season)

    monthly_sales = seasonal_df.groupby("Month")["Sales"].sum()
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    dow_sales = seasonal_df.groupby("DayName")["Sales"].sum().reindex(day_order)
    season_sales = seasonal_df.groupby("Season")["Sales"].sum().reindex(["Winter", "Spring", "Summer", "Fall"])

    fig, axes = plt.subplots(3, 1, figsize=(10, 14))

    monthly_sales.plot(kind="line", marker="o", ax=axes[0])
    axes[0].set_title("Sales by Month")
    axes[0].set_xlabel("Month")
    axes[0].set_ylabel("Sales ($)")

    dow_sales.plot(kind="bar", ax=axes[1])
    axes[1].set_title("Sales by Day of Week")
    axes[1].set_xlabel("Day")
    axes[1].set_ylabel("Sales ($)")
    axes[1].tick_params(axis="x", rotation=45)

    season_sales.plot(kind="bar", ax=axes[2])
    axes[2].set_title("Sales by Season")
    axes[2].set_xlabel("Season")
    axes[2].set_ylabel("Sales ($)")
    axes[2].tick_params(axis="x", rotation=0)

    fig.tight_layout()

    print("\nSeasonal Pattern Analysis")
    print("-" * 40)
    print("Monthly Sales:")
    print(monthly_sales.round(2))
    print("\nSales by Day of Week:")
    print(dow_sales.round(2))
    print("\nSales by Season:")
    print(season_sales.round(2))

    return {
        "monthly_sales": monthly_sales,
        "dow_sales": dow_sales,
        "seasonal_fig": fig
    }

def predict_store_sales():
    model_df = pd.merge(store_df, operational_df[["Store", "AnnualSales"]], on="Store")

    features = ["SquareFootage", "StaffCount", "YearsOpen", "WeeklyMarketingSpend"]
    X = model_df[features].values
    y = model_df["AnnualSales"].values

    X_design = np.column_stack([np.ones(len(X)), X])

    beta, _, _, _ = np.linalg.lstsq(X_design, y, rcond=None)

    intercept = beta[0]
    coeff_values = beta[1:]
    predictions = X_design @ beta

    ss_total = np.sum((y - y.mean()) ** 2)
    ss_res = np.sum((y - predictions) ** 2)
    r_squared = 1 - (ss_res / ss_total)

    coefficients = {"Intercept": intercept}
    for feature, coef in zip(features, coeff_values):
        coefficients[feature] = coef

    predictions_series = pd.Series(predictions, index=model_df["Store"], name="PredictedSales")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(y, predictions)
    min_val = min(y.min(), predictions.min())
    max_val = max(y.max(), predictions.max())
    ax.plot([min_val, max_val], [min_val, max_val], linestyle="--")
    for i, store in enumerate(model_df["Store"]):
        ax.annotate(store, (y[i], predictions[i]), fontsize=8)
    ax.set_title("Actual vs Predicted Store Sales")
    ax.set_xlabel("Actual Annual Sales")
    ax.set_ylabel("Predicted Annual Sales")
    fig.tight_layout()

    print("\nStore Sales Prediction Model")
    print("-" * 40)
    print("Model Coefficients:")
    for k, v in coefficients.items():
        print(f"{k}: {v:.4f}")
    print(f"R-squared: {r_squared:.4f}")

    return {
        "coefficients": coefficients,
        "r_squared": float(r_squared),
        "predictions": predictions_series,
        "model_fig": fig
    }

def forecast_department_sales():
    temp = sales_df.copy()
    temp["Month"] = temp["Date"].dt.to_period("M").astype(str)

    dept_trends = temp.groupby(["Month", "Department"])["Sales"].sum().unstack()
    growth_rates = dept_trends.pct_change().mean().sort_values(ascending=False) * 100

    forecast_values = dept_trends.tail(3).mean()
    forecast_month = "2024-01"
    dept_trends.loc[forecast_month] = forecast_values

    fig, ax = plt.subplots(figsize=(11, 6))
    for dept in dept_trends.columns:
        ax.plot(dept_trends.index, dept_trends[dept], marker="o", label=dept)
    ax.set_title("Department Sales Trends with Simple Forecast")
    ax.set_xlabel("Month")
    ax.set_ylabel("Sales ($)")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    fig.tight_layout()

    print("\nDepartment Sales Forecast")
    print("-" * 40)
    print("Average Monthly Growth Rates (%):")
    print(growth_rates.round(2))
    print("\nForecast for next month based on 3-month moving average:")
    print(forecast_values.round(2))

    return {
        "dept_trends": dept_trends,
        "growth_rates": growth_rates,
        "forecast_fig": fig
    }

def identify_profit_opportunities():
    store_dept_profit = (
        sales_df.groupby(["Store", "Department"])
        .agg(
            TotalSales=("Sales", "sum"),
            TotalProfit=("Profit", "sum"),
            AvgMargin=("ProfitMargin", "mean")
        )
        .reset_index()
    )

    top_combinations = store_dept_profit.sort_values("TotalProfit", ascending=False).head(10)
    underperforming = store_dept_profit.sort_values("TotalProfit", ascending=True).head(10)

    segment_store = (
        customer_df.groupby(["PreferredStore", "Segment"])
        .agg(
            CustomerCount=("CustomerID", "count"),
            AvgMonthlySpend=("MonthlySpend", "mean"),
            TotalMonthlySpend=("MonthlySpend", "sum")
        )
        .reset_index()
    )

    store_profit_rank = operational_df.set_index("Store")["AnnualProfit"].rank(ascending=False, pct=True)
    customer_store_spend = segment_store.groupby("PreferredStore")["TotalMonthlySpend"].sum()

    opportunity_score = (
        customer_store_spend / customer_store_spend.max()
        + (1 - store_profit_rank)
    ).sort_values(ascending=False)

    print("\nProfit Opportunity Identification")
    print("-" * 40)
    print("Top 10 Store-Department Combinations by Profit:")
    print(top_combinations.round(2))
    print("\nBottom 10 Store-Department Combinations by Profit:")
    print(underperforming.round(2))
    print("\nOpportunity Score by Store:")
    print(opportunity_score.round(3))

    return {
        "top_combinations": top_combinations,
        "underperforming": underperforming,
        "opportunity_score": opportunity_score
    }

def develop_recommendations():
    store_profit_rank = operational_df.sort_values("AnnualProfit", ascending=False)
    best_store = store_profit_rank.iloc[0]["Store"]
    worst_store = store_profit_rank.iloc[-1]["Store"]

    dept_profit = sales_df.groupby("Department")["Profit"].sum().sort_values(ascending=False)
    best_dept = dept_profit.index[0]
    weakest_dept = dept_profit.index[-1]

    segment_spend = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False)
    top_segment = segment_spend.index[0]

    monthly_sales = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum()
    top_month = monthly_sales.idxmax()

    recommendations = [
        f"Expand successful practices from {best_store}, especially merchandising and staffing approaches, to lower-performing stores such as {worst_store}.",
        f"Increase focus on the {best_dept} department because it generates the strongest profit contribution across stores.",
        f"Review pricing, assortment, and promotion strategy in the {weakest_dept} department to improve its margin and sales productivity.",
        f"Target the {top_segment} customer segment with personalized promotions and loyalty offers because this segment has the highest average monthly spend.",
        f"Prepare inventory and staffing increases ahead of month {top_month}, when sales peak, to avoid stockouts and capture seasonal demand.",
        "Use store-level efficiency metrics such as sales per square foot and sales per staff member to guide labor scheduling and floor-space allocation.",
        "Invest marketing dollars more heavily in stores with strong customer demand but weaker current profit performance, where upside appears greatest."
    ]

    print("\nRecommendations")
    print("-" * 40)
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec}")

    return recommendations

def generate_executive_summary():
    total_sales = sales_df["Sales"].sum()
    total_profit = sales_df["Profit"].sum()

    top_store = operational_df.sort_values("AnnualProfit", ascending=False).iloc[0]["Store"]
    low_store = operational_df.sort_values("AnnualProfit", ascending=True).iloc[0]["Store"]

    top_department = sales_df.groupby("Department")["Profit"].sum().sort_values(ascending=False).index[0]
    low_department = sales_df.groupby("Department")["Profit"].sum().sort_values().index[0]

    top_segment = customer_df.groupby("Segment")["MonthlySpend"].mean().sort_values(ascending=False).index[0]
    peak_month = sales_df.groupby(sales_df["Date"].dt.month)["Sales"].sum().idxmax()

    print("Overview:")
    print(
        f"GreenGrocer generated ${total_sales:,.2f} in annual sales and ${total_profit:,.2f} in annual profit "
        f"across five Florida stores. Performance is uneven across locations and departments, with clear leaders "
        f"and underperformers. The analysis also shows distinct seasonal demand patterns and meaningful differences "
        f"in spending across customer segments, creating opportunities for more targeted resource allocation."
    )

    print("\nKey Findings:")
    print(f"- {top_store} is the top-performing store by annual profit, while {low_store} trails the portfolio.")
    print(f"- {top_department} is the most profitable department, whereas {low_department} shows the weakest profit contribution.")
    print(f"- {top_segment} customers have the highest average monthly spend and represent a high-value segment for retention efforts.")
    print(f"- Sales peak during month {peak_month}, confirming a strong seasonal pattern in customer demand.")
    print("- Operational factors such as square footage, staffing, and marketing spend are positively related to store sales.")

    print("\nRecommendations:")
    print(f"- Replicate best practices from {top_store} in lower-performing locations.")
    print(f"- Prioritize product assortment and promotion investment in {top_department}.")
    print(f"- Redesign the strategy for {low_department} to improve sales mix and margin.")
    print(f"- Launch loyalty and promotion campaigns aimed at {top_segment} shoppers.")
    print("- Align staffing, inventory, and marketing with peak seasonal demand periods.")

    print("\nExpected Impact:")
    print(
        "If management acts on these findings, GreenGrocer should be able to improve sales efficiency, increase profit "
        "in weaker stores and departments, and better match inventory and labor to demand patterns. A more focused "
        "customer strategy would also help the company deepen loyalty among higher-value shoppers while improving returns "
        "on marketing and operating investments."
    )

def main():
    print("\n" + "=" * 60)
    print("GREENGROCER BUSINESS ANALYTICS RESULTS")
    print("=" * 60)

    sales_metrics = analyze_sales_performance()
    dist_figs = visualize_sales_distribution()
    customer_analysis = analyze_customer_segments()

    print("\n--- DIAGNOSTIC ANALYTICS: UNDERSTANDING RELATIONSHIPS ---")
    correlations = analyze_sales_correlations()
    store_comparison = compare_store_performance()
    seasonality = analyze_seasonal_patterns()

    print("\n--- PREDICTIVE ANALYTICS: FORECASTING ---")
    sales_model = predict_store_sales()
    dept_forecast = forecast_department_sales()

    print("\n--- BUSINESS INSIGHTS AND RECOMMENDATIONS ---")
    opportunities = identify_profit_opportunities()
    recommendations = develop_recommendations()

    print("\n--- EXECUTIVE SUMMARY ---")
    generate_executive_summary()

    plt.show()

    return {
        'sales_metrics': sales_metrics,
        'customer_analysis': customer_analysis,
        'correlations': correlations,
        'store_comparison': store_comparison,
        'seasonality': seasonality,
        'sales_model': sales_model,
        'dept_forecast': dept_forecast,
        'opportunities': opportunities,
        'recommendations': recommendations
    }

if __name__ == "__main__":
    results = main()