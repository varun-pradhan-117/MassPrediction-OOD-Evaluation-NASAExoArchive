

def print_data_summary(df):
    print("Data Summary:")
    print(f"Total records: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")
    print("Missing values per column:")
    print(df.isna().sum())