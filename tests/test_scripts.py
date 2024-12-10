import sys
import os

# Add the root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import unittest
import pandas as pd
from scripts.data_processing import load_and_clean_data, summarize_statistics

class TestSolarDataAnalysis(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment by creating a sample DataFrame.
        """
        data = {
            "GHI": [200, 300, None, 400],
            "DNI": [150, None, 200, 250],
            "DHI": [50, 100, 150, None],
            "Country": ["Benin", "Sierra Leone", "Togo", "Benin"]
        }
        self.test_df = pd.DataFrame(data)

    def test_load_and_clean_data(self):
        """
        Test the `load_and_clean_data` function to ensure it handles missing data correctly.
        """
        cleaned_df = load_and_clean_data(self.test_df)
        # Ensure there are no missing values in the cleaned DataFrame
        self.assertFalse(cleaned_df.isnull().values.any(), "DataFrame still contains missing values after cleaning.")

    def test_summarize_statistics(self):
        """
        Test the `summarize_statistics` function to verify it returns correct statistical summaries.
        """
        stats = summarize_statistics(self.test_df)
        # Check that the summary statistics are correct
        self.assertAlmostEqual(stats["GHI"], 300, places=2, msg="GHI mean is incorrect.")
        self.assertAlmostEqual(stats["DNI"], 200, places=2, msg="DNI mean is incorrect.")

    def test_country_column_exists(self):
        """
        Verify that the `Country` column exists in the dataset.
        """
        self.assertIn("Country", self.test_df.columns, "The 'Country' column is missing from the DataFrame.")

if __name__ == "__main__":
    unittest.main()
