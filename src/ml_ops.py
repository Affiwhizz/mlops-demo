import pandas as pd
import numpy as np

# --------------------------------------------------------
# 1. Series creation
# --------------------------------------------------------
lst = [5.7, 75.2, 74.4, 84.0, 66.5, 66.3, 55.8, 75.7, 29.1, 43.7]
series = pd.Series(lst)
print("Series:\n", series)

# Third value
print("\nThird value in the Series:", series.iloc[2])

# --------------------------------------------------------
# 2. DataFrame creation
# --------------------------------------------------------
b = [[53.1, 95.0, 67.5, 35.0, 78.4],
     [61.3, 40.8, 30.8, 37.8, 87.6],
     [20.6, 73.2, 44.2, 14.6, 91.8],
     [57.4, 0.1, 96.1, 4.2, 69.5],
     [83.6, 20.5, 85.4, 22.8, 35.9],
     [49.0, 69.0, 0.1, 31.8, 89.1],
     [23.3, 40.7, 95.0, 83.8, 26.9],
     [27.6, 26.4, 53.8, 88.8, 68.5],
     [96.6, 96.4, 53.4, 72.4, 50.1],
     [73.7, 39.0, 43.2, 81.6, 34.7]]

df_b = pd.DataFrame(b)
print("\nDataFrame df_b:\n", df_b)

# Rename columns
df_b.columns = ["Score_1", "Score_2", "Score_3", "Score_4", "Score_5"]
print("\nDataFrame with renamed columns:\n", df_b.head())

# Subset with Score 1, 3, 5
subset = df_b[["Score_1", "Score_3", "Score_5"]]
print("\nSubset (Score_1, Score_3, Score_5):\n", subset.head())

# Average Score_3
print("\nAverage Score_3:", df_b["Score_3"].mean())

# Max Score_4
print("Max Score_4:", df_b["Score_4"].max())

# Median Score_2
print("Median Score_2:", df_b["Score_2"].median())

# --------------------------------------------------------
# 3. Orders dictionary → DataFrame
# --------------------------------------------------------
orders = {
    'Description': [
        'LUNCH BAG APPLE DESIGN',
        'SET OF 60 VINTAGE LEAF CAKE CASES ',
        'RIBBON REEL STRIPES DESIGN ',
        'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
        'PLAYING CARDS JUBILEE UNION JACK',
        'POPCORN HOLDER',
        'BOX OF VINTAGE ALPHABET BLOCKS',
        'PARTY BUNTING',
        'JAZZ HEARTS ADDRESS BOOK',
        'SET OF 4 SANTA PLACE SETTINGS'
    ],
    'Quantity': [1, 24, 1, 2880, 2, 7, 1, 4, 10, 48],
    'UnitPrice': [1.65, 0.55, 1.65, 0.18, 1.25, 0.85, 11.95, 4.95, 0.19, 1.25],
    'Revenue': [1.65, 13.2, 1.65, 518.4, 2.5, 5.95, 11.95, 19.8, 1.9, 60.0]
}

orders_df = pd.DataFrame(orders)
print("\nOrders DataFrame:\n", orders_df)

# Total quantity and revenue
print("\nTotal Quantity Ordered:", orders_df["Quantity"].sum())
print("Total Revenue:", orders_df["Revenue"].sum())

# Most vs least expensive
max_price = orders_df["UnitPrice"].max()
min_price = orders_df["UnitPrice"].min()
print("Price Difference (max - min):", max_price - min_price)

# --------------------------------------------------------
# 4. Admissions dataset
# --------------------------------------------------------
admissions = pd.read_csv("data/Admission_Predict.csv")

print("\nAdmissions Preview:\n", admissions.head())

# Check for missing values
print("\nMissing values per column:\n", admissions.isnull().sum())

# Set Serial No. as index (but keep the column)
admissions_indexed = admissions.set_index("Serial No.", drop=False)
print("\nAdmissions with Serial No. as index:\n", admissions_indexed.head())

# Example filter: CGPA > 9
high_cgpa = admissions[admissions["CGPA"] > 9]
print("\nNumber of students with CGPA > 9:", len(high_cgpa))

# CGPA > 9 and SOP < 3.5
subset_cgpa_sop = admissions[(admissions["CGPA"] > 9) & (admissions["SOP"] < 3.5)]
print("\nMean Chance of Admit for CGPA>9 and SOP<3.5:", subset_cgpa_sop["Chance of Admit "].mean())
