import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def save_to_csv(df: pd.DataFrame, path='products.csv'):
    try:
        df.to_csv(path, index=False)
    except Exception as e:
        print(f"Error saving to CSV: {e}")

def save_to_gsheet(df: pd.DataFrame, json_path='dicoding-458914-67fb3c487653.json', sheet_id='18Fg09R_jxwDR7evNIfumL5VeBEJNRlC9lDJw5c248og'):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_key(sheet_id)
        # sheet.share('', perm_type='anyone', role='writer')
        ws = sheet.sheet1
        ws.clear()
        ws.update([df.columns.values.tolist()] + df.values.tolist())

        print("Data successfully updated in Google Sheets!")
    except Exception as e:
        print(f"Error saving to Google Sheets: {e}")
