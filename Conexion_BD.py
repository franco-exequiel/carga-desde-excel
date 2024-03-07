import psycopg2
from data_sencible import Get_data
# Generamos la conexión a la base de datos dependiendo el nombre asignado toma el
# IP correspondiente a la base.


def get_connection(database_name=''):
    if database_name == '':
        return print("Nombre de db erronea")
    # Get_data returns: "host = {} dbname = {} password = {} user = {}"
    conn = Get_data(database_name)
    # Retornamos el cursor asignado para empezar a trabajar desde otro archivo
    return psycopg2.connect(conn)
