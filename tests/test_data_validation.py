import unittest
from data_validation.polars_data_validation import validate_data
import polars as pl

class TestDataValidation(unittest.TestCase):

    def test_validate_data(self):
        # Setup: Create a valid Polars DataFrame
        data = {"campaign_name": ["Campaign1"], "clicks": [100], "impressions": [1000], "date": ["2024-01-01"]}
        df = pl.DataFrame(data)
        
        # Load a mock validation config (just a basic example)
        validation_config = "validation_config/facebook_ads_expectations.yml"
        
        # Test validation
        result = validate_data(df, validation_config)
        
        # Assertions
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
