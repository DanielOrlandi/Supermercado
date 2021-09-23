

from sql_connection import get_sql_connection

def get_all_produto(connection):
    cursor = connection.cursor()

    query = (
        "SELECT produto.produto_id, produto.produto_nome, produto.produto_mdm_id, produto.produto_preço, mdm.mdm_nome "
        "FROM produto inner join mdm on produto_mdm_id = mdm_id")

    cursor.execute(query)

    response = []

    for (produto_id, produto_nome, produto_mdm_id, produto_preço, mdm_nome) in cursor:
        response.append(
            {
                'produto_id': produto_id,
                'produto_nome': produto_nome,
                'produto_mdm_id': produto_mdm_id,
                'produto_preço': produto_preço,
                'mdm_nome': mdm_nome
            }
        )

    return response

def insert_new_produto(connection, produto):
    cursor = connection.cursor()

    query = ("INSERT INTO produto "
             "(produto_nome, produto_mdm_id, produto_preço)"
             "VALUES (%s, %s, %s)")

    data = (produto['produto_nome'], produto['produto_mdm_id'], produto['produto_preço'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_produto(connection, produto_id):
    cursor = connection.cursor()
    query = ("DELETE FROM produto where produto_id=" + str(produto_id))
    cursor.execute(query)
    connection.commit()

if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_produto(connection, 4))
