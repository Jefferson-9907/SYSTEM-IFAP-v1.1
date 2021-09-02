import random
from time import strftime

from tkinter import *
from tkinter.ttk import Treeview
from datetime import datetime

import Backend.connection
import Model_class.implement_registration
import Model_class.facturas_registration

from tkinter import messagebox
from ttkthemes import themed_tk as tk
from modelos import Producto, ProductoFacturar, Factura
from reportes import ReciboFactura

import Model_class.students_registration

import Frontend.Principal_Window_A
import Frontend.login_form
import Frontend.Student_Window_A
import Frontend.Matricula_Window_A
import Frontend.Assesor_Window_A
import Frontend.Course_Window_A
import Frontend.Paralelo_Window_A
import Frontend.Implements_Window_A
import Frontend.Report_Window_A
import Frontend.Password_Window_A
import Frontend.Users_Window_A


class Ventana_Principal:
    """
    Contiene todos los widgets necesario para la facturacion
    """

    def __init__(self, root):

        self.root = root
        self.root.title("SYST_CONTROL--›FACTURACIÓN")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('./recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        self.imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_add.png'),
            'editar': PhotoImage(file='./recursos/icon_update.png'),
            'reportes': PhotoImage(file='./recursos/icon_up.png'),
            'new': PhotoImage(file='./recursos/icon_new_ind.png'),
            'buscar': PhotoImage(file='./recursos/icon_buscar.png'),
            'todo': PhotoImage(file='./recursos/icon_ver_todo.png'),
            'facturar': PhotoImage(file='./recursos/icon_aceptar.png'),
            'actualizar': PhotoImage(file='./recursos/icon_upd.png')
        }

        # =============================================================
        # BANNER PANTALLA ESTUDIANTES
        # =============================================================

        self.txt = "SYSTEM CONTROL IFAP (FACTURACIÓN)"
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
        self.Column4.add_command(label='Menú Cursos', command=self.courses_btn)
        self.Column4.add_command(label='Menú Paralelos')
        self.Column4.add_command(label='Implementos', command=self.implements_btn)
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

        self.factura = Factura()
        self.search_field_impl = StringVar()

        self.validatecommand = self.root.register(self.solo_numero)
        self.validate_subtotal = self.root.register(self.mostrar_sub_total)

        # OPCIONES PRINCIPALES DE FACTURACIÓN
        self.Manage_Frame_impl = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_impl.place(x=15, y=85, width=520, height=605)

        self.l_Buscar = Label(self.Manage_Frame_impl, text="BUSCAR :", bg='#a27114', fg="White",
                              font=("Copperplate Gothic Bold", 10, "bold"))
        self.l_Buscar.place(x=5, y=15)

        self.txtBuscar = Entry(self.Manage_Frame_impl, width=20, textvariable=self.search_field_impl)
        self.txtBuscar.bind('<Return>', self.buscar_productos)
        self.txtBuscar.place(x=90, y=15)

        self.btnBuscar = Button(self.Manage_Frame_impl, image=self.imagenes['buscar'], text='BUSCAR', width=80,
                                command=lambda: self.buscar_productos(1), compound="right")
        self.btnBuscar.image = self.imagenes['buscar']
        self.btnBuscar.place(x=220, y=10)

        self.show_all_btn = Button(self.Manage_Frame_impl, image=self.imagenes['todo'], text='VER TODO',
                                   command=self.listar_productos, width=85, compound="right")
        self.show_all_btn.image = self.imagenes['todo']
        self.show_all_btn.place(x=315, y=10)

        self.BtnReportes = Button(self.Manage_Frame_impl, image=self.imagenes['reportes'],
                                  command=self.listar_productos, text='REFRESCAR', width=80, compound="right")
        self.BtnReportes.image = self.imagenes['reportes']
        self.BtnReportes.place(x=415, y=10)

        # Table Frame
        Table_Frame_impl = Frame(self.Manage_Frame_impl)
        Table_Frame_impl.place(x=5, y=65, width=500, height=520)

        Y_scroll = Scrollbar(Table_Frame_impl, orient=VERTICAL)
        self.listdetalle = Treeview(Table_Frame_impl, columns=("id_impl", "desc", "valor"), yscrollcommand=Y_scroll.set)
        self.listdetalle.tag_configure('gr', background='green')

        Y_scroll.pack(side=RIGHT, fill=Y)
        Y_scroll.config(command=self.listdetalle.yview)
        self.listdetalle.heading("id_impl", text="CÓD.")
        self.listdetalle.heading("desc", text="DESCRIPCIÓN")
        self.listdetalle.heading("valor", text="VALOR")

        self.listdetalle['show'] = "headings"
        self.listdetalle.column("id_impl", width=5)
        self.listdetalle.column("desc", width=290)
        self.listdetalle.column("valor", width=5)

        self.listdetalle.pack(fill=BOTH, expand=1)
        self.listdetalle.bind('<Double-1>', self.widget_agregar_producto_factura)
        self.listar_productos()

        self.label_facturacion = LabelFrame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.label_facturacion.place(x=550, y=85, width=800, height=605)

        self.lb_cod_factura = Label(self.label_facturacion, text='No. FACTURA', bg='#a27114', fg="White",
                                    font=("Copperplate Gothic Bold", 12, "bold"))
        self.lb_cod_factura.place(x=225, y=10)

        self.codigo_factura = StringVar()

        try:
            obj_courses_database = Model_class.facturas_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_courses_database.get_database())

            query = "SELECT isnull(max(id_factura+1), 1) FROM facturas"
            id_tuple = self.db_connection.select(query)

            self.id_list = []
            for i in id_tuple:
                id_factura = i[0]
                self.id_list.append(id_factura)

        except BaseException as msg:
            print(msg)

        self.txt_cod_factura = Entry(self.label_facturacion, state='readonly', textvariable=self.codigo_factura,
                                     fg='Red', width=10, font=('Copperplate Gothic Bold', 14), relief=RIDGE)
        self.codigo_factura.set(self.id_list)
        self.txt_cod_factura.place(x=375, y=10)

        self.search_field = StringVar()
        self.l_ced_al = Label(self.label_facturacion, text='No. C.I ALUMNO', font=('Copperplate Gothic Bold', 10),
                              bg='#808080')
        self.l_ced_al.place(x=10, y=40)
        self.e_n_ced_al = Entry(self.label_facturacion, textvariable=self.search_field, width=19)
        self.e_n_ced_al.place(x=140, y=40)

        self.b_buscar_al = Button(self.label_facturacion, text='BUSCAR', font=('Copperplate Gothic Bold', 8),
                                  bg='#333333', fg='white', command=self.search_data_al)
        self.b_buscar_al.place(x=275, y=40)

        self.l_name = Label(self.label_facturacion, text='NOMBRES', font=('Copperplate Gothic Bold', 10),
                            bg='#808080')
        self.l_name.place(x=10, y=70)
        self.nombres_al = StringVar()
        self.name_e = Entry(self.label_facturacion, width=27, textvariable=self.nombres_al, state='readonly')
        self.name_e.place(x=110, y=70)

        self.ape_l = Label(self.label_facturacion, text='APELLIDOS', font=('Copperplate Gothic Bold', 10),
                           bg='#808080')
        self.ape_l.place(x=285, y=70)
        self.apellidos_al = StringVar()
        self.ape_e_ = Entry(self.label_facturacion, width=30, textvariable=self.apellidos_al, state='readonly')
        self.ape_e_.place(x=390, y=70)

        self.lb_direccion = Label(self.label_facturacion, text='DIRECCIÓN', font=('Copperplate Gothic Bold', 10),
                                  bg='#808080')
        self.lb_direccion.place(x=10, y=100)
        self.direcccion_al = StringVar()
        self.dir_e_al = Entry(self.label_facturacion, width=66, textvariable=self.direcccion_al, state='readonly')
        self.dir_e_al.place(x=110, y=100)

        self.detalle_factura = Treeview(self.label_facturacion, columns=('#0', '#1', '#2', '#3'))
        self.detalle_factura.place(x=10, y=190, width=770, height=275)

        self.detalle_factura.heading('#0', text='Implemento')
        self.detalle_factura.heading('#1', text='Cant.')
        self.detalle_factura.heading('#2', text='P. Unit')
        self.detalle_factura.heading('#3', text='Subtotal')

        self.detalle_factura.column('#0', width=475)
        self.detalle_factura.column('#1', width=100)
        self.detalle_factura.column('#2', width=100)
        self.detalle_factura.column('#3', width=100)

        self.lb_detalle = Label(self.label_facturacion, text='-----DETALLE FACTURA-----', bg='#a27114', fg="White",
                                font=("Copperplate Gothic Bold", 16, "bold"))
        self.lb_detalle.place(x=230, y=160)

        self.total = StringVar()
        self.lb_total = Label(self.label_facturacion, text='TOTAL  $', font=("Britannic", 10, "bold"), width=8)
        self.lb_total.place(x=630, y=475)
        self.tx_total = Entry(self.label_facturacion, state='readonly', textvariable=self.total, width=11)
        self.tx_total.place(x=710, y=475)

        self.lb_pago = Label(self.label_facturacion, text='PAGO    $', font=("Britannic", 10, "bold"), width=8)
        self.lb_pago.place(x=630, y=500)
        self.txt_pago = Entry(self.label_facturacion, validate='key', validatecommand=(self.validatecommand, "%S"),
                              width=11)
        self.txt_pago.bind('<Return>', self.calcular_cambio)
        self.txt_pago.place(x=710, y=500)

        self.cambio = StringVar()
        self.lb_cambio = Label(self.label_facturacion, text='CAMBIO $', font=("Britannic", 10, "bold"), width=8)
        self.lb_cambio.place(x=630, y=525)
        self.tx_cambio = Entry(self.label_facturacion, state='readonly', textvariable=self.cambio, width=11)
        self.tx_cambio.place(x=710, y=525)

        self.act_btn = Button(self.label_facturacion, image=self.imagenes['actualizar'], text='NUEVA FACTURA',
                              font=("Britannic", 10, "bold"), compound="right", width=140,
                              command=self.facturation_btn)
        self.act_btn.image = self.imagenes['actualizar']
        self.act_btn.place(x=200, y=500)

        self.BtnFacturar = Button(self.label_facturacion, text='FACTURAR', font=("Britannic", 10, "bold"),
                                  image=self.imagenes['facturar'], compound="right", width=100,
                                  command=self.guardar_factura)
        self.BtnFacturar.images = self.imagenes['facturar']
        self.BtnFacturar.place(x=400, y=500)

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

    def solo_numero(self, char):
        return char in '1234567890.'

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

    def buscar_productos(self, event):
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
                        for child in self.listdetalle.get_children():
                            val = self.listdetalle.item(child)["values"][1]
                            search_list.append(val)

                        sorted_list = self.bubble_sort(search_list)
                        self.output = self.binary_search(sorted_list, self.search_field_impl.get())

                        if self.output:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->ENCONTRADO",
                                                f"EL IMPLEMENTO: '{self.output}' HA SIDO ENCONTRADO")

                            obj_implements_database = Model_class.implement_registration.GetDatabase('use '
                                                                                                     'ddbb_sys_ifap;')
                            self.db_connection.create(obj_implements_database.get_database())

                            query = "select * from implementos where descripcion LIKE '" + str(self.output) + "%'"
                            data = self.db_connection.select(query)
                            self.listdetalle.delete(*self.listdetalle.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2]]

                                self.listdetalle.insert('', END, values=data_list)
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
                            self.listdetalle.delete(*self.listdetalle.get_children())

                            for values in data:
                                data_list = [values[0], values[1], values[2]]

                                self.listdetalle.insert('', END, values=data_list)
                                self.search_field_impl.set("")

                    except BaseException as msg:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                             f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                             f"REVISE LA CONEXIÓN: {msg}")
                else:
                    self.listar_productos()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO DE BÚSQUEDA SE ENCUENTRA VACÍO\n"
                                                                "INGRESE EL NOMBRE DEL IMPLEMENTO.")

    def search_data_al(self):
        self.n_c_al = self.search_field.get()
        if self.search_field.get() == "":
            messagebox.showerror("SYST_CONTROL (IFAP®)-ERROR!!!", "INGRESE EL CAMPO: No. CÉDULA ESTUDIANTE")

        else:
            try:
                obj_matricula_database = Model_class.students_registration.GetDatabase('use ddbb_sys_ifap;')
                self.db_connection.create(obj_matricula_database.get_database())

                query = "select * from estudiantes where id_estudiante='" + self.n_c_al + "';"
                data = self.db_connection.select(query)
                for values in data:
                    data_list_n = str(values[1])
                    data_list_a = str(values[2])
                    data_list_d = str(values[4])
                    self.nombres_al.set(data_list_n)
                    self.apellidos_al.set(data_list_a)
                    self.direcccion_al.set(data_list_d)

            except BaseException as msg:
                messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                      f"REVISE LA CONEXIÓN: {msg}")

    def agregar_producto_factura(self, ):
        """
         Funcion asociada para agregar un producto a la
         factura
        """
        producto_factura = ProductoFacturar()
        producto_factura.id_factura = self.codigo_factura.get()
        producto_factura.id = self.codigo.get()
        producto_factura.descripcion = self.descripcion.get()
        producto_factura.precio = float(self.precio.get())
        producto_factura.cantidad = int(self.txt_cantidad.get())
        producto_factura.sub_total = str(producto_factura.calcular_subtotal())

        id = self.validar_producto_existente_factura(producto_factura.descripcion)  # Valida si el producto esta
        # existente solo para aumentar su cantidad
        if id:
            self.factura.remover_producto(producto_factura.descripcion)
            producto_facturar_edit = self.detalle_factura.item(id)
            producto_viejo_valores = producto_facturar_edit['values']
            producto_factura_cant_ant = int(producto_viejo_valores[0])
            self.detalle_factura.delete(id)
            nueva_cantidad = int(producto_factura.cantidad) + int(producto_factura_cant_ant)
            producto_factura.cantidad = nueva_cantidad
            producto_factura.sub_total = str(producto_factura.calcular_subtotal())
            self.detalle_factura.insert('', 0, text=producto_factura.descripcion, values=(
                producto_factura.cantidad, producto_factura.precio, producto_factura.sub_total), iid=id)

        else:
            self.detalle_factura.insert('', 0, text=producto_factura.descripcion, values=(
                producto_factura.cantidad, producto_factura.precio, producto_factura.sub_total))
        self.factura.lista_productos.append(producto_factura)

        self.producto_factura.destroy()
        self.total.set(str(self.factura.calcular_total()))

    def mostrar_sub_total(self, event):
        # Calcula el subtotal del un producto y lo muestra
        sub_total = float(self.precio.get()) * int(self.txt_cantidad.get())
        self.sub_total.set(str(sub_total))

    def widget_agregar_producto_factura(self, event):
        """
         Ventana hija asociada al momento de selecionar
         un producto y muestra su informacion y la cantidad
         de producto requerida
        """
        id = self.listdetalle.focus()
        producto_focus = self.listdetalle.item(id)
        lista = []
        for atributos in producto_focus['values']:
            lista.append(atributos)

        self.producto_factura = Toplevel()
        self.producto_factura.geometry('475x200')
        self.producto_factura.title('AGREGAR A FACTURA')
        self.producto_factura.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.producto_factura.configure(bg='#a27114')
        self.producto_factura.wait_visibility()
        self.producto_factura.grab_set()
        self.producto_factura.transient(master=self.root)

        # Variables
        self.codigo = StringVar()
        self.descripcion = StringVar()
        self.precio = StringVar()
        self.cantidad = StringVar()
        self.sub_total = StringVar()

        self.lb_cod_producto = Label(self.producto_factura, text='CÓD. IMPLEMENTO', font=("Britannic", 10, "bold"),
                                     bg='#808080')

        self.lb_cod_producto.place(x=10, y=10)
        self.tx_codigo = Entry(self.producto_factura, state='readonly', textvariable=self.codigo, width=10)
        self.tx_codigo.place(x=150, y=10)

        self.codigo.set(producto_focus['text'])
        self.codigo.set(lista[0])

        self.lb_nb_producto = Label(self.producto_factura, text='DESCRIPCIÓN', font=('Copperplate Gothic Bold', 10),
                                    bg='#808080')
        self.lb_nb_producto.place(x=10, y=40)

        self.txt_nb_producto = Entry(self.producto_factura, state='readonly', textvariable=self.descripcion, width=50)
        self.txt_nb_producto.place(x=150, y=40)
        self.descripcion.set(lista[1])

        self.lb_precio = Label(self.producto_factura, text='PRECIO', font=("Britannic", 10, "bold"), bg='#808080')
        self.lb_precio.place(x=10, y=70)

        self.txt_precio = Entry(self.producto_factura, state='readonly', textvariable=self.precio, width=10)
        self.txt_precio.place(x=150, y=70)
        self.precio.set(lista[2])

        self.lb_cantidad = Label(self.producto_factura, text='CANTIDAD', font=("Britannic", 10, "bold"), bg='#808080')
        self.lb_cantidad.place(x=10, y=100)

        self.cantidad.set('1')
        self.txt_cantidad = Entry(self.producto_factura, textvariable=self.cantidad, validate='key',
                                  validatecommand=(self.validatecommand, "%S"), width=10)

        self.txt_cantidad.bind('<Return>', self.mostrar_sub_total)
        self.txt_cantidad.place(x=150, y=100)
        self.txt_cantidad.focus()

        self.lb_sub_total = Label(self.producto_factura, text='SUB-TOTAL', font=("Britannic", 10, "bold"), bg='#808080')
        self.lb_sub_total.place(x=10, y=130)

        self.txt_sub_total = Entry(self.producto_factura, state='readonly', textvariable=self.sub_total, width=10)
        self.txt_sub_total.place(x=150, y=130)

        self.btAdd = Button(self.producto_factura, text='AÑADIR A FACTURA', font=("Britannic", 10, "bold"),
                            command=self.agregar_producto_factura)
        self.btAdd.place(x=175, y=160)

    def listar_productos(self):
        try:
            obj_student_database = Model_class.implement_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_student_database.get_database())

            query = "select * from implementos;"
            data = self.db_connection.select(query)
            self.listdetalle.delete(*self.listdetalle.get_children())
            for values in data:
                data_list = [values[0], values[1], values[2]]
                self.listdetalle.insert('', END, values=data_list)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)",
                                 f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                 f"REVISE LA CONEXIÓN: {msg}")

    def validar_producto_existente_factura(self, nombre):
        """
        Funcion que verifica si un producto esta añadido a la factura
        Si el caso es verdadero la cantidad solo se actualiza
        """
        lista_producto = self.detalle_factura.get_children()

        for productos in lista_producto[::-1]:
            producto_agregado = self.detalle_factura.item(productos)
            if nombre == producto_agregado['text']:
                return productos
            else:
                return False

    def calcular_cambio(self, event):
        # Calcula el cambio
        billete = float(self.txt_pago.get())
        cambio = billete - float(self.total.get())
        self.cambio.set(str(cambio))

    def guardar_factura(self):
        """Guarda el registro de la factura"""
        if self.txt_pago != '':  # Si el pago no esta vacio
            factura = self.factura

            for productos_factura in self.factura.lista_productos:
                productos_factura.guardar()

            factura.id_factura = self.codigo_factura.get()
            id_al = self.name_e.get()
            lista_al = id_al.split('_')
            factura.id_alumno = lista_al[0]
            factura.nom_ape_al = self.name_e.get() + " " + self.apellidos_al.get()
            factura.n_c_al = self.e_n_ced_al.get()
            factura.dir_al = self.dir_e_al.get()
            data = datetime.now()
            fomato_f = "%A %d-%B-%Y--%H:%M:%S %p "
            form_fecha = "%d-%m-%Y"
            factura.fecha = str(data.strftime(form_fecha))
            form_hora = "%H:%M:%S"
            factura.hora = str(data.strftime(form_hora))
            factura.fecha_creacion = str(data.strftime(fomato_f))
            factura.pago = self.txt_pago.get()
            factura.cambio = self.cambio.get()
            recibo = ReciboFactura()  # Instancia del recibo factura
            recibo.detalles_factura(factura)  # se pasa el objeto para ser llenado el recibo
            recibo.save()

            recibo.__del__()

            factura.guardar()
            factura.lista_productos.clear()
            self.listar_productos()
        else:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "EL CAMPO: PAGO NO PUEDE ESTAR VACÍO!!!")





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
    Ventana_Principal(root)
    root.mainloop()


if __name__ == '__main__':
    root()
