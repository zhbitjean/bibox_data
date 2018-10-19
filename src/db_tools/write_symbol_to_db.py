import pandas as pd
import sqlalchemy
from get_symbols.bibox_symbols import get_symbol_df


def write_symbol_to_db():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:myiCloud@881@localhost:3306/vocean')
    df = get_symbol_df()
    df.to_sql(
        name='bix_gusd',
        con=engine,
        index=False,
        if_exists='replace'
    )

