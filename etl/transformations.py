import polars as pl
import logging

logging.basicConfig(level=logging.INFO)

def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    """
    Applies transformations to the input Polars DataFrame.

    Args:
    - df (pl.DataFrame): Input Polars DataFrame with raw data.

    Returns:
    - pl.DataFrame: Transformed Polars DataFrame.

    Raises:
    - Exception: If any error occurs during transformations.
    """
    try:
        # Fill null values in clicks and impressions with 0
        df = df.with_columns([
            pl.col("clicks").fill_null(0),
            pl.col("impressions").fill_null(0)
        ])

        # Add a column calculating CTR (click-through rate)
        df = df.with_columns([
            (pl.col("clicks") / pl.col("impressions").fill_null(1)).alias("ctr")
        ])

        # Drop duplicates based on campaign name and date
        df = df.unique(subset=["campaign_name", "date"])

        logging.info("Data transformation completed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise
