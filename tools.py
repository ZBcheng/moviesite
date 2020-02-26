from db_super_airdrop.db_handle.pg_handle import PgHandler


def create_db(db_name):
    '''创建数据库'''

    pg_handler = PgHandler(password='0000')
    pg_handler.create_database(db_name)


def drop_db(db_name):
    pg_handler = PgHandler(password='0000')
    pg_handler.drop_database(db_name)


def rebulid_db(db_name):
    '''重建database {db_name}'''
    pg_handler = PgHandler(password='0000')
    pg_handler.execute(f"DROP DATABASE {db_name}")
    pg_handler.execute(f"CREATE DATABASE {db_name}")


if __name__ == "__main__":
    freq = {"0": "1111", "1": "222"}
    for i in range(4, 5):
        print(i)
        i *= 2 / 3
    print(i)
    # create_db('haha')
    # rebulid_db('moviesite')
