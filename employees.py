import mysql.connector
from datetime import date
from historical import create_historical

# CRUD de empleados
def create_employee(db_connection, employee_data):
    try:
        cursor = db_connection.cursor()

        # Verificar si la empleado ya existe en la base de datos
        query = "SELECT empl_email FROM empleados WHERE empl_email = %s"
        cursor.execute(query, (employee_data["employee_email"],))
        existing_employee = cursor.fetchone()
        
        if existing_employee:
            return "El empleado ya existe en la base de datos."
        
        if employee_data["employee_boss_id"]:
            # Insertar el nuevo empleado en la base de datos
            insert_query = "INSERT INTO empleados (empl_primer_nombre, empl_segundo_nombre, empl_email, empl_fecha_nac, empl_sueldo, empl_comision, empl_cargo_id, empl_gerente_id, empl_dpto_id, empl_localiz_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (employee_data["employee_name"], employee_data["employee_surname"], employee_data["employee_email"], employee_data["employee_birth_date"], employee_data["employee_salary"], employee_data["employee_commission"], employee_data["employee_position_id"], employee_data["employee_boss_id"], employee_data["employee_department_id"], employee_data["employee_location_id"]))
        else:
            # Insertar el nuevo empleado en la base de datos
            insert_query = "INSERT INTO empleados (empl_primer_nombre, empl_segundo_nombre, empl_email, empl_fecha_nac, empl_sueldo, empl_comision, empl_cargo_id, empl_dpto_id, empl_localiz_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (employee_data["employee_name"], employee_data["employee_surname"], employee_data["employee_email"], employee_data["employee_birth_date"], employee_data["employee_salary"], employee_data["employee_commission"], employee_data["employee_position_id"], employee_data["employee_department_id"], employee_data["employee_location_id"]))
        
        # Guardar los cambios en la base de datos
        db_connection.commit()
        
        return "Empleado creado exitosamente."
    
    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al crear la empleado: {error}"

def modify_employee(db_connection, employee_data):
    try:
        cursor = db_connection.cursor()

        # Verificar si el empleado existe en la base de datos
        query = "SELECT empl_id FROM empleados WHERE empl_id = %s"
        cursor.execute(query, (employee_data["employee_id"],))
        existing_employee = cursor.fetchone()

        if not existing_employee:
            return "El empleado no existe en la base de datos."

        # Verificar si el email de el empleado ya está en uso
        query = "SELECT empl_email FROM empleados WHERE empl_email = %s AND empl_id != %s"
        cursor.execute(query, (employee_data["empl_email"], employee_data["employee_id"]))
        duplicate_employee = cursor.fetchone()

        if duplicate_employee:
            return "Ya existe otro empleado con el mismo email."

        if employee_data["employee_boss_id"]:
            # Actualizar el nombre del empleado en la base de datos
            update_query = "UPDATE empleados SET empl_primer_nombre = %s, empl_segundo_nombre = %s, empl_email = %s, empl_fecha_nac = %s, empl_sueldo = %s, empl_comision = %s, empl_cargo_id = %s, empl_gerente_id = %s, empl_dpto_id = %s, empl_localiz_id = %s WHERE empl_id = %s"
            cursor.execute(update_query, (employee_data["employee_name"], employee_data["employee_surname"], employee_data["employee_email"], employee_data["employee_birth_date"], employee_data["employee_salary"], employee_data["employee_commission"], employee_data["employee_position_id"], employee_data["employee_boss_id"], employee_data["employee_department_id"], employee_data["employee_location_id"]))
        else: 
            # Actualizar el nombre del empleado en la base de datos
            update_query = "UPDATE empleados SET empl_primer_nombre = %s, empl_segundo_nombre = %s, empl_email = %s, empl_fecha_nac = %s, empl_sueldo = %s, empl_comision = %s, empl_cargo_id = %s, empl_dpto_id = %s, empl_localiz_id = %s WHERE empl_id = %s"
            cursor.execute(update_query, (employee_data["employee_name"], employee_data["employee_surname"], employee_data["employee_email"], employee_data["employee_birth_date"], employee_data["employee_salary"], employee_data["employee_department_id"], employee_data["employee_location_id"]))

        # Guardar los cambios en la base de datos
        db_connection.commit()

        return "Empleado modificado exitosamente."

    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al modificar el empleado: {error}"

