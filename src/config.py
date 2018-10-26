import sqlalchemy


class LogInfo(object):
    api = {"apiKey": 'eeccea338ecb24b796497f82765ba8ab71561d52',
           "secret": '5f7e2c9bd79ca6b3a7676ff7cdc6765e6d1c68ac'}
    engine_str = 'mysql+pymysql://root:myiCloud@881@localhost:3306/vocean'
    conn = sqlalchemy.create_engine('mysql+pymysql://root:myiCloud@881@localhost:3306/vocean')
