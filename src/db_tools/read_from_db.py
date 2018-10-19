import pandas as pd
import sqlalchemy
from get_symbols.bibox_symbols import get_symbol_df


def read_symbol_from_db():
    engine = sqlalchemy.create_engine('mysql+pymysql://root:myiCloud@881@localhost:3306/vocean')
    df = pd.read_sql_table(
        'bix_gusd',
        con=engine,
    )
    return df

