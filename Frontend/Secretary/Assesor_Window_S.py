# Import Modules
import random
from _datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk

import Backend.connection
import Model_class.assesor_registration

import Frontend.login_form
import Frontend.Secretary.Principal_Window_S
import Frontend.Secretary.Student_Window_S
import Frontend.Secretary.Matricula_Window_S
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
            'nuevo': PhotoImage(file='recursos\\icon_aceptar.png'),
            'matricular': PhotoImage(file='recursos\\icon_add.png'),
            'editar': PhotoImage(file='recursos\\icon_update.png'),
            'eliminar': PhotoImage(file='recursos\\icon_del.png'),
            'limpiar': PhotoImage(file='recursos\\icon_clean.png'),
            'buscar': PhotoImage(file='recursos\\icon_buscar.png'),
            'todo': PhotoImage(file='recursos\\icon_ver_todo.png'),
            'actualizar': PhotoImage(file='recursos\\icon_upd.png')

        }

        # =============================================================
        # BANNER PANTALLA ASESORES
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (ASESORES)"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=1367)

        self.slider()
        self.heading_color()

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

        # =============================================================
        # CREACIÓN DE LA BARRA DE MENÚ
        # =============================================================
        self.menubarra = Menu(self.root)

        # =============================================================
        # CREACIÓN DEL MENÚ
        # =============================================================
        self.menubarra.add_cascade(label='ASESORES')
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
        self.Column2.add_command(label='Alumnos', command=self.student_btn)
        self.Column2.add_command(label='Matriculación', command=self.matricula_btn)
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
        self.Column4.add_command(label='Cursos', command=self.courses_btn)
        self.Column4.add_command(label='Paralelos', command=self.paralelos_btn)
        self.Column4.add_command(label='Implementos', command=self.implements_btn)
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
        self.Column6.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column6.add_separator()
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DE PIÉ DE PANTALLA
        # =============================================================
        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=195, bg='black',
                              fg='white')
        self.footer_4.place(x=0, y=725)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y"

        self.footer = Label(self.root, text='  FECHA Y HORA: ', font=("Cooper Black", 9), bg='black',
                            fg='white')
        self.footer.place(x=930, y=725)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='black',
                              fg='white')
        self.footer_1.place(x=1040, y=727)

        self.clock = Label(self.root)
        self.clock['text'] = '00:00:00'
        self.clock['font'] = 'Tahoma 9 bold'
        self.clock['bg'] = 'black'
        self.clock['fg'] = 'white'
        self.clock.place(x=1275, y=725)
        self.tic()
        self.tac()

        # Manage Frame
        Manage_Frame = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        Manage_Frame.place(x=15, y=85, width=385, height=605)

        # Variables
        self.e_n_ced_as = StringVar()
        self.e_nombres_as = StringVar()
        self.e_apellidos_as = StringVar()
        self.e_direccion_as = StringVar()
        self.e_correo_as = StringVar()
        self.e_n_celular_as = StringVar()

        self.search_entry = StringVar()

        m_title = Label(Manage_Frame, text="-ADMINISTAR ASESORES-", font=("Copperplate Gothic Bold", 16, "bold"),
                        bg='#a27114', fg="White")
        m_title.grid(row=0, columnspan=2, padx=25, pady=50)

        self.l_cedula = Label(Manage_Frame, text='No. CÉDULA', width='15', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_cedula.grid(column=0, row=1, padx=1, pady=5)
        self.e_cedula = Entry(Manage_Frame, textvariable=self.e_n_ced_as, width='13')
        self.e_cedula.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_cedula.focus()

        self.l_nombres = Label(Manage_Frame, text='NOMBRES', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_nombres.grid(column=0, row=2, padx=0, pady=5)
        self.e_nombres = Entry(Manage_Frame, textvariable=self.e_nombres_as, width='33')
        self.e_nombres.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_apellidos = Label(Manage_Frame, text='APELLIDOS', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_apellidos.grid(column=0, row=3, padx=1, pady=5)
        self.e_apellidos = Entry(Manage_Frame, textvariable=self.e_apellidos_as, width='33')
        self.e_apellidos.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        self.l_direccion = Label(Manage_Frame, text='DIRECCIÓN', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_direccion.grid(column=0, row=5, padx=1, pady=5)
        self.e_direccion = Entry(Manage_Frame, textvariable=self.e_direccion_as, width='33')
        self.e_direccion.grid(column=1, row=5, padx=1, pady=5, sticky="W")

        self.l_correo = Label(Manage_Frame, text='CORREO', width='15', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_correo.grid(column=0, row=6, padx=1, pady=5)
        self.e_correo = Entry(Manage_Frame, textvariable=self.e_correo_as, width='33')
        self.e_correo.grid(column=1, row=6, padx=1, pady=5, sticky="W")

        self.l_celular = Label(Manage_Frame, text='No. CELULAR', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_celular.grid(column=0, row=7, padx=1, pady=5)
        self.e_celular = Entry(Manage_Frame, textvariable=self.e_n_celular_as, width='13')
        self.e_celular.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame_as = Frame(Manage_Frame, bg='#a27114')
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
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#a27114')
        self.Detail_Frame.place(x=405, y=85, width=940, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_entry,
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

        self.click_home()

        self.act_btn = Button(self.Detail_Frame, image=imagenes['actualizar'], text='ACTUALIZAR', width=100,
                              command=self.assesor_btn, compound="right")
        self.act_btn.image = imagenes['actualizar']
        self.act_btn.grid(row=0, column=4, padx=10, pady=10)

        # Table Frame
        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=920, height=535)

        Y_scroll = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame, columns=("ci", "nom", "ape", "dir", "cor", "cel"),
                                  yscrollcommand=Y_scroll.set)

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.Table.yview)

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

    def tic(self):
        self.clock["text"] = strftime("%H:%M:%S %p")

    def tac(self):
        self.tic()
        self.clock.after(1000, self.tac)

    def slider(self):
        """creates slides for heading by taking the text,
        and that text are called after every 100 ms"""
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

    def click_home(self):
        try:
            obj_student_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "SELECT COUNT(*) FROM asesores;"
            data = self.db_connection.select(query)
            global no_assesors
            for value in data:
                no_assesors = value[0]

            total_assesors = Label(self.Detail_Frame, text=f" TOTAL ASESORES: {no_assesors}",
                                   font=("Copperplate Gothic Bold", 12, "bold"), bg='#a27114', fg="White")
            total_assesors.grid(row=0, column=5, padx=60, pady=10)

        except BaseException as msg:
            print(msg)

    def add_asessor(self):
        try:
            obj_assesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_assesor_database.get_database())

            query = "select id_asesor from asesores;"
            data = self.db_connection.select(query)

            self.asesor_list = []
            for values in data:
                asesor_data_list = values[0]
                self.asesor_list.append(asesor_data_list)

        except BaseException as msg:
            print(msg)

        if self.e_n_ced_as.get() == '' or self.e_nombres_as.get() == '' or self.e_apellidos_as.get() == '' or \
                self.e_direccion_as.get() == '' or self.e_correo_as.get() == '' or self.e_n_celular_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. DE CELULAR")
            self.e_celular.focus()

        elif self.e_n_ced_as.get() in self.asesor_list:
            messagebox.showerror("YA EXISTE!!!", f"EL ESTUDIANTE CON No. DE CÉDULA: {self.e_n_ced_as.get()} "
                                                 f"YA EXISTE!")
        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de estudiantes después de la validación exitosa de esos datos
        """
        try:
            obj_assesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_assesor_database.get_database())

            query = 'insert into asesores (id_asesor, nombres, apellidos, direccion, correo, celular) ' \
                    'values (?, ?, ?, ?, ?, ?);'
            values = (self.e_n_ced_as.get(), self.e_nombres_as.get(), self.e_apellidos_as.get(),
                      self.e_direccion_as.get(), self.e_correo_as.get(), self.e_n_celular_as.get()
                      )

            self.db_connection.insert(query, values)

            self.show_data_as()
            self.clear_field_as()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"ASESOR: {values[1]} {values[2]}\n "
                                                       f"CON No. DE CÉDULA: {values[0]}\n"
                                                       f"REGISTRADO CORRECTAMENTE")

        except BaseException as msg:
            messagebox.showerror("ERROR!!!", f"NO SE HAN PODIDO GUARDAR LOS DATOS DEL ASESOR {msg}")

    def clear_field_as(self):
        self.e_n_ced_as.set('')
        self.e_nombres_as.set('')
        self.e_apellidos_as.set('')
        self.e_direccion_as.set('')
        self.e_correo_as.set('')
        self.e_n_celular_as.set('')
        self.e_cedula.focus()
        self.update_btn["state"] = "disabled"
        self.delete_btn["state"] = "disabled"

    def get_fields_as(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.e_n_ced_as.set(row[0])
        self.e_nombres_as.set(row[1])
        self.e_apellidos_as.set(row[2])
        self.e_direccion_as.set(row[3])
        self.e_correo_as.set(row[4])
        self.e_n_celular_as.set(row[5])

        self.add_btn["state"] = "normal"
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

    def validation(self):
        try:
            obj_asesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_asesor_database.get_database())

            query = "select * from asesores;"
            data = self.db_connection.select(query)
            self.asesor_list = []

            for values in data:
                n_c_i = values[0]
                self.asesor_list.append(n_c_i)

        except BaseException as msg:
            messagebox.showerror("Error", f"{msg}")
        if self.e_n_ced_as.get() == '' or self.e_nombres_as.get() == '' or self.e_apellidos_as.get() == '' \
                or self.e_direccion_as.get() == '' or self.e_correo_as.get() == '' or self.e_n_celular_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.update_as()

    def update_as(self):
        try:
            obj_students_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_students_database.get_database())

            query = 'UPDATE asesores SET id_asesor=?, nombres=?, apellidos=?, direccion=?, correo=?, celular=? ' \
                    'WHERE id_asesor=?'
            values = (self.e_n_ced_as.get(), self.e_nombres_as.get(), self.e_apellidos_as.get(),
                      self.e_direccion_as.get(), self.e_correo_as.get(), self.e_n_celular_as.get(),
                      self.e_n_ced_as.get()
                      )
            self.db_connection.insert(query, values)

            self.show_data_as()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL ESTUDIANTE: {self.e_nombres_as.get()} "
                                                       f"{self.e_apellidos_as.get()}\n"
                                                       f"CON No. DE CÉDULA: {self.e_n_ced_as.get()}\n"
                                                       f"HAN SIDO ACTUALIZADOS DEL REGISTRO")
            self.clear_field_as()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def delete_as(self):
        try:
            obj_asesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_asesor_database.get_database())

            tree_view_content = self.Table.focus()
            tree_view_items = self.Table.item(tree_view_content)
            tree_view_values = tree_view_items['values'][1]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ELIMINAR AL ASESOR: {tree_view_values}")
            if ask is True:
                query = "delete from asesores where nombres=?;"
                self.db_connection.delete(query, tree_view_values)

                self.clear_field_as()
                self.show_data_as()
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL ASESOR: {tree_view_values} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")
            else:
                pass

        except BaseException as msg:
            messagebox.showerror("Error", f"SE GENERÓ UN ERROR AL INTENTAR ELIMINAR DATOS DE UN ASESOR: {msg}")

    # =======================================================================
    # ========================Searching Started==============================
    # =======================================================================
    @classmethod
    def binary_search(cls, _list, target):
        """this is class method searching for user input into the table"""
        start = 0
        end = len(_list) - 1

        while start <= end:
            middle = (start + end) // 2
            midpoint = _list[middle]
            if midpoint > target:
                end = middle - 1
            elif midpoint < target:
                start = middle + 1
            else:
                return midpoint

    @classmethod
    def bubble_sort(self, _list):
        """this class methods sort the string value of user input such as name, email"""
        for j in range(len(_list) - 1):
            for i in range(len(_list) - 1):
                if _list[i].upper() > _list[i + 1].upper():
                    _list[i], _list[i + 1] = _list[i + 1], _list[i]
        return _list

    def search_data_as(self):
        a = self.search_entry.get()
        if self.search_entry.get() != '':
            if a.isnumeric():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN NÚMEROS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE ASESOR")
                self.search_entry.set("")
            elif a.isspace():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN ESPACIOS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE ASESOR")
                self.search_entry.set("")
            else:
                if a.isalpha():
                    try:
                        search_list = []
                        for child in self.Table.get_children():
                            val = self.Table.item(child)["values"][1]
                            search_list.append(val)

                        sorted_list = self.bubble_sort(search_list)
                        self.output = self.binary_search(sorted_list, self.search_entry.get())

                        if self.output:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->ENCONTRADO",
                                                f"EL ASESOR: '{self.output}' HA SIDO ENCONTRADO")

                            obj_asesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_asesor_database.get_database())

                            query = "select * from asesores where nombres LIKE '" + str(self.output) + "%'"
                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3], values[4], values[5]]

                                self.Table.insert('', END, values=data_list)
                                self.search_entry.set("")

                        else:
                            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR",
                                                 "ASESOR NO ENCONTRADO,\nSE MOSTRARÁN RESULTADOS RELACIONADOS.")

                            obj_asesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_asesor_database.get_database())

                            query = "select * from asesores where nombres LIKE '%" + \
                                    str(self.search_entry.get()) + "%'"

                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3], values[4], values[5]]

                                # self.student_tree.delete(*self.student_tree.get_children())
                                self.Table.insert('', END, values=data_list)
                                self.search_entry.set("")

                    except BaseException as msg:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                             f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                             f"REVISE LA CONEXIÓN: {msg}")
                else:
                    self.show_data_as()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL ASESOR.")

    def show_data_as(self):
        try:
            obj_asesor_database = Model_class.assesor_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_asesor_database.get_database())

            query = "select * from asesores;"
            data = self.db_connection.select(query)
            self.Table.delete(*self.Table.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3], values[4], values[5]]
                self.Table.insert('', END, values=data_list)

        except BaseException as msg:
            print(msg)

    def logout(self):
        root = Toplevel()
        Frontend.login_form.Login(root)
        self.root.withdraw()
        root.deiconify()

    def principal_btn(self):
        root = Toplevel()
        Frontend.Secretary.Principal_Window_S.Principal_S(root)
        self.root.withdraw()
        root.deiconify()

    def student_btn(self):
        root = Toplevel()
        Frontend.Secretary.Student_Window_S.Student_S(root)
        self.root.withdraw()
        root.deiconify()

    def matricula_btn(self):
        root = Toplevel()
        Frontend.Secretary.Matricula_Window_S.Matricula_S(root)
        self.root.withdraw()
        root.deiconify()

    def assesor_btn(self):
        root = Toplevel()
        Frontend.Secretary.Assesor_Window_S.Assesor_S(root)
        self.root.withdraw()
        root.deiconify()

    def courses_btn(self):
        root = Toplevel()
        Frontend.Secretary.Course_Window_S.Course_S(root)
        self.root.withdraw()
        root.deiconify()

    def paralelos_btn(self):
        root = Toplevel()
        Frontend.Secretary.Paralelo_Window_S.Paralelo_S(root)
        self.root.withdraw()
        root.deiconify()

    def implements_btn(self):
        root = Toplevel()
        Frontend.Secretary.Implements_Window_S.Implement_S(root)
        self.root.withdraw()
        root.deiconify()

    def pass_btn(self):
        root = Toplevel()
        Frontend.Secretary.Password_Window_S.Password_S(root)
        self.root.withdraw()
        root.deiconify()

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
