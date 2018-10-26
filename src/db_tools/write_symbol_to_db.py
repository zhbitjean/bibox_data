import pandas as pd
import sqlalchemy


def write_symbol_to_db(df):
    engine = sqlalchemy.create_engine('mysql+pymysql://root:myiCloud@881@localhost:3306/vocean')
    df.to_sql(
        name='bix_usdt',
        con=engine,
        index=False,
        if_exists='replace'
    )


def df_to_db(df, table_name, conn):
    df.to_sql(
        name=table_name,
        con=conn,
        index=False,
        if_exists='append'
    )


if __name__ == "__main__":
    df = pd.read_csv("../fetch_data/trades copy.csv")
    df = df.set_index(['timestamp'])
    df.reset_index(inplace=True)
    print(df)
    print(df.index)
    engine = sqlalchemy.create_engine('mysql+pymysql://root:myiCloud@881@localhost:3306/vocean')
    sql_db = pd.io.sql.SQLDatabase(engine)

    # Create the db table if necessary
    if not sql_db.has_table("my_table"):
        args = ["my_table", sql_db]
        kwargs = {
            "frame": df,
            "index": True,
            "index_label": "timestamp",
            "keys": "timestamp"
        }
        sql_table = pd.io.sql.SQLTable(*args, **kwargs)
        sql_table.create()

    # Insert the DataFrame rows into the table via to_sql() method (omit the index)
    df.to_sql("my_table", con=engine, if_exists='append', index=False)
