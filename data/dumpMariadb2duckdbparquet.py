"""
Docstring for dumpMariadb2duckdbparquet
20260206 in copilot
strange the new gpt5.2 in copilot took 10 rounds to do a mariadb sql dump to a duckdb file dump and throws in parquet ... but 10 cycles of logic bugs .... code from pre duckdb10 with standard sql connect logic out of other sql python drivers ... which does not work for multiple connections of duckdb which can't see the original attach mysql conn ... after 7 tries it finally does a single connection and each run is a confident piece of prod code which is totally buggy.... run 10 finally works.
"""


import duckdb
import logging
import os
import traceback

logging.basicConfig(level=logging.INFO)

MARIADB_CONN = (
    "host=127.0.0.1 "
    "user=<<yoyouuser>>"
    "password=<<youuserpwd>> "
    "database=kenousa "
    "port=3307"
)

OUTPUT_DUCKDB = "kenousa.duckdb"

def main():
    logging.info("Starting DuckDB…")

    con = duckdb.connect(OUTPUT_DUCKDB)

    logging.info("Attaching MariaDB…")
    con.execute(f"ATTACH '{MARIADB_CONN}' AS mysqldb (TYPE mysql)")

    logging.info("Fetching table list…")
    tables = con.execute("""
        SELECT table_name
        FROM mysqldb.information_schema.tables
        WHERE table_schema = 'kenousa'
    """).fetchall()

    logging.info(f"Found {len(tables)} tables")

    for (table_name,) in tables:
        full_name = f"mysqldb.kenousa.{table_name}"
        logging.info(f"Processing table: {table_name}")

        try:
            # ---------------------------------------------------
            # 1. Load table into main DuckDB
            # ---------------------------------------------------
            con.execute(f"DROP TABLE IF EXISTS {table_name}")
            con.execute(f"""
                CREATE TABLE {table_name} AS
                SELECT * FROM {full_name}
            """)

            # ---------------------------------------------------
            # 2. Write Parquet
            # ---------------------------------------------------
            parquet_file = f"{table_name}.parquet"
            con.execute(f"""
                COPY (SELECT * FROM {table_name})
                TO '{parquet_file}'
                (FORMAT PARQUET)
            """)

            # ---------------------------------------------------
            # 3. Write per-table DuckDB
            # ---------------------------------------------------
            single_file = f"{table_name}.duckdb"
            if os.path.exists(single_file):
                os.remove(single_file)

            with duckdb.connect(single_file) as outcon:
                outcon.execute(f"""
                    CREATE TABLE {table_name} AS
                    SELECT * FROM read_parquet('{parquet_file}')
                """)

            logging.info(f"✓ {table_name}: main duckdb + per-table duckdb + parquet written")

        except Exception as e:
            logging.error(f"✗ ERROR processing table {table_name}: {e}")
            traceback.print_exc()
            logging.info("Skipping this table and continuing…")
            continue

    logging.info("All tables processed.")

if __name__ == "__main__":
    main()