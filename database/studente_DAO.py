
from database.DB_connect import get_connection
from model.studente import Studente


def get_studenti_by_corso(codins):
    cnx = get_connection()
    cursor = cnx.cursor(dictionary=True)

    query = """ select s.*
                from studente s, iscrizione i 
                where i.matricola = s.matricola 
                and i.codins = %s
            """
    cursor.execute(query, (codins,))

    res = []
    # Appendo alla lista res un nuovo oggetto Studente
    for row in cursor:
            res.append(Studente(
                matricola = row["matricola"],
                cognome = row["cognome"],
                nome = row["nome"],
                CDS = row["CDS"]
            ))

    cursor.close()
    cnx.close()
    return res