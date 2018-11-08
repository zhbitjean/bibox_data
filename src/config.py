import sqlalchemy


class DBInfo(object):
    api = {"apiKey": 'eeccea338ecb24b796497f82765ba8ab71561d52',
           "secret": '5f7e2c9bd79ca6b3a7676ff7cdc6765e6d1c68ac'}
    # engine_str = 'mysql+pymysql://root:myiCloud@881@localhost:3306/vocean'
    engine_str = 'mysql+pymysql://bingli:vocean881@bibox-test.cpmufxrvk62o.us-east-2.rds.amazonaws.com:3306/bibox_trade'
    conn = sqlalchemy.create_engine(engine_str)
