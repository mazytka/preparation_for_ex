import pymysql


db_params = {

    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'dbname': 'preraration',
    'password': '1234'
}

connection = pymysql.connect(
    host=db_params['host'],
    port=db_params['port'],
    user=db_params['user'],
    database=db_params['dbname'],
    password=db_params['password']
)

print(bool(connection))