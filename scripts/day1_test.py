import duckdb
import pandas as pd

# 1. Connect to DuckDB
con = duckdb.connect()

#2. Create a sample data
df = pd.DataFrame({
    'day': [1,2,3],
    'topic': ['DuckDB Setup', 'SQL Joins', 'Aggregations'],
    'status': ['Complete', 'Pending', 'Pending']
})

#3. Query with SQL
result = con.execute("SELECT * FROM df WHERE status = 'Complete'").df

print("--- Day 1 Setup Verification ---")
print(result)