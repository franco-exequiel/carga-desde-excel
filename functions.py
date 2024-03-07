from openpyxl import load_workbook
from Conexion_BD import get_connection
from data_sencible import D, E, N, query_editar


def load_book(route=''):
    try:
        dataset = list()
        workbook = load_workbook(filename=route)
        sheet = workbook.active
        # Busca todos los datos dentro del rango 2 (la posicion 1 está reservada para la cabecera) hasta 1500
        for i in range(2, 1500):
            if sheet[f"A{i}"].value == None:
                break
            else:
                dataset.append(
                    [str((sheet[f"A{i}"].value)), str((sheet[f"B{i}"].value))])
        # Devuelve todos los codigos que hay que cambiar y a qué hay que cambiarlo
        return dataset
    except:
        print("Error al cargar los prod")


def get_product_id(first_query, dataset, db):
    # Importamos la conexión a la base de datos
    conexion = get_connection(db)
    cursor = conexion.cursor()
    cursor.execute(first_query)
    query = cursor.fetchall()
    new_dataset = list()

    for line in query:  # Line brings: Descripcion transicion | id tran | Prod id | Prod codigo
        for data in dataset:  # dataset brings: Codigo | Transicion requerida
            if line[-1] == data[0]:
                id = line[-2]
                prod = line[-1]
                trans_req = data[1]
                new_dataset.append((id, prod, trans_req))

    cursor.close()
    conexion.close()
    # Retorna: ID_Producto, codigo_producto, Transicion_solicitada
    return new_dataset


def change_data(db, dataset):
    # Importamos la conexión a la base de datos
    conexion = get_connection(db)
    cursor = conexion.cursor()
    for dato in dataset:
        # (D = Disponible | N = No disponible | E = E-commerce) (Cambia transicion y flag)
        if dato[-1] == 'D':
            cursor.execute(query_editar, (D[0], D[1], dato[0]))
        elif dato[-1] == 'N':
            cursor.execute(query_editar, (N[0], N[1], dato[0]))
        elif dato[-1] == 'E':
            cursor.execute(query_editar, (E[0], E[1], dato[0]))
        else:
            pass
    conexion.commit()
    cursor.close()
    conexion.close()
