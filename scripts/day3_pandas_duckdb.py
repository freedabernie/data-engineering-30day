import pandas as pd
import duckdb

print("--- 1. Loading messy CSV into Pandas ---")
df_users = pd.read_csv('data/messy_users.csv')
df_users['name'] = df_users['name'].str.strip().str.title()
df_users['email'] = df_users['email'].fillna('unknown@example.com')

print("Cleaned Pandas DataFrame:")
print(df_users)

print("\n--- 2. Querying Pandas DataFrame with DuckDB SQL ---")
con = duckdb.connect()

query = """
    SELECT 
        user_id,
        name,
        email,
        COALESCE(spending_score, 0) as spending_score
    FROM df_users
    WHERE spending_score > 50 OR spending_score IS NULL
    ORDER BY spending_score DESC
"""

df_cleaned = con.execute(query).df()
print("DuckDB SQL Output:")
print(df_cleaned)

df_cleaned.to_csv('data/cleaned_users.csv', index=False)
print("\nSaved cleaned data to data/cleaned_users.csv!")