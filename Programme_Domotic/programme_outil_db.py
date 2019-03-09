import sqlite3
import time
import os

def lecture_db(variable_input):

    chemin_base = os.getcwd()+"/domotic.db"
    
    with sqlite3.connect(chemin_base, timeout=50) as co_db:
        curseur = co_db.cursor()
        curseur.execute("""SELECT etat FROM variables WHERE var=?""", (variable_input,))
        variable_output=(curseur.fetchone()[0])
    co_db.close()
    return variable_output


def update_db(variable_input, variable_etat):

    chemin_base = os.getcwd()+"/domotic.db"

    try:
        with sqlite3.connect(chemin_base, timeout=50) as co_db:
            curseur = co_db.cursor()
            curseur.execute("""UPDATE variables SET etat = ? WHERE var = ?""", (variable_etat,variable_input,))
        co_db.close()

    except:
        i=1
        while i==1:
            with sqlite3.connect(chemin_base, timeout=50) as co_db:
                curseur = co_db.cursor()
                curseur.execute("""UPDATE variables SET etat = ? WHERE var = ?""", (variable_etat,variable_input,))
                i=0
            co_db.close()
            
            
