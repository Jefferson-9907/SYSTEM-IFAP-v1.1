# Import Modules
from _datetime import datetime

from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Treeview

import mariadb


class Course_S:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Cursos")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_aceptar.png'),
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
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (CURSOS-PARALELOS)')
        self.texto1.config(font=("Britannic", 20, "bold"), fg='black', bg="#a27114")
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
        self.Column3.add_command(label='Menú Asesores', command=self.assesor_btn)
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ CURSOS
        # =============================================================
        self.menus.add_cascade(label='CURSOS', menu=self.Column4)
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

        # Manage Frame Cursos
        self.Manage_Frame_cur = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_cur.place(x=20, y=75, width=508, height=605)

        m_title_c = Label(self.Manage_Frame_cur, text="-ADMINISTAR CURSOS-", font=("Copperplate Gothic Bold", 16,
                                                                                   "bold"), bg='#0d1e24', fg="White")
        m_title_c.grid(row=0, columnspan=2, padx=110, pady=20)

        self.id_curso = IntVar()
        self.nombre_cur = StringVar()
        self.costo_matricula = DoubleVar()
        self.costo_mensual = DoubleVar()
        self.search_field_curso = StringVar()

        self.l_id_curso = Label(self.Manage_Frame_cur, text='ID CURSO', width='18',
                                font=('Copperplate Gothic Bold', 10),
                                bg='#808080')
        self.l_id_curso.grid(column=0, row=1, padx=1, pady=5)
        self.e_id_curso = Entry(self.Manage_Frame_cur, textvariable=self.id_curso, width='10')
        self.e_id_curso.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_id_curso.focus()
        self.id_curso.set('')

        self.l_n_curso = Label(self.Manage_Frame_cur, text='NOMBRE CURSO', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_curso.grid(column=0, row=2, padx=1, pady=5)
        self.e_n_curso = Entry(self.Manage_Frame_cur, textvariable=self.nombre_cur, width='40')
        self.e_n_curso.grid(column=1, row=2, padx=1, pady=5, sticky="W")

        self.l_cost_mat = Label(self.Manage_Frame_cur, text='COSTO MATRÍCULA', width='18',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_cost_mat.grid(column=0, row=3, padx=0, pady=5)
        self.e_cost_mat = Entry(self.Manage_Frame_cur, textvariable=self.costo_matricula, width='8')
        self.e_cost_mat.grid(column=1, row=3, padx=0, pady=5, sticky="W")

        self.l_cost_men = Label(self.Manage_Frame_cur, text='COSTO MENSUAL', width='18',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_cost_men.grid(column=0, row=4, padx=1, pady=5)
        self.e_cost_men = Entry(self.Manage_Frame_cur, textvariable=self.costo_mensual, width='8')
        self.e_cost_men.grid(column=1, row=4, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_frame = Frame(self.Manage_Frame_cur, bg='#0d1e24')
        self.btn_frame.place(x=20, y=190, width=455)

        self.add_btn = Button(self.btn_frame, image=imagenes['nuevo'], text='REGISTAR', width=80,
                              command=self.add_cur, compound=TOP)
        self.add_btn.image = imagenes['nuevo']
        self.add_btn.grid(row=0, column=1, padx=15, pady=10)

        self.update_btn = Button(self.btn_frame, image=imagenes['editar'], text='MODIFICAR', width=80,
                                 command=self.update_cur, compound=TOP)
        self.update_btn.image = imagenes['editar']
        self.update_btn.grid(row=0, column=2, padx=15, pady=10)
        self.update_btn["state"] = "disabled"

        self.delete_btn = Button(self.btn_frame, image=imagenes['eliminar'], text='ELIMINAR', width=80,
                                 command=self.delete_cur, compound=TOP)
        self.delete_btn.image = imagenes['eliminar']
        self.delete_btn.grid(row=0, column=3, padx=15, pady=10)
        self.delete_btn["state"] = "disabled"

        self.clear_btn = Button(self.btn_frame, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_cur, compound=TOP)
        self.clear_btn.image = imagenes['limpiar']
        self.clear_btn.grid(row=0, column=4, padx=15, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=29, y=340, width=490, height=330)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field_curso,
                                font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_cur, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_cur, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame

        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=470, height=255)

        Y_scroll = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = Treeview(Table_Frame, columns=("id_cur", "nom_cur", "cos_cur", "cost_men"),
                              yscrollcommand=Y_scroll.set)

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.Table.yview)
        self.Table.heading("id_cur", text="ID")
        self.Table.heading("nom_cur", text="NOMBRE")
        self.Table.heading("cos_cur", text="V. MATRÍCULA")
        self.Table.heading("cost_men", text="V. MENSUAL")

        self.Table['show'] = "headings"
        self.Table.column("id_cur", width=5)
        self.Table.column("nom_cur", width=70)
        self.Table.column("cos_cur", width=5)
        self.Table.column("cost_men", width=5)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_cur)

        self.show_data_cur()

        # Manage Frame Paralelos
        self.Manage_Frame_par = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_par.place(x=535, y=75, width=815, height=605)

        m_title_p = Label(self.Manage_Frame_par, text="-ADMINISTAR PARALELOS-", font=("Copperplate Gothic Bold", 16,
                                                                                      "bold"), bg='#0d1e24', fg="White")
        m_title_p.grid(row=0, columnspan=2, padx=90, pady=10)

        self.id_par = IntVar()
        self.id_par.set('')
        self.id_cur_par = IntVar()
        self.id_cur_par.set('')
        self.n_par = StringVar()
        self.dia_par = StringVar()
        self.dia_par.set('')
        self.hora_par = StringVar()
        self.h_add_par = StringVar()
        self.f_ini_par = StringVar()
        self.f_fin_par = StringVar()
        self.dur_par = StringVar()

        self.search_field_par = StringVar()

        self.l_id_paralelo = Label(self.Manage_Frame_par, text='ID PARALELO', width='18',
                                   font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_paralelo.grid(column=0, row=1, padx=1, pady=5)
        self.e_id_paralelo = Entry(self.Manage_Frame_par, textvariable=self.id_par, width='11')
        self.e_id_paralelo.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.e_id_paralelo.focus()
        self.id_curso.set('')

        self.l_id_c_paralelo = Label(self.Manage_Frame_par, text='ID CURSO', width='18',
                                     font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_c_paralelo.grid(column=0, row=2, padx=1, pady=5)
        self.e_id_c_paralelo = ttk.Combobox(self.Manage_Frame_par, textvariable=self.id_cur_par, width='7',
                                            font=("Arial", 9, "bold"), state="readonly")
        self.e_id_c_paralelo['values'] = ("3001", "3002", "3003", "3004")
        self.e_id_c_paralelo.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_nom_par = Label(self.Manage_Frame_par, text='NOMBRE PARALELO', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_nom_par.grid(column=0, row=3, padx=0, pady=5)
        self.e_nom_par = Entry(self.Manage_Frame_par, textvariable=self.n_par, width='40')
        self.e_nom_par.grid(column=1, row=3, padx=0, pady=5, sticky="W")

        self.l_dia = Label(self.Manage_Frame_par, text='DÍA', width='18', font=('Copperplate Gothic Bold', 10),
                           bg='#808080')
        self.l_dia.grid(column=0, row=4, padx=1, pady=5)
        self.e_dia = ttk.Combobox(self.Manage_Frame_par, textvariable=self.dia_par, width='7',
                                  font=("Arial", 9, "bold"), state="readonly")
        self.e_dia['values'] = ("1", "2", "3", "4", "5", "6", "7")
        self.e_dia.grid(column=1, row=4, padx=0, pady=5, sticky="W")

        self.l_h_paralelo = Label(self.Manage_Frame_par, text='HORA', width='18',
                                  font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_h_paralelo.grid(column=0, row=5, padx=1, pady=5)
        self.e_hor = Entry(self.Manage_Frame_par, textvariable=self.hora_par, width='18')
        self.e_hor.grid(column=1, row=5, padx=0, pady=5, sticky="W")

        self.frame_add_h = Frame(self.Manage_Frame_par, bg='#0d1e24')
        self.frame_add_h.place(x=310, y=187, width=200)

        self.l_f_i_par = Label(self.Manage_Frame_par, text='FECHA INICIO', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_f_i_par.grid(column=0, row=6, padx=0, pady=5)
        self.e_f_i_par = Entry(self.Manage_Frame_par, textvariable=self.f_ini_par, width='18')
        self.e_f_i_par.grid(column=1, row=6, padx=0, pady=5, sticky="W")

        self.l_f_f_par = Label(self.Manage_Frame_par, text='FECHA FIN', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_f_f_par.grid(column=0, row=7, padx=1, pady=5)
        self.e_f_f_par = Entry(self.Manage_Frame_par, textvariable=self.f_fin_par, width='18')
        self.e_f_f_par.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        self.l_dur_par = Label(self.Manage_Frame_par, text='DURACIÓN', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_dur_par.grid(column=0, row=8, padx=1, pady=5)
        self.e_dur_par = Entry(self.Manage_Frame_par, textvariable=self.dur_par, width='18')
        self.e_dur_par.grid(column=1, row=8, padx=1, pady=5, sticky="W")

        # Button Frame
        self.btn_par_frame_par = Frame(self.Manage_Frame_par, bg='#0d1e24')
        self.btn_par_frame_par.place(x=25, y=300, width=450)

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

        # Detail Frame
        self.Detail_Frame_par = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame_par.place(x=545, y=450, width=795, height=220)

        self.lbl_search = Label(self.Detail_Frame_par, text="BUSCAR", bg='#0d1e24', fg="White",
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
        Table_Frame_par = Frame(self.Detail_Frame_par, bg="#0A090C")
        Table_Frame_par.place(x=5, y=60, width=775, height=145)

        Y_scroll = Scrollbar(Table_Frame_par, orient=VERTICAL)
        self.Table_par = Treeview(Table_Frame_par, columns=("id_par", "nom_cur", "nom_par", "nom_dia", "id_hor",
                                                            "f_ini", "f_fin", "dur"), yscrollcommand=Y_scroll.set)

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.Table_par.yview)
        self.Table_par.heading("id_par", text="ID")
        self.Table_par.heading("nom_cur", text="CURSO")
        self.Table_par.heading("nom_par", text="PARALELO")
        self.Table_par.heading("nom_dia", text="DÍA")
        self.Table_par.heading("id_hor", text="HORA")
        self.Table_par.heading("f_ini", text="F. INICIO")
        self.Table_par.heading("f_fin", text="F. FIN")
        self.Table_par.heading("dur", text="DURACIÓN")

        self.Table_par['show'] = "headings"
        self.Table_par.column("id_par", width=5)
        self.Table_par.column("nom_cur", width=100)
        self.Table_par.column("nom_par", width=120)
        self.Table_par.column("nom_dia", width=10)
        self.Table_par.column("id_hor", width=10)
        self.Table_par.column("f_ini", width=22)
        self.Table_par.column("f_fin", width=20)
        self.Table_par.column("dur", width=20)

        self.Table_par.pack(fill=BOTH, expand=1)
        self.Table_par.bind('<ButtonRelease 1>', self.get_fields_par)

        self.show_data_par()

        # FUNCIONES CURSOS

    def add_cur(self):
        if self.id_curso.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: ID CURSO")
            self.e_id_curso.focus()

        if self.nombre_cur.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: NOMBRE DE CURSO")
            self.e_n_curso.focus()

        elif self.costo_matricula.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: COSTO MATRÍCULA")
            self.e_cost_mat.focus()

        elif self.costo_mensual.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: COSTO MENSUAL")
            self.e_cost_men.focus()

        else:
            cone = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            cursor = cone.cursor()
            sql = "INSERT INTO cursos(id_curso, nombre_curso, costo_matricula, costo_mensual) VALUES (?, ?, ?, ?)"
            cursor.execute(sql, (self.id_curso.get(), self.nombre_cur.get(), self.costo_matricula.get(),
                                 self.costo_mensual.get()))
            cone.commit()

            self.clear_field_cur()
            self.show_data_cur()
            # self.clear_field()
            cone.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL PARALELO GUARDADOS EN EL REGISTRO CORRECTAMENTE!!!")

    def clear_field_cur(self):
        self.id_curso.set('')
        self.nombre_cur.set('')
        self.costo_matricula.set('')
        self.costo_mensual.set('')
        self.e_id_curso.focus()
        self.update_btn["state"] = "disabled"
        self.delete_btn["state"] = "disabled"

    def get_fields_cur(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']
        self.id_curso.set(row[0])
        self.nombre_cur.set(row[1])
        self.costo_matricula.set(row[2])
        self.costo_mensual.set(row[3])
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

    def update_cur(self):
        if self.id_curso.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE MODIFICAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()

            sql = f"""UPDATE cursos SET nombre_curso="{self.nombre_cur.get()}",\
                    costo_matricula="{self.costo_matricula.get()}",\
                    costo_mensual="{self.costo_mensual.get()}" WHERE id_curso={self.id_curso.get()}"""
            self.curr.execute(sql)
            self.connect.commit()

            self.show_data_cur()
            # self.connect.close()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL CURSO: " + self.nombre_cur.get() +
                                " HA SIDO ACTUALIZADO EN EL REGISTRO CORRECTAMENTE!!!")
            self.clear_field_cur()

    def delete_cur(self):
        if self.nombre_cur.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.conn.cursor()

            self.sql = f"""DELETE FROM cursos WHERE id_curso={self.id_curso.get()}"""
            self.curr.execute(self.sql)

            self.conn.commit()

            self.show_data_cur()
            self.clear_field_cur()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL ESTUDIANTE ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")

    def search_data_cur(self):
        if self.search_field_curso.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: ID DE CURSO")
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_id_curso = self.search_field_curso.get()
        sql = f"""SELECT id_curso FROM cursos WHERE id_curso = {self.search_id_curso}"""
        self.curr.execute(sql)
        self.curr.fetchall()
        if self.curr.rowcount == 1:
            self.sql = f"""SELECT id_curso, nombre_curso, costo_matricula, costo_mensual FROM cursos\
                        WHERE id_curso={self.search_id_curso}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                self.Table.delete(*self.Table.get_children())
                for self.row in self.rows:
                    self.Table.insert('', END, values=self.row)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO DEL CURSO CON EL ID: " +
                                 self.search_id_curso)
            self.search_field_curso.set('')

    def show_data_cur(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("SELECT * FROM cursos")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table.delete(*self.Table.get_children())
            for self.row in self.rows:
                self.Table.insert('', END, values=self.row)

            self.connect.commit()
        self.connect.close()

    def add_par(self):
        if self.n_par.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: NOMBRE DEL PARALELO")
            self.e_nom_par.focus()

        elif self.dia_par.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: ID HORARIO")
            self.e_dia.focus()

        else:
            cone = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            cursor = cone.cursor()
            sql = "INSERT INTO paralelos(id_paralelo, id_curso, nombre_paralelo, id_horario, id_hora, " \
                  "fecha_inicio, fecha_fin, duracion) " \
                  "VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(sql, (self.id_par.get(), self.id_cur_par.get(), self.n_par.get(), self.dia_par.get(),
                                 self.hora_par.get(), self.f_ini_par.get(), self.f_fin_par.get(), self.dur_par.get()))
            cone.commit()

            self.clear_field_par()
            self.show_data_par()
            cone.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL PARALELO GUARDADOS EN EL REGISTRO CORRECTAMENTE!!!")

    def clear_field_par(self):
        self.id_par.set('')
        self.id_cur_par.set('')
        self.n_par.set('')
        self.dia_par.set('')
        self.hora_par.set('')
        self.f_ini_par.set('')
        self.f_fin_par.set('')
        self.dur_par.set('')
        self.e_id_paralelo.focus()
        self.update_par_btn["state"] = "disabled"
        self.delete_par_btn["state"] = "disabled"

    def get_fields_par(self, row_p):
        self.cursor_row = self.Table_par.focus()
        self.content = self.Table_par.item(self.cursor_row)
        row_p = self.content['values']
        self.id_par.set(row_p[0])
        self.id_cur_par.set(row_p[1])
        self.n_par.set(row_p[2])
        self.dia_par.set(row_p[3])
        self.hora_par.set(row_p[4])
        self.f_ini_par.set(row_p[5])
        self.f_fin_par.set(row_p[6])
        self.dur_par.set(row_p[7])
        self.update_par_btn["state"] = "normal"
        self.delete_par_btn["state"] = "normal"

    def update_par(self):
        if self.n_par.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE MODIFICAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()
            sql = f"""UPDATE paralelos SET id_curso="{self.id_cur_par}",\
                    nombre_paralelo="{self.n_par.get()}", id_horario="{self.dia_par.get()}",\
                    id_hora="{self.hora_par}", fecha_inicio="{self.f_ini_par.get()}",\
                    fecha_fin="{self.f_fin_par.get()}", duracion="{self.dur_par.get()}" 
WHERE id_paralelo={self.id_par.get()}"""
            self.curr.execute(sql)
            self.connect.commit()

            self.show_data_par()
            # self.connect.close()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL PARALELO: " + self.n_par.get() +
                                " HA SIDO ACTUALIZADO EN EL REGISTRO CORRECTAMENTE!!!")
            self.clear_field_par()

    def delete_par(self):
        if self.n_par.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.conn.cursor()

            self.sql = f"""DELETE FROM paralelos WHERE id_paralelo={self.id_par.get()}"""
            self.curr.execute(self.sql)

            self.conn.commit()

            self.show_data_par()
            self.clear_field_par()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL PARALELO ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")

    def search_data_par(self):
        if self.search_field_par.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: ID DE PARALELO")
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_id_par = self.search_field_par.get()
        sql = f"""SELECT id_paralelo FROM paralelos WHERE id_paralelo= {self.search_id_par}"""
        self.curr.execute(sql)
        self.curr.fetchall()
        if self.curr.rowcount == 1:
            self.sql = f"""SELECT id_paralelo, id_curso, nombre_paralelo, id_horario, id_hora,\
                    DATE_FORMAT(fecha_inicio, '%d/%m/%Y'), DATE_FORMAT(fecha_fin, '%d/%m/%Y'), duracion FROM paralelos\
                     WHERE id_paralelo={self.search_id_par} """
            self.curr.execute(self.sql)
            self.rows_p = self.curr.fetchall()

            if len(self.rows_p) != 0:
                self.Table_par.delete(*self.Table_par.get_children())
                for self.row_p in self.rows_p:
                    self.Table_par.insert('', END, values=self.row_p)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO DEL PARALELO CON EL ID: " +
                                 self.search_id_par)
            self.search_field_par.set('')

    def show_data_par(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("SELECT * FROM paralelos")

        self.rows_p = self.curr.fetchall()
        if len(self.rows) != 0:

            self.Table_par.delete(*self.Table_par.get_children())
            for self.row_p in self.rows_p:
                self.Table_par.insert('', END, values=self.row_p)

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

    def assesor_btn(self):
        self.root.destroy()

        from Secretaria.Assesor_Window_S import Assesor_S
        st_root = Tk()
        Assesor_S(st_root)
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
    application = Course_S(root)
    root.mainloop()
