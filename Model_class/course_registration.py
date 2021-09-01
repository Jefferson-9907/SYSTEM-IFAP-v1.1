class CourseRegistration:
    """
        Esta clase es una clase modelo para obtener valores del formulario de registro del curso y
        establecer todos los datos en la tabla de la base de datos backend llamada Course_Window
    """

    def __init__(self, id_curso, nombre_cur, costo_matricula, costo_mensual):
        self.__id_curso = id_curso
        self.__nombre_cur = nombre_cur
        self.__costo_matricula = costo_matricula
        self.__costo_mensual = costo_mensual

    # ===========================set methods=======================
    def set_id_curso(self, id_curso):
        self.__id_curso = id_curso

    def set_nombre_cur(self, nombre_cur):
        self.__nombre_cur = nombre_cur

    def set_costo_matricula(self, costo_matricula):
        self.__costo_matricula = costo_matricula

    def set_costo_mensual(self, costo_mensual):
        self.__costo_mensual = costo_mensual

    # =====================get methods========================
    def get_id_curso(self):
        return self.__id_curso

    def get_nombre_cur(self):
        return self.__nombre_cur

    def get_costo_matricula(self):
        return self.__costo_matricula

    def get_costo_mensual(self):
        return self.__costo_mensual


class GetDatabase:
    def __init__(self, database):
        self.__database = database

    def get_database(self):
        return self.__database
