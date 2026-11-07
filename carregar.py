import duckdb

con = duckdb.connect("credito.duckdb")

con.execute("""
    CREATE OR REPLACE TABLE credito AS
    SELECT * FROM read_csv_auto('cs-training.csv')
""")

print(con.execute("SELECT COUNT(*) FROM credito").fetchall())
con.close()