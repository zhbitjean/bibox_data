import pandas as pd
import sqlalchemy
import matplotlib.pyplot as plt


def read_symbol_from_db():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:myiCloud@881@localhost:3306/vocean')
    df = pd.read_sql_table(
        'bix_usdt',
        con=engine,
    )
    return df


def read_df_from_db(table_name, conn):
    df = pd.read_sql_table(
        table_name,
        con=conn,
    )
    return df


def get_latest_trade_from_db(table_name, conn):
    sql_db = pd.io.sql.SQLDatabase(conn)
    query = f"SELECT * FROM {table_name} WHERE id IN (SELECT MAX(id) FROM {table_name})"
    if not sql_db.has_table(table_name):
        return None
    else:
        obj = pd.read_sql(query, conn)
    return obj


def get_recent_records(table_name, conn, limit=200):
    sql_db = pd.io.sql.SQLDatabase(conn)
    query = f"SELECT * FROM {table_name} ORDER BY id DESC LIMIT {limit};"
    if not sql_db.has_table(table_name):
        return None
    else:
        obj = pd.read_sql(query, conn)
    return obj


if __name__ == "__main__":
    df = read_symbol_from_db()
    plot_df = df.set_index(['date'])
    plot_df['Close'].plot.line()
    plt.show()
