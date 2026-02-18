import pandas as pd
import glob

files = glob.glob("data/CCA_tables/page_37.xlsx")

df_list = []

for file in files:
    df = pd.read_excel(file)
    df_list.append(df)

merged = pd.concat(df_list, ignore_index=True)

merged.to_csv("data/cca_unified_dataset.csv", index=False)
