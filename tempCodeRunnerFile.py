
# def create_db(db_name):
#     '''创建数据库'''

#     pg_handler = PgHandler(password='0000')
#     pg_handler.create_database(db_name)


# def drop_db(db_name):
#     pg_handler = PgHandler(password='0000')
#     pg_handler.drop_database(db_name)


# def rebulid_db(db_name):
#     '''重建database {db_name}'''
#     pg_handler = PgHandler(password='0000')
#     pg_handler.execute(f"DROP DATABASE {db_name}")
#     pg_handler.execute(f"CREATE DATABASE {db_name}")