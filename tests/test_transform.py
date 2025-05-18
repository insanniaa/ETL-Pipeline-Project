import pytest
import pandas as pd
from utils.transform import transform_data

def test_transform_valid_output():
    data = {
        "Title": ["Shirt", "Pants", "Unknown Product"],
        "Price": ["$10", "$20", "$30"],
        "Rating": ["4.8 / 5", "3.5 / 5", "Invalid Rating"],
        "Colors": ["3 Colors", "2 Colors", "1 Color"],
        "Size": ["Size: M", "Size: L", "Size: XL"],
        "Gender": ["Gender: Male", "Gender: Female", "Gender: Unisex"],
        "Timestamp": ["2024-05-05", "2024-05-05", "2024-05-05"]
    }
    df = pd.DataFrame(data)
    
    #transformasi data
    clean_df = transform_data(df)

    #memastikan tidak ada missiong value
    assert clean_df.isnull().sum().sum() == 0
    
    #memastikan tipe datanya sudah benar
    assert clean_df.dtypes.to_dict() == {
        'Title': 'object',
        'Price': 'float64',
        'Rating': 'float64',
        'Colors': 'int64',
        'Size': 'object',
        'Gender': 'object',
        'Timestamp': 'object'
    }

    #mwmastikan produk yang tidak valid (Unknown Product) sudah dihapus
    assert "Unknown Product" not in clean_df['Title'].values
