import sqlite3
import pandas as pd
import os

# Path to your Excel file in Downloads
excel_file = r'C:\Users\HP\Downloads\Dataset for Data analytics(AutoRecovered).xlsx' 

if not os.path.exists(excel_file):
    print(f"❌ Error: Could not find the file at: {excel_file}")
else:
    print("⏳ Reading 'Sheet1' (Raw Data) from your Excel file...")
    # Reading the correct sheet by its name
    df = pd.read_excel(excel_file, sheet_name='Sheet1')
    
    conn = sqlite3.connect('project3.db')
    print("⏳ Creating SQL table...")
    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    
    print("✅ Done! Your database is successfully updated with the correct raw data.")
    conn.close()