import pandas as pd

def load_and_clean_data(df):
    """
    Clean the dataset by handling missing values and ensuring correct data types.
    
    Args:
        df (pd.DataFrame): The raw DataFrame containing solar data.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    # Fill missing values in numerical columns with the median
    for col in df.select_dtypes(include=["float64", "int64"]).columns:
        df[col].fillna(df[col].median(), inplace=True)
    
    # Convert 'Timestamp' to datetime if it's in the dataset
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    
    # Ensure 'Country' is categorical (optional)
    if 'Country' in df.columns:
        df['Country'] = df['Country'].astype("category")
    
    # Drop duplicates if any
    df.drop_duplicates(inplace=True)
    
    return df

def summarize_statistics(df):
    """
    Generate summary statistics for the dataset, grouped by country if applicable.
    
    Args:
        df (pd.DataFrame): The cleaned DataFrame containing solar data.
    
    Returns:
        dict: A dictionary of summary statistics for numerical columns.
    """
    summary_stats = {}
    
    # Group by 'Country' if 'Country' column exists, otherwise use the entire dataset
    if 'Country' in df.columns:
        grouped = df.groupby('Country')
        summary_stats['GHI'] = grouped['GHI'].describe()
        summary_stats['DNI'] = grouped['DNI'].describe()
        summary_stats['DHI'] = grouped['DHI'].describe()
    else:
        summary_stats['GHI'] = df['GHI'].describe()
        summary_stats['DNI'] = df['DNI'].describe()
        summary_stats['DHI'] = df['DHI'].describe()

    return summary_stats
