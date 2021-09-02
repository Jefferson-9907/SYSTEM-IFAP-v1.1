class DetalleFacturasRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del implemento y
        establecer todos los datos en la tabla de la base de datos backend llamada implementos
    """

    def __init__(self, id_detalle_factura, id_factura, id_implemento, cantidad, total_factura):
        self.__id_factura = id_detalle_factura
        self.__id_estudiante = id_factura
        self.__fecha = id_implemento
        self.__hora = cantidad
        self.__fecha = total_factura

    # ===========================set methods=======================

    def set_id_detalle_factura(self, id_detalle_factura):
        self.__id_detalle_factura = id_detalle_factura

    def set_id_factura(self, id_factura):
        self.__id_factura = id_factura

    def set_id_implemento(self, id_implemento):
        self.__id_implemento = id_implemento

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_total_factura(self, total_factura):
        self.__total_factura = total_factura

    # =====================get methods========================

    def get_id_detalle_factura(self):
        return self.__id_detalle_factura

    def get_id_factura(self):
        return self.__id_factura

    def get_id_implemento(self):
        return self.__id_implemento

    def get_cantidad(self):
        return self.__cantidad

    def get_total_factura(self):
        return self.__total_factura


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
