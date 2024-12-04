from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

"""[not in use] sql connector"""
# def connect_field():
#     fields = {
#         "host": "HOST_IP",
#         "username": "USERNAME",
#         "password": "PASSWORD",
#         "database": "DB_NAME",
#         "port": 3306
#     }
#     return fields


def connect_field_postgres():
    fields = {
        "host": "localhost",
        "username": "postgres",
        "password": "pass1234",
        "database": "postgres",
        "port": 5433
    }
    return fields


# table: table name, flag: mysql | postgres
def fetch_dataframe_from_table(table, flag):
    if flag == "postgres":
        fields = connect_field_postgres()
        conn = f"postgresql+psycopg2://{fields['username']}:{fields['password']}@{fields['host']}:{fields['port']}/{fields['database']}"
    elif flag == "mysql":
        fields = connect_field()
        conn = f"mysql+mysqlconnector://{fields['username']}:{fields['password']}@{fields['host']}:{fields['port']}/{fields['database']}"

    try:
        engine = create_engine(conn)
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, con=engine)

        # # 쿼리 작성: 테이블이 'ratings'인 경우 제한 적용
        # if table == 'ratings':
        #     query = "SELECT * FROM ratings LIMIT 100000"
        # else:
        #     query = f"SELECT * FROM {table}"
    except SQLAlchemyError as e:
        # 에러 처리 및 로그 출력
        print(f"Error while inserting data: {e}")
        return None
    else:
        engine.dispose()
        print("Data selected..")

    return df
