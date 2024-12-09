import pytest
from scripts.analyze_data import load_and_clean_data, summarize_data

def test_load_and_clean_data():
    data = load_and_clean_data("data/benin-malanville.csv")
    assert not data.isnull().values.any(), "Data contains null values."
    assert "GHI" in data.columns, "GHI column missing."

def test_summarize_data():
    data = load_and_clean_data("data/benin-malanville.csv")
    summary = summarize_data(data)
    assert "mean" in summary.index, "Summary does not include mean."
