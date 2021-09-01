from socket import gethostname
from tkinter import messagebox

import pyodbc

driver = "{ODBC Driver 17 for SQL Server}"
server = gethostname() + "\SQLEXPRESS"
database = "ddbb_sys_ifap"
try:
    conn = pyodbc.connect('DRIVER=' + driver + ';'
                                               'SERVER=' + server + ';'
                                                                    'Database=' + database + ';'
                                                                                             'Trusted_Connection=yes;')
except BaseException as msg:
    messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                         f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                         f"REVISE LA CONEXIÓN: {msg}")
