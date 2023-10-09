import pandas as pd
import numpy as np

df = pd.read_excel("dataProject4.xlsx")

# remove "Results" columns
# this column is treated as an outlier in the data since it sums each CRM's
# sales per year and became significantly bigger than others
df = df[df['CRM'] != 'Result']

# remove duplicates and reset index
# so that the manipulated indexes are back in order
df.drop_duplicates()
df.reset_index(drop = True)

# renamed the columns for convenience of analysis
df = df.rename(columns = {'Horeca menu webshop': 'Category', 'Prd. name Webshop' : 'ProdName',
    'Customer Classification (CRM)': 'CRM', '2f. Customer number': 'Customer', 
    '1c. Brand name': 'Brand' })