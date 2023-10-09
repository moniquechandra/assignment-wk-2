import pandas as pd

df = pd.read_excel("hotelBookings.xlsx")

# Drop duplicates and NaN/blank values
df.drop_duplicates()
df.dropna()

# Fix inconsistent format in "adr"
for number in df["adr"]:
    number = float(number)

print(df["adr"].head())

# Remove year 2099 from "arrival_date_year"
df = df[df["arrival_date_year"] != 2099]

# Remove numbers from "country"
condition = df["country"].astype(str).str.isnumeric()
df = df[~condition]

# Fix inconsistent spacing from "meal"
df = df["meal"].str.strip()
