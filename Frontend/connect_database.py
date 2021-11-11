from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
import random
import Backend.connection
import Frontend.login_form
from tkinter import messagebox
import Frontend.database_connected
import Model_class.connect_database
import pickle
import os


class ConnectDatabase:
    """
        Esta clase permite al usuario conectarse con el host y la base de datos utilizando GUI,
        el usuario puede elegir su host, puerto, nombre de usuario y contraseña de su servidor proxy
    """

    def __init__(self, root):
        self.root = root
        self.root.geometry("538x520")
        self.root.title("SYST_CONTROL(IFAP®) (CONEXIÓN AL SERVIDOR)")
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.resizable(False, False)

        # ======================Backendconnection=============
        self.db_connection = Backend.connection.DatabaseConnection()

        imagenes = {
            'new': PhotoImage(file='recursos\\icon_aceptar.png'),
            'login': PhotoImage(file='recursos\\icon_login.png'),
            'delete': PhotoImage(file='recursos\\icon_delete.png'),
            'exit': PhotoImage(file='recursos\\icon_del.png'),
        }

        # SaveDatabaseHost()
        self.Manage_Frame_Connec_ddbb = Frame(self.root, bd=4, bg='#a27114')
        self.Manage_Frame_Connec_ddbb.place(x=0, y=65, width=538, height=495)

        self.login_frame = ImageTk.PhotoImage(file='recursos\\connect_database_frame.png')
        self.image_panel = Label(self.Manage_Frame_Connec_ddbb, image=self.login_frame, bg='#a27114')
        self.image_panel.place(x=40, y=0)

        self.txt = "CONECTAR AL SERVIDOR"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35),
                             bg="#000000", fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=538)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ============================Host========================================
        # ========================================================================

        self.host_label = Label(self.Manage_Frame_Connec_ddbb, text="Host Name ", bg="#a27114", fg="Black",
                                font=("yu gothic ui", 13, "bold"))
        self.host_label.place(x=85, y=23)

        self.host_entry = Entry(self.Manage_Frame_Connec_ddbb, highlightthickness=0, relief=FLAT, bg="white",
                                fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.host_entry.insert(0, "localhost")
        self.host_entry.place(x=85, y=53, width=380)

        # ========================================================================
        # =============================Puerto=====================================
        # ========================================================================

        self.port_label = Label(self.Manage_Frame_Connec_ddbb, text="Port ", bg="#a27114", fg="Black",
                                font=("yu gothic ui", 13, "bold"))
        self.port_label.place(x=85, y=110)

        self.port_entry = Entry(self.Manage_Frame_Connec_ddbb, highlightthickness=0, relief=FLAT, bg="white",
                                fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.port_entry.insert(0, "3306")
        self.port_entry.place(x=85, y=140, width=380)

        # ========================================================================
        # ============================Usuario=====================================
        # ========================================================================

        self.username_label = Label(self.Manage_Frame_Connec_ddbb, text="Username ", bg="#a27114", fg="Black",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=85, y=210)

        self.username_entry = Entry(self.Manage_Frame_Connec_ddbb, highlightthickness=0, relief=FLAT, bg="white",
                                    fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.username_entry.insert(0, "root")
        self.username_entry.place(x=85, y=240, width=380)  # trebuchet ms

        # ========================================================================
        # ===========================Contraseña===================================
        # ========================================================================

        self.password_label = Label(self.Manage_Frame_Connec_ddbb, text="Password ", bg="#a27114", fg="Black",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=85, y=300)

        self.password_entry = Entry(self.Manage_Frame_Connec_ddbb, highlightthickness=0, relief=FLAT, bg="white",
                                    fg="#6b6a69", font=("yu gothic ui semibold", 12))
        self.password_entry.insert(0, "root")
        self.password_entry.place(x=85, y=330, width=380)

        # ========================================================================
        # ============================Guardar Datos===============================
        # ========================================================================
        self.submit_button = Button(self.Manage_Frame_Connec_ddbb, image=imagenes['new'], text=' GUARDAR ',
                                    font=("yu gothic ui", 13, "bold"), command=self.click_submit, compound="left")
        self.submit_button.image = imagenes['new']
        self.submit_button.place(x=5, y=400, width=120)

        # ========================================================================
        # =====================Botón de inicio de sesión==========================
        # ========================================================================
        self.login_button = Button(self.Manage_Frame_Connec_ddbb, image=imagenes['login'], text=' INGRESAR ',
                                   font=("yu gothic ui", 13, "bold"), command=self.click_login, compound="left")
        self.login_button.image = imagenes['login']
        self.login_button.place(x=130, y=400, width=120)

        # ========================================================================
        # =======================Borrar la base de datos==========================
        # ========================================================================
        self.delete_button = Button(self.Manage_Frame_Connec_ddbb, image=imagenes['delete'], text=' ELIMINAR DDBB ',
                                    font=("yu gothic ui", 13, "bold"), command=self.click_wipe, compound="left")
        self.delete_button.image = imagenes['delete']
        self.delete_button.place(x=255, y=400, width=165)

        # ========================================================================
        # ============================BOTÓN SALIR=================================
        # ========================================================================
        self.exit_button = Button(self.Manage_Frame_Connec_ddbb, image=imagenes['exit'], text=' SALIR ',
                                  font=("yu gothic ui", 13, "bold"), command=self.click_exit, compound="left")
        self.exit_button.image = imagenes['exit']
        self.exit_button.place(x=425, y=400, width=100)

        # ========================================================================
        # ==================Instrucción de la base de datos=======================
        # ========================================================================

        self.database_ins_label = Label(self.Manage_Frame_Connec_ddbb, text="Ingrese las credenciales de inicio de "
                                                                            "sesión del servidor y guarde.**",
                                        bg="white", fg="#4f4e4d", font=("yu gothic ui", 10, "bold"))
        self.database_ins_label.place(x=75, y=365)

    def slider(self):

        """
            Crea diapositivas para el encabezamiento tomando el texto
            y ese texto se llama cada 100 ms
        """

        if self.count >= len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text + self.txt[self.count]
            self.heading.config(text=self.text)
        self.count += 1

        self.heading.after(100, self.slider)

    def heading_color(self):

        """
            configures heading label
            :return: every 50 ms returned new random color.
        """

        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def store_database(self):

        """
        toma como parámetros las entradas del usuario para la conexión al servidor
        """

        self.dictcred = {}

        le = os.path.getsize("database_data.txt")

        host = self.host_entry.get()
        port = self.port_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # verifica si las entradas están vacías
        if host == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "RELLENE EL CAMPO: Host")
            self.host_entry.focus()

        elif port == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "RELLENE EL CAMPO: Port")
            self.port_entry.focus()

        elif username == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "RELLENE EL CAMPO: Username")
            self.username_entry.focus()

        elif password == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "RELLENE EL CAMPO: Password")
            self.password_entry.focus()

        else:
            self.listcred1 = [host, port, username, password]
            di = {1: self.listcred1}

            if le == 0:
                f = open("database_data.txt", "wb")
                self.dictcred.update(di)
                pickle.dump(self.dictcred, f)
                messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", "CONEXIÓN AL SERVIDOR HA SIDO GUARDADA "
                                                                     "CORRECTAMENTE")
                f.close()

            else:
                messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "YA SE ENCUENTRA CONECTADO AL "
                                                                              "SERVIDOR\n ¿DESEA DESCONECTARSE?")

    def click_submit(self):
        """
            Si hay algún valor en el archivo .txt, crea una nueva base de datos llamada 'ifap'
            después de eso, se crean todas las tablas de la base de datos requerida.
        """

        try:
            le = os.path.getsize("./database_data.txt")
            if le == 0:
                obj_connect_db = Model_class.connect_database.ConnectDatabase(self.host_entry.get(),
                                                                              self.port_entry.get(),
                                                                              self.username_entry.get(),
                                                                              self.password_entry.get())
                self.db_connection.d_connection(obj_connect_db.get_host(), obj_connect_db.get_port(),
                                                obj_connect_db.get_username(),
                                                obj_connect_db.get_password())
                messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", "CONEXION AL SERVIDOR EXITOSA")
                self.store_database()

                try:
                    obj_create_database = Model_class.connect_database.CreateDatabase('CREATE DATABASE IF NOT EXISTS '
                                                                                      'ddbb_sys_ifap;')
                    self.db_connection.create(obj_create_database.get_database())
                    messagebox.showinfo("ÉXITO", "BASE DE DATOS \n ddbb_sys_ifap\n CREADA SATISFACTORIAMENTE")
                    self.create_tables()

                except BaseException as msg:
                    obj_create_database = Model_class.connect_database.CreateDatabase('USE ddbb_sys_ifap;')
                    self.db_connection.create(obj_create_database.get_database())
                    messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"CREACIÓN DE BASE DE DATOS INTERRUMPIDA,\n"
                                                                          f"YA EXISTE LA BASE DE DATOS!\n {msg}")
                    return

            else:
                messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", "ES POSIBLE QUE LA BASE DE DATOS YA ESTÉ "
                                                                      "CONECTADA")
                """self.create_tables()"""

        except BaseException as msg:

            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE AL SERVIDOR\n {msg}")
            return

    def create_tables(self):
        try:
            obj_create_database = Model_class.connect_database.CreateDatabase('USE ddbb_sys_ifap;')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS usuarios('
                'id_usuario int AUTO_INCREMENT NOT NULL,'
                'usuario varchar(256) NOT NULL,'
                'email varchar(100) NOT NULL,'
                'contrasena varchar(254) NOT NULL,'
                'tipo VARCHAR(20) NOT NULL,'
                'PRIMARY KEY (id_usuario),'
                'UNIQUE (usuario),'
                'UNIQUE (email));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS auditoria_usuarios('
                'id_auditoria int AUTO_INCREMENT NOT NULL,'
                'usuario varchar(50) NOT NULL,'
                'accion varchar(50) NOT NULL,'
                'fecha DATE NOT NULL,'
                'hora TIME NOT NULL,'
                'PRIMARY KEY (id_auditoria));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS estudiantes('
                'id_estudiante VARCHAR(20) NOT NULL,'
                'nombres VARCHAR(50) NOT NULL,'
                'apellidos VARCHAR(50) NOT NULL,'
                'edad INT NOT NULL,'
                'direccion VARCHAR(100) NOT NULL,'
                'correo VARCHAR(50) NOT NULL,'
                'celular VARCHAR(20) NOT NULL,'
                'telefono VARCHAR(20) NOT NULL,'
                'representante VARCHAR(50),'
                'cedula_r VARCHAR(20),'
                'observacion VARCHAR(50) NOT NULL,'
                'PRIMARY KEY (id_estudiante),'
                'UNIQUE (nombres));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS asesores('
                'id_asesor VARCHAR(20) NOT NULL,'
                'nombres VARCHAR(50) NOT NULL,'
                'apellidos VARCHAR(50) NOT NULL,'
                'direccion VARCHAR(50) NOT NULL,'
                'correo VARCHAR(50) NOT NULL,'
                'celular VARCHAR(20) NOT NULL,'
                'PRIMARY KEY (id_asesor),'
                'UNIQUE (apellidos));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS cursos('
                'id_curso INT AUTO_INCREMENT NOT NULL,'
                'nombre_curso VARCHAR(50),'
                'costo_matricula REAL,'
                'costo_mensual REAL,'
                'PRIMARY KEY (id_curso),'
                'UNIQUE (nombre_curso));')
            self.db_connection.create(obj_create_database.get_database())

            """obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS dias('
                'id_dia INT AUTO_INCREMENT NOT NULL,'
                'dia VARCHAR(20) NOT NULL,'
                'PRIMARY KEY (id_dia),'
                'UNIQUE (dia));')
            self.db_connection.create(obj_create_database.get_database())"""

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS horas('
                'id_hora INT AUTO_INCREMENT,'
                'hora VARCHAR(20),'
                'PRIMARY KEY (id_hora),'
                'UNIQUE (hora));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS paralelos('
                'id_paralelo INT AUTO_INCREMENT NOT NULL,'
                'nombre_curso VARCHAR(50) NOT NULL,'
                'nombre_paralelo VARCHAR(50) NOT NULL,'
                'dia VARCHAR(20) NOT NULL,'
                'hora VARCHAR(50) NOT NULL,'
                'fecha_inicio DATE NOT NULL,'
                'fecha_fin DATE NOT NULL,'
                'duracion VARCHAR(20) NOT NULL,'
                'PRIMARY KEY (id_paralelo),'
                'UNIQUE (nombre_paralelo));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS implementos('
                'id_implemento INT AUTO_INCREMENT,'
                'descripcion VARCHAR(50) NOT NULL,'
                'costo_implemento REAL NOT NULL,'
                'PRIMARY KEY (id_implemento),'
                'UNIQUE (descripcion));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS matriculas('
                'id_matricula VARCHAR(20) NOT NULL,'
                'estudiante VARCHAR(100) NOT NULL,'
                'paralelo VARCHAR(50) NOT NULL,'
                'asesor VARCHAR(50) NOT NULL,'
                'PRIMARY KEY (id_matricula),'
                'UNIQUE (estudiante));')
            self.db_connection.create(obj_create_database.get_database())

            """obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS facturas('
                'id_factura VARCHAR(20) NOT NULL,'
                'id_estudiante VARCHAR(20) NOT NULL,'
                'fecha VARCHAR(50) NOT NULL,'
                'hora VARCHAR(50) NOT NULL,'
                'PRIMARY KEY (id_factura));')
            self.db_connection.create(obj_create_database.get_database())

            obj_create_database = Model_class.connect_database.CreateDatabase(
                'CREATE TABLE IF NOT EXISTS detalle_facturas('
                'id_detalle_factura VARCHAR(20) NOT NULL,'
                'id_factura VARCHAR(20) NOT NULL,'
                'id_implemento INT NOT NULL,'
                'cantidad VARCHAR(50) NOT NULL,'
                'total_factura VARCHAR(50) NOT NULL,'
                'PRIMARY KEY (id_detalle_factura),'
                'FOREIGN KEY (id_Factura) REFERENCES facturas (id_factura),'
                'FOREIGN KEY (id_implemento) REFERENCES implementos (id_implemento));')
            self.db_connection.create(obj_create_database.get_database())"""

            messagebox.showinfo("ÉXITO!!!", "TABLAS DE LA BASE DE DATOS CREADAS CORRECTAMENTE.")

        except BaseException as msg:
            messagebox.showerror("ERROR!!!", f"FALLÓ AL CREAR LAS TABLAS EN LA BASE DE DATOS,\n{msg}")

        ask = messagebox.askokcancel("ADMINISTRADOR DE CONFIGURACIÓN",
                                     "¿CONFIGUAR INICIO DE SESIÓN POR PRIMERA "
                                     "VEZ?, \n TARDARÁ SOLO UNOS SEGUNDOS.....")
        if ask is True:
            root = Toplevel()
            Frontend.database_connected.DatabaseConnected(root)
            self.root.withdraw()
            root.deiconify()

    def click_login(self):
        """
           Cuando se hace clic en el botón de inicio de sesión, dirigirá a ese usuario al formulario de inicio de sesión
        """
        win = Toplevel()
        Frontend.login_form.Login(win)
        self.root.withdraw()
        win.deiconify()

    def click_exit(self):
        """
            when clicked exit button
            :return self.widow.quit()
        """
        ask = messagebox.askokcancel("SALIR", "¿ESTÁS SEGURO/A DE SALIR DEL SISTEMA?")
        if ask is True:
            self.root.quit()

    def click_wipe(self):
        try:
            ask = messagebox.askokcancel("ELIMINAR", "¿ESTÁS SEGURO/A DE BORRAR LA BASE DE DATOS DEL SISTEMA??\n"
                                                     "TUS DATOS SERÁN GUARDADOS!!!")
            if ask is True:
                obj_create_database = Model_class.connect_database.CreateDatabase('use ddbb_sys_ifap;')
                self.db_connection.create(obj_create_database.get_database())

                obj_create_database = Model_class.connect_database.CreateDatabase('drop database ddbb_sys_ifap;')
                self.db_connection.create(obj_create_database.get_database())
                messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", f"BASE DE DATOS ELIMINADA EXITOSAMENTE")

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"DEBE DE CONECTARSE PRIMERO A LA BASE DE DATOS,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")


class SaveDatabaseHost(Backend.connection.DatabaseConnection):
    """
        Hereda la clase DatabaseConnection del backend y extiende la funcionalidad
        obteniendo los datos del archivo .txt y estableciendo esos datos en el host actual para hacer
        conexión con la base de datos.
    """

    def __init__(self):

        super().__init__()
        self.file()

    def file(self):
        self.len = os.path.getsize("./database_data.txt")
        if self.len > 0:
            f = open("./database_data.txt", "rb")
            self.dictcred = pickle.load(f)

            for k, p in self.dictcred.items():
                l = p[0]
                po = p[1]
                u = p[2]
                pa = p[3]
                self.d_connection(l, po, u, pa)


def root():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    ConnectDatabase(root)
    root.mainloop()


if __name__ == '__main__':
    root()
