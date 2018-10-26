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


if __name__ == "__main__":
    df = read_symbol_from_db()
    plot_df = df.set_index(['date'])
    plot_df['Close'].plot.line()
    plt.show()

