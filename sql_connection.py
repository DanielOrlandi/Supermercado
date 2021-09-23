import  mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='1!2@3#4$5%Ironman732',
                                        host='127.0.0.1',
                                        database='supermercado')

    return __cnx

