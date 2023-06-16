import mysql.connector

# CRUD de cargos
def create_position(db_connection, position_data):
    try:
        cursor = db_connection.cursor()

        # Verificar si el cargo ya existe en la base de datos
        query = "SELECT cargo_nombre FROM cargos WHERE cargo_nombre = %s"
        cursor.execute(query, (position_data["position_name"],))
        existing_position = cursor.fetchone()
        
        if existing_position:
            return "El cargo ya existe en la base de datos."
        
        # Insertar el nuevo cargo en la base de datos
        insert_query = "INSERT INTO cargos (cargo_nombre, cargo_sueldo_minimo, cargo_sueldo_maximo) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (position_data["position_name"], position_data["salary_min"], position_data["salary_max"]))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "Cargo creado exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear el cargo: {error}"

def list_positions(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de cargos de la base de datos
        query = "SELECT * FROM cargos"
        cursor.execute(query)
        positions = cursor.fetchall()

        if not positions:
            return "No hay cargos registrados en la base de datos."

        # Formatear la lista de cargos como una cadena de texto
        position_list = "\n".join([str(position[0]) + " | " + str(position[1]) + " | " + str(position[2]) + " | " + str(position[3]) for position in positions])

        return f"Lista de cargos:\n{position_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de cargos: {error}"
