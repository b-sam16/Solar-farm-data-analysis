import pandas as pd

def load_and_clean_data(df):
    """
    Cleans the DataFrame by filling missing numerical values with the median of their respective columns.

    Args:
        df (pd.DataFrame): The input DataFrame with potential missing values.

    Returns:
        pd.DataFrame: The cleaned DataFrame with no missing numerical values.
    """
    for col in df.select_dtypes(include=["float", "int"]).columns:
        df[col] = df[col].fillna(df[col].median())
    return df

def summarize_statistics(df):
    """
    Calculates summary statistics (mean, median, std, etc.) for numerical columns.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        dict: A dictionary containing the mean values for each column.
    """
    summary = df.describe().to_dict()
    means = {col: summary[col]["mean"] for col in summary if "mean" in summary[col]}
    return means
