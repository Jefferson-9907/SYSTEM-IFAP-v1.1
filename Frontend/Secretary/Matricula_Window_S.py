# Import Modules
from _datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import themed_tk as tk
import random

import Backend.connection
import Model_class.matricula_registration

import Frontend.login_form
import Frontend.Secretary.Student_Window_S
import Frontend.Secretary.Assesor_Window_S
import Frontend.Secretary.Course_Window_S
import Frontend.Secretary.Paralelo_Window_S
import Frontend.Secretary.Implements_Window_S
import Frontend.Secretary.Password_Window_S


class Matricula_S:
    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›MATRICULACIÓN")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        self.imagenes = {
            'matricula': PhotoImage(file='recursos\\icon_n_al.png'),
            'matricular': PhotoImage(file='recursos\\icon_aceptar.png'),
            'editar': PhotoImage(file='recursos\\icon_update.png'),
            'eliminar': PhotoImage(file='recursos\\icon_del.png'),
            'limpiar': PhotoImage(file='recursos\\icon_clean.png'),
            'buscar': PhotoImage(file='recursos\\icon_buscar.png'),
            'todo': PhotoImage(file='recursos\\icon_ver_todo.png'),
            'actualizar': PhotoImage(file='recursos\\icon_upd.png')
        }

        # =============================================================
        # BANNER PANTALLA MATRÍCULA
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (MATRÍCULAS)"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=1367)

        self.slider()
        self.heading_color()

        # =============================================================
        # BANNER PANTALLA MATRÍCULA
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (MATRÍCULAS)"
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
        self.Column2.add_command(label='Matriculación')
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL MENÚ ASESORES
        # =============================================================
        self.menus.add_cascade(label='ASESORES', menu=self.Column3)
        self.Column3.add_command(label='Menú Asesores', command=self.assesor_btn)
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
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column7)
        self.Column7.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column7.add_separator()
        self.root.config(menu=self.menus)

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
        self.Manage_Frame_m = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_m.place(x=20, y=85, width=435, height=350)

        # Variables
        self.e_n_mat_al_m = StringVar()
        self.e_nombres_al = StringVar()
        self.e_n_paralelo = StringVar()
        self.e_nombres_as = StringVar()
        self.search_field = StringVar()

        self.m_title = Label(self.Manage_Frame_m, text="-ADMINISTRAR MATRÍCULA-",
                             font=("Copperplate Gothic Bold", 16, "bold"), bg='#a27114', fg="White")
        self.m_title.grid(column=0, row=0, columnspan=3, padx=50, pady=25, sticky="W")

        self.Manage_Frame_m_1 = Frame(self.root, bd=4, bg='#a27114')
        self.Manage_Frame_m_1.place(x=25, y=150, width=420, height=250)

        self.l_n_c_al_m = Label(self.Manage_Frame_m_1, text='C.I ESTUDIANTE', width='15',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_c_al_m.grid(column=0, row=0, padx=5, pady=5, sticky="W")
        self.e_n_c_al_m = Entry(self.Manage_Frame_m_1, textvariable=self.e_n_mat_al_m, width='15')
        self.e_n_c_al_m.grid(column=1, row=0, padx=0, pady=5, sticky="W")
        self.e_n_c_al_m.focus()

        self.search_btn = Button(self.Manage_Frame_m_1, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_al, compound="right")
        self.search_btn.image = self.imagenes['buscar']
        self.search_btn.grid(column=1, row=0, padx=100, pady=10)

        self.v_l_nombres = Label(self.Manage_Frame_m_1, text='NOMBRES', width='15',
                                 font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.v_l_nombres.grid(column=0, row=1, padx=0, pady=5)
        self.v_e_nombres = Entry(self.Manage_Frame_m_1, textvariable=self.e_nombres_al, width='40')
        self.v_e_nombres.grid(column=1, row=1, padx=0, pady=5, sticky="W")
        self.v_e_nombres["state"] = "disabled"

        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "select * from paralelos"
            paralelos_tuple = self.db_connection.select(query)

            self.paralelos_list = []
            for i in paralelos_tuple:
                paralelos_name = i[2]
                self.paralelos_list.append(paralelos_name)

        except BaseException as msg:
            print(msg)

        self.l_cur_m = Label(self.Manage_Frame_m_1, text='PARALELO', width='15', font=('Copperplate Gothic Bold',
                                                                                       10), bg='#808080')
        self.l_cur_m.grid(column=0, row=2, padx=5, pady=5, sticky="W")
        self.e_id_par_al_m = ttk.Combobox(self.Manage_Frame_m_1, textvariable=self.e_n_paralelo, width='30')
        self.e_id_par_al_m['values'] = self.paralelos_list
        self.e_id_par_al_m.grid(column=1, row=2, padx=1, pady=5, sticky="W")

        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "select * from asesores;"
            data = self.db_connection.select(query)
            self.asesores_list = []

            for values in data:
                asesores_name = str(values[1]) + " " + str(values[2])
                self.asesores_list.append(asesores_name)

        except BaseException as msg:
            print(msg)

        self.v_l_n_as_m = Label(self.Manage_Frame_m_1, text='ASESOR', width='15', font=('Copperplate Gothic Bold',
                                                                                        10), bg='#808080')
        self.v_l_n_as_m.grid(column=0, row=3, padx=5, pady=5, sticky="W")
        self.v_e_n_as_m = ttk.Combobox(self.Manage_Frame_m_1, textvariable=self.e_nombres_as, width='33')
        self.v_e_n_as_m['values'] = self.asesores_list
        self.v_e_n_as_m.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame_m = Frame(self.root, bg='#a27114')
        self.btn_frame_m.place(x=50, y=320, width=375, height=75)

        self.add_btn = Button(self.btn_frame_m, image=self.imagenes['matricular'], text='MATRICULAR', width=80,
                              command=self.add_mat_al, compound=TOP)
        self.add_btn.image = self.imagenes['matricular']
        self.add_btn.grid(row=0, column=1, padx=3, pady=10)
        self.add_btn["state"] = "normal"

        self.up_btn = Button(self.btn_frame_m, image=self.imagenes['editar'], text='MODIFICAR', width=80,
                             command=self.update, compound=TOP)
        self.up_btn.image = self.imagenes['editar']
        self.up_btn.grid(row=0, column=2, padx=3, pady=10)
        self.up_btn["state"] = "disabled"

        self.del_btn = Button(self.btn_frame_m, image=self.imagenes['eliminar'], text='ELIMINAR', width=80,
                              command=self.delete_m, compound=TOP)
        self.del_btn.image = self.imagenes['eliminar']
        self.del_btn.grid(row=0, column=3, padx=3, pady=10)
        self.del_btn["state"] = "disabled"

        self.clean_btn = Button(self.btn_frame_m, image=self.imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_m, compound=TOP)
        self.clean_btn.image = self.imagenes['limpiar']
        self.clean_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#a27114')
        self.Detail_Frame.place(x=460, y=85, width=885, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field, font=("Arial", 10, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_m, compound="right")
        self.search_btn.image = self.imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=self.imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_m, compound="right")
        self.show_all_btn.image = self.imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        self.click_home()

        self.act_btn = Button(self.Detail_Frame, image=self.imagenes['actualizar'], text='ACTUALIZAR', width=100,
                              command=self.matricula_btn, compound="right")
        self.act_btn.image = self.imagenes['actualizar']
        self.act_btn.grid(row=0, column=4, padx=10, pady=10)

        # Table Frame administar matrícula

        self.Table_Frame = Frame(self.Detail_Frame)
        self.Table_Frame.place(x=5, y=60, width=865, height=525)

        self.Y_scroll = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(self.Table_Frame, columns=("ci_est", "est", "par", "ase"),
                                  yscrollcommand=self.Y_scroll.set)

        self.Y_scroll.pack(side=RIGHT, fill=Y)
        self.Y_scroll.config(command=self.Table.yview)

        self.Table.heading("ci_est", text="C.I ESTUDIANTE")
        self.Table.heading("est", text="ESTUDIANTE")
        self.Table.heading("par", text="PARALELO")
        self.Table.heading("ase", text="ASESOR")

        self.Table['show'] = "headings"
        self.Table.column("ci_est", width=10)
        self.Table.column("est", width=200)
        self.Table.column("par", width=200)
        self.Table.column("ase", width=100)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_m)
        self.show_data_m()

    def tic(self):
        self.clock["text"] = strftime("%H:%M:%S %p")

    def tac(self):
        self.tic()
        self.clock.after(1000, self.tac)

    def slider(self):
        """
            creates slides for heading by taking the text,
            and that text are called after every 100 ms
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

    def click_home(self):
        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "SELECT COUNT(*) FROM matriculas;"
            data = self.db_connection.select(query)
            for value in data:
                self.no_matriculas = value[0]

            total_matriculas = Label(self.Detail_Frame, text=f" TOTAL MATRÍCULAS: {self.no_matriculas}",
                                     font=("Copperplate Gothic Bold", 12, "bold"), bg='#a27114', fg="White")
            total_matriculas.grid(row=0, column=5, padx=60, pady=10)

        except BaseException as msg:
            print(msg)

    def search_data_al(self):
        self.n_c_al = self.e_n_mat_al_m.get()
        if self.e_n_mat_al_m.get() == "":
            messagebox.showerror("SYST_CONTROL (IFAP®)-ERROR!!!", "INGRESE EL CAMPO: No. CÉDULA ESTUDIANTE")

        else:
            try:
                obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
                self.db_connection.create(obj_matricula_database.get_database())

                query = "select * from estudiantes where id_estudiante='" + self.n_c_al + "';"
                data = self.db_connection.select(query)
                for values in data:
                    data_list = str(values[1]) + " " + str(values[2])
                    self.e_nombres_al.set(data_list)

            except BaseException as msg:
                messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                      f"REVISE LA CONEXIÓN: {msg}")

    def add_mat_al(self):
        try:
            obj_course_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            query = "select id_matricula from matriculas;"
            data = self.db_connection.select(query)

            self.matriculas_list = []
            for values in data:
                matriculas_data_list = values[0]
                self.matriculas_list.append(matriculas_data_list)

        except BaseException as msg:
            messagebox.showerror("Error", f"{msg}")

        if self.e_n_mat_al_m.get() == '' or self.e_nombres_al.get() == '' or self.e_n_paralelo.get() == '' or \
                self.e_nombres_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de estudiantes después de la validación exitosa de esos datos
        """
        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = 'insert into matriculas (id_matricula, estudiante, paralelo, asesor) values (?, ?, ?, ?);'
            values = (self.e_n_mat_al_m.get(), self.e_nombres_al.get(), self.e_n_paralelo.get(), self.e_nombres_as.get()
                      )

            self.db_connection.insert(query, values)

            self.show_data_m()
            self.clear_field_m()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"MATRÍCULA DEL ESTUDIANTE: {values[1]}\n "
                                                       f"CON No. DE CÉDULA: {values[0]}\n"
                                                       f"REGISTRADO HA SIDO REGISTRADA CORRECTAMENTE")

        except BaseException:
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ERROR)", f"EL ESTUDIANTE YA SE ENVUENTRA MATRICULADO "
                                                                    f"EN UN CURSO!!!")

    def clear_field_m(self):
        self.e_n_mat_al_m.set('')
        self.e_nombres_al.set('')
        self.e_n_paralelo.set('')
        self.e_nombres_as.set('')
        self.add_btn["state"] = "normal"
        self.up_btn["state"] = "disabled"
        self.del_btn["state"] = "disabled"

    def get_fields_m(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.e_n_mat_al_m.set(row[0])
        self.e_nombres_al.set(row[1])
        self.e_n_paralelo.set(row[2])
        self.e_nombres_as.set(row[3])
        self.add_btn["state"] = "disabled"
        self.up_btn["state"] = "normal"
        self.del_btn["state"] = "normal"

    def validation(self):
        try:
            obj_matricula_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_matricula_database.get_database())

            query = "select * from matriculas;"
            data = self.db_connection.select(query)
            self.matriculas_list = []

            for values in data:
                n_c_i = values[0]
                self.matriculas_list.append(n_c_i)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

        if self.e_n_mat_al_m.get() == '' or self.e_nombres_al.get() == '' or self.e_n_paralelo.get() == '' or \
                self.e_nombres_as.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.update()

    def update(self):
        try:
            obj_students_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_students_database.get_database())

            query = f"""update matriculas SET id_matricula=?, estudiante=?, paralelo=?, asesor=? WHERE id_matricula=?"""
            values = (self.e_n_mat_al_m.get(), self.e_nombres_al.get(), self.e_n_paralelo.get(),
                      self.e_nombres_as.get(), self.e_n_mat_al_m.get()
                      )
            self.db_connection.insert(query, values)

            self.show_data_m()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"LA MATRÍCULA DEL ESTUDIANTE: {self.e_nombres_al.get()}\n"
                                                       f"CON No. DE CÉDULA: {self.e_n_mat_al_m.get()}\n"
                                                       f"HA SIDO ACTUALIZADA DEL REGISTRO CORRECTAMENTE!!!")
            self.clear_field_m()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def delete_m(self):
        try:
            obj_student_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            tree_view_content = self.Table.focus()
            tree_view_items = self.Table.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ELIMINAR LA MATRÍCULA: {tree_view_values}")
            if ask is True:
                query = "delete from matriculas where id_matricula=?;"
                self.db_connection.delete(query, tree_view_values)

                self.show_data_m()
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DE LA MATRÍCULA: {tree_view_values} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")
                self.clear_field_m()
            else:
                pass

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

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

    def search_data_m(self):
        a = self.search_field.get()
        if self.search_field.get() != '':
            if a.isalpha():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN LETRAS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE ESTUDIANTE")
                self.search_field.set('')

            elif a.isspace():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN ESPACIOS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE ESTUDIANTE")
                self.search_field.set("")

            else:
                if a.isnumeric():
                    try:
                        search_list = []
                        for child in self.Table.get_children():
                            val = self.Table.item(child)["values"][1]
                            search_list.append(val)

                        sorted_list = self.bubble_sort(search_list)
                        self.output = self.binary_search(sorted_list, self.search_field.get())

                        if self.output:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->ENCONTRADO",
                                                f"EL ESTUDIANTE: '{self.output}' HA SIDO ENCONTRADO")

                            obj_student_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_student_database.get_database())

                            query = "select * from matriculas where estudiante LIKE '" + str(self.output) + "%'"
                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3]]

                                # self.student_tree.delete(*self.student_tree.get_children())
                                self.Table.insert('', END, values=data_list)
                                self.search_field.set("")

                        else:
                            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR",
                                                 "MATRÍCULA NO ENCONTRADA,\nSE MOSTRARÁN RESULTADOS RELACIONADOS.")

                            obj_student_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_student_database.get_database())

                            query = "select * from matriculas where estudiante LIKE '%" + \
                                    str(self.search_field.get()) + "%'"

                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3]]

                                # self.student_tree.delete(*self.student_tree.get_children())
                                self.Table.insert('', END, values=data_list)
                                self.search_field.set("")

                    except BaseException as msg:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                             f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                             f"REVISE LA CONEXIÓN: {msg}")
                else:
                    self.show_data_m()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL ESTUDIANTE.")

    def show_data_m(self):
        try:
            obj_student_database = Model_class.matricula_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from matriculas;"
            data = self.db_connection.select(query)
            self.Table.delete(*self.Table.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3]]
                self.Table.insert('', END, values=data_list)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

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


def root():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    Matricula_S(root)
    root.mainloop()


if __name__ == '__main__':
    root()
