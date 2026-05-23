import sqlite3
import pandas as pd

# 1. Connect to the database
conn = sqlite3.connect('project3.db')

# 2. Final SQL Query using the correct 'TotalPrice' column
query = """
SELECT 
    COUNT(*) AS total_orders, 
    SUM(TotalPrice) AS total_revenue, 
    AVG(TotalPrice) AS average_order_value
FROM sales_data;
"""

try:
    # 3. Run and display the final results beautifully
    df = pd.read_sql_query(query, conn)
    print("\n📊 ============================================= 📊")
    print("🚀 --- PROJECT 3: FINAL DATA ANALYSIS RESULTS --- 🚀")
    print("=================================================\n")
    
    # Formatting numbers for a cleaner look
    print(f"🔹 Total Orders       : {df['total_orders'].iloc[0]:,}")
    print(f"🔹 Total Revenue      : ${df['total_revenue'].iloc[0]:,.2f}")
    print(f"🔹 Avg Order Value    : ${df['average_order_value'].iloc[0]:,.2f}")
    
    print("\n=================================================\n")

except Exception as e:
    print(f"❌ Error running final SQL: {e}")

# 4. Close connection
conn.close()