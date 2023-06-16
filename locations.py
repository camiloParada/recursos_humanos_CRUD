import mysql.connector

# CRUD de localizaciones
def create_location(db_connection, location_data):
    try:
        cursor = db_connection.cursor()

        # Verificar si la localización ya existe en la base de datos
        query = "SELECT localiz_direccion FROM localizaciones WHERE localiz_direccion = %s AND localiz_ciudad_id = %s"
        cursor.execute(query, (location_data["location_name"], location_data["city_id"]))
        existing_location = cursor.fetchone()
        
        if existing_location:
            return "La localización de esa ciudad ya existe en la base de datos."
        
        # Insertar la nueva localización en la base de datos
        insert_query = "INSERT INTO localizaciones (localiz_direccion, localiz_ciudad_id) VALUES (%s, %s)"
        cursor.execute(insert_query, (location_data["location_name"], location_data["city_id"]))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "Localización creada exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear la localización: {error}"

def list_locations(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de localizaciones de la base de datos
        query = "SELECT * FROM localizaciones"
        cursor.execute(query)
        locations = cursor.fetchall()

        if not locations:
            return "No hay localizaciones registradas en la base de datos."

        # Formatear la lista de localizaciones como una cadena de texto
        location_list = "\n".join([str(location[0]) + " | " + str(location[1]) + " | " + str(location[2]) for location in locations])

        return f"Lista de localizaciones:\n{location_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de localizaciones: {error}"
