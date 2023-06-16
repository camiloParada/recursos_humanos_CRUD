import socket
import mysql.connector
import json
import signal
import sys
from countries import create_country, list_countries
from cities import create_city, list_cities
from locations import create_location, list_locations
from departments import create_department, list_departments
from positions import create_position, list_positions
from employees import create_employee, modify_employee, list_employees, search_employee, delete_employee
from historical import list_historical

def handle_client_connection(client_socket, db_connection):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        json_data = json.loads(data)
        command = json_data["command"]
        
        if command == "create_country":
            client_socket.send(create_country(db_connection, json_data["country_name"]).encode())
        elif command == "list_countries":
            client_socket.send(str(list_countries(db_connection)).encode())
        elif command == "create_city":
            client_socket.send(create_city(db_connection, json_data).encode())
        elif command == "list_cities":
            client_socket.send(str(list_cities(db_connection)).encode())
        elif command == "create_location":
            client_socket.send(create_location(db_connection, json_data).encode())
        elif command == "list_locations":
            client_socket.send(str(list_locations(db_connection)).encode())
        elif command == "create_department":
            client_socket.send(create_department(db_connection, json_data["department_name"]).encode())
        elif command == "list_departments":
            client_socket.send(str(list_departments(db_connection)).encode())
        elif command == "create_position":
            client_socket.send(create_position(db_connection, json_data).encode())
        elif command == "list_positions":
            client_socket.send(str(list_positions(db_connection)).encode())
        elif command == "create_employee":
            client_socket.send(create_employee(db_connection, json_data).encode())
        elif command == "modify_employee":
            client_socket.send(modify_employee(db_connection, json_data).encode())
        elif command == "list_employees":
            client_socket.send(str(list_employees(db_connection)).encode())
        elif command == "search_employee":
            client_socket.send(str(search_employee(db_connection, json_data["employee_id"])).encode())
        elif command == "delete_employee":
            client_socket.send(delete_employee(db_connection, json_data["employee_id"]).encode())
        elif command == "list_historical":
            client_socket.send(str(list_historical(db_connection)).encode())
        else:
            client_socket.send("Petición invalida.".encode())
            break

def handle_interrupt(signal, frame):
    print("Interrupción detectada. Cerrando el servidor...")
    sys.exit(0)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 4200))
    server_socket.listen(1)
    
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="pass1234",
        database="recursos_humanos"
    )
    
    print("Servidor iniciado. Escuchando conexiones...")
   
    while True:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Cliente conectado: {client_address}")
            handle_client_connection(client_socket, db_connection)
            client_socket.close()      
        except KeyboardInterrupt:
            server_socket.close()
            handle_interrupt(signal.SIGINT, None)
            

if __name__ == "__main__":
    start_server()

