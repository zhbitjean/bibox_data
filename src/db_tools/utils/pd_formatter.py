from db_tools.read_from_db import read_symbol_from_db


class Formatter(object):
    def df_to_json(self, df):
        return df


if __name__ == "__main__":
    df = read_symbol_from_db()
    df_string = df.T.to_json()
    print(df_string)
    print(type(df_string))
