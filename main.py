from utils.extract import extract_product_data
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_gsheet

if __name__ == "__main__":
    df_raw = extract_product_data()
    print("Data hasil ekstraksi:")
    print(df_raw.head())        
    print("Kolom yang diekstrak:", df_raw.columns.tolist())  

    df_clean = transform_data(df_raw)
    print("\nData setelah transformasi:")
    print(df_clean.head())
    print("Kolom setelah transformasi:", df_clean.columns.tolist())
    print(df_clean.info())
    save_to_csv(df_clean)
    save_to_gsheet(df_clean)

    print("\nETL Pipeline Selesai 🚀")
