import psycopg2


def connect_to_db():
    print("*************************")
    connection = psycopg2.connect(database="",
                                 host="", port=5432, user="",
                                 password="ekf2F_uq8ZmndZm")
    cursor = connection.cursor()
    cursor.execute(open("dumb.sql", "r").read())
    connection.commit()


connect_to_db()