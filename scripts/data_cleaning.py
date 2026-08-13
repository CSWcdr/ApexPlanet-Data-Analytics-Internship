from pathlib import Path

import numpy as np
import pandas as pd


# --------------------------------------------------
# Project Paths
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ApexPlanet_DataAnalytics_Dataset.xlsx"
)

OUTPUT_EXCEL = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "cleaned_sales_dataset.xlsx"
)

OUTPUT_CSV = (
    PROJECT_ROOT
    / "data"
    / "cleaned"
    / "cleaned_sales_dataset.csv"
)


# --------------------------------------------------
# Load Data
# --------------------------------------------------

df = pd.read_excel(
    INPUT_FILE,
    sheet_name="Sales_Dataset"
)

df_clean = df.copy()


# --------------------------------------------------
# Correct Order IDs
# --------------------------------------------------

expected_order_ids = [
    f"ORD{100002 + idx}"
    for idx in df_clean.index
]

for idx in df_clean.index:
    expected_id = expected_order_ids[idx]

    if df_clean.loc[idx, "Order_ID"] != expected_id:
        df_clean.loc[idx, "Order_ID"] = expected_id


# --------------------------------------------------
# Convert Dates
# --------------------------------------------------

df_clean["Order_Date"] = pd.to_datetime(
    df_clean["Order_Date"],
    errors="coerce"
)


# --------------------------------------------------
# Handle Missing Age
# --------------------------------------------------

age_median = df_clean["Age"].median()

df_clean["Age"] = (
    df_clean["Age"]
    .fillna(age_median)
    .astype(int)
)


# --------------------------------------------------
# Handle Missing City
# --------------------------------------------------

df_clean["City"] = (
    df_clean["City"]
    .fillna("Unknown")
)


# --------------------------------------------------
# Standardize Text Columns
# --------------------------------------------------

text_columns = [
    "Order_ID",
    "Customer_ID",
    "Customer_Name",
    "Gender",
    "City",
    "Product",
    "Category"
]

for column in text_columns:
    df_clean[column] = df_clean[column].str.strip()


# --------------------------------------------------
# Feature Engineering
# --------------------------------------------------

df_clean["Order_Year"] = (
    df_clean["Order_Date"].dt.year
)

df_clean["Order_Month"] = (
    df_clean["Order_Date"].dt.month
)

df_clean["Order_Month_Name"] = (
    df_clean["Order_Date"].dt.month_name()
)

age_bins = [17, 25, 35, 45, 55, 65]

age_labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56-65"
]

df_clean["Age_Group"] = pd.cut(
    df_clean["Age"],
    bins=age_bins,
    labels=age_labels
)


# --------------------------------------------------
# Validation
# --------------------------------------------------

assert df_clean["Order_ID"].nunique() == len(df_clean)
assert df_clean["Order_Date"].isna().sum() == 0
assert df_clean["Age"].isna().sum() == 0
assert df_clean["City"].isna().sum() == 0

calculated_sales = (
    df_clean["Quantity"]
    * df_clean["Unit_Price"]
)

assert np.isclose(
    df_clean["Total_Sales"],
    calculated_sales,
    atol=0.01
).all()


# --------------------------------------------------
# Export
# --------------------------------------------------

OUTPUT_EXCEL.parent.mkdir(
    parents=True,
    exist_ok=True
)

df_clean.to_excel(
    OUTPUT_EXCEL,
    index=False
)

df_clean.to_csv(
    OUTPUT_CSV,
    index=False
)

print("Data cleaning completed successfully.")
print(f"Rows: {df_clean.shape[0]}")
print(f"Columns: {df_clean.shape[1]}")
print(f"Excel output: {OUTPUT_EXCEL}")
print(f"CSV output: {OUTPUT_CSV}")