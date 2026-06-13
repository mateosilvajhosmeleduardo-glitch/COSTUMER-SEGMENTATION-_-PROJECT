"""Reusable preprocessing helpers for the customer segmentation project."""

from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_customer_data(path: str | Path = "data/Customer_Data.csv") -> pd.DataFrame:
    """Load the customer dataset from a repository-relative path."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def scale_numeric_features(df: pd.DataFrame, exclude: list[str] | None = None):
    """Return scaled numeric features and the fitted scaler."""
    exclude = exclude or []
    features = df.select_dtypes(include="number").drop(columns=exclude, errors="ignore")
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)
    return scaled, scaler, features.columns.tolist()
