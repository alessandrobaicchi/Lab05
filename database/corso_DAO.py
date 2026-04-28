from database.DB_connect import get_connection
from model.corso import Corso


def get_all_corsi():
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """ SELECT codins, crediti, nome, pd
                    FROM corso
                    ORDER BY nome
                    """
    cursor.execute(query)

    res = []
    # Appendo alla lista res un nuovo oggetto Corso
    for row in cursor:
            res.append(Corso(
                codins = row["codins"],
                crediti = row["crediti"],
                nome = row["nome"],
                pd = row["pd"]
            ))

    cursor.close()
    cnx.close()
    return res