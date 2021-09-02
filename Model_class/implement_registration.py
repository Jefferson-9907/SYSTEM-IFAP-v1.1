class ImplementRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del implemento y
        establecer todos los datos en la tabla de la base de datos backend llamada implementos
    """

    def __init__(self, descripcion, costo):
        self.__descripcion = descripcion
        self.__email = costo

    # ===========================set methods=======================

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_costo(self, costo):
        self.__costo = costo

    # =====================get methods========================

    def get_descripcion(self):
        return self.__descripcion

    def get_costo(self):
        return self.__costo


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
