# Import Modules
from _datetime import datetime
import random
from tkinter import *
from tkcalendar import *
from ttkthemes import themed_tk as tk
from tkinter import messagebox, ttk
from tkinter.ttk import Treeview

import Backend.connection
import Model_class.paralelos_registration

import Frontend.Principal_Window_A
import Frontend.login_form
import Frontend.Student_Window_A
import Frontend.Matricula_Window_A
import Frontend.Assesor_Window_A
import Frontend.Course_Window_A
import Frontend.Implements_Window_A
import Frontend.Facturation_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A
import Frontend.Users_Window_A


class Paralelo:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Paralelos")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('./recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_aceptar.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'eliminar': PhotoImage(file='./recursos/icon_del.png'),
            'limpiar': PhotoImage(file='./recursos/icon_clean.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),

        }

        # =============================================================
        # BANNER PANTALLA PARALELOS
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (PARALELOS)"
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
        self.menubarra.add_cascade(label='PARALELOS')
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
        self.Column4.add_command(label='Menú Paralelos')
        self.Column4.add_command(label='Implementos', command=self.implements_btn)
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
        self.Column6.add_command(label='Menú Reportes', command=self.report_btn)
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ USUARIOS
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

        # Manage Frame Paralelos
        self.Manage_Frame_par = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_par.place(x=15, y=85, width=500, height=400)

        m_title_p = Label(self.Manage_Frame_par, text="-ADMINISTAR PARALELOS-", font=("Copperplate Gothic Bold", 16,
                                                                                      "bold"), bg='#a27114', fg="White")
        m_title_p.grid(row=0, columnspan=2, padx=90, pady=10)

        self.e_id_paralelo_1 = IntVar()
        self.e_nombre_curso_1 = StringVar()
        self.e_nom_par_1 = StringVar()
        self.e_dia_1 = StringVar()
        self.e_hora_1 = StringVar()
        self.e_f_i_par_1 = StringVar()
        self.e_f_f_par_1 = StringVar()
        self.e_dur_par_1 = StringVar()

        self.search_field_par = StringVar()

        self.l_id_paralelo = Label(self.Manage_Frame_par, text='ID PARALELO', width='20',
                                   font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_paralelo.grid(column=0, row=1, padx=1, pady=5)
        self.e_id_paralelo = Entry(self.Manage_Frame_par, textvariable=self.e_id_paralelo_1, width='11')
        self.e_id_paralelo.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_id_paralelo.focus()

        try:
            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelo_database.get_database())

            query = "select * from cursos"
            course_tuple = self.db_connection.select(query)

            self.course_list = []
            for i in course_tuple:
                course_name = i[1]
                self.course_list.append(course_name)

        except BaseException as msg:
            print(msg)

        self.l_id_c_paralelo = Label(self.Manage_Frame_par, text='CURSO', width='20',
                                     font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_c_paralelo.grid(column=0, row=2, padx=1, pady=5)
        self.e_nombre_curso = ttk.Combobox(self.Manage_Frame_par, textvariable=self.e_nombre_curso_1, width='25',
                                           font=("Arial", 9, "bold"), state="readonly")
        self.e_nombre_curso['values'] = self.course_list

        self.e_nombre_curso.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_nom_par = Label(self.Manage_Frame_par, text='PARALELO', width='20',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_nom_par.grid(column=0, row=3, padx=0, pady=5)
        self.e_nom_par = Entry(self.Manage_Frame_par, textvariable=self.e_nom_par_1, width='30')
        self.e_nom_par.grid(column=1, row=3, padx=0, pady=5, sticky="W")

        self.l_dia = Label(self.Manage_Frame_par, text='DÍA', width='20', font=('Copperplate Gothic Bold', 10),
                           bg='#808080')
        self.l_dia.grid(column=0, row=4, padx=1, pady=5)
        self.e_dia = ttk.Combobox(self.Manage_Frame_par, textvariable=self.e_dia_1, width='15',
                                  font=("Arial", 9, "bold"), state="readonly")
        self.e_dia["values"] = ["LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO"]
        self.e_dia.grid(column=1, row=4, padx=0, pady=5, sticky="W")

        try:
            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelo_database.get_database())

            query = "select * from horas"
            hora_tuple = self.db_connection.select(query)

            self.horas_list = []
            for i in hora_tuple:
                hora = i[1]
                self.horas_list.append(hora)

        except BaseException as msg:
            print(msg)

        self.l_h_paralelo = Label(self.Manage_Frame_par, text='HORA', width='20',
                                  font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_h_paralelo.grid(column=0, row=5, padx=1, pady=5)
        self.e_hora = ttk.Combobox(self.Manage_Frame_par, textvariable=self.e_hora_1, width='15',
                                   font=("Arial", 9, "bold"), state="readonly")
        self.e_hora['values'] = self.horas_list
        self.e_hora.grid(column=1, row=5, padx=0, pady=5, sticky="W")

        self.frame_add_h = Frame(self.Manage_Frame_par, bg='#0d1e24')
        self.frame_add_h.place(x=310, y=187, width=200)

        self.l_f_i_par = Label(self.Manage_Frame_par, text='FECHA INICIO', width='20',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_f_i_par.grid(column=0, row=6, padx=0, pady=5)
        self.e_f_i_par = Entry(self.Manage_Frame_par, textvariable=self.e_f_i_par_1, width='10',
                               font=("Arial", 9, "bold"))
        self.e_f_i_par.insert(0, "yyyy//mm/dd")
        self.e_f_i_par.bind("<1>", self.pick_date_i)
        self.e_f_i_par.grid(column=1, row=6, padx=0, pady=5, sticky="W")

        self.l_f_f_par = Label(self.Manage_Frame_par, text='FECHA FIN', width='20',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_f_f_par.grid(column=0, row=7, padx=1, pady=5)
        self.e_f_f_par = Entry(self.Manage_Frame_par, textvariable=self.e_f_f_par_1, width='10',
                               font=("Arial", 9, "bold"))
        self.e_f_f_par.insert(0, "yyyy//mm/dd")
        self.e_f_f_par.bind("<1>", self.pick_date_f)
        self.e_f_f_par.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        self.l_dur_par = Label(self.Manage_Frame_par, text='DURACIÓN', width='20',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_dur_par.grid(column=0, row=8, padx=1, pady=5)
        self.e_dur_par = Entry(self.Manage_Frame_par, textvariable=self.e_dur_par_1, width='18')
        self.e_dur_par.grid(column=1, row=8, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_par_frame_par = Frame(self.Manage_Frame_par, bg='#a27114')
        self.btn_par_frame_par.place(x=25, y=320, width=450)

        self.add_par_btn = Button(self.btn_par_frame_par, image=imagenes['nuevo'], text='REGISTAR', width=80,
                                  command=self.add_par, compound=TOP)
        self.add_par_btn.image = imagenes['nuevo']
        self.add_par_btn.grid(row=0, column=0, padx=15, pady=10)

        self.update_par_btn = Button(self.btn_par_frame_par, image=imagenes['editar'], text='MODIFICAR', width=80,
                                     command=self.update_par, compound=TOP)
        self.update_par_btn.image = imagenes['editar']
        self.update_par_btn.grid(row=0, column=1, padx=15, pady=10)
        self.update_par_btn["state"] = "disabled"

        self.delete_par_btn = Button(self.btn_par_frame_par, image=imagenes['eliminar'], text='ELIMINAR', width=80,
                                     command=self.delete_par, compound=TOP)
        self.delete_par_btn.image = imagenes['eliminar']
        self.delete_par_btn.grid(row=0, column=2, padx=15, pady=10)
        self.delete_par_btn["state"] = "disabled"

        self.clean_par_btn = Button(self.btn_par_frame_par, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                    command=self.clear_field_par, compound=TOP)
        self.clean_par_btn.image = imagenes['limpiar']
        self.clean_par_btn.grid(row=0, column=3, padx=15, pady=10)

        # Manage Frame hora y día
        self.Manage_Frame_h_d = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_h_d.place(x=15, y=490, width=500, height=200)

        m_title_d_h = Label(self.Manage_Frame_h_d, text="-ADMINISTAR HORAS-",
                            font=("Copperplate Gothic Bold", 16, "bold"), bg='#a27114', fg="White")
        m_title_d_h.grid(row=0, columnspan=1, padx=110, pady=10)

        self.e_n_hora_e = StringVar()
        self.e_n_hora_s = StringVar()

        self.Manage_Frame_h_d_1 = Frame(self.Manage_Frame_h_d, bd=4, bg='#a27114')
        self.Manage_Frame_h_d_1.place(x=30, y=50, width=450, height=100)

        self.l_hora_e = Label(self.Manage_Frame_h_d_1, text='HORA ENTRADA', width='15',
                              font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_hora_e.grid(column=0, row=1, padx=5, pady=5)
        self.e_hora_e = ttk.Combobox(self.Manage_Frame_h_d_1, textvariable=self.e_n_hora_e, width='15',
                                     font=("Arial", 9, "bold"), state="readonly")
        self.e_hora_e["values"] = ["08:00:00", "08:30:00", "09:00:00", "09:30:00", "10:00:00", "10:30:00",
                                   "11:00:00", "11:30:00", "12:00:00", "12:30:00", "13:00:00", "13:30:00",
                                   "14:00:00", "14:30:00", "15:00:00", "15:30:00", "16:00:00", "16:30:00",
                                   "17:00:00", "17:30:00", "18:00:00", "18:30:00", "19:00:00", "19:30:00"]
        self.e_hora_e.grid(column=1, row=1, padx=5, pady=5, sticky="W")

        self.l_hora_s = Label(self.Manage_Frame_h_d_1, text='HORA SALIDA', width='15',
                              font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_hora_s.grid(column=0, row=2, padx=5, pady=5)
        self.e_hora_s = ttk.Combobox(self.Manage_Frame_h_d_1, textvariable=self.e_n_hora_s, width='15',
                                     font=("Arial", 9, "bold"), state="readonly")
        self.e_hora_s["values"] = ["08:00:00", "08:30:00", "09:00:00", "09:30:00", "10:00:00", "10:30:00",
                                   "11:00:00", "11:30:00", "12:00:00", "12:30:00", "13:00:00", "13:30:00",
                                   "14:00:00", "14:30:00", "15:00:00", "15:30:00", "16:00:00", "16:30:00",
                                   "17:00:00", "17:30:00", "18:00:00", "18:30:00", "19:00:00", "19:30:00"]
        self.e_hora_s.grid(column=1, row=2, padx=5, pady=5, sticky="W")

        self.add_hora_btn = Button(self.Manage_Frame_h_d_1, image=imagenes['nuevo'], text='AÑADIR',
                                   command=self.add_hora, compound="right")
        self.add_hora_btn.image = imagenes['nuevo']
        self.add_hora_btn.place(x=300, y=20)

        # Detail Frame
        self.Detail_Frame_par = Frame(self.root, bd=4, relief=RIDGE, bg='#a27114')
        self.Detail_Frame_par.place(x=520, y=85, width=825, height=605)

        self.lbl_search = Label(self.Detail_Frame_par, text="BUSCAR", bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame_par, width=15, textvariable=self.search_field_par,
                                font=("Arial", 10, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame_par, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_par, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame_par, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_par, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame
        Table_Frame_par = Frame(self.Detail_Frame_par, bg='#a27114')
        Table_Frame_par.place(x=5, y=60, width=805, height=525)

        scroll_x = Scrollbar(Table_Frame_par, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame_par, orient=VERTICAL)
        self.Table_par = Treeview(Table_Frame_par, columns=("id_par", "nom_cur", "nom_par", "nom_dia", "hora",
                                                            "f_ini", "f_fin", "dur"),
                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Table_par.xview)
        scroll_y.config(command=self.Table_par.yview)
        self.Table_par.heading("id_par", text="ID")
        self.Table_par.heading("nom_cur", text="CURSO")
        self.Table_par.heading("nom_par", text="PARALELO")
        self.Table_par.heading("nom_dia", text="DÍA")
        self.Table_par.heading("hora", text="HORA")
        self.Table_par.heading("f_ini", text="F. INICIO")
        self.Table_par.heading("f_fin", text="F. FIN")
        self.Table_par.heading("dur", text="DURACIÓN")

        self.Table_par['show'] = "headings"
        self.Table_par.column("id_par", width=5)
        self.Table_par.column("nom_cur", width=100)
        self.Table_par.column("nom_par", width=120)
        self.Table_par.column("nom_dia", width=10)
        self.Table_par.column("hora", width=50)
        self.Table_par.column("f_ini", width=22)
        self.Table_par.column("f_fin", width=20)
        self.Table_par.column("dur", width=20)

        self.Table_par.pack(fill=BOTH, expand=1)
        self.Table_par.bind('<ButtonRelease 1>', self.get_fields_par)

        self.show_data_par()

    def add_hora(self):
        if self.e_n_hora_e == "" or self.e_n_hora_s == "":
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")
        else:
            self.hora_e_s = (self.e_n_hora_e.get() + "-" + self.e_hora_s.get())
            try:
                obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
                self.db_connection.create(obj_paralelo_database.get_database())

                query = 'insert into horas (hora) values (?);'
                values = self.hora_e_s
                self.db_connection.insert(query, values)
                self.e_hora.set("")
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"HORA: {values[1]}\n "
                                                           f"REGISTRADO CORRECTAMENTE")

            except BaseException as msg:
                messagebox.showerror("ERROR!!!", f"NO SE HAN PODIDO GUARDAR LA HORA DE ENTRADA Y SALIDA: {msg}")

    def pick_date_i(self, event):
        """
            left click event is being handled when trying to add DOB
        """
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('FECHA DE INICIO')
        self.date_win.geometry('260x220')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="y-mm-dd")
        self.cal.place(x=15, y=10)

        self.okay_btn = ttk.Button(self.date_win, text="AÑADIR FECHA", command=self.grab_date_i)
        self.okay_btn.place(x=80, y=195)

    def grab_date_i(self):
        """Grabs the date that being handled in pick_date() methods"""
        self.e_f_i_par.delete(0, END)
        self.e_f_i_par.insert(0, self.cal.get_date())
        self.date_win.destroy()

    def pick_date_f(self, event):
        """left click event is being handled when trying to add DOB"""
        self.date_win = tk.ThemedTk()
        self.date_win.get_themes()
        self.date_win.set_theme("arc")
        self.date_win.grab_set()
        self.date_win.title('FECHA DE FIN')
        self.date_win.geometry('260x220')
        self.cal = Calendar(self.date_win, selectmode="day", date_pattern="y-mm-dd")
        self.cal.place(x=15, y=10)

        self.okay_btn = ttk.Button(self.date_win, text="AÑADIR FECHA", command=self.grab_date_f)
        self.okay_btn.place(x=80, y=195)

    def grab_date_f(self):
        """Grabs the date that being handled in pick_date() methods"""
        self.e_f_f_par.delete(0, END)
        self.e_f_f_par.insert(0, self.cal.get_date())
        self.date_win.destroy()

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

    # FUNCIONES CURSOS

    def add_par(self):
        try:
            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelo_database.get_database())

            query = "select id_paralelo from paralelos;"
            data = self.db_connection.select(query)

            self.paralelos_list = []
            for values in data:
                paralelo_data_list = values[0]
                self.paralelos_list.append(paralelo_data_list)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

        if self.e_id_paralelo == '' or self.e_nombre_curso == '' or self.e_nom_par.get() == '' or \
                self.e_dia.get() == '' or self.e_hora.get() == '' or self.e_f_i_par == '' or \
                self.e_f_f_par.get() == '' or self.e_dur_par.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        else:
            self.click_submit_par()

    def click_submit_par(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de usuarios después de la validación exitosa de esos datos
        """
        try:
            obj_paralelos_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelos_database.get_database())
            query = 'insert into paralelos (id_paralelo, nombre_curso, nombre_paralelo, dia, hora, ' \
                    'fecha_inicio, fecha_fin, duracion) values (?, ?, ?, ?, ?, ?, ?, ?);'
            values = (self.e_id_paralelo.get(), self.e_nombre_curso.get(), self.e_nom_par.get(), self.e_dia.get(),
                      self.e_hora.get(), self.e_f_i_par.get(), self.e_f_f_par.get(), self.e_dur_par.get()
                      )
            self.db_connection.insert(query, values)
            self.show_data_par()
            self.clear_field_par()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL PARALELO GUARDADOS CORRECTAMENTE\n "
                                                       f"PARALELO={values[2]}")

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def clear_field_par(self):
        self.e_id_paralelo_1.set('')
        self.e_nombre_curso_1.set('')
        self.e_nom_par_1.set('')
        self.e_dia_1.set('')
        self.e_hora_1.set('')
        self.e_f_i_par_1.set('')
        self.e_f_f_par_1.set('')
        self.e_dur_par_1.set('')

        self.e_id_paralelo.focus()
        self.update_par_btn["state"] = "disabled"
        self.delete_par_btn["state"] = "disabled"

    def get_fields_par(self, row_p):
        self.cursor_row = self.Table_par.focus()
        self.content = self.Table_par.item(self.cursor_row)
        row_p = self.content['values']

        self.e_id_paralelo_1.set(row_p[0])
        self.e_nombre_curso_1.set(row_p[1])
        self.e_nom_par_1.set(row_p[2])
        self.e_dia_1.set(row_p[3])
        self.e_hora_1.set(row_p[4])
        self.e_f_i_par_1.set(row_p[5])
        self.e_f_f_par_1.set(row_p[6])
        self.e_dur_par_1.set(row_p[7])

        self.update_par_btn["state"] = "normal"
        self.delete_par_btn["state"] = "normal"

    def update_par(self):
        try:
            obj_paralelos_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelos_database.get_database())

            query = 'update paralelos set id_paralelo=?, nombre_curso=?, nombre_paralelo=?, dia=?, hora=?, ' \
                    'fecha_inicio=?, fecha_fin=?, duracion=? where id_paralelo=?'
            values = (self.e_id_paralelo.get(), self.e_nombre_curso.get(), self.e_nom_par.get(), self.e_dia.get(),
                      self.e_hora.get(), self.e_f_i_par.get(), self.e_f_f_par.get(), self.e_dur_par.get(),
                      self.e_id_paralelo.get()
                      )
            self.db_connection.insert(query, values)

            self.clear_field_par()
            self.show_data_par()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL PARALELO:  {values[2]}\n"
                                                       f"ACTUALIZADOS CORRECTAMENTE\n")

        except BaseException as msg:
            self.clear_field_par()
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def delete_par(self):
        try:
            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelo_database.get_database())

            tree_view_content = self.Table_par.focus()
            tree_view_items = self.Table_par.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            tree_view_values_1 = tree_view_items['values'][2]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ELIMINAR AL PARALELO: {tree_view_values_1}")
            if ask is True:
                query = "delete from paralelos where id_paralelo=?;"
                self.db_connection.delete(query, tree_view_values)

                self.clear_field_par()
                self.show_data_par()
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL PARALELO: {tree_view_values_1} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")

            else:
                pass

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
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

    def search_data_par(self):
        a = self.search_field_par.get()
        if self.search_field_par.get() != '':
            if a.isnumeric():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN NÚMEROS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE PARALELO")
                self.search_field_par.set("")
            elif a.isspace():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN ESPACIOS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DE PARALELO")
                self.search_field_par.set("")
            else:
                if a.isalpha():
                    try:
                        search_list = []
                        for child in self.Table_par.get_children():
                            val = self.Table_par.item(child)["values"][1]
                            search_list.append(val)

                        sorted_list = self.bubble_sort(search_list)
                        self.output = self.binary_search(sorted_list, self.search_field_par.get())

                        if self.output:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->ENCONTRADO",
                                                f"EL PARALELO: '{self.output}' HA SIDO ENCONTRADO")

                            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_paralelo_database.get_database())

                            query = "select * from paralelos where nombre_paralelo LIKE '" + str(self.output) + "%'"
                            data = self.db_connection.select(query)

                            self.Table_par.delete(*self.Table_par.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3], values[4], values[5],
                                             values[6], values[7]]

                                self.Table_par.insert('', END, values=data_list)
                                self.search_field_par.set("")

                        else:
                            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR",
                                                 "PARALELO NO ENCONTRADO,\nSE MOSTRARÁN RESULTADOS RELACIONADOS.")

                            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_paralelo_database.get_database())

                            query = "select * from paralelos where nombre_paralelo LIKE '%" + \
                                    str(self.search_field_par.get()) + "%'"

                            data = self.db_connection.select(query)
                            self.Table_par.delete(*self.Table_par.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2], values[3], values[4], values[5],
                                             values[6], values[7]]

                                self.Table_par.insert('', END, values=data_list)
                                self.search_field_par.set("")

                    except BaseException as msg:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                             f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                             f"REVISE LA CONEXIÓN: {msg}")
                else:
                    self.search_data_par()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL PARALELO.")

    def show_data_par(self):
        try:
            obj_paralelo_database = Model_class.paralelos_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_paralelo_database.get_database())

            query = "select * from paralelos;"
            data = self.db_connection.select(query)

            self.Table_par.delete(*self.Table_par.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7]]

                self.Table_par.insert('', END, values=data_list)

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
    Paralelo(root)
    root.mainloop()


if __name__ == '__main__':
    root()
