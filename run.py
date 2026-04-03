import pandas as pd
from src.validator import DataGuard

# 1. Load the "dirty" data we just made
raw_data = pd.read_csv('data/raw_data.csv')
print("--- Original Data ---")
print(raw_data)

# 2. Initialize our Guard with that data
guard = DataGuard(raw_data)

# 3. Run the age validation
clean, quarantine = guard.validate_age()

# 4. See the results!
print("\n--- Clean Data (Safe to use) ---")
print(clean)

print("\n--- Quarantine (The Bad Stuff) ---")
print(quarantine)