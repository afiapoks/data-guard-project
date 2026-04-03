import pandas as pd

class DataGuard:
    def __init__(self, df):
        # We store the original data here
        self.df = df
        # We start with empty buckets for clean and bad data
        self.clean_df = pd.DataFrame()
        self.quarantine_df = pd.DataFrame()

    def validate_age(self):
        """Checks if the 'age' column is between 0 and 120."""
        
        # This creates a list of True/False values for every row
        # True if age is between 0 and 120, False if it's an outlier
        is_valid_age = (self.df['age'] >= 0) & (self.df['age'] <= 120)
        
        # Put the 'True' rows in the clean bucket
        self.clean_df = self.df[is_valid_age].copy()
        
        # Put the 'False' rows (the ~ means NOT) in the bad bucket
        self.quarantine_df = self.df[~is_valid_age].copy()
        
        # If we found bad data, add a note explaining why
        if not self.quarantine_df.empty:
            self.quarantine_df['error_reason'] = 'Invalid Age'

        return self.clean_df, self.quarantine_df
    
    def validate_email(self, df_to_check):
        """Checks if the 'email' column follows a valid pattern."""
        # This is a 'Regex' pattern for a basic email check
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        # Vectorized check: returns True for valid emails, False for bad ones
        is_valid_email = df_to_check['email'].str.contains(email_pattern, regex=True, na=False)
        
        # Split the data
        clean = df_to_check[is_valid_email].copy()
        bad = df_to_check[~is_valid_email].copy()
        
        # Add the reason if it failed
        if not bad.empty:
            bad['error_reason'] = 'Invalid Email'
            
        return clean, bad
    
    def validate_name(self, df_to_check):
        """Checks for missing or empty names."""
        # .isna() finds empty cells, .str.strip() == "" finds names that are just spaces
        is_invalid_name = df_to_check['name'].isna() | (df_to_check['name'].str.strip() == "")
        
        # We want the VALID ones (not invalid)
        clean = df_to_check[~is_invalid_name].copy()
        bad = df_to_check[is_invalid_name].copy()
        
        if not bad.empty:
            bad['error_reason'] = 'Missing Name'
            
        return clean, bad