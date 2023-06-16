import mysql.connector

# CRUD de históricos
def list_historical(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de históricos de la base de datos
        query = "SELECT h.emphist_id, h.emphist_fecha_retiro, e.empl_primer_nombre, e.empl_segundo_nombre, cg.cargo_nombre, d.depto_nombre FROM historico AS h JOIN empleados AS e ON e.empl_id = h.emphist_empl_id JOIN cargos AS cg ON cg.cargo_id = emphist_cargo_id JOIN departamentos AS d ON d.depto_id = emphist_depto_id"
        cursor.execute(query)
        historical = cursor.fetchall()

        if not historical:
            return "No hay históricos registrados en la base de datos."

        # Formatear la lista de históricos como una cadena de texto
        historical_list = "\n".join([str(row[0]) + " | " + str(row[1]) + " | " + str(row[2]) + " | " + str(row[3]) + " | " + str(row[4]) + " | " + str(row[5]) for row in historical])

        return f"Lista de históricos:\nID | Fecha de retiro | Nombre empleado | Apellido empleado | Cargo | Departamento \n{historical_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de históricos: {error}"

def create_historical(db_connection, historical_data):
    try:
        cursor = db_connection.cursor()
        
        # Insertar el nuevo histórico en la base de datos
        insert_query = "INSERT INTO historico (emphist_fecha_retiro, emphist_cargo_id, emphist_depto_id, emphist_empl_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (historical_data["retirement_date"], historical_data["position_id"], historical_data["department_id"], historical_data["employee_id"]))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "Histórico creado exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear la histórico: {error}"
