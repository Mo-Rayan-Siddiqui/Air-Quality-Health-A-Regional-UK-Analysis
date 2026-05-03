import os
import pandas as pd
import pytest

CLEAN_DATA_PATH = os.path.join("data", "clean", "merged_regional_data.csv")

def test_clean_data_exists():
    """Test if the clean data file has been generated."""
    assert os.path.exists(CLEAN_DATA_PATH), f"File {CLEAN_DATA_PATH} does not exist."

def test_clean_data_columns():
    """Test if the merged dataset has the expected columns."""
    df = pd.read_csv(CLEAN_DATA_PATH)
    expected_columns = [
        'region', 'year', 'respiratory_admissions', 
        'population', 'admission_rate_per_100k', 
        'PM2.5', 'NO2', 'O3'
    ]
    for col in expected_columns:
        assert col in df.columns, f"Missing expected column: {col}"

def test_clean_data_no_nulls():
    """Test if there are any missing values in the dataset."""
    df = pd.read_csv(CLEAN_DATA_PATH)
    assert df.isnull().sum().sum() == 0, "Dataset contains null values."

def test_clean_data_types():
    """Test if the variables have correct types."""
    df = pd.read_csv(CLEAN_DATA_PATH)
    assert pd.api.types.is_numeric_dtype(df['PM2.5']), "PM2.5 is not numeric"
    assert pd.api.types.is_numeric_dtype(df['admission_rate_per_100k']), "Admission rate is not numeric"
    assert pd.api.types.is_string_dtype(df['region']) or pd.api.types.is_object_dtype(df['region']), "Region should be string"

def test_data_logic():
    """Test if admission rate is correctly calculated."""
    df = pd.read_csv(CLEAN_DATA_PATH)
    # admission_rate_per_100k should be closely equal to (respiratory_admissions / population) * 100000
    calculated_rate = (df['respiratory_admissions'] / df['population']) * 100000
    # allow a tiny difference due to float rounding
    assert (df['admission_rate_per_100k'] - calculated_rate).abs().max() < 0.1, "Admission rate calculation mismatch."
