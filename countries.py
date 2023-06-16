import mysql.connector

# CRUD de países
def create_country(db_connection, country_name):
    try:
        cursor = db_connection.cursor()

        # Verificar si el país ya existe en la base de datos
        query = "SELECT pais_nombre FROM paises WHERE pais_nombre = %s"
        cursor.execute(query, (country_name,))
        existing_country = cursor.fetchone()
        
        if existing_country:
            return "El país ya existe en la base de datos."
        
        # Insertar el nuevo país en la base de datos
        insert_query = "INSERT INTO paises (pais_nombre) VALUES (%s)"
        cursor.execute(insert_query, (country_name,))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "País creado exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear el país: {error}"

def list_countries(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de países de la base de datos
        query = "SELECT * FROM paises"
        cursor.execute(query)
        countries = cursor.fetchall()

        if not countries:
            return "No hay países registrados en la base de datos."

        # Formatear la lista de países como una cadena de texto
        country_list = "\n".join([str(country[0]) + " - " + str(country[1]) for country in countries])

        return f"Lista de países:\n{country_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de países: {error}"
