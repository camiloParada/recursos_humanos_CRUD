import mysql.connector

# CRUD de departamentos
def create_department(db_connection, department_name):
    try:
        cursor = db_connection.cursor()

        # Verificar si el departamento ya existe en la base de datos
        query = "SELECT depto_nombre FROM departamentos WHERE depto_nombre = %s"
        cursor.execute(query, (department_name,))
        existing_department = cursor.fetchone()
        
        if existing_department:
            return "El departamento ya existe en la base de datos."
        
        # Insertar el nuevo departamento en la base de datos
        insert_query = "INSERT INTO departamentos (depto_nombre) VALUES (%s)"
        cursor.execute(insert_query, (department_name,))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "Departamento creado exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear el departamento: {error}"

def list_departments(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de departamentos de la base de datos
        query = "SELECT * FROM departamentos"
        cursor.execute(query)
        departments = cursor.fetchall()

        if not departments:
            return "No hay departamentos registrados en la base de datos."

        # Formatear la lista de departamentos como una cadena de texto
        department_list = "\n".join([str(department[0]) + " - " + str(department[1]) for department in departments])

        return f"Lista de departamentos:\n{department_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de departamentos: {error}"
