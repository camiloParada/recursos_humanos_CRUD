import mysql.connector

# CRUD de ciudades
def create_city(db_connection, city_data):
    try:
        cursor = db_connection.cursor()

        # Verificar si la ciudad ya existe en la base de datos
        query = "SELECT ciud_nombre FROM ciudades WHERE ciud_nombre = %s AND ciud_pais_id = %s"
        cursor.execute(query, (city_data["city_name"], city_data["country_id"]))
        existing_city = cursor.fetchone()
        
        if existing_city:
            return "La ciudad de ese país ya existe en la base de datos."
        
        # Insertar la nueva ciudad en la base de datos
        insert_query = "INSERT INTO ciudades (ciud_nombre, ciud_pais_id) VALUES (%s, %s)"
        cursor.execute(insert_query, (city_data["city_name"], city_data["country_id"]))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "Ciudad creada exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear la ciudad: {error}"

def modify_city(db_connection, city_data):
    try:
        cursor = db_connection.cursor(as_dict=True)
        change_country = False

        # Verificar si la ciudad existe en la base de datos
        query = "SELECT ciud_id FROM ciudades WHERE ciud_id = %s"
        cursor.execute(query, (city_data["city_id"]))
        existing_city = cursor.fetchone()

        if not existing_city:
            return "La ciudad no existe en la base de datos."

        country_id = existing_city["ciud_pais_id"]
        if city_data["country_id"] and city_data["country_id"] != existing_city["ciud_pais_id"]:
            country_id = city_data["country_id"]
            change_country = True

        # Verificar si el nuevo nombre de la ciudad ya está en uso
        query = "SELECT ciud_nombre FROM ciudades WHERE ciud_nombre = %s AND ciud_pais_id = %s AND ciud_id != %s"
        cursor.execute(query, (city_data["city_name"], country_id, city_data["city_id"]))
        duplicate_city = cursor.fetchone()

        if duplicate_city:
            return "Ya existe otra ciudad del mismo país con el nuevo nombre."

        # Actualizar el nombre del país en la base de datos
        if change_country:
            update_query = "UPDATE ciudades SET ciud_nombre = %s, ciud_pais_id = %s WHERE ciud_id = %s"
            cursor.execute(update_query, (city_data["city_name"], country_id, city_data["city_id"]))
        else:
            update_query = "UPDATE ciudades SET ciud_nombre = %s WHERE ciud_id = %s"
            cursor.execute(update_query, (city_data["city_name"], city_data["city_id"]))

        # Guardar los cambios en la base de datos
        db_connection.commit()

        return "Ciudad modificada exitosamente."

    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al modificar la ciudad: {error}"

def list_cities(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de ciudades de la base de datos
        query = "SELECT ciud_id, ciud_nombre FROM ciudades"
        cursor.execute(query)
        cities = cursor.fetchall()

        if not cities:
            return "No hay ciudades registradas en la base de datos."

        # Formatear la lista de ciudades como una cadena de texto
        city_list = "\n".join([str(city[0]) + " - " + str(city[1]) for city in cities])

        return f"Lista de ciudades:\n{city_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de ciudades: {error}"

def delete_city(db_connection, city_id):
    try:
        cursor = db_connection.cursor()

        # Verificar si la ciudad existe en la base de datos
        query = "SELECT ciud_nombre FROM ciudades WHERE ciud_id = %s"
        cursor.execute(query, (city_id,))
        existing_city = cursor.fetchone()

        if not existing_city:
            return "La ciudad no existe en la base de datos."

        # Eliminar la ciudad de la base de datos
        delete_query = "DELETE FROM ciudades WHERE ciud_id = %s"
        cursor.execute(delete_query, (city_id,))

        # Guardar los cambios en la base de datos
        db_connection.commit()

        return "Ciudad eliminada exitosamente."

    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al eliminar la ciudad: {error}"
    