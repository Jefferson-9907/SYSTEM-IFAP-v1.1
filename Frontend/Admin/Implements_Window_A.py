# Import Modules
import random
from _datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

import Backend.connection
import Model_class.implement_registration

import Frontend.login_form
import Frontend.Admin.Principal_Window_A
import Frontend.Admin.Student_Window_A
import Frontend.Admin.Matricula_Window_A
import Frontend.Admin.Assesor_Window_A
import Frontend.Admin.Course_Window_A
import Frontend.Admin.Paralelo_Window_A
import Frontend.Admin.Facturation_Window_A
import Frontend.Admin.Report_Window_A
import Frontend.Admin.Password_Window_A
import Frontend.Admin.Users_Window_A


class Implement:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Implementos")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'nuevo': PhotoImage(file='recursos\\icon_aceptar.png'),
            'editar': PhotoImage(file='recursos\\icon_update.png'),
            'eliminar': PhotoImage(file='recursos\\icon_del.png'),
            'limpiar': PhotoImage(file='recursos\\icon_clean.png'),
            'buscar': PhotoImage(file='recursos\\icon_buscar.png'),
            'todo': PhotoImage(file='recursos\\icon_ver_todo.png'),

        }

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

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

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (IMPLEMENTOS)')
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
        self.Column2.add_command(label='Alumnos', command=self.student_btn)
        self.Column2.add_command(label='Matriculación', command=self.matricula_btn)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL MENÚ ASESORES
        # =============================================================
        self.menus.add_cascade(label='ASESORES', menu=self.Column3)
        self.Column3.add_command(label='Asesores', command=self.assesor_btn)
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ CURSOS
        # =============================================================
        self.menus.add_cascade(label='CURSOS', menu=self.Column4)
        self.Column4.add_command(label='Cursos', command=self.courses_btn)
        self.Column4.add_command(label='Paralelos', command=self.paralelos_btn)
        self.Column4.add_command(label='Implementos')
        self.Column5 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ FACTURACIÓN
        # =============================================================
        self.menus.add_cascade(label='FACTURACIÓN', menu=self.Column5)
        self.Column5.add_command(label='Facturación', command=self.facturation_btn)
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ REPORTES
        # =============================================================
        self.menus.add_cascade(label='REPORTES', menu=self.Column6)
        self.Column6.add_command(label='Generar Reportes', command=self.report_btn)
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

        # Manage Frame Cursos
        self.Manage_Frame_impl = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_impl.place(x=20, y=75, width=450, height=605)

        m_title_c = Label(self.Manage_Frame_impl, text="-ADMINISTAR IMPLEMENTOS-",
                          font=("Copperplate Gothic Bold", 16, "bold"), bg='#a27114', fg="White")
        m_title_c.grid(row=0, columnspan=2, padx=40, pady=20)

        self.id_implemento = IntVar()
        self.id_implemento.set('')
        self.descripcion = StringVar()
        self.costo_impl = DoubleVar()
        self.search_field_impl = StringVar()

        try:
            obj_implements_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_implements_database.get_database())

            query = "SELECT isnull(max(id_implemento+1), 1) FROM implementos"
            id_tuple = self.db_connection.select(query)

            self.id_list = []
            for i in id_tuple:
                id_implemento = i[0]
                self.id_list.append(id_implemento)

        except BaseException as msg:
            print(msg)

        self.l_id_impl = Label(self.Manage_Frame_impl, text='CÓDIGO', width='12',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_impl.grid(column=0, row=1, padx=0, pady=5)
        self.e_id_impl = Entry(self.Manage_Frame_impl, textvariable=self.id_implemento, width='10')
        self.e_id_impl.grid(column=1, row=1, padx=0, pady=5, sticky="W")
        self.id_implemento.set(self.id_list)

        self.l_descr = Label(self.Manage_Frame_impl, text='DESCRIPCIÓN', width='12',
                             font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_descr.grid(column=0, row=2, padx=0, pady=5)
        self.e_descr = Entry(self.Manage_Frame_impl, textvariable=self.descripcion, width='50')
        self.e_descr.focus()
        self.e_descr.grid(column=1, row=2, padx=0, pady=5, sticky="W")

        self.l_cost_imple = Label(self.Manage_Frame_impl, text='COSTO', width='12',
                                  font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_cost_imple.grid(column=0, row=3, padx=0, pady=5)
        self.e_cost_imple = Entry(self.Manage_Frame_impl, textvariable=self.costo_impl, width='8')
        self.e_cost_imple.grid(column=1, row=3, padx=0, pady=5, sticky="W")

        # Button Frame
        self.btn_frame = Frame(self.Manage_Frame_impl, bg='#a27114')
        self.btn_frame.place(x=5, y=250, width=430)

        self.add_btn = Button(self.btn_frame, image=imagenes['nuevo'], text='REGISTAR', width=80,
                              command=self.add_impl, compound=TOP)
        self.add_btn.image = imagenes['nuevo']
        self.add_btn.grid(row=0, column=1, padx=10, pady=10)

        self.update_btn = Button(self.btn_frame, image=imagenes['editar'], text='MODIFICAR', width=80,
                                 command=self.update_impl, compound=TOP)
        self.update_btn.image = imagenes['editar']
        self.update_btn.grid(row=0, column=2, padx=10, pady=10)
        self.update_btn["state"] = "disabled"

        self.delete_btn = Button(self.btn_frame, image=imagenes['eliminar'], text='ELIMINAR', width=80,
                                 command=self.delete_impl, compound=TOP)
        self.delete_btn.image = imagenes['eliminar']
        self.delete_btn.grid(row=0, column=3, padx=10, pady=10)
        self.delete_btn["state"] = "disabled"

        self.clear_btn = Button(self.btn_frame, image=imagenes['limpiar'], text='LIMPIAR', width=80,
                                command=self.clear_field_impl, compound=TOP)
        self.clear_btn.image = imagenes['limpiar']
        self.clear_btn.grid(row=0, column=4, padx=10, pady=10)

        # Detail Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#a27114')
        self.Detail_Frame.place(x=475, y=75, width=865, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 12, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=2, sticky="w")

        self.txt_search = Entry(self.Detail_Frame, width=15, textvariable=self.search_field_impl,
                                font=("Arial", 10, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, pady=10, padx=5, ipady=4, sticky="w")

        self.search_btn = Button(self.Detail_Frame, image=imagenes['buscar'], text='BUSCAR', width=80,
                                 command=self.search_data_impl, compound="right")
        self.search_btn.image = imagenes['buscar']
        self.search_btn.grid(row=0, column=2, padx=10, pady=10)

        self.show_all_btn = Button(self.Detail_Frame, image=imagenes['todo'], text='VER TODO', width=80,
                                   command=self.show_data_impl, compound="right")
        self.show_all_btn.image = imagenes['todo']
        self.show_all_btn.grid(row=0, column=3, padx=10, pady=10)

        # Table Frame

        Table_Frame = Frame(self.Detail_Frame, bg="#0A090C")
        Table_Frame.place(x=5, y=60, width=845, height=525)

        Y_scroll = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Table = Treeview(Table_Frame, columns=("id_impl", "descr_impl", "cost_impl"),
                              yscrollcommand=Y_scroll.set)

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.Table.yview)
        self.Table.heading("id_impl", text="ID IMPLEMENTO")
        self.Table.heading("descr_impl", text="DESCRIPCIÓN")
        self.Table.heading("cost_impl", text="PRECIO")

        self.Table['show'] = "headings"
        self.Table.column("id_impl", width=10)
        self.Table.column("descr_impl", width=400)
        self.Table.column("cost_impl", width=10)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_impl)

        self.show_data_impl()

        # FUNCIONES IMPLEMENTOS
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

    def add_impl(self):
        try:
            obj_user_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_user_database.get_database())

            query = "select * from implementos;"
            data = self.db_connection.select(query)
            self.implement_list = []

            for values in data:
                implement_data_list = values[1]
                self.implement_list.append(implement_data_list)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

        if self.descripcion.get() == "" or self.costo_impl.get() == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->ERROR", "TODOS LOS CAMPOS SON OBLIGATORIOS!!!")

        elif self.descripcion.get() in self.implement_list:
            messagebox.showerror("YA EXISTE!!!", f"{self.e_descr.get()} EL IMPLEMENTO YA EXISTE, INTENTE OTRO NOMBRE")

        else:
            self.click_submit()

    def click_submit(self):
        """
            Inicializar al hacer clic en el botón enviar, que tomará los datos del cuadro de entrada
            e inserte esos datos en la tabla de implementos después de la validación exitosa de esos datos
        """
        try:
            obj_usuarios_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_usuarios_database.get_database())

            query = 'insert into implementos (descripcion, costo_implemento) values (%s, %s);'
            values = (self.e_descr.get(), self.e_cost_imple.get())
            self.db_connection.insert(query, values)

            self.show_data_impl()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS GUARDADOS CORRECTAMENTE\n "
                                                       f"IMPLEMENTO={values[1]},\n "
                                                       f"COSTO={values[2]}")
            self.clear_field_impl()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def clear_field_impl(self):
        self.id_implemento.set('')
        self.descripcion.set('')
        self.costo_impl.set('')
        self.e_id_impl.focus()
        self.update_btn["state"] = "disabled"
        self.delete_btn["state"] = "disabled"

    def get_fields_impl(self, row):
        self.cursor_row = self.Table.focus()
        self.content = self.Table.item(self.cursor_row)
        row = self.content['values']
        self.id_implemento.set(row[0])
        self.descripcion.set(row[1])
        self.costo_impl.set(row[2])
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

    def update_impl(self):
        try:
            obj_implements_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_implements_database.get_database())

            query = f"""UPDATE implementos SET descripcion=%s, costo_implemento=%s WHERE id_implemento=%s"""

            values = (self.descripcion.get(), self.costo_impl.get(), self.id_implemento.get())
            self.db_connection.insert(query, values)

            self.show_data_impl()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL IMPLEMENTO\n"
                                                       f"IMPLEMENTO: {self.descripcion.get()}\n"
                                                       f"COSTO: {self.costo_impl.get()}\n"
                                                       f"HAN SIDO ACTUALIZADOS DEL REGISTRO")
            self.clear_field_impl()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def delete_impl(self):
        try:
            obj_implements_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_implements_database.get_database())

            tree_view_content = self.Table.focus()
            tree_view_items = self.Table.item(tree_view_content)
            tree_view_values = tree_view_items['values'][0]
            tree_view_values_1 = tree_view_items['values'][1]
            ask = messagebox.askyesno("SYST_CONTROL(IFAP®) (CONFIRMACIÓN ELIMINAR)",
                                      f"DESEA ALIMINAR AL IMPLEMENTO: {tree_view_values_1}")
            if ask is True:
                query = "delete from implementos where descripcion=%s;"
                self.db_connection.delete(query, (tree_view_values,))

                self.show_data_impl()
                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"DATOS DEL IMPLEMENTO: {tree_view_values_1} "
                                                           f"ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")
                self.clear_field_impl()

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

    def search_data_impl(self):
        a = self.search_field_impl.get()
        if self.search_field_impl.get() != '':
            if a.isnumeric():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN NÚMEROS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DEL IMPLEMENTO")
                self.search_field_impl.set("")
            elif a.isspace():
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "NO SE ADMITEN ESPACIOS EN EL CAMPO DE BÚSQUEDA "
                                                                    "DEL IMPLEMENTO")
                self.search_field_impl.set("")
            else:
                if a.isalpha():
                    try:
                        search_list = []
                        for child in self.Table.get_children():
                            val = self.Table.item(child)["values"][1]
                            search_list.append(val)

                        sorted_list = self.bubble_sort(search_list)
                        self.output = self.binary_search(sorted_list, self.search_field_impl.get())

                        if self.output:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->ENCONTRADO",
                                                f"EL IMPLEMENTO: '{self.output}' HA SIDO ENCONTRADO")

                            obj_implements_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
                            self.db_connection.create(obj_implements_database.get_database())

                            query = "select * from implementos where descripcion LIKE '" + str(self.output) + "%'"
                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2]]

                                self.Table.insert('', END, values=data_list)
                                self.search_field_impl.set("")

                        else:
                            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR",
                                                 "IMPLEMENTO NO ENCONTRADO,\nSE MOSTRARÁN RESULTADOS RELACIONADOS.")

                            obj_implements_database = Model_class.implement_registration.GetDatabase('use '
                                                                                                     'ddbb_sys_ifap;')
                            self.db_connection.create(obj_implements_database.get_database())

                            query = "select * from implementos where descripcion LIKE '%" + \
                                    str(self.search_field_impl.get()) + "%'"

                            data = self.db_connection.select(query)
                            self.Table.delete(*self.Table.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2]]

                                self.Table.insert('', END, values=data_list)
                                self.search_field_impl.set("")

                    except BaseException as msg:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                             f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                             f"REVISE LA CONEXIÓN: {msg}")
                else:
                    self.show_data_impl()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL IMPLEMENTO.")

    def show_data_impl(self):
        try:
            obj_implements_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_implements_database.get_database())

            query = "select * from implementos;"
            data = self.db_connection.select(query)
            self.Table.delete(*self.Table.get_children())

            for values in data:
                data_list = [values[0], values[1], values[2]]
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
        Frontend.Admin.Principal_Window_A.Principal(root)
        self.root.withdraw()
        root.deiconify()

    def student_btn(self):
        root = Toplevel()
        Frontend.Admin.Student_Window_A.Student(root)
        self.root.withdraw()
        root.deiconify()

    def matricula_btn(self):
        root = Toplevel()
        Frontend.Admin.Matricula_Window_A.Matricula(root)
        self.root.withdraw()
        root.deiconify()

    def assesor_btn(self):
        root = Toplevel()
        Frontend.Admin.Assesor_Window_A.Assesor(root)
        self.root.withdraw()
        root.deiconify()

    def courses_btn(self):
        root = Toplevel()
        Frontend.Admin.Course_Window_A.Course(root)
        self.root.withdraw()
        root.deiconify()

    def paralelos_btn(self):
        root = Toplevel()
        Frontend.Admin.Paralelo_Window_A.Paralelo(root)
        self.root.withdraw()
        root.deiconify()

    def implements_btn(self):
        root = Toplevel()
        Frontend.Admin.Implements_Window_A.Implement(root)
        self.root.withdraw()
        root.deiconify()

    def facturation_btn(self):
        root = Toplevel()
        Frontend.Admin.Facturation_Window_A.Ventana_Principal(root)
        self.root.withdraw()
        root.deiconify()

    def report_btn(self):
        root = Toplevel()
        Frontend.Admin.Report_Window_A.Reports(root)
        self.root.withdraw()
        root.deiconify()

    def pass_btn(self):
        root = Toplevel()
        Frontend.Admin.Password_Window_A.Password(root)
        self.root.withdraw()
        root.deiconify()

    def users_btn(self):
        root = Toplevel()
        Frontend.Admin.Users_Window_A.Users(root)
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
                                        'contrato "J.C.F DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 J.C.F DESING®. Todos los derechos reservados')


if __name__ == '__main__':
    root = Tk()
    application = Implement(root)
    root.mainloop()
