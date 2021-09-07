# Import Modules
from _datetime import datetime

import mariadb
from tkinter import *
from tkinter import messagebox, ttk

import Frontend.login_form
import Frontend.Secretary.Principal_Window_S
import Frontend.Secretary.Student_Window_S
import Frontend.Secretary.Matricula_Window_S
import Frontend.Secretary.Assesor_Window_S
import Frontend.Secretary.Course_Window_S
import Frontend.Secretary.Paralelo_Window_S
import Frontend.Secretary.Implements_Window_S
import Frontend.Secretary.Password_Window_S

class Assesor_S:

    def __init__(self, root):

        self.root = root
        self.root.title("SYST_CONTROL--›Asesores")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_aceptar.png'),
            'matricular': PhotoImage(file='./recursos/icon_add.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'eliminar': PhotoImage(file='./recursos/icon_del.png'),
            'limpiar': PhotoImage(file='./recursos/icon_clean.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),

        }

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (ASESORES)')
        self.texto1.config(font=("Copperplate Gothic Bold", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=475, pady=0)

        # =============================================================
        # CREACIÓN DE LA BARRA DE MENÚ
        # =============================================================
        self.menubarra = Menu(self.root)

        # =============================================================
        # CREACIÓN DEL MENÚ
        # =============================================================
        self.menubarra.add_cascade(label='ALUMNOS')
        self.root.config(menu=self.menubarra)
        self.menus = Menu(self.root)
        self.Column1 = Menu(self.menus, tearoff=0)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ PRINCIPAL
        # =============================================================
        self.menus.add_cascade(label='INICIO', menu=self.Column1)
        self.Column1.add_command(label='Menú Inicio', command=self.principal_btn)
        self.Column2 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ ALUMNO
        # =============================================================
        self.menus.add_cascade(label='ALUMNOS', menu=self.Column2)
        self.Column2.add_command(label='Menú Alumnos', command=self.student_btn)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL MENÚ ASESORES
        # =============================================================
        self.menus.add_cascade(label='ASESORES', menu=self.Column3)
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ CURSOS
        # =============================================================
        self.menus.add_cascade(label='CURSOS', menu=self.Column4)
        self.Column4.add_command(label='Menú Cursos', command=self.courses_btn)
        self.Column5 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column5)
        self.Column5.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column5.add_command(label='Cambiar Contraseña', command=self.pass_btn)
        self.Column5.add_separator()
        self.Column5.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column5.add_separator()
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column6)
        self.Column6.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column6.add_separator()
        self.Column6.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column6.add_separator()
        self.root.config(menu=self.menus)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10), bg='Honeydew2',
                            relief=RIDGE)
        self.footer.place(x=0, y=703)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='Honeydew2',
                              relief=RIDGE)
        self.footer_1.place(x=212, y=704)

        self.footer_4 = Label(self.root, text='DESING® | Derechos Reservados 2021', width=195, bg='black', fg='white')
        self.footer_4.place(x=0, y=725)

        # Variables
        self.n_ced_as = StringVar()
        self.nombres_as = StringVar()
        self.apellidos_as = StringVar()
        self.direccion_as = StringVar()
        self.correo_as = StringVar()
        self.n_celular_as = StringVar()
        self.as_tot = IntVar()

        self.search_field_as = StringVar()

        # Manage Frame
        Manage_Frame = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        Manage_Frame.place(x=15, y=75, width=385, height=605)

        m_title = Label(Manage_Frame, text="-ADMINISTAR ASESORES-", font=("Copperplate Gothic Bold", 16, "bold"),
                        bg='#0d1e24', fg="White")
        m_title.grid(row=0, columnspan=2, padx=25, pady=50)

        self.l_cedula = Label(Manage_Frame, text='No. CÉDULA', width='15', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_cedula.grid(column=0, row=1, padx=1, pady=5)
        self.e_cedula = Entry(Manage_Frame, textvariable=self.n_ced_as, width='13')
        self.e_cedula.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_cedula.focus()

        self.l_nombres = Label(Manage_Frame, text='NOMBRES', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_nombres.grid(column=0, row=2, padx=0, pady=5)
        self.e_nombres = Entry(Manage_Frame, textvariable=self.nombres_as, width='33')
        self.e_nombres.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_apellidos = Label(Manage_Frame, text='APELLIDOS', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_apellidos.grid(column=0, row=3, padx=1, pady=5)
        self.e_apellidos = Entry(Manage_Frame, textvariable=self.apellidos_as, width='33')
        self.e_apellidos.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        self.l_direccion = Label(Manage_Frame, text='DIRECCIÓN', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_direccion.grid(column=0, row=5, padx=1, pady=5)
        self.e_direccion = Entry(Manage_Frame, textvariable=self.direccion_as, width='33')
        self.e_direccion.grid(column=1, row=5, padx=1, pady=5, sticky="W")

        self.l_correo = Label(Manage_Frame, text='CORREO', width='15', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_correo.grid(column=0, row=6, padx=1, pady=5)
        self.e_correo = Entry(Manage_Frame, textvariable=self.correo_as, width='33')
        self.e_correo.grid(column=1, row=6, padx=1, pady=5, sticky="W")

        self.l_celular = Label(Manage_Frame, text='No. CELULAR', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_celular.grid(column=0, row=7, padx=1, pady=5)
        self.e_celular = Entry(Manage_Frame, textvariable=self.n_celular_as, width='13')
        self.e_celular.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame_as = Frame(Manage_Frame, bg='#0d1e24')
        self.btn_frame_as.place(x=5, y=510, width=360)

        self.add_btn = Button(self.btn_frame_as, image=imagenes['matricular'], text='REGISTAR', width=80,
                              command=self.add_asessor, compound=TOP)
        self.add_btn.image = imagenes['matricular']
        self.add_btn.grid(row=0, column=1, padx=3, pady=10)

        self.update_btn = Button(self.btn_frame_as, image=imagenes['editar'], text='MODIFICAR', width=80,
                                 command=self.update_as, compound=TOP)
        self.update_btn.image = imagenes['editar']
        self.update_btn.grid(row=0, column=2, padx=3, pady=10)
        self.update_btn["state"] = "disabled"

        self.delete_btn = Button(self.btn_frame_as, image=imagenes['eliminar'], text='ELIMINAR', width=80,
                                 command=self.delete_as, compound=TOP)
        self.delete_btn.image = imagenes['eliminar']
        self.delete_btn.grid(row=0, column=3, padx=3, pady=10)
        self.delete_btn["state"] = "disabled"

        self.clear_btn = Button(self.btn_frame_as, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_as, compound=TOP)
        self.clear_btn.image = imagenes['limpiar']
        self.clear_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=405, y=75, width=940, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field_as,
                                font=("Arial", 10, "bold"), bd=5,
                                relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_as, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_as, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame
        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=920, height=525)

        Y_scroll = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame, columns=("ci", "nom", "ape", "dir", "cor", "cel"),
                                  yscrollcommand=Y_scroll.set)

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.Table.yview)
        # bg="#00A1E4", fg="#FFFCF9", font=("Arial", 10, "bold")
        self.Table.heading("ci", text="No. C.I")
        self.Table.heading("nom", text="NOMBRES")
        self.Table.heading("ape", text="APELLIDOS")
        self.Table.heading("dir", text="DIRECCIÓN")
        self.Table.heading("cor", text="CORREO")
        self.Table.heading("cel", text="CELULAR")

        self.Table['show'] = "headings"
        self.Table.column("ci", width=20)
        self.Table.column("nom", width=70)
        self.Table.column("ape", width=70)
        self.Table.column("dir", width=150)
        self.Table.column("cor", width=150)
        self.Table.column("cel", width=20)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_as)

        self.show_data_as()

    def add_asessor(self):
        if self.n_ced_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA")
            self.e_cedula.focus()

        elif self.nombres_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: NOMBRES")
            self.e_nombres.focus()

        elif self.apellidos_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: APELLIDOS")
            self.e_apellidos.focus()

        elif self.direccion_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: DIRECCIÓN")
            self.e_direccion.focus()

        elif self.correo_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: CORREO")
            self.e_correo.focus()

        elif self.n_celular_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. DE CELULAR")
            self.e_celular.focus()

        else:
            cone = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            cursor = cone.cursor()
            sql = "INSERT INTO asesores(id_estudiante, nombres, apellidos, direccion, correo, celular) " \
                  "VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (self.n_ced_as.get(), self.nombres_as.get(), self.apellidos_as.get(),
                                 self.direccion_as.get(), self.correo_as.get(), self.n_celular_as.get()))
            cone.commit()

            self.n_ced_as.set('')
            self.nombres_as.set('')
            self.apellidos_as.set('')
            self.direccion_as.set('')
            self.correo_as.set('')
            self.n_celular_as.set('')
            self.e_cedula.focus()

            self.show_data_as()
            # self.clear_field()
            cone.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ASESOR GUARDADOS EN EL REGISTRO CORRECTAMENTE!!!")

    def asesores_t(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("SELECT COUNT(id_asesor) FROM asesores")
        self.rows_t = self.curr.fetchall()
        return self.rows_t

    def clear_field_as(self):
        self.n_ced_as.set('')
        self.nombres_as.set('')
        self.apellidos_as.set('')
        self.direccion_as.set('')
        self.correo_as.set('')
        self.n_celular_as.set('')
        self.e_cedula.focus()
        self.update_btn["state"] = "disabled"
        self.delete_btn["state"] = "disabled"

    def get_fields_as(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.n_ced_as.set(row[0])
        self.nombres_as.set(row[1])
        self.apellidos_as.set(row[2])
        self.direccion_as.set(row[3])
        self.correo_as.set(row[4])
        self.n_celular_as.set(row[5])

        self.add_btn["state"] = "normal"
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

    def update_as(self):
        if self.n_ced_as.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE MODIFICAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()

            sql = f"""UPDATE asesores SET nombres="{self.nombres_as.get()}", apellidos="{self.apellidos_as.get()}",\
                                direccion="{self.direccion_as.get()}", correo="{self.correo_as.get()}",\
                                celular="{self.n_celular_as.get()}" WHERE id_asesor={self.n_ced_as.get()}"""
            self.curr.execute(sql)
            self.connect.commit()

            self.show_data_as()
            # self.connect.close()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ASESOR: " + self.nombres_as.get() +
                                " CON No. C.I: " + self.n_ced_as.get() + " HAN SIDO ACTUALIZADOS EN EL "
                                                                         "REGISTRO CORRECTAMENTE!!!")
            self.n_ced_as.set('')
            self.nombres_as.set('')
            self.apellidos_as.set('')
            self.direccion_as.set('')
            self.correo_as.set('')
            self.n_celular_as.set('')
            self.e_cedula.focus()

    def delete_as(self):
        if self.n_ced_as.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.conn.cursor()

            self.sql = f"""DELETE FROM asesores WHERE id_asesor={self.n_ced_as.get()}"""
            # self.sql = "DELETE FROM estudiantes WHERE cedula= %"
            # self.curr.execute(self.sql, self.datos)
            self.curr.execute(self.sql)

            self.conn.commit()

            self.show_data_as()
            self.clear_field_as()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ESTUDIANTE ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")

    def search_data_as(self):
        if self.search_field_as.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA")
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_n_ced_as = self.search_field_as.get()
        sql = f"""SELECT id_asesor FROM asesores WHERE id_asesor = {self.search_n_ced_as}"""
        self.curr.execute(sql)
        self.curr.fetchall()
        if self.curr.rowcount == 1:
            self.sql = f"""SELECT id_asesor, nombres, apellidos, direccion, correo, celular FROM asesores\
                    WHERE id_asesor={self.search_n_ced_as}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                self.Table.delete(*self.Table.get_children())
                for self.row in self.rows:
                    self.Table.insert('', END, values=self.row)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO DEL ASESOR CON EL No. DE CÉDULA: " +
                                 self.search_n_ced_as)
            self.search_field_as.set('')

    def show_data_as(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS asesores("
                          "id_asesor VARCHAR(20) PRIMARY KEY,"
                          "nombres VARCHAR(50),"
                          "apellidos VARCHAR(50),"
                          "direccion VARCHAR(50),"
                          "correo VARCHAR(50),"
                          "celular VARCHAR(20))")

        self.curr.execute("SELECT * FROM asesores ORDER BY id_asesor ASC")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table.delete(*self.Table.get_children())
            for self.row in self.rows:
                self.Table.insert('', END, values=self.row)

            self.connect.commit()
        self.connect.close()

    def logout(self):
        self.root.destroy()

        from Login_Window import Login
        st_root = Tk()
        Login(st_root)
        st_root.mainloop()

    def principal_btn(self):
        self.root.destroy()

        from Secretaria.Principal_Window_S import Principal_S
        st_root = Tk()
        Principal_S(st_root)
        st_root.mainloop()

    def student_btn(self):
        self.root.destroy()

        from Secretaria.Student_Window_S import Student_S
        st_root = Tk()
        Student_S(st_root)
        st_root.mainloop()

    def courses_btn(self):
        self.root.destroy()

        from Secretaria.Course_Window_S import Course_S
        st_root = Tk()
        Course_S(st_root)
        st_root.mainloop()

    def pass_btn(self):
        self.root.destroy()

        from Secretaria.Password_Window_S import Password_S
        st_root = Tk()
        Password_S(st_root)
        st_root.mainloop()

    def salir_principal(self):
        self.sa = messagebox.askyesno('CERRAR SESIÓN', 'CERRAR SYST_CONTROL(IFAP®)')
        if self.sa:
            exit()

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL INSTITUTO(INFO)
    # =============================================================
    def caja_info_ifap(self):
        self.men1 = messagebox.showinfo('SIST_CONTROL (IFAP®)', 'INSTITUTO DE FORMACIÓN ACADEMICA PROEZAS(IFAP®)')

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL SISTEMA(INFO)
    # =============================================================
    def caja_info_sist(self):
        self.men2 = messagebox.showinfo('SIST_CONTROL (IFAP®)',
                                        'SIST_CONTROL (IFAP®) v2.0\n'
                                        'El uso de este software queda sujeto a los términos y condiciones del '
                                        'contrato "BJM DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 BJM DESING®. Todos los derechos reservados')


if __name__ == '__main__':
    root = Tk()
    application = Assesor_S(root)
    root.mainloop()
