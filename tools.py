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


def inline(word, list_):
    count = 0
    for item in list_:
        count += item.count(word)
    return count


def outline(word, list_):
    count = 0
    for item in list_:
        if word in set(item):
            count += 1
    return count


if __name__ == "__main__":
    create_db('haha')
    rebulid_db('moviesite')
