from functions import load_book, get_product_id, change_data
from data_sencible import route_excel, query_busqueda, db


# __________________#
# Exportamos de excel los códigos y el cambio solicitado (D = Disponible | N = No disponible | E = E-commerce)
# Formato: MKU - Cambio
codigos = load_book(route_excel)
# Filtramos SÓLO los productos solicitados y traemos_(D = Disponible | N = No disponible | E = E-commerce)
# Formato: ID_Producto, codigo_producto, Transicion_solicitada
id_productos = get_product_id(query_busqueda, codigos, db)

# Realizamos los cambios en la base de datos:
change_data(db, id_productos)