def list_employees(db_connection):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de empleados de la base de datos
        query = "SELECT * FROM empleados"
        cursor.execute(query)
        employees = cursor.fetchall()

        if not employees:
            return "No hay empleados registrados en la base de datos."

        # Formatear la lista de empleados como una cadena de texto
        employee_list = "\n".join([str(employee[0]) + " | " + str(employee[1]) + " | " + str(employee[2]) + " | " + str(employee[3]) + " | " + str(employee[4]) + " | " + str(employee[5]) + " | " + str(employee[6]) + " | " + str(employee[7]) + " | " + str(employee[8]) + " | " + str(employee[9]) + " | " + str(employee[10]) for employee in employees])

        return f"Lista de empleados:\n{employee_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de empleados: {error}"

def search_employee(db_connection, employee_id):
    try:
        cursor = db_connection.cursor()

        # Obtener la lista de empleados de la base de datos
        query = "SELECT e.empl_id, e.empl_primer_nombre, e.empl_segundo_nombre, e.empl_email, e.empl_fecha_nac, e.empl_sueldo, e.empl_comision, d.depto_nombre, cg.cargo_nombre, c.ciud_nombre, l.localiz_direccion, e.empl_status FROM empleados AS e JOIN cargos AS cg ON cg.cargo_id = e.empl_cargo_id JOIN departamentos AS d ON d.depto_id = e.empl_dpto_id JOIN localizaciones AS l ON l.localiz_id = e.empl_localiz_id JOIN ciudades AS c ON c.ciud_id = l.localiz_ciudad_id WHERE empl_id = %s"
        cursor.execute(query, (employee_id,))
        employees = cursor.fetchall()

        if not employees:
            return "No se encuentra registrado el empleado en la base de datos."

        # Formatear la lista de empleados como una cadena de texto
        employee_list = "\n".join([str(employee[0]) + " | " + str(employee[1]) + " | " + str(employee[2]) + " | " + str(employee[3]) + " | " + str(employee[4]) + " | " + str(employee[5]) + " | " + str(employee[6]) + " | " + str(employee[7]) + " | " + str(employee[8]) + " | " + str(employee[9]) + " | " + str(employee[10]) + " | " + str(employee[11]) for employee in employees])

        return f"Información Empleado:\nID | Nombre | Apellido | Email | Fecha Nac. | Sueldo | Comisión | Departamento | Cargo | Ciudad | Localización \n{employee_list}"

    except mysql.connector.Error as error:
        return f"Error al obtener la lista de empleados: {error}"

def delete_employee(db_connection, employee_id):
    try:
        cursor = db_connection.cursor()

        # Verificar si el empleado existe en la base de datos
        query = "SELECT * FROM empleados WHERE empl_id = %s"
        cursor.execute(query, (employee_id,))
        existing_employee = cursor.fetchone()

        if not existing_employee:
            return "El empleado no existe en la base de datos."

        # Eliminar el empleado de la base de datos
        delete_query = "UPDATE empleados SET empl_status = 'DELETED' WHERE empl_id = %s"
        cursor.execute(delete_query, (employee_id,))

        # Guardar los cambios en la base de datos
        db_connection.commit()

        data = {
            "retirement_date": str(date.today()),
            "position_id": existing_employee[7],
            "department_id": existing_employee[9],
            "employee_id": employee_id
        }
        create_historical(db_connection, data)

        return "Empleado eliminado exitosamente."

    except mysql.connector.Error as error:
        db_connection.rollback()
        return f"Error al eliminar el empleado: {error}"

