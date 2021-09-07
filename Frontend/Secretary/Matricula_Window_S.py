# Import Modules
from _datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox, ttk
import random

import Backend.connection
import Model_class.matricula_registration

import Frontend.login_form
import Frontend.Secretary.Principal_Window_S
import Frontend.Secretary.Student_Window_S
import Frontend.Secretary.Matricula_Window_S
import Frontend.Secretary.Assesor_Window_S
import Frontend.Secretary.Course_Window_S
import Frontend.Secretary.Paralelo_Window_S
import Frontend.Secretary.Implements_Window_S
import Frontend.Secretary.Password_Window_S


class Matricula_S:

    def __init__(self, root):
        self.acciones = CRUD.Form_Matricula()

        self.root = root
        self.root.title("SYST_CONTROL--›MATRICULACIÓN")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'matricula': PhotoImage(file='./recursos/icon_n_al.png'),
            'matricular': PhotoImage(file='./recursos/icon_aceptar.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'eliminar': PhotoImage(file='./recursos/icon_del.png'),
            'limpiar': PhotoImage(file='./recursos/icon_clean.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),

        }

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=630, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=630, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (MATRICULACIÓN)')
        self.texto1.config(font=("Britannic", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=250, pady=0)

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

        self.cuaderno = ttk.Notebook(self.root, width=1345, height=625)
        self.cuaderno.grid(row=1, column=0, sticky='nw', padx=10, pady=5)

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
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='AYUDA', menu=self.Column6)
        self.Column6.add_command(label='Tutorial')
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column7)
        self.Column7.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column7.add_separator()
        self.Column7.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column7.add_separator()
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
        self.n_mat_al_m = StringVar()
        self.n_ced_al_m = StringVar()
        self.id_par_m = IntVar()
        self.id_par_m.set('')
        self.n_ced_as_m = StringVar()

        self.v_n_mat_al_m = StringVar()
        self.v_n_ced_al_m = StringVar()
        self.v_nombres_al = StringVar()
        self.v_apellidos_al = StringVar()
        self.v_id_par_m = IntVar()
        self.v_n_paralelo = StringVar()
        self.v_nombres_as = StringVar()
        self.v_apellidos_as = StringVar()

        self.search_field = StringVar()

        # Manage Frame
        self.Manage_Frame_m = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_m.place(x=20, y=75, width=435, height=285)

        self.m_title = Label(self.Manage_Frame_m, text="-ADMINISTRAR MATRÍCULA-",
                             font=("Copperplate Gothic Bold", 16, "bold"), bg='#0d1e24', fg="White")
        self.m_title.grid(column=0, row=0, columnspan=3, padx=50, pady=25, sticky="W")

        self.Manage_Frame_m_1 = Frame(self.root, bd=4, bg='#0d1e24')
        self.Manage_Frame_m_1.place(x=25, y=150, width=420, height=185)

        self.l_n_mat_m = Label(self.Manage_Frame_m_1, text='No. MATRÍCULA', width='18',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_mat_m.grid(column=0, row=2, padx=5, pady=5, sticky="W")
        self.e_n_mat_m = Entry(self.Manage_Frame_m_1, textvariable=self.n_ced_al_m, width='13')
        self.e_n_mat_m.grid(column=1, row=2, padx=1, pady=5, sticky="W")
        self.e_n_mat_m["state"] = "disabled"

        self.l_n_c_al_m = Label(self.Manage_Frame_m_1, text='No. C.I ESTUDIANTE', width='18',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_c_al_m.grid(column=0, row=3, padx=5, pady=5, sticky="W")
        self.e_n_c_al_m = Entry(self.Manage_Frame_m_1, textvariable=self.n_ced_al_m, width='13')
        self.e_n_c_al_m.grid(column=1, row=3, padx=0, pady=5, sticky="W")
        self.e_n_c_al_m.focus()

        self.l_cur_m = Label(self.Manage_Frame_m_1, text='ID PARALELO', width='18', font=('Copperplate Gothic Bold',
                                                                                          10), bg='#808080')
        self.l_cur_m.grid(column=0, row=6, padx=5, pady=5, sticky="W")
        self.e_id_par_al_m = Entry(self.Manage_Frame_m_1, textvariable=self.id_par_m, width='32')
        self.e_id_par_al_m.grid(column=1, row=6, padx=1, pady=5, sticky="W")

        self.l_n_c_as_m = Label(self.Manage_Frame_m_1, text='No. C.I ASESOR', width='18',
                                font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_n_c_as_m.grid(column=0, row=7, padx=5, pady=5, sticky="W")
        self.e_n_c_as_m = Entry(self.Manage_Frame_m_1, textvariable=self.n_ced_as_m, width='32')
        self.e_n_c_as_m.grid(column=1, row=7, padx=1, pady=5, sticky="W")

        self.Manage_Frame_m_2 = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_m_2.place(x=20, y=365, width=435, height=315)

        self.v_m_title = Label(self.Manage_Frame_m_2, text="-VISUALIZAR MATRÍCULA-",
                               font=("Copperplate Gothic Bold", 16, "bold"), bg='#0d1e24', fg="White")
        self.v_m_title.grid(column=0, row=0, columnspan=3, padx=35, pady=25, sticky="W")

        self.clean_btn = Button(self.Manage_Frame_m_2, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_m1, compound=TOP)
        self.clean_btn.image = imagenes['limpiar']

        self.clean_btn.place(x=275, y=87)

        self.v_l_n_mat_m = Label(self.Manage_Frame_m_2, text='No. MATRÍCULA', width='18',
                                 font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.v_l_n_mat_m.grid(column=0, row=1, padx=5, pady=5, sticky="W")
        self.v_e_n_mat_m = Entry(self.Manage_Frame_m_2, textvariable=self.v_n_mat_al_m, width='13')
        self.v_e_n_mat_m.grid(column=1, row=1, padx=1, pady=5, sticky="W")
        self.v_e_n_mat_m["state"] = "disabled"

        self.v_l_n_c_al_m = Label(self.Manage_Frame_m_2, text='No. C.I ESTUDIANTE', width='18',
                                  font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.v_l_n_c_al_m.grid(column=0, row=2, padx=5, pady=5, sticky="W")
        self.v_e_n_c_al_m = Entry(self.Manage_Frame_m_2, textvariable=self.v_n_ced_al_m, width='13')
        self.v_e_n_c_al_m.grid(column=1, row=2, padx=0, pady=5, sticky="W")
        self.v_e_n_c_al_m["state"] = "disabled"

        self.v_l_nombres = Label(self.Manage_Frame_m_2, text='NOMBRES', width='18',
                                 font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.v_l_nombres.grid(column=0, row=3, padx=0, pady=5)
        self.v_e_nombres = Entry(self.Manage_Frame_m_2, textvariable=self.v_nombres_al, width='33')
        self.v_e_nombres.grid(column=1, row=3, padx=0, pady=5, sticky="W")
        self.v_e_nombres["state"] = "disabled"

        self.v_l_apellidos = Label(self.Manage_Frame_m_2, text='APELLIDOS', width='18', font=('Copperplate Gothic Bold',
                                                                                              10), bg='#808080')
        self.v_l_apellidos.grid(column=0, row=4, padx=1, pady=5)
        self.v_e_apellidos = Entry(self.Manage_Frame_m_2, textvariable=self.v_apellidos_al, width='33')
        self.v_e_apellidos.grid(column=1, row=4, padx=1, pady=5, sticky="W")
        self.v_e_apellidos["state"] = "disabled"

        self.v_l_n_c_as_m = Label(self.Manage_Frame_m_2, text='PARALELO', width='18',
                                  font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.v_l_n_c_as_m.grid(column=0, row=6, padx=5, pady=5, sticky="W")
        self.v_e_n_c_as_m = Entry(self.Manage_Frame_m_2, textvariable=self.v_n_paralelo, width='33')
        self.v_e_n_c_as_m.grid(column=1, row=6, padx=1, pady=5, sticky="W")
        self.v_e_n_c_as_m["state"] = "disabled"

        self.v_l_n_as_m = Label(self.Manage_Frame_m_2, text='N. ASESOR', width='18', font=('Copperplate Gothic Bold',
                                                                                           10), bg='#808080')
        self.v_l_n_as_m.grid(column=0, row=8, padx=5, pady=5, sticky="W")
        self.v_e_n_as_m = Entry(self.Manage_Frame_m_2, textvariable=self.v_nombres_as, width='33')
        self.v_e_n_as_m.grid(column=1, row=8, padx=1, pady=5, sticky="W")
        self.v_e_n_as_m["state"] = "disabled"

        self.v_l_a_as_m = Label(self.Manage_Frame_m_2, text='A. ASESOR', width='18',
                                font=('Copperplate Gothic Bold', 10),
                                bg='#808080')
        self.v_l_a_as_m.grid(column=0, row=9, padx=5, pady=5, sticky="W")
        self.v_e_a_as_m = Entry(self.Manage_Frame_m_2, textvariable=self.v_apellidos_as, width='33')
        self.v_e_a_as_m.grid(column=1, row=9, padx=1, pady=5, sticky="W")
        self.v_e_a_as_m["state"] = "disabled"

        # Button Frame
        self.btn_frame_m = Frame(self.root, bg='#0d1e24')
        self.btn_frame_m.place(x=50, y=280, width=375, height=75)

        self.add_btn = Button(self.btn_frame_m, image=imagenes['matricular'], text='MATRICULAR', width=80,
                              command=self.add_mat_al, compound=TOP)
        self.add_btn.image = imagenes['matricular']
        self.add_btn.grid(row=0, column=1, padx=3, pady=10)
        self.add_btn["state"] = "normal"

        self.up_btn = Button(self.btn_frame_m, image=imagenes['editar'], text='MODIFICAR', width=80,
                             command=self.update_m, compound=TOP)
        self.up_btn.image = imagenes['editar']
        self.up_btn.grid(row=0, column=2, padx=3, pady=10)
        self.up_btn["state"] = "disabled"

        self.del_btn = Button(self.btn_frame_m, image=imagenes['eliminar'], text='ELIMINAR', width=80,
                              command=self.delete_m, compound=TOP)
        self.del_btn.image = imagenes['eliminar']
        self.del_btn.grid(row=0, column=3, padx=3, pady=10)
        self.del_btn["state"] = "disabled"

        self.clean_btn = Button(self.btn_frame_m, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_m, compound=TOP)
        self.clean_btn.image = imagenes['limpiar']
        self.clean_btn.grid(row=0, column=4, padx=3, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=460, y=75, width=885, height=285)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field, font=("Arial", 10, "bold"),
                                bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_m, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_m, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame administar matrícula

        self.Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        self.Table_Frame.place(x=5, y=60, width=865, height=210)

        self.Y_scroll = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.Table = ttk.Treeview(self.Table_Frame, columns=("no_ma", "ci_est", "n_est", "a_est"),
                                  yscrollcommand=self.Y_scroll.set)

        self.Y_scroll.pack(side=RIGHT, fill=Y)
        self.Y_scroll.config(command=self.Table.yview)
        # bg="#00A1E4", fg="#FFFCF9", font=("Arial", 10, "bold")
        self.Table.heading("no_ma", text="No. MAT.")
        self.Table.heading("ci_est", text="C.I ESTUDIANTE")
        self.Table.heading("n_est", text="ID PARALELO")
        self.Table.heading("a_est", text="ID ASESOR")

        self.Table['show'] = "headings"
        self.Table.column("no_ma", width=10)
        self.Table.column("ci_est", width=20)
        self.Table.column("n_est", width=75)
        self.Table.column("a_est", width=75)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_m)

        # Table Frame administar matrícula
        # Detail Frame
        self.Detail_Frame1 = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame1.place(x=460, y=365, width=885, height=315)

        self.Table_Frame1 = Frame(self.Detail_Frame1, bg="#0A090C")
        self.Table_Frame1.place(x=5, y=15, width=865, height=280)

        self.Y_scroll1 = Scrollbar(self.Table_Frame1, orient=VERTICAL)
        self.Table1 = ttk.Treeview(self.Table_Frame1, columns=("no_ma", "ci_est", "n_est", "a_est", "cur", "n_ase",
                                                               "a_ase"), yscrollcommand=self.Y_scroll1.set)

        self.Y_scroll1.pack(side=RIGHT, fill=Y)
        self.Y_scroll1.config(command=self.Table1.yview)
        # bg="#00A1E4", fg="#FFFCF9", font=("Arial", 10, "bold")
        self.Table1.heading("no_ma", text="No. MAT.")
        self.Table1.heading("ci_est", text="No. C.I")
        self.Table1.heading("n_est", text="NOMBRES ESTUDIANTE")
        self.Table1.heading("a_est", text="APELLIDOS ESTUDIANTE")
        self.Table1.heading("cur", text="PARALELO")
        self.Table1.heading("n_ase", text="NOMBRES ASESOR")
        self.Table1.heading("a_ase", text="APELLIDOS ASESOR")

        self.Table1['show'] = "headings"
        self.Table1.column("no_ma", width=10)
        self.Table1.column("ci_est", width=10)
        self.Table1.column("n_est", width=70)
        self.Table1.column("a_est", width=70)
        self.Table1.column("cur", width=50)
        self.Table1.column("n_ase", width=75)
        self.Table1.column("a_ase", width=40)

        self.Table1.pack(fill=BOTH, expand=1)
        self.Table1.bind('<ButtonRelease 1>', self.get_fields_m1)
        self.show_data_m()
        self.show_data_m1()

    def add_mat_al(self):
        if self.n_ced_al_m.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA ALUMNO")
            self.e_n_c_al_m.focus()

        elif self.n_ced_as_m.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: No. CÉDULA ASESOR")
            self.e_n_c_as_m.focus()

        else:
            datos = (self.n_ced_al_m.get(), self.n_ced_al_m.get(), self.id_par_m.get(), self.n_ced_as_m.get())
            self.acciones.add_mat(datos)

            # self.clear_field()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DE LA MATRÍCULA GUARDADA EN EL REGISTRO "
                                                       "CORRECTAMENTE!!!")
            self.show_data_m()
            self.show_data_m1()

    def clear_field_m(self):
        self.n_ced_al_m.set('')
        """self.nombres_al.set('')
        self.apellidos_al.set('')"""
        self.id_par_m.set('')
        self.n_ced_as_m.set('')
        self.e_n_c_al_m.focus()
        self.add_btn["state"] = "normal"
        self.up_btn["state"] = "disabled"
        self.del_btn["state"] = "disabled"

    def clear_field_m1(self):
        self.v_n_mat_al_m.set('')
        self.v_n_ced_al_m.set('')
        self.v_nombres_al.set('')
        self.v_apellidos_al.set('')
        self.v_n_paralelo.set('')
        self.v_nombres_as.set('')
        self.v_apellidos_as.set('')

    def get_fields_m(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']

        self.n_mat_al_m.set(row[0])
        self.n_ced_al_m.set(row[1])
        self.id_par_m.set(row[2])
        self.n_ced_as_m.set(row[3])
        self.add_btn["state"] = "disabled"
        self.up_btn["state"] = "normal"
        self.del_btn["state"] = "normal"

    def get_fields_m1(self, row):
        self.cursor_row = self.Table1.focus()
        self.content = self.Table1.item(self.cursor_row)
        row = self.content['values']

        self.v_n_mat_al_m.set(row[0])
        self.v_n_ced_al_m.set(row[1])
        self.v_nombres_al.set(row[2])
        self.v_apellidos_al.set(row[3])
        self.v_n_paralelo.set(row[4])
        self.v_nombres_as.set(row[5])
        self.v_apellidos_as.set(row[6])

    def update_m(self):
        if self.n_ced_al_m.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE MODIFICAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()

            sql = f"""UPDATE matricula SET id_matricula="{self.n_mat_al_m.get()}",\
                    id_estudiante="{self.n_ced_al_m.get()}", id_paralelo="{self.id_par_m.get()}",\
                    id_asesor="{self.n_ced_as_m.get()}" WHERE id_matricula={str(self.n_mat_al_m.get())}"""
            self.curr.execute(sql)
            self.connect.commit()

            self.show_data_m()
            # self.connect.close()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DE LA MATRÍCULA DEL ESTUDIANTE CON No. C.I: " +
                                self.n_ced_al_m.get() + " HAN SIDO ACTUALIZADOS EN EL REGISTRO CORRECTAMENTE!!!")
            self.clear_field_m()

    def delete_m(self):
        if self.n_mat_al_m.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.conn.cursor()

            self.sql = f"""DELETE FROM matricula WHERE id_matricula='{self.n_mat_al_m.get()}'"""
            self.curr.execute(self.sql)

            self.conn.commit()
            self.show_data_m()
            self.clear_field_m()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "MATRÍCULA ELIMINADA DEL REGISTRO CORRECTAMENTE!!!")

    def search_data_m(self):
        if self.search_field.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: No. DE CÉDULA")
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_n_ced = self.search_field.get()
        sql = f"""SELECT id_matricula, id_estudiante, id_paralelo, id_asesor\
                FROM matricula WHERE id_matricula={self.search_n_ced}"""
        self.curr.execute(sql)
        self.curr.fetchall()

        if self.curr.rowcount == 1:
            self.search_field.set('')
            self.sql = f"""SELECT id_matricula, id_estudiante, id_paralelo, id_asesor\
                    FROM matricula WHERE id_matricula={self.search_n_ced}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                self.Table.delete(*self.Table.get_children())
                for self.row in self.rows:
                    self.Table.insert('', END, values=self.row)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO CON EL No. CÉDULA: " +
                                 self.search_n_ced)
            self.search_field.set('')

    def show_data_m(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS matricula("
                          "id_matricula INT PRIMARY KEY, "
                          "id_estudiante VARCHAR(20), "
                          "id_curso INT, "
                          "id_paralelo INT, "
                          "id_asesor VARCHAR(20))")
        self.curr.execute("SELECT * FROM matricula ORDER BY id_matricula ASC ")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table.delete(*self.Table.get_children())
            for self.row in self.rows:
                self.Table.insert('', END, values=self.row)

            self.connect.commit()
        self.connect.close()

    def show_data_m1(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("SELECT id_matricula, e.id_estudiante, e.nombres, e.apellidos, p.nombre_paralelo, a.nombres, "
                          "a.apellidos "
                          "FROM matricula m "
                          "INNER JOIN estudiantes e ON m.id_estudiante = e.id_estudiante "
                          "INNER JOIN paralelos p "
                          "ON m.id_paralelo = p.id_paralelo "
                          "INNER JOIN asesores a "
                          "ON m.id_asesor = a.id_asesor ")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table1.delete(*self.Table1.get_children())
            for self.row1 in self.rows:
                self.Table1.insert('', END, values=self.row1)

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
    application = Matricula_S(root)
    root.mainloop()