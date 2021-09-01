# Import Modules
import random
from _datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.ttk import Treeview

import mariadb
import Backend.connection

import Frontend.login_form
import Frontend.Principal_Window_A
import Frontend.Student_Window_A
import Frontend.Matricula_Window_A
import Frontend.Assesor_Window_A
import Frontend.Course_Window_A
import Frontend.Paralelo_Window_A
import Frontend.Facturation_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A
import Frontend.Users_Window_A


class Implement:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Implementos")
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
        self.cuaderno = ttk.Notebook(self.root, width=1340, height=625)
        self.cuaderno.grid(row=1, column=0, sticky='nw', padx=10, pady=5)

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
        self.Column4.add_command(label='Menú Cursos', command=self.courses_btn)
        self.Column4.add_command(label='Menú Paralelos', command=self.paralelos_btn)
        self.Column4.add_command(label='Implementos')
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
        self.Column8.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column8.add_separator()
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

        # Manage Frame Cursos
        self.Manage_Frame_impl = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_impl.place(x=20, y=75, width=450, height=605)

        m_title_c = Label(self.Manage_Frame_impl, text="-ADMINISTAR IMPLEMENTOS-",
                          font=("Copperplate Gothic Bold", 16, "bold"), bg='#0d1e24', fg="White")
        m_title_c.grid(row=0, columnspan=2, padx=40, pady=20)

        self.id_implemento = IntVar()
        self.id_implemento.set('')
        self.id_curso = IntVar()
        self.id_curso.set('')
        self.descripcion = StringVar()
        self.costo_impl = DoubleVar()
        self.costo_impl.set('')
        self.search_field_impl = StringVar()

        self.l_id_impl = Label(self.Manage_Frame_impl, text='CÓDIGO', width='12',
                               font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_impl.grid(column=0, row=1, padx=0, pady=5)
        self.e_id_impl = Entry(self.Manage_Frame_impl, textvariable=self.id_implemento, width='10')
        self.e_id_impl.grid(column=1, row=1, padx=0, pady=5, sticky="W")
        self.e_id_impl.focus()
        # self.e_id_impl["state"] = "disabled"

        self.l_id_cur = Label(self.Manage_Frame_impl, text='ID CURSO', width='12',
                              font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_id_cur.grid(column=0, row=2, padx=0, pady=5)
        id_curso_box = ttk.Combobox(self.Manage_Frame_impl, textvariable=self.id_curso, width='6',
                                    font=("Arial", 9, "bold"), state="readonly")
        id_curso_box['values'] = ("3001", "3002", "3003", "3004")
        id_curso_box.grid(column=1, row=2, padx=0, pady=10, sticky="W")

        self.l_descr = Label(self.Manage_Frame_impl, text='DESCRIPCIÓN', width='12',
                             font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_descr.grid(column=0, row=3, padx=0, pady=5)
        self.e_descr = Entry(self.Manage_Frame_impl, textvariable=self.descripcion, width='50')
        self.e_descr.grid(column=1, row=3, padx=0, pady=5, sticky="W")

        self.l_cost_imple = Label(self.Manage_Frame_impl, text='COSTO', width='12',
                                  font=('Copperplate Gothic Bold', 10), bg='#808080')
        self.l_cost_imple.grid(column=0, row=4, padx=0, pady=5)
        self.e_cost_imple = Entry(self.Manage_Frame_impl, textvariable=self.costo_impl, width='8')
        self.e_cost_imple.grid(column=1, row=4, padx=0, pady=5, sticky="W")

        # Button Frame
        self.btn_frame = Frame(self.Manage_Frame_impl, bg='#0d1e24')
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
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='#0d1e24')
        self.Detail_Frame.place(x=475, y=75, width=865, height=605)

        self.lbl_search = Label(self.Detail_Frame, text="BUSCAR", bg='#0d1e24', fg="White",
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
        self.Table = Treeview(Table_Frame, columns=("id_impl", "id_cur", "descr_impl", "cost_impl"),
                              yscrollcommand=Y_scroll.set)

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.Table.yview)
        self.Table.heading("id_impl", text="ID IMPLEMENTO")
        self.Table.heading("id_cur", text="ID CURSO")
        self.Table.heading("descr_impl", text="DESCRIPCIÓN")
        self.Table.heading("cost_impl", text="PRECIO")

        self.Table['show'] = "headings"
        self.Table.column("id_impl", width=10)
        self.Table.column("id_cur", width=10)
        self.Table.column("descr_impl", width=400)
        self.Table.column("cost_impl", width=10)

        self.Table.pack(fill=BOTH, expand=1)
        self.Table.bind('<ButtonRelease 1>', self.get_fields_impl)

        self.show_data_impl()

        # FUNCIONES CURSOS

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
        if self.descripcion.get() == '':
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE EL CAMPO: DESCRIPCIÓN ")
            self.e_descr.focus()

        else:
            cone = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            cursor = cone.cursor()
            sql = "INSERT INTO implementos(id_curso, descripcion, costo_implemento) VALUES (?, ?, ?)"
            cursor.execute(sql, (self.id_curso.get(), self.descripcion.get(), self.costo_impl.get()))
            cone.commit()

            self.clear_field_impl()
            self.show_data_impl()
            # self.clear_field()
            cone.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL IMPLEMENTO GUARDADOS EN EL REGISTRO CORRECTAMENTE!!!")

    def clear_field_impl(self):
        self.id_implemento.set('')
        self.id_curso.set('')
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
        self.id_curso.set(row[1])
        self.descripcion.set(row[2])
        self.costo_impl.set(row[3])
        self.update_btn["state"] = "normal"
        self.delete_btn["state"] = "normal"

    def update_impl(self):
        if self.id_curso.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE MODIFICAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.connect.cursor()

            sql = f"""UPDATE implementos SET id_curso="{self.id_curso.get()}", descripcion="{self.descripcion.get()}"\
            WHERE id_implemento={self.id_implemento.get()}"""
            self.curr.execute(sql)
            self.connect.commit()

            self.show_data_impl()
            # self.connect.close()
            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL IMPLEMENTO: " + self.descripcion.get() +
                                " HAN SIDO ACTUALIZADO EN EL REGISTRO CORRECTAMENTE!!!")
            self.clear_field_impl()

    def delete_impl(self):
        if self.id_implemento.get() == "":
            messagebox.showerror("ERROR!!!", "NO HAY CAMPOS CON DATOS QUE ELIMINAR,\n"
                                             "SELECCIONE UN REGISTRO!!!")

        else:
            self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
            self.curr = self.conn.cursor()

            self.sql = f"""DELETE FROM implementos WHERE id_implemento={self.id_implemento.get()}"""
            self.curr.execute(self.sql)

            self.conn.commit()

            self.show_data_impl()
            self.clear_field_impl()
            self.conn.close()

            messagebox.showinfo("SYST_CONTROL(IFAP®)", "DATOS DEL IMPLEMENTO ELIMINADOS DEL REGISTRO CORRECTAMENTE!!!")

    def search_data_impl(self):
        if self.search_field_impl.get() == "":
            messagebox.showerror("ERROR!!!", "POR FAVOR INGRESE EL CAMPO: ID DE IMPLEMENTO")
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.search_id_impl = self.search_field_impl.get()
        sql = f"""SELECT id_implemento FROM implementos WHERE id_implemento = {self.search_id_impl}"""
        self.curr.execute(sql)
        self.curr.fetchall()
        if self.curr.rowcount == 1:
            self.sql = f"""SELECT * FROM implementos WHERE id_implemento={self.search_id_impl}"""
            self.curr.execute(self.sql)
            self.rows = self.curr.fetchall()

            if len(self.rows) != 0:
                self.Table.delete(*self.Table.get_children())
                for self.row in self.rows:
                    self.Table.insert('', END, values=self.row)
                self.connect.commit()
        else:
            messagebox.showerror("ERROR!!!", "NO EXISTE EL REGISTRO DEL IMPLEMENTO CON EL ID: " +
                                 self.search_id_impl)
            self.search_field_impl.set('')

    def show_data_impl(self):
        self.connect = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.connect.cursor()
        self.curr.execute("SELECT * FROM implementos")
        self.rows = self.curr.fetchall()

        if len(self.rows) != 0:

            self.Table.delete(*self.Table.get_children())
            for self.row in self.rows:
                self.Table.insert('', 0, values=self.row)

            self.connect.commit()
        self.connect.close()

    def conex_impl(self):
        self.conn = mariadb.connect(host="localhost", user="root", passwd="", database="system_bd_ifap")
        self.curr = self.conn.cursor()
        self.curr.execute("SELECT nombre_curso FROM cursos")
        self.result = self.curr.fetchall()
        self.conn.commit()

        return self.result

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
