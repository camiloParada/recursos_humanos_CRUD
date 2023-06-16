import socket
import json

def connect_to_server():
    server_ip = input("Ingrese la IP del servidor: ")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 4200))
    
    return client_socket

# CRUD para países
def create_country(client_socket):
    country_name = input("Ingrese el nombre del país: ")
    data = {
        "command": "create_country",
        "country_name": country_name
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def list_countries(client_socket):
    data = {
        "command": "list_countries"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    countries = client_socket.recv(1024).decode()
    print(countries)

# CRUD para ciudades
def create_city(client_socket):
    city_name = input("Ingrese el nombre de la ciudad: ")
    country_id = input("Ingrese el ID del país al que pertenece: ")
    data = {
        "command": "create_city",
        "city_name": city_name,
        "country_id": country_id
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def list_cities(client_socket):
    data = {
        "command": "list_cities"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    cities = client_socket.recv(1024).decode()
    print(cities)

# CRUD para localizaciones
def create_location(client_socket):
    location_name = input("Ingrese el nombre de la localización: ")
    city_id = input("Ingrese el ID de la ciudad a la que pertenece: ")
    data = {
        "command": "create_location",
        "location_name": location_name,
        "city_id": city_id
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def list_locations(client_socket):
    data = {
        "command": "list_locations"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    locations = client_socket.recv(1024).decode()
    print(locations)

# CRUD para Departamentos
def create_department(client_socket):
    department_name = input("Ingrese el nombre del departamento: ")
    data = {
        "command": "create_department",
        "department_name": department_name
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def list_departments(client_socket):
    data = {
        "command": "list_departments"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    departments = client_socket.recv(1024).decode()
    print(departments)

# CRUD para cargos
def create_position(client_socket):
    position_name = input("Ingrese el nombre del cargo: ")
    salary_min = input("Ingrese el salario mínimo: ")
    salary_max = input("Ingrese el salario máximo: ")
    data = {
        "command": "create_position",
        "position_name": position_name,
        "salary_min": salary_min,
        "salary_max": salary_max
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def list_positions(client_socket):
    data = {
        "command": "list_positions"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    positions = client_socket.recv(1024).decode()
    print(positions)

# CRUD para empleados
def create_employee(client_socket):
    employee_name = input("Ingrese el nombre del empleado: ")
    employee_surname = input("Ingrese el apellido del empleado: ")
    employee_email = input("Ingrese el email del empleado: ")
    employee_birth_date = input("Ingrese la fecha de nacimiento del empleado: ")
    employee_salary = input("Ingrese el sueldo del empleado: ")
    employee_commission = input("Ingrese la comisión del empleado: ")
    employee_position_id = input("Ingrese el ID del cargo del empleado: ")
    employee_department_id = input("Ingrese el ID del departamento del empleado: ")
    employee_boss_id = input("Ingrese el ID del jefe directo del empleado: ")
    employee_location_id = input("Ingrese el ID de la localización del empleado: ")
    data = {
        "command": "create_employee",
        "employee_name": employee_name,
        "employee_surname": employee_surname,
        "employee_email": employee_email,
        "employee_birth_date": employee_birth_date,
        "employee_salary": employee_salary,
        "employee_commission": employee_commission,
        "employee_position_id": employee_position_id,
        "employee_department_id": employee_department_id,
        "employee_boss_id": employee_boss_id,
        "employee_location_id": employee_location_id
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def modify_employee(client_socket):
    employee_id = input("Ingrese el ID del empleado: ")
    new_employee_name = input("Ingrese el nuevo nombre del empleado: ")
    new_employee_surname = input("Ingrese el nuevo apellido del empleado: ")
    new_employee_email = input("Ingrese el nuevo email del empleado: ")
    new_employee_birth_date = input("Ingrese la nueva fecha de naciemiento del empleado: ")
    new_employee_salary = input("Ingrese el nuevo sueldo del empleado: ")
    new_employee_commission = input("Ingrese la nueva comisión del empleado: ")
    new_employee_position_id = input("Ingrese el nuevo ID del cargo del empleado: ")
    new_employee_department_id = input("Ingrese el nuevo ID del departamento del empleado: ")
    new_employee_boss_id = input("Ingrese el nuevo ID del jefe directo del empleado: ")
    new_employee_location_id = input("Ingrese el nuevo ID de la localización del empleado: ")
    data = {
        "command": "modify_employee",
        "employee_name": new_employee_name,
        "employee_id": employee_id,
        "employee_surname": new_employee_surname,
        "employee_email": new_employee_email,
        "employee_birth_date": new_employee_birth_date,
        "employee_salary": new_employee_salary,
        "employee_commission": new_employee_commission,
        "employee_position_id": new_employee_position_id,
        "employee_department_id": new_employee_department_id,
        "employee_boss_id": new_employee_boss_id,
        "employee_location_id": new_employee_location_id
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

def list_employees(client_socket):
    data = {
        "command": "list_employees"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    employees = client_socket.recv(1024).decode()
    print(employees)

def search_employee(client_socket):
    employee_id = input("Ingrese el ID del empleado: ")
    data = {
        "command": "search_employee",
        "employee_id": employee_id
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    employee = client_socket.recv(1024).decode()
    print(employee)

def delete_employee(client_socket):
    employee_id = input("Ingrese el ID del empleado: ")
    data = {
        "command": "delete_employee",
        "employee_id": employee_id
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    response = client_socket.recv(1024).decode()
    print(response)

# CRUD para históricos
def list_historical(client_socket):
    data = {
        "command": "list_historical"
    }
    json_data = json.dumps(data)
    client_socket.send(json_data.encode())
    historical = client_socket.recv(1024).decode()
    print(historical)


def start_client():
    client_socket = connect_to_server()
    
    while True:
        print("\n---------------------")
        print("1. Crear país")
        print("2. Listar países")
        print("3. Crear ciudad")
        print("4. Listar ciudades")
        print("5. Crear localización")
        print("6. Listar localizaciones")
        print("7. Crear departamento")
        print("8. Listar departamentos")
        print("9. Crear cargo")
        print("10. Listar cargos")
        print("11. Crear empleado")
        print("12. Modificar empleado")
        print("13. Listar empleados")
        print("14. Buscar empleado")
        print("15. Retirar empleado")
        print("16. Listar históricos")

        print("17. Salir")
        
        choice = input("Ingrese su opción: ")
        print("\n")
        
        if choice == "1":
            create_country(client_socket)
        elif choice == "2":
            list_countries(client_socket)
        elif choice == "3":
            create_city(client_socket)
        elif choice == "4":
            list_cities(client_socket)
        elif choice == "5":
            create_location(client_socket)
        elif choice == "6":
            list_locations(client_socket)
        elif choice == "7":
            create_department(client_socket)
        elif choice == "8":
            list_departments(client_socket)
        elif choice == "9":
            create_position(client_socket)
        elif choice == "10":
            list_positions(client_socket)
        elif choice == "11":
            create_employee(client_socket)
        elif choice == "12":
            modify_employee(client_socket)
        elif choice == "13":
            list_employees(client_socket)
        elif choice == "14":
            search_employee(client_socket)
        elif choice == "15":
            delete_employee(client_socket)
        elif choice == "16":
            list_historical(client_socket)
        elif choice == "17":
            break
        else:
            print("Opción invalida.")
    
    client_socket.close()

if __name__ == "__main__":
    start_client()
