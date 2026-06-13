"""Reusable preprocessing helpers for the customer segmentation project."""
from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_customer_data(path: str | Path = "data/Customer_Data.csv") -> pd.DataFrame:
    """Load the public credit card customer dataset."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def prepare_features(df: pd.DataFrame):
    """Remove the customer identifier, impute missing numeric values, and standardize features."""
    features = df.drop(columns=["CUST_ID"], errors="ignore").copy()
    features = features.fillna(features.median(numeric_only=True))
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)
    return features, X_scaled, scaler
