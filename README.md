# ApexPlanet Data Analytics Internship

## Task 1: Data Immersion & Wrangling

### Objective

The objective of this task was to understand, assess, clean, transform, and validate the provided sales dataset to create an analysis-ready dataset.

## Dataset

The original dataset contains 1,000 sales transaction records across 12 variables covering:

- Orders
- Customers
- Customer demographics
- Locations
- Products
- Categories
- Quantities
- Prices
- Sales amounts

## Data Quality Issues Identified

- 20 missing values in `Age`
- 13 missing values in `City`
- Eight incorrectly assigned `Order_ID` values
- `Order_Date` stored as string data
- High-value statistical outliers in `Total_Sales`

No exact duplicate records, invalid numerical values, or sales calculation errors were identified.

## Data Cleaning Performed

- Corrected invalid order identifiers
- Converted order dates to datetime
- Imputed missing ages using median age
- Replaced missing cities with `Unknown`
- Standardized text fields
- Validated transaction calculations
- Retained legitimate high-value sales observations

## Feature Engineering

The following analytical variables were created:

- `Order_Year`
- `Order_Month`
- `Order_Month_Name`
- `Age_Group`

## Final Dataset

The cleaned dataset contains:

- 1,000 transaction records
- No missing values
- No duplicate Order IDs
- Valid dates
- Valid numerical values
- Consistent sales calculations

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Microsoft Excel

## Project Structure

```text
intern_task1/
├── data/
│   ├── raw/
│   └── cleaned/
├── data_dictionary/
├── notebooks/
├── scripts/
├── README.md
└── requirements.txt