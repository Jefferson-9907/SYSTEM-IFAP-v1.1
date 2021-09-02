"""from funciones_auxiliares import conexion_consulta"""
from tkinter import messagebox

from reportes import ReciboFactura

import Backend.connection
import Model_class.facturas_registration
import Model_class.detalle_facturas_registration

class Producto:

    def __init__(self, *args, **kwargs):

        self.id_implemento = None
        self.descripcion = None
        self.precio = None

    """def seleccionar(self):
        consulta = 'SELECT * FROM implementos WHERE id_implemento=?'
        parametros = [self.id_implemento]
        return conexion_consulta(consulta, parametros)"""

    def validar(self):  # Metodo que valida que los inputs no ingrese valores nulos
        atributos = self.__dict__.items()
        centinela = True

        for datos in atributos:
            if datos[1] == '':
                centinela = False
                break
            elif datos[1] is not None:
                centinela = True

        return centinela


class ProductoFacturar(Producto):

    def __init__(self, *args, **kwargs):
        super(Producto, self).__init__(*args, **kwargs)
        self.id_factura = ''
        self.id_implemento = ''
        self.precio = 0
        self.cantidad = 0
        self.sub_total = 0
        self.lista_productos = []
        self.total = 0
        self.pago = 0
        self.cambio = 0

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

    def calcular_subtotal(self):
        return self.precio * self.cantidad

    def convertir_dic(self):
        return {'codigo': self.id_implemento,
                'nombre': self.descripcion,
                'precio_venta': self.precio,
                'cantidad': self.cantidad,
                'sub-total': self.sub_total
                }

    def guardar(self):
        try:
            obj_course_database = Model_class.facturas_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            query = 'INSERT INTO detalle_facturas (id_detalle_factura, id_factura, id_implemento, cantidad, ' \
                   'total_factura) VALUES(?, ?, ?, ?, ?)'
            values = (self.id_factura, self.id_implemento, self.precio, self.cantidad)
            self.db_connection.insert(query, values)

        except BaseException as msg:
            messagebox.showerror("ERROR!!!", f"NO SE HAN PODIDO GUARDAR EL DETALLE DE LA FACTURA {msg}")

class Factura(ReciboFactura):

    def __init__(self, *args, **kwargs):
        super(Factura, self).__init__(*args, **kwargs)

        self.id_factura = ''
        self.e_n_ced_al = ''
        self.fecha_creacion = ''
        self.hora_creacion = ''
        self.lista_productos = []

        # ======================Backend connection=============
        self.db_connection = Backend.connection.DatabaseConnection()

    def guardar(self):
        try:
            obj_course_database = Model_class.facturas_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_course_database.get_database())

            query = 'INSERT INTO facturas (id_factura, id_estudiante, fecha, hora) VALUES(?, ?, ?, ?)'
            values = (self.id_factura, self.e_n_ced_al, self.fecha_creacion, self.hora_creacion)
            self.db_connection.insert(query, values)

        except BaseException as msg:
            messagebox.showerror("ERROR!!!", f"NO SE HAN PODIDO GUARDAR EL DETALLE DE LA FACTURA {msg}")

    def remover_producto(self, nombre):
        for lista_productos in self.lista_productos:
            if nombre == lista_productos.descripcion:
                self.lista_productos.remove(lista_productos)
        return True

    def calcular_total(self):
        total = 0
        for sub_total in self.lista_productos:
            total = float(sub_total.calcular_subtotal()) + total
        self.total = total
        return total
