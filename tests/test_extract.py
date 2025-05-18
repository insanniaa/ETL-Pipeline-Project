import pytest
from utils.extract import extract_product_data
import pandas as pd

def test_extract_structure():
    df = extract_product_data()
    
    #mengecek apa semua kolomnya ada di df
    assert all(col in df.columns for col in ["Title", "Price", "Rating", "Colors", "Size", "Gender", "Timestamp"])

def test_extract_non_empty():
    df = extract_product_data()
    
    #mengecek apakah df tidak kosong
    assert df.shape[0] > 0, "DataFrame hasil ekstraksi kosong"
