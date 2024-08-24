import polars as pl

def transform_data(df: pl.DataFrame) -> pl.DataFrame:
    """
    Applies necessary transformations to the input Polars DataFrame.
    
    Parameters:
    - df: Input Polars DataFrame with raw data.
    
    Returns:
    - Transformed Polars DataFrame.
    """
    
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

    return df
