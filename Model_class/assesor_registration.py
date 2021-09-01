class AssesorsRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del estudiante y
        establecer todos los datos en la tabla de la base de datos backend llamada estudiantes
    """

    def __init__(self, cedula_as, nombres_as, apellidos_as, direccion_as, correo_as, celular_as):
        self.__cedula_as = cedula_as
        self.__nombres_as = nombres_as
        self.__apellidos_as = apellidos_as
        self.__direccion_as = direccion_as
        self.__correo_as = correo_as
        self.__celular_as = celular_as

    # ===========================set methods=======================

    def set_cedula_as(self, cedula_as):
        self.__cedula_as = cedula_as

    def set_nombres_as(self, nombres_as):
        self.__nombres_as = nombres_as

    def set_apellidos_as(self, apellidos_as):
        self.__apellidos_as = apellidos_as

    def set_direccion_as(self, direccion_as):
        self.__direccion_as = direccion_as

    def set_correo_as(self, correo_as):
        self.__correo_as = correo_as

    def set_celular_as(self, celular_as):
        self.__celular_as = celular_as

    # =====================get methods========================

    def get_cedula_as(self):
        return self.__cedula_as

    def get_nombres_as(self):
        return self.__nombres_as

    def get_apellidos_as(self):
        return self.__apellidos_as

    def get_direccion_as(self):
        return self.__direccion_as

    def get_correo_as(self):
        return self.__correo_as

    def get_celular_as(self):
        return self.__celular_as

class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database

