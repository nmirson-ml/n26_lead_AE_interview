import unittest
import polars as pl
from etl.transformations import transform_data

class TestETLTransformations(unittest.TestCase):

    def test_transform_data(self):
        # Setup: Create a mock Polars DataFrame
        data = {"campaign_name": ["Campaign1"], "clicks": [100], "impressions": [1000], "date": ["2024-01-01"]}
        df = pl.DataFrame(data)
        
        # Transform the data
        transformed_df = transform_data(df)
        
        # Assertions
        self.assertIn("ctr", transformed_df.columns)
        self.assertEqual(transformed_df["ctr"][0], 0.1)
        self.assertEqual(transformed_df.shape[0], 1)

if __name__ == '__main__':
    unittest.main()
