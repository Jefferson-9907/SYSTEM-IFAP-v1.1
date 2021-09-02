# Import Modules
from _datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import themed_tk as tk
import random

import Backend.connection
import Model_class.students_registration

import Frontend.Principal_Window_A
import Frontend.login_form
import Frontend.Matricula_Window_A
import Frontend.Assesor_Window_A
import Frontend.Course_Window_A
import Frontend.Paralelo_Window_A
import Frontend.Implements_Window_A
import Frontend.Facturation_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A
import Frontend.Users_Window_A


class Student:
    """
        Permite a los administradores gestionar a los estudiantes; añadir, actualizar, eliminar, obtener los datos,
        aquí, el administrador puede ver todos los detalles de estudiantes y tener varias opciones para realizar,
        pueden buscarlos por nombre, esto se hizo mediante el uso de la función de comodín de MySQL después de
        agarrar todos los datos y luego realizar la ordenación de burbuja en eso y más tarde enviado al método de
        búsqueda binaria si los datos existen entonces todos los datos.
    """
    list_of_tree = []
    get_id = []

    def __init__(self, root):

        self.root = root
        self.root.title("SYST_CONTROL--›ALUMNOS")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        self.imagenes = {
            'nuevo': PhotoImage(file='recursos\\icon_aceptar.png'),
            'matricular': PhotoImage(file='recursos\\icon_add.png'),
            'editar': PhotoImage(file='recursos\\icon_update.png'),
            'eliminar': PhotoImage(file='recursos\\icon_del.png'),
            'limpiar': PhotoImage(file='recursos\\icon_clean.png'),
            'buscar': PhotoImage(file='recursos\\icon_buscar.png'),
            'todo': PhotoImage(file='recursos\\icon_ver_todo.png'),
            'actualizar': PhotoImage(file='./recursos/icon_upd.png')
        }

        # =============================================================
        # BANNER PANTALLA ESTUDIANTES
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (ESTUDIANTES)"
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
        self.menubarra.add_cascade(label='ESTUDIANTES')
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
        self.Column2.add_command(label='Menú Alumnos')
        self.Column2.add_command(label='Matriculación', command=self.matricula_btn)
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
        # CREACIÓN DEL DE MENÚ FACTURACIÓN
        # =============================================================
        self.menus.add_cascade(label='FACTURACIÓN', menu=self.Column5)
        self.Column5.add_command(label='Menú Facturación', command=self.facturation_btn)
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ REPORTES
        # =============================================================
        self.menus.add_cascade(label='REPORTES', menu=self.Column6)
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column7)
        self.Column7.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column7.add_command(label='Cambiar Contraseña', command=self.pass_btn)
        self.Column7.add_separator()
        self.Column7.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column7.add_separator()
        self.Column8 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column8)
        self.Column8.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column8.add_separator()
        self.root.config(menu=self.menus)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10), bg='Honeydew2',
                            relief=RIDGE)
        self.footer.place(x=0, y=703)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='Honeydew2',
                              relief=RIDGE)
        self.footer_1.place(x=212, y=704)

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=195, bg='black',
                              fg='white')
        self.footer_4.place(x=0, y=725)

        # Manage Frame
        Manage_Frame = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        Manage_Frame.place(x=15, y=85, width=385, height=605)

        self.e_cedula_al_1 = StringVar()
        self.e_nombres_al_1 = StringVar()
        self.e_apellidos_al_1 = StringVar()
        self.e_edad_al_1 = IntVar()
        self.e_direccion_al_1 = StringVar()
        self.e_correo_al_1 = StringVar()
        self.e_celular_al_1 = StringVar()
        self.e_telefono_al_1 = StringVar()
        self.e_representante_al_1 = StringVar()
        self.e_n_c_representante_al_1 = StringVar()
        self.e_observacion_al_1 = StringVar()

        self.search_entry = StringVar()

        m_title = Label(Manage_Frame, text="-ADMINISTAR ESTUDIANTES-", font=("Copperplate Gothic Bold", 16, "bold"),
                        bg='#a27114', fg="White")
        m_title.grid(row=0, columnspan=2, padx=10, pady=50)

        self.l_cedula_al = Label(Manage_Frame, text='No. CÉDULA', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_cedula_al.grid(column=0, row=1, padx=1, pady=5)
        self.e_cedula_al = Entry(Manage_Frame, textvariable=self.e_cedula_al_1, width='13')
        self.e_cedula_al.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_cedula_al.focus()

        self.l_nombres_al = Label(Manage_Frame, text='NOMBRES', width='15', font=('Copperplate Gothic Bold', 10),
                                  bg='#808080')
        self.l_nombres_al.grid(column=0, row=2, padx=0, pady=5)
        self.e_nombres_al = Entry(Manage_Frame, textvariable=self.e_nombres_al_1, width='33')
        self.e_nombres_al.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_apellidos_al = Label(Manage_Frame, text='APELLIDOS', width='15', font=('Copperplate Gothic Bold', 10),
                                    bg='#808080')
        self.l_apellidos_al.grid(column=0, row=3, padx=1, pady=5)
        self.e_apellidos_al = Entry(Manage_Frame, textvariable=self.e_apellidos_al_1, width='33')
        self.e_apellidos_al.grid(column=1, row=3, padx=1, pady=5, sticky="W")

        self.l_edad_al = Label(Manage_Frame, text='EDAD', width='15', font=('Copperplate Gothic Bold', 10),
                               bg='#808080')
        self.l_edad_al.grid(column=0, row=4, padx=1, pady=5)
        self.e_edad_al = Entry(Manage_Frame, textvariable=self.e_edad_al_1, width='8')
        self.e_edad_al.grid(column=1, row=4, padx=1, pady=5, sticky="W")

        self.l_direccion_al = Label(Manage_Frame, text='DIRECCIÓN', width='15', font=('Copperplate Gothic Bold', 10),
                                    bg='#808080')
        self.l_direccion_al.grid(column=0, row=5, padx=1, pady=5)
        self.e_direccion_al = Entry(Manage_Frame, textvariable=self.e_direccion_al_1, width='33')
        self.e_direccion_al.grid(column=1, row=5, padx=1, pady=5, sticky="W")

        self.l_correo_al = Label(Manage_Frame, text='CORREO', width='15', font=('Copperplate Gothic Bold', 10),
                                 bg='#808080')
        self.l_correo_al.grid(column=0, row=6, padx=1, pady=5)
        self.e_correo_al = Entry(Manage_Frame, textvariable=self.e_correo_al_1, width='33')
        self.e_correo_al.grid(column=1, row=6, padx=1, pady=5, sticky="W")

        self.l_celular_al = Label(Manage_Frame, text='No. CELULAR', width='15', font=('Copperplate Gothic Bold', 10),
                                  bg='#808080')
        self.l_celular_al.grid(column=0, row=7, padx=1, pady=5)
        self.e_celular_al = Entry(Manage_Frame, textvariable=self.e_celular_al_1, width='13')
        self.e_celular_al.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        self.l_telefono_al = Label(Manage_Frame, text='No. TELÉFONO', width='15', font=('Copperplate Gothic Bold', 10),
                                   bg='#808080')
        self.l_telefono_al.grid(column=0, row=8, padx=1, pady=5)
        self.e_telefono_al = Entry(Manage_Frame, textvariable=self.e_telefono_al_1, width='13')
        self.e_telefono_al.grid(column=1, row=8, padx=1, pady=5, sticky="W")

        self.l_representante_al = Label(Manage_Frame, text='NOMBRE REPR.', width='15',
                                        font=('Copperplate Gothic Bold', 10),
                                        bg='#808080')
        self.l_representante_al.grid(column=0, row=9, padx=1, pady=5)
        self.e_representante_al = Entry(Manage_Frame, textvariable=self.e_representante_al_1, width='33')
        self.e_representante_al.grid(column=1, row=9, padx=1, pady=5, sticky="W")

        self.l_n_c_representante_al = Label(Manage_Frame, text='No. CÉDULA REPR.', width='15',
                                            font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_c_representante_al.grid(column=0, row=10, padx=1, pady=5)
        self.e_n_c_representante_al = Entry(Manage_Frame, textvariable=self.e_n_c_representante_al_1, width='33')
        self.e_n_c_representante_al.grid(column=1, row=10, padx=1, pady=5, sticky="W")

        self.l_observacion_al = Label(Manage_Frame, text='OBSERV.', width='15', font=('Copperplate Gothic Bold', 10),
                                      bg='#808080')
        self.l_observacion_al.grid(column=0, row=11, padx=1, pady=5)
        self.e_observacion_al = Entry(Manage_Frame, textvariable=self.e_observacion_al_1, width='33')
        self.e_observacion_al.grid(column=1, row=11, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame = Frame(Manage_Frame, bg='#a27114')
        self.btn_frame.place(x=10, y=500, width=360)

        self.add_btn = Button(self.btn_frame, image=self.imagenes['nuevo'], text='REGISTAR', command=self.add_student,
                              compound=TOP)
        self.add_btn.image = self.imagenes['nuevo']
        self.add_btn.grid(row=0, column=0, padx=3, pady=10)

        self.m_btn = Button(self.btn_frame, image=self.imagenes['matricular'], text='MATRICULAR',
                            command=self.matricula_btn, compound=TOP)
        self.m_btn.image = self.imagenes['matricular']
        self.m_btn.grid(row=0, column=1, padx=3, pady=10)
        self.m_btn["state"] = "disabled"

        self.up_btn = Button(self.btn_frame, image=self.imagenes['editar'], text='MODIFICAR', command=self.update,
                             compound=TOP)
        self.up_btn.image = self.imagenes['editar']
        self.up_btn.grid(row=0, column=2, padx=3, pady=10)
        self.up_btn["state"] = "disabled"

        self.del_btn = Button(self.btn_frame, image=self.imagenes['eliminar'], text='ELIMINAR', command=self.delete,
                              compound=TOP)
        self.del_btn.image = self.imagenes['eliminar']
        self.del_btn.grid(row=0, column=3, padx=3, pady=10)
        self.del_btn["state"] = "disabled"

        self.clean_btn = Button(self.btn_frame, image=self.imagenes['limpiar'], text='LIMPIAR',
                                command=self.clear_field, compound=TOP)
        self.clean_btn.image = self.imagenes['limpiar']
        self.clean_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#a27114')
        self.Detail_Frame.place(x=405, y=85, width=940, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_entry,
                                font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data, compound="right")
        self.search_btn.image = self.imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=self.imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data, compound="right")
        self.show_all_btn.image = self.imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        self.click_home()

        self.act_btn = Button(self.Detail_Frame, image=self.imagenes['actualizar'], text='ACTUALIZAR', width=100,
                              command=self.student_btn, compound="right")
        self.act_btn.image = self.imagenes['actualizar']
        self.act_btn.grid(row=0, column=4, padx=10, pady=10)

        # Table Frame

        Table_Frame = Frame(self.Detail_Frame)
        Table_Frame.place(x=5, y=60, width=920, height=535)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame, columns=("ci", "nom", "ape", "edad", "dir", "em", "cel", "tel", "n_rep",
                                                        "c_rep", "ob"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Table.xview)
        scroll_y.config(command=self.Table.yview)

        self.Table.heading("ci", text="No. C.I")
        self.Table.heading("nom", text="NOMBRES")
        self.Table.heading("ape", text="APELLIDOS")
        self.Table.heading("edad", text="EDAD")
        self.Table.heading("dir", text="DIRECCIÓN")
        self.Table.heading("em", text="EMAIL")
        self.Table.heading("cel", text="CELULAR")
        self.Table.heading("tel", text="TELÉFONO")
        self.Table.heading("n_rep", text="REPRESENTANTE")
        self.Table.heading("c_rep", text="C.I REPRESENTANTE")
        self.Table.heading("ob", text="OBSERVACIÓN")

        self.Table['show'] = "headings"
        self.Table.column("ci", width=100)
        self.Table.column("nom", width=150)
        self.Table.column("ape", width=150)
        self.Table.column("edad", width=50)
        self.Table.column("dir", width=250)
        self.Table.column("em", width=250)
        self.Table.column("cel", width=75)
        self.Table.column("tel", width=75)
        self.Table.column("n_rep", width=250)
        self.Table.column("c_rep", width=150)
        self.Table.column("ob", width=250)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields)

        self.show_data()

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
            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "SELECT COUNT(*) FROM estudiantes;"
            data = self.db_connection.select(query)
            for value in data:
                self.no_students = value[0]

            total_students = Label(self.Detail_Frame, text=f" TOTAL ESTUDIANTES: {self.no_students}",
                                   font=("Copperplate Gothic Bold", 12, "bold"), bg='#a27114', fg="White")
            total_students.grid(row=0, column=5, padx=60, pady=10)

        except BaseException as msg:
            print(msg)

    def add_student(self):
        try:
            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select id_estudiante from estudiantes;"
            data = self.db_connection.select(query)

            self.estudiante_list = []
            for values in data:
                estudiante_data_list = values[0]
                self.estudiante_list.append(estudiante_data_list)

        except BaseException as msg:
            print(msg)

        if self.e_cedula_al.get() == '' or self.e_nombres_al.get() == '' or self.e_apellidos_al.get() == '' or \
                self.e_edad_al.get() == '' or self.e_direccion_al.get() == '' or self.e_correo_al.get() == '' or \
                self.e_celular_al.get() == '' or self.e_telefono_al.get() == '' or self.e_representante_al.get() == '' \
                or self.e_n_c_representante_al.get() == '' or self.e_observacion_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        elif self.e_cedula_al.get() in self.estudiante_list:
            messagebox.showerror("YA EXISTE!!!", f"EL ESTUDIANTE CON No. DE CÉDULA: {self.e_cedula_al.get()} "
                                                 f"YA EXISTE!")
        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de estudiantes después de la validación exitosa de esos datos
        """
        try:
            obj_students_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_students_database.get_database())

            query = 'insert into estudiantes (id_estudiante, nombres, apellidos, edad, direccion, correo, celular, ' \
                    'telefono, representante, cedula_r, observacion) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
            values = (self.e_cedula_al.get(), self.e_nombres_al.get(), self.e_apellidos_al.get(), self.e_edad_al.get(),
                      self.e_direccion_al.get(), self.e_correo_al.get(), self.e_celular_al.get(),
                      self.e_telefono_al.get(), self.e_representante_al.get(), self.e_n_c_representante_al.get(),
                      self.e_observacion_al.get()
                      )
            self.db_connection.insert(query, values)

            self.show_data()
            self.clear_field()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"ESTUDIANTE: {values[1]} {values[2]}\n "
                                                       f"CON No. DE CÉDULA: {values[0]}\n"
                                                       f"REGISTRADO CORRECTAMENTE")

        except BaseException as msg:
            messagebox.showerror("ERROR!!!", f"NO SE HAN PODIDO GUARDAR LOS DATOS DEL ESTUDIANTE {msg}")

    def clear_field(self):
        self.e_cedula_al_1.set('')
        self.e_nombres_al_1.set('')
        self.e_apellidos_al_1.set('')
        self.e_edad_al_1.set('')
        self.e_direccion_al_1.set('')
        self.e_correo_al_1.set('')
        self.e_celular_al_1.set('')
        self.e_telefono_al_1.set('')
        self.e_representante_al_1.set('')
        self.e_n_c_representante_al_1.set('')
        self.e_observacion_al_1.set('')
        self.e_cedula_al.focus()
        self.m_btn["state"] = "normal"
        self.up_btn["state"] = "disabled"
        self.del_btn["state"] = "disabled"

    def get_fields(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.e_cedula_al_1.set(row[0])
        self.e_nombres_al_1.set(row[1])
        self.e_apellidos_al_1.set(row[2])
        self.e_edad_al_1.set(row[3])
        self.e_direccion_al_1.set(row[4])
        self.e_correo_al_1.set(row[5])
        self.e_celular_al_1.set(row[6])
        self.e_telefono_al_1.set(row[7])
        self.e_representante_al_1.set(row[8])
        self.e_n_c_representante_al_1.set(row[9])
        self.e_observacion_al_1.set(row[10])

        self.m_btn["state"] = "normal"
        self.up_btn["state"] = "normal"
        self.del_btn["state"] = "normal"

    def validation(self):
        try:
            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from estudiantes;"
            data = self.db_connection.select(query)
            # print(data)
            self.estudiante_list = []
            for values in data:
                # print(values)
                n_c_i = values[0]
                self.estudiante_list.append(n_c_i)

        except BaseException as msg:
            messagebox.showerror("Error", f"{msg}")
        if self.e_cedula_al.get() == '' or self.e_nombres_al.get() == '' or self.e_apellidos_al.get() == '' or \
                self.e_edad_al.get() == '' or self.e_direccion_al.get() == '' or self.e_correo_al.get() == '' or \
                self.e_celular_al.get() == '' or self.e_telefono_al.get() == '' or self.e_representante_al.get() == '' \
                or self.e_n_c_representante_al.get() == '' or self.e_observacion_al.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.update()

    def update(self):
        try:
            obj_students_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_students_database.get_database())

            query = 'update estudiantes set id_estudiante=?, nombres=?, apellidos=?, edad=?, direccion=?, correo=?, ' \
                    'celular=?, telefono=?, representante=?, cedula_r=?, observacion=? where id_estudiante=?'
            values = (self.e_cedula_al.get(), self.e_nombres_al.get(), self.e_apellidos_al.get(), self.e_edad_al.get(),
                      self.e_direccion_al.get(), self.e_correo_al.get(), self.e_celular_al.get(),
                      self.e_telefono_al.get(), self.e_representante_al.get(), self.e_n_c_representante_al.get(),
                      self.e_observacion_al.get(), self.e_cedula_al.get()
                      )
            self.db_connection.insert(query, values)
            self.show_data()
            messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", f"DATOS DEL ESTUDIANTE: {self.e_nombres_al.get()}"
                                                       f"{self.e_apellidos_al.get()}\n"
                                                       f"CON No. DE CÉDULA: {self.e_cedula_al.get()}\n"
                                                       f"HAN SIDO ACTUALIZADOS DEL REGISTRO")
            self.clear_field()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def delete(self):
        try:
            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            tree_view_content = self.Table.focus()
            tree_view_items = self.Table.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            tree_view_values_1 = tree_view_items['values'][1] + " " + tree_view_items['values'][2]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ELIMINAR AL ESTUDIANTE: {tree_view_values_1}")
            if ask is True:
                query = "delete from estudiantes where id_estudiante=?;"
                self.db_connection.delete(query, tree_view_values)

                self.show_data()
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL ESTUDIANTE: {tree_view_values} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")
                self.clear_field()

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

    def search_data(self):
        a = self.search_entry.get()
        if self.search_entry.get() != '':
            if a.isnumeric():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN NÚMEROS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE ESTUDIANTE")
                self.search_entry.set("")
            elif a.isspace():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN ESPACIOS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE ESTUDIANTE")
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
                                                f"EL ESTUDIANTE: '{self.output}' HA SIDO ENCONTRADO")

                            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_student_database.get_database())

                            query = "select * from estudiantes where nombres LIKE '" + str(self.output) + "%'"
                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3], values[4], values[5],
                                             values[6], values[7], values[8], values[9], values[10]]

                                self.Table.insert('', END, values=data_list)
                                self.search_entry.set("")

                        else:
                            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR",
                                                 "ESTUDIANTE NO ENCONTRADO,\nSE MOSTRARÁN RESULTADOS RELACIONADOS.")

                            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_student_database.get_database())

                            query = "select * from estudiantes where nombres LIKE '%" + \
                                    str(self.search_entry.get()) + "%'"

                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3], values[4], values[5],
                                             values[6], values[7], values[8], values[9], values[10]]

                                # self.student_tree.delete(*self.student_tree.get_children())
                                self.Table.insert('', END, values=data_list)
                                self.search_entry.set("")

                    except BaseException as msg:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                             f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                             f"REVISE LA CONEXIÓN: {msg}")
                else:
                    self.show_data()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL ESTUDIANTE.")

    def show_data(self):
        try:
            obj_student_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from estudiantes;"
            data = self.db_connection.select(query)
            self.Table.delete(*self.Table.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7],
                             values[8], values[9], values[10]]
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
        Frontend.Principal_Window_A.Principal(root)
        self.root.withdraw()
        root.deiconify()

    def student_btn(self):
        root = Toplevel()
        Frontend.Student_Window_A.Student(root)
        self.root.withdraw()
        root.deiconify()

    def matricula_btn(self):
        root = Toplevel()
        Frontend.Matricula_Window_A.Matricula(root)
        self.root.withdraw()
        root.deiconify()

    def assesor_btn(self):
        root = Toplevel()
        Frontend.Assesor_Window_A.Assesor(root)
        self.root.withdraw()
        root.deiconify()

    def courses_btn(self):
        root = Toplevel()
        Frontend.Course_Window_A.Course(root)
        self.root.withdraw()
        root.deiconify()

    def paralelos_btn(self):
        root = Toplevel()
        Frontend.Paralelo_Window_A.Paralelo(root)
        self.root.withdraw()
        root.deiconify()

    def implements_btn(self):
        root = Toplevel()
        Frontend.Implements_Window_A.Implement(root)
        self.root.withdraw()
        root.deiconify()

    def facturation_btn(self):
        root = Toplevel()
        Frontend.Facturation_Window_A.Ventana_Principal(root)
        self.root.withdraw()
        root.deiconify()

    def report_btn(self):
        root = Toplevel()
        Frontend.Report_Window_A.Reports(root)
        self.root.withdraw()
        root.deiconify()

    def pass_btn(self):
        root = Toplevel()
        Frontend.Password_Window_A.Password(root)
        self.root.withdraw()
        root.deiconify()

    def users_btn(self):
        root = Toplevel()
        Frontend.Users_Window_A.Users(root)
        self.root.withdraw()
        root.deiconify()

    def salir_principal(self):
        self.sa = messagebox.askyesno('CERRAR SESIÓN', 'CERRAR SYST_CONTROL(IFAP®)')
        if self.sa:
            exit()

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL SISTEMA(INFO)
    # =============================================================
    def caja_info_sist(self):
        self.men2 = messagebox.showinfo('SIST_CONTROL (IFAP®)',
                                        'SIST_CONTROL (IFAP®) v2.0\n'
                                        'El uso de este software queda sujeto a los términos y condiciones del '
                                        'contrato "J.C.F DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 BJM DESING®. Todos los derechos reservados')


def root():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    Student(root)
    root.mainloop()


if __name__ == '__main__':
    root()
