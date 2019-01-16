import sqlite3
import time

def lecture_db(variable_input):
    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
        curseur = co_db.cursor()
        curseur.execute("""SELECT etat FROM variables WHERE var=?""", (variable_input,))
        variable_output=(curseur.fetchone()[0])
    co_db.close()
    return variable_output


def update_db(variable_input, variable_etat):
    with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
        curseur = co_db.cursor()
        curseur.execute("""SELECT etat FROM variables WHERE var=?""", ('base_verrouillee',))
        base_verrouille=(curseur.fetchone()[0])
    co_db.close()
    
    if base_verrouille==1:
        while base_verrouille ==1:
            with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
                curseur = co_db.cursor()
                curseur.execute("""SELECT etat FROM variables WHERE var=?""", ('base_verrouillee',))
                base_verrouille=(curseur.fetchone()[0])
            co_db.close()
        with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
            curseur = co_db.cursor()
            curseur.execute("""UPDATE variables SET etat = 1 WHERE var=?""", ('base_verrouillee',))
            curseur.execute("""UPDATE variables SET etat = ? WHERE var = ?""", (variable_etat,variable_input,))
            curseur.execute("""UPDATE variables SET etat = 0 WHERE var=?""", ('base_verrouillee',))
        co_db.close()
    else:
        with sqlite3.connect('/home/pi/Desktop/Programme_Domotic/domotic.db') as co_db:
            curseur = co_db.cursor()
            curseur.execute("""UPDATE variables SET etat = 1 WHERE var=?""", ('base_verrouillee',))
            curseur.execute("""UPDATE variables SET etat = ? WHERE var = ?""", (variable_etat,variable_input,))
            curseur.execute("""UPDATE variables SET etat = 0 WHERE var=?""", ('base_verrouillee',))
        co_db.close()      
