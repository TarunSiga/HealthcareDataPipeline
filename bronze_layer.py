
import pandas as pd

def load_bronze_layer(file_path):
    """Load raw data into the Bronze layer."""
    try:
        data = pd.read_csv(file_path, on_bad_lines='skip')
        data.to_csv("bronze_raw_data.csv", index=False)
        print("✅ Data successfully ingested into the Bronze layer.")
        return data
    except Exception as e:
        print(f"❌ Error loading data into the Bronze layer: {e}")
        return None

if __name__ == "__main__":
    file_path = r"C:\Users\tarun\OneDrive\Desktop\UMKC\TwinHealth\healtcare_data.csv"  # Path to the raw dataset
    load_bronze_layer(file_path)
