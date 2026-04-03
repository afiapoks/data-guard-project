import pandas as pd
from src.validator import DataGuard

# 1. Load the data
raw_data = pd.read_csv('data/raw_data.csv')

# 2. Initialize our Guard
guard = DataGuard(raw_data)

# 3. STEP ONE: Filter by Age
clean_after_age, quarantine_age = guard.validate_age()

# 4. STEP TWO: Filter the 'clean' results by Email
# Notice we pass 'clean_after_age' into the email check!
final_clean, quarantine_email = guard.validate_email(clean_after_age)

# 5. Results
print("--- FINAL CLEAN DATA ---")
print(final_clean)

print("\n--- QUARANTINE (AGE ERRORS) ---")
print(quarantine_age)

print("\n--- QUARANTINE (EMAIL ERRORS) ---")
print(quarantine_email)