from funciones_auxiliares import conexion_consulta
from reportes import ReciboFactura


class Producto:

    def __init__(self, *args, **kwargs):

        self.id_implemento = None
        self.id_curso = None
        self.descripcion = None
        self.precio = None
        self.stock = None
        self.estado = None

    def seleccionar(self):
        consulta = 'SELECT * FROM implementos WHERE id_implemento=?'
        parametros = [self.id_implemento]
        return conexion_consulta(consulta, parametros)

    def guardar(self):
        consulta = 'INSERT INTO implementos(id_implemento, id_curso, descripcion, costo_implemento, inventario, ' \
                   'estado) VALUES(?, ?, ?, ?, ?, ?)'
        parametros = [(parametro[1]) for parametro in self.__dict__.items()]

        return conexion_consulta(consulta, parametros)

    def actualizar(self):
        consulta = 'UPDATE implementos set id_implemento=?, id_curso=?, descripcion=?, costo_implemento=?, ' \
                   'inventario=?, estado=?  WHERE id_implemento=?'
        parametros = [(parametro[1]) for parametro in self.__dict__.items()]
        parametros.append(self.id_implemento)
        print(parametros)

        return conexion_consulta(consulta, parametros)

    def inactivar(self):
        consulta = 'UPDATE implementos set estado=? WHERE id_implemento=?'
        parametros = [self.estado, self.id_implemento]
        return conexion_consulta(consulta, parametros)

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
        consulta = 'INSERT INTO detalle_facturas VALUES(?, ?, ?, ?)'
        parametros = [self.id_factura, self.id_implemento, self.precio, self.cantidad]
        conexion_consulta(consulta, parametros)
        # self.reducir_existencia()

    """def reducir_existencia(self):
        producto_reducir = self.seleccionar()
        for producto_reducido in producto_reducir:
            stock = int(producto_reducido[4])
        
        nuevo_stock = stock-self.cantidad

        consulta = 'UPDATE producto set inventario=? WHERE id=?'
        parametros = [nuevo_stock, self.id]
        conexion_consulta(consulta, parametros)"""


class Factura(ReciboFactura):

    def __init__(self, *args, **kwargs):
        super(Factura, self).__init__(*args, **kwargs)

        self.id_factura = ''
        # self.e_n_ced_al = ''
        self.fecha_creacion = ''
        self.hora_creacion = ''
        self.lista_productos = []

    def guardar(self):
        consulta = 'INSERT INTO facturas VALUES(?, ?, ?)'
        parametros = [
            self.id_factura, self.fecha_creacion,
            self.hora_creacion
        ]
        conexion_consulta(consulta, parametros)

    """def obtener_numero_factura(self):
        self.codigo_factura = self.codigo_factura + 1

        return self.codigo_factura"""

    def remover_producto(self, nombre):
        for lista_productos in self.lista_productos:
            if nombre == lista_productos.nombre:
                self.lista_productos.remove(lista_productos)
        return True

    def calcular_total(self):
        total = 0
        for sub_total in self.lista_productos:
            total = float(sub_total.calcular_subtotal()) + total
        self.total = total
        return total


"""class Cliente:

    def __init__(self, *args, **kwargs):
        self.id = ''
        self.nombre = ''
        self.direccion = ''

    def guardar(self):
        consulta = 'INSERT INTO Cliente VALUES (?, ?, ?)'
        parametros = [self.id, self.nombre, self.direccion]
        conexion_consulta(consulta, parametros)"""
