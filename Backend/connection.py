from socket import gethostname

import pyodbc
import os
import pickle


class DatabaseConnection:
    """
        Conectando el front-end a la base de datos, aquí se escribe todo el código del backend, como insertar,
        actualizar, borrar, seleccionar
    """

    def __init__(self):
        # Frontend.connect_database.SaveDatabaseHost()
        self.file()

    def file(self):
        """
            Eliminando los archivos y extrayendo las credenciales de host, como:
            host, puerto, nombre de usuario, contraseña que luego se utilizan para conectarse a la base de datos
        """
        l = gethostname() + "\SQLEXPRESS"
        u = 'sa'
        pa = '12345678'
        self.d_connection(l, u, pa)

    def d_connection(self, host, username, password):
        """
            Tomando 4 argumentos funcionales el host es el dominio del servidor, el puerto es donde el servidor proxy
            reenvía,nombre de usuario es el nombre de usuario del host y la contraseña es la contraseña utilizada al
            configurar el usuario
        """
        server = gethostname() + "\SQLEXPRESS"

        self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=' + server + ';'
                                 'Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()

    def __del__(self):
        """
            Si la conexión se encuentra sin uso, esto cerrará de todos modos esa conexión
        """
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()

        except BaseException as msg:
            pass

    def create(self, query):
        """
            Utilizado para crear la base de datos en el host
        """
        self.cursor.execute(query)
        self.connection.commit()

    def search(self, query, values):
        """
            Buscar los valores de la base de datos
        """
        self.cursor.execute(query, values)
        data = self.cursor.fetchall()
        self.connection.commit()
        return data

    def insert(self, query, values):
        """
            Insertar valores desde la interfaz a la base de datos
        """
        self.cursor.execute(query, values)
        self.connection.commit()

    def select(self, query):
        """
            :returns data
        """
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        self.connection.commit()
        return data

    def update(self, query, values):
        """
            Actualiza los valores de la interfaz
        """
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete(self, query, values):
        """
            Elimina los valores de la interfaz
        """
        self.cursor.execute(query, values)
        self.connection.commit()


DatabaseConnection()
