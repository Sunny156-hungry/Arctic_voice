"""
Cetacean Interaction Events
Data Cleaning Script
---------------------------------
Input: raw_extracted_data.csv
Output: cetacean_interaction_events_cleaned.csv
"""

import pandas as pd

# ============================================
# 1. LOAD RAW DATA
# ============================================

INPUT_FILE = "raw_extracted_data.csv"
OUTPUT_FILE = "cetacean_interaction_events_cleaned.csv"

df = pd.read_csv(INPUT_FILE)

# ============================================
# 2. BASIC CLEANING
# ============================================

# Standardize column names
df.columns = df.columns.str.strip().str.upper()

# Convert DATE to datetime
df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")

# Remove rows without valid date
df = df[df["DATE"].notna()]

# Strip whitespace
df["FACILITY"] = df["FACILITY"].str.strip()
df["SPECIES"] = df["SPECIES"].str.strip()
df["EVENT"] = df["EVENT"].str.strip()

# ============================================
# 3. FEATURE ENGINEERING
# ============================================

# Extract Year & Month
df["YEAR"] = df["DATE"].dt.year
df["MONTH"] = df["DATE"].dt.month

# Primary species (if multiple listed)
df["PRIMARY_SPECIES"] = df["SPECIES"].str.split(",").str[0].str.strip()

# Event classification
def classify_event(event):
    event_lower = str(event).lower()
    
    if "photo" in event_lower:
        return "Photo opportunity"
    elif "swim" in event_lower or "interaction" in event_lower:
        return "Swim/Interaction"
    elif "feed" in event_lower or "contact" in event_lower:
        return "Feeding/Contact"
    elif "kiss" in event_lower:
        return "Kissing"
    elif "trainer" in event_lower:
        return "Trainer program"
    elif "children" in event_lower or "autism" in event_lower:
        return "Special needs program"
    else:
        return "Other"

df["EVENT_TYPE"] = df["EVENT"].apply(classify_event)

# ============================================
# 4. FINAL SELECTION
# ============================================

df_clean = df[
    ["DATE", "YEAR", "MONTH", "FACILITY", "SPECIES", "PRIMARY_SPECIES", "EVENT_TYPE", "EVENT"]
].copy()

# ============================================
# 5. EXPORT
# ============================================

df_clean.to_csv(OUTPUT_FILE, index=False)

print("Cleaning complete.")
print(f"Saved to: {OUTPUT_FILE}")
print(f"Total records: {len(df_clean)}")
