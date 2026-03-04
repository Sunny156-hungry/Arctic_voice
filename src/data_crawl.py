!pip install camelot-py[cv] openpyxl pymupdf --quiet

import camelot
import os
import pandas as pd
import fitz
from google.colab import files

PDF_PATH = "Final_24-CCA-Report-English.pdf"
OUTPUT_DIR = "tables_by_page"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# total pages number
doc = fitz.open(PDF_PATH)
total_pages = doc.page_count
doc.close()

print(f"PDF number of total pages: {total_pages}")

for page in range(34, total_pages + 1):
    print(f"\nprocessing {page} page...")

    try:
        # use stream （fit better than lattice）
        tables = camelot.read_pdf(
            PDF_PATH,
            pages=str(page),
            flavor="stream",
            strip_text="\n"
        )

        # if tables are not detected
        if tables.n == 0:
            print("  ⚠️ tables not detected")
            continue

        valid_tables = []

        for table in tables:
            df = table.df

            # filter the blank tables
            if not df.empty and df.shape[1] > 1:
                valid_tables.append(df)

        if len(valid_tables) == 0:
            print("  ⚠️ pass the blank tables")
            continue

        output_file = os.path.join(OUTPUT_DIR, f"page_{page}.xlsx")

        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            for i, df in enumerate(valid_tables):
                df.to_excel(
                    writer,
                    sheet_name=f"table_{i+1}",
                    index=False,
                    header=False
                )

        print(f"  ✅ save {len(valid_tables)} tables")

    except Exception as e:
        print(f"  ❌ error: {e}")

print("\n🎉 All tables are extracted!")
