from socket import gethostname
from tkinter import messagebox
import pyodbc


def conexion_consulta(consulta, parametros=()):
    driver = "{ODBC Driver 17 for SQL Server}"
    server = gethostname() + "\SQLEXPRESS"
    database = "ddbb_sys_ifap"
    try:
        conn = pyodbc.connect('DRIVER=' + driver + ';'
                                                   'SERVER=' + server + ';'
                                                                        'Database=' + database + ';'
                                                                                                 'Trusted_Connection'
                                                                                                 '=yes;')
        cursor = conn.cursor()
        conexion_consulta(consulta, parametros)
        resultado = cursor.execute(consulta, parametros)  # Establece la consulta sql a realizar y sus parametros
        conn.commit()

        return resultado

    except BaseException as msg:
        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                              f"REVISE LA CONEXIÓN: {msg}")

