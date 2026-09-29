import duckdb

# Connect to in-memory DuckDB engine
con = duckdb.connect()

print("--- 1. Querying raw CSV directly with SQL ---")
query_csv = """
    SELECT 
        category,
        COUNT(transaction_id) as total_tx,
        ROUND(SUM(amount), 2) as total_spend
    FROM 'data/raw_transactions.csv'
    WHERE status = 'Completed'
    GROUP BY category
    ORDER BY total_spend DESC;
"""
df_summary = con.execute(query_csv).df()
print(df_summary)

print("\n--- 2. Exporting SQL Results directly to Parquet ---")
# Parquet is the high-performance columnar data format used in data engineering
con.execute("""
    COPY (
        SELECT * FROM 'data/raw_transactions.csv' WHERE status = 'Completed'
    ) TO 'data/cleaned_transactions.parquet' (FORMAT PARQUET);
""")
print("Successfully created 'data/cleaned_transactions.parquet'!")