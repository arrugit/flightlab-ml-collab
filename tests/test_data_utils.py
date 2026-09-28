
"""Tests for FlightLab data utilities."""

import pandas as pd
import pytest

from src.data_utils import load_dataset


def test_load_dataset(tmp_path):
    """Verify that a valid CSV is loaded correctly."""
    csv_path = tmp_path / "sample.csv"
    expected = pd.DataFrame(
        {
            "flight": ["FL101", "FL202"],
            "delay_minutes": [15, 0],
        }
    )
    expected.to_csv(csv_path, index=False)

    actual = load_dataset(csv_path)

    pd.testing.assert_frame_equal(actual, expected)


def test_missing_dataset_raises_error(tmp_path):
    """Verify that a missing file raises FileNotFoundError."""
    missing_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        load_dataset(missing_path)