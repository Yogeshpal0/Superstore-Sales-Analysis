# %%
# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt


# %%
# Load Dataset & Data Cleaning

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

print(df.shape)
print(df.isnull().sum())

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("Duplicate Rows:", df.duplicated().sum())

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month_name()
df["Quarter"] = df["Order Date"].dt.quarter

df["Delivery Days"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days


# %%
# KPI Analysis

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

print("Average Sales:", df["Sales"].mean())
print("Average Profit:", df["Profit"].mean())


# %%
# Category Analysis

print(
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)


# %%
# Sub-Category Analysis

print(
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)


# %%
# Region Analysis

print(
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)


# %%
# Shipping Analysis

print(
    df.groupby("Ship Mode")["Delivery Days"]
      .mean()
      .sort_values()
)


# %%
# Top Product Analysis

print(
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)


# %%
# Save Clean Dataset

df.to_csv("clean_superstore.csv", index=False)

print("Cleaned dataset saved successfully!")


# %%
# Monthly Sales Trend

month_order = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

monthly_sales = (
    df.groupby("Month")["Sales"]
      .sum()
      .reindex(month_order)
)

print(monthly_sales)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)
plt.xticks(rotation=45)

plt.show()


# %%
# Monthly Profit Trend

monthly_profit = (
    df.groupby("Month")["Profit"]
      .sum()
      .reindex(month_order)
)

print(monthly_profit)

plt.figure(figsize=(10, 5))

plt.plot(
    monthly_profit,
    marker="o",
    linewidth=2
)

plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit")

plt.grid(True)
plt.xticks(rotation=45)

plt.show()

print("Highest Profit Month:", monthly_profit.idxmax())
print("Highest Profit:", monthly_profit.max())


# %%
# Sales by Category

category_sales = (
    df.groupby("Category")["Sales"]
      .sum()
)

print(category_sales)

plt.figure(figsize=(8, 5))

plt.bar(
    category_sales.index,
    category_sales.values
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.show()


# %%
# Profit by Category

category_profit = (
    df.groupby("Category")["Profit"]
      .sum()
)

print(category_profit)

plt.figure(figsize=(8, 5))

plt.bar(
    category_profit.index,
    category_profit.values
)

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Total Profit")

plt.show()


# %%
# Sales by Sub-Category

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print(subcategory_sales)

plt.figure(figsize=(12, 6))

plt.bar(
    subcategory_sales.index,
    subcategory_sales.values
)

plt.title("Sales by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)

plt.show()


# %%
# Profit by Sub-Category

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print(subcategory_profit)

plt.figure(figsize=(12, 6))

plt.bar(
    subcategory_profit.index,
    subcategory_profit.values
)

plt.title("Profit by Sub-Category")
plt.xlabel("Sub-Category")
plt.ylabel("Total Profit")

plt.xticks(rotation=90)

plt.show()


# %%
# Sales by Region

region_sales = (
    df.groupby("Region")["Sales"]
      .sum()
)

print(region_sales)

plt.figure(figsize=(8, 5))

plt.bar(
    region_sales.index,
    region_sales.values
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.show()


# %%
# Profit by Region

region_profit = (
    df.groupby("Region")["Profit"]
      .sum()
)

print(region_profit)

plt.figure(figsize=(8, 5))

plt.bar(
    region_profit.index,
    region_profit.values
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.show()

print("Highest Profit Region:", region_profit.idxmax())
print("Highest Profit:", region_profit.max())


# %%
# Average Delivery Days by Ship Mode

ship_days = (
    df.groupby("Ship Mode")["Delivery Days"]
      .mean()
)

print(ship_days)

plt.figure(figsize=(8, 5))

plt.bar(
    ship_days.index,
    ship_days.values
)

plt.title("Average Delivery Days by Ship Mode")
plt.xlabel("Ship Mode")
plt.ylabel("Average Delivery Days")

plt.xticks(rotation=20)

plt.show()


# %%
# Top 10 Products by Sales

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12, 6))

plt.barh(
    top_products.index,
    top_products.values
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")

plt.show()


# %%
# Top 10 Products by Profit

top_profit_products = (
    df.groupby("Product Name")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12, 6))

plt.barh(
    top_profit_products.index,
    top_profit_products.values
)

plt.title("Top 10 Products by Profit")
plt.xlabel("Profit")
plt.ylabel("Product")

plt.show()


# %%
# Sales by Segment

segment_sales = (
    df.groupby("Segment")["Sales"]
      .sum()
)

plt.figure(figsize=(8, 5))

plt.bar(
    segment_sales.index,
    segment_sales.values
)

plt.title("Sales by Segment")
plt.xlabel("Segment")
plt.ylabel("Total Sales")

plt.show()


# %%
# Profit by Segment

segment_profit = (
    df.groupby("Segment")["Profit"]
      .sum()
)

plt.figure(figsize=(8, 5))

plt.bar(
    segment_profit.index,
    segment_profit.values
)

plt.title("Profit by Segment")
plt.xlabel("Segment")
plt.ylabel("Total Profit")

plt.show()


# %%
# Sales vs Profit Scatter Plot

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Sales"],
    df["Profit"]
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()