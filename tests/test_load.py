import pandas as pd
from utils.load import save_to_csv, save_to_gsheet
import os

def test_save_to_csv(tmp_path):
    #menyiapkan dataframe
    df = pd.DataFrame({
        "Title": ["Shirt"],
        "Price": [160000],
        "Rating": [4.5],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Male"],
        "Timestamp": ["2024-05-05"]
    })
   
    #hasilnya disimpan ke dalam file CSV
    output = tmp_path / "test_products.csv"
    save_to_csv(df, str(output))
    
    #validasi apkha file tersimpan
    assert output.exists()
    
    #membaca file CSV dan memverifikasi isinya
    df_loaded = pd.read_csv(output)
    assert df_loaded.equals(df)

def test_save_to_gsheet(monkeypatch):
    class MockClient:
        def create(self, sheet_name):
            class MockSheet:
                def sheet1(self):
                    return self
                def update(self, data):
                    pass
                def share(self, email, perm_type, role):
                    pass
            return MockSheet()

    def mock_authorize(creds):
        return MockClient()

    #mocking gspread authorize agar dia tidak benar-benar ke Google Sheets
    monkeypatch.setattr("gspread.authorize", mock_authorize)

    #fataFrame yg digunakan untuk pengujian
    df = pd.DataFrame({
        "Title": ["Shirt"],
        "Price": [160000],
        "Rating": [4.5],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Male"],
        "Timestamp": ["2024-05-05"]
    })

    #test coba disave ke gsheet
    save_to_gsheet(df)
