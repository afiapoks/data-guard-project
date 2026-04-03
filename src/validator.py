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