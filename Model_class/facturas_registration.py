class FacturasRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del implemento y
        establecer todos los datos en la tabla de la base de datos backend llamada implementos
    """

    def __init__(self, id_factura, id_estudiante, fecha, hora):
        self.__id_factura = id_factura
        self.__id_estudiante = id_estudiante
        self.__fecha = fecha
        self.__hora = hora

    # ===========================set methods=======================

    def set_id_factura(self, id_factura):
        self.__id_factura = id_factura

    def set_id_estudiante(self, id_estudiante):
        self.__id_estudiante = id_estudiante

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_hora(self, hora):
        self.__hora = hora

    # =====================get methods========================

    def get_id_factura(self):
        return self.__id_factura

    def get_id_estudiante(self):
        return self.__id_estudiante

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
