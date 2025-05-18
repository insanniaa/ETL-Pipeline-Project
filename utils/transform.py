import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        df = df.copy()

        #menghapus produk yang tidak valid
        df = df[~df['Title'].str.contains("Unknown Product", na=False)]
        df = df[~df['Title'].str.endswith('.jpeg')]

        #menghapus data yg duplikasi
        df.drop_duplicates(inplace=True)

        #membersihkan kolom Price (hapus simbol $ + konversi ke matauang rupiah)
        df['Price'] = pd.to_numeric(df['Price'].replace(r'[\$,]', '', regex=True), errors='coerce') * 16000

        #membersihkan kolom Rating (mengambil angkany saja, jika tidak valid diisi NaN)
        df['Rating'] = pd.to_numeric(df['Rating'].replace('[⭐]', '', regex=True), errors='coerce')

        #membersihkan kolom Colors (mengambil angkany saja, jika tidak valid diisi NaN)
        if df['Colors'].dtype == 'object':
            df['Colors'] = pd.to_numeric(df['Colors'].str.extract(r'(\d+)')[0], errors='coerce')
        
        #membersihkan kolom Size dan Gender (buang teks "Size: " n "Gender: ")
        df['Size'] = df['Size'].str.replace('Size: ', '')
        df['Gender'] = df['Gender'].str.replace('Gender: ', '')

        #menghapus missing value
        df.dropna(inplace=True)

        #memastikan tipe datanya udah sesuai
        df['Title'] = df['Title'].astype(str)
        df['Price'] = df['Price'].astype(float)
        df['Rating'] = df['Rating'].astype(float)
        df['Colors'] = df['Colors'].astype(int)
        df['Size'] = df['Size'].astype(str)
        df['Gender'] = df['Gender'].astype(str)

        print(f"{len(df)} data berhasil ditransformasi.")

    except Exception as e:
        print(f"Error in transform_data: {e}")
    
    return df
