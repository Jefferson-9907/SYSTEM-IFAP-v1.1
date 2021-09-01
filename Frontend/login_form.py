import random
from datetime import datetime
from tkinter import *
from PIL import ImageTk
from ttkthemes import themed_tk as tk
from tkinter import messagebox

from Backend.conexion import conn
import Frontend.connect_database
import Frontend.database_connected
import Backend.connection

from Principal_Window_A import Principal


class Login:
    """
        Permite al usuario iniciar sesión en el sistema proporcionándoles una interfaz de usuario, verifica el nombre
        de usuario correo electrónico y la contraseña de la tabla no verificada y de administración de la base de datos,
        si el usuario existe, verifique la contraseña y permita que inicien sesión si coincidió, de lo contrario,
        mensaje de error emergente.
    """
    current_user = []
    id_user = []

    def __init__(self, root):
        """
            Ventana para mostrar todos los atributos y métodos para esta clase
        """
        self.root = root
        self.root.geometry("530x350")
        self.root.title("SYST_CONTROL(IFAP®) (INICIAR SESIÓN)")
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.resizable(False, False)

        imagenes = {
            'login': PhotoImage(file='recursos\\icon_login.png'),
            'change': PhotoImage(file='recursos\\icon_upd.png'),
        }

        self.db_connection = Backend.connection.DatabaseConnection()

        self.Manage_Frame_login = Frame(self.root, bd=4, bg='#a27114')
        self.Manage_Frame_login.place(x=0, y=0, width=530, height=350)

        self.login_frame = ImageTk.PhotoImage(file='recursos\\login_frame.png')
        self.image_panel = Label(self.Manage_Frame_login, image=self.login_frame, bg='#a27114')
        self.image_panel.place(x=100, y=100)

        self.txt = "INICIO DE SESIÓN"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=550)
        self.slider()
        self.heading_color()

        # ========================================================================
        # ============================Usuario=====================================
        # ========================================================================

        self.username_label = Label(self.Manage_Frame_login, text="USUARIO ", bg="#a27114", fg="Black",
                                    font=("Cooper Black", 12))
        self.username_label.place(x=140, y=75)

        self.username_entry = Entry(self.Manage_Frame_login, highlightthickness=0, relief=FLAT, bg="#D3D3D3",
                                    fg="#4f4e4d", font=("Cooper Black", 12))
        self.username_entry.place(x=140, y=110, width=250)  # trebuchet ms

        # ========================================================================
        # ===========================Contraseña===================================
        # ========================================================================

        self.password_label = Label(self.Manage_Frame_login, text="CONTRASEÑA ", bg="#a27114", fg="Black",
                                    font=("Cooper Black", 12))
        self.password_label.place(x=140, y=155)

        self.password_entry = Entry(self.Manage_Frame_login, highlightthickness=0, relief=FLAT, bg="#D3D3D3",
                                    fg="#4f4e4d", font=("Cooper Black", 12), show="*")
        self.password_entry.place(x=140, y=191, width=250)

        self.show_image = ImageTk.PhotoImage(file='recursos\\show.png')
        self.hide_image = ImageTk.PhotoImage(file='recursos\\hide.png')

        self.show_button = Button(self.Manage_Frame_login, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=400, y=192)

        # ========================================================================
        # ==========================Botón de Ingreso==============================
        # ========================================================================

        self.login_button = Button(self.root, image=imagenes['login'], text=' INGRESAR ', bg="#003366", fg='White',
                                   font=("Cooper Black", 12), command=self.validation, compound="left")
        self.login_button.image = imagenes['login']
        self.login_button.place(x=220, y=230, width=130)

        # ========================================================================
        # ===================Etiqueta y botón de la base de datos=================
        # ========================================================================

        self.database_label = Label(self.Manage_Frame_login, text="* PUEDES CAMBIAR EL SERVIDOR AQUÍ", bg="#a27114",
                                    fg="#4f4e4d", font=("Cooper Black", 9, "underline"))
        self.database_label.place(x=25, y=275)

        self.submit_button = Button(self.root, image=imagenes['change'], text=' CAMBIAR SERVIDOR ',
                                    font=("Cooper Black", 12), command=self.click_database, compound="left")
        self.submit_button.image = imagenes['change']
        self.submit_button.place(x=290, y=275)

        self.data = datetime.now()
        self.fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.formato_d = " %A %d/%B/%Y"
        self.fecha = str(self.data.strftime(self.formato_d))
        self.formato_h = "%H:%M:%S %p "
        self.hora = str(self.data.strftime(self.formato_h))
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10),
                            bg='black', fg='white', relief=RIDGE)
        self.footer.place(x=0, y=310)
        self.footer_1 = Label(self.Manage_Frame_login, text=str(self.data.strftime(self.fomato_f)),
                              font=("Cooper Black", 10), bg='Honeydew2', relief=RIDGE, width=35)
        self.footer_1.place(x=205, y=305)

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=75,
                              bg='black', fg='white')
        self.footer_4.place(x=0, y=330)

    def show(self):
        """
            Permitir al usuario mostrar la contraseña en el campo de contraseña
        """
        self.hide_button = Button(self.Manage_Frame_login, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=400, y=192)
        self.password_entry.config(show='')

    def hide(self):
        """
            Permitir al usuario ocultar la contraseña en el campo de contraseña
        """
        self.show_button = Button(self.Manage_Frame_login, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=400, y=192)
        self.password_entry.config(show='*')

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

    def validation(self):
        try:
            """
                Valida si las entradas de nombre de usuario/contraseña existen en la base de datos o no, si
                existen y coinciden con el usuario contraseña, les permite iniciar sesión llamando a otro método,
                BaseException se maneja con el fin de evitar cualquier error en tiempo de ejecución
            """
            if self.username_entry.get() == "":
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE SU USUARIO")

            elif self.password_entry.get() == "":
                messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", "POR FAVOR INGRESE SU CONTRASEÑA")

            else:
                with conn.cursor() as cursor:
                    self.tipo = 'Administrador'
                    self.accion = "INGRESO (USUARIO ADMIN)"

                    self.query = "SELECT usuario, contrasena, tipo FROM usuarios WHERE usuario=? AND contrasena=?;"
                    cursor.execute(self.query, (self.username_entry.get(), self.password_entry.get()))
                    resultado = cursor.fetchall()

                    if resultado:
                        self.query = "SELECT usuario, contrasena, tipo FROM usuarios WHERE usuario=? " \
                                     "AND contrasena=? AND tipo=?;"
                        cursor.execute(self.query, (self.username_entry.get(), self.password_entry.get(), self.tipo))
                        resultado = cursor.fetchall()

                        if resultado:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"REGISTRO DE INGRESO (USUARIO)\n"
                                                                       f"USUARIO: {self.username_entry.get()}\n"
                                                                       f"ACCIÓN: {self.accion}\n"
                                                                       f"FECHA: {self.fecha}\n"
                                                                       f"HORA: {self.hora}")
                            root = Toplevel()
                            Principal(root)
                            self.root.withdraw()
                            root.deiconify()
                        else:
                            self.tipo = 'Secretaría'
                            self.accion = "INGRESO (USUARIO SECRETARÍA)"

                            self.query = "SELECT usuario, contrasena, tipo FROM usuarios WHERE usuario=? AND " \
                                         "contrasena=? AND tipo=?;"
                            cursor.execute(self.query,
                                           (self.username_entry.get(), self.password_entry.get(), self.tipo))
                            resultado = cursor.fetchall()

                            if resultado:
                                messagebox.showinfo("SYST_CONTROL(IFAP®)", f"REGISTRO DE INGRESO (USUARIO)\n"
                                                                           f"USUARIO: {self.username_entry.get()}\n"
                                                                           f"ACCIÓN: {self.accion}\n"
                                                                           f"FECHA: {self.fecha}\n"
                                                                           f"HORA: {self.hora}")
                            else:
                                self.tipo = 'Caja'
                                self.accion = "INGRESO (USUARIO CAJA)"

                                self.query = "SELECT usuario, contrasena, tipo FROM usuarios WHERE usuario=? AND " \
                                             "contrasena=? AND tipo=?;"
                                cursor.execute(self.query,
                                               (self.username_entry.get(), self.password_entry.get(), self.tipo))
                                resultado = cursor.fetchall()

                                if resultado:
                                    messagebox.showinfo("SYST_CONTROL(IFAP®)", f"REGISTRO DE INGRESO (USUARIO)\n"
                                                                               f"USUARIO: {self.username_entry.get()}\n"
                                                                               f"ACCIÓN: {self.accion}\n"
                                                                               f"FECHA: {self.fecha}\n"
                                                                               f"HORA: {self.hora}")

                                else:
                                    messagebox.showwarning("SYST_CONTROL(IFAP®)-->ERROR", "CREDENCIALES INCORRECTAS,\n"
                                                                                          "INTÉNTELO NUEVAMENTE")
                                    self.username_entry.delete(0, END)
                                    self.password_entry.delete(0, END)
                                    self.username_entry.focus()
                    else:
                        messagebox.showerror("SYST_CONTROL(IFAP®)-->ERROR", f"EL USUARIO: {self.username_entry.get()} "
                                                                            "NO EXISTE\nINTÉNTELO NUEVAMENTE")
                        self.username_entry.delete(0, END)
                        self.password_entry.delete(0, END)
                        self.username_entry.focus()

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    """def audi_users(self):
        try:
            obj_aud_user_database = Model_class.auditoria_u_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_aud_user_database.get_database())

            query = 'insert into auditoria_usuarios values (?, ?, ?, ?);'
            values = (self.username_entry.get(), self.accion, self.fecha, self.hora)

            self.db_connection.insert(query, values)
            messagebox.showinfo("SYST_CONTROL(IFAP®)", f"REGISTRO (USUARIOS)\n"
                                                       f"USUARIO: {self.username_entry.get()}\n"
                                                       f"ACCIÓN: {self.accion}\n"
                                                       f"FECHA: {self.fecha}\n"
                                                       f"HORA: {self.hora}")

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")"""

    def click_database(self):
        """"
            Cuando haga clic en el botón Cambiar base de datos, les pedirá que confirmen el cambio de dirección de host,
            y también les informará que esta confirmación eliminará las credenciales de host actuales, después de
            : devuelve True, luego se abre una nueva ventana guiándolos para configurar su host nuevamente
        """
        ques = messagebox.askyesno("ADVERTENCIA!!!", "ESTÁS SEGURO/A DE CAMBIAR DE HOST")
        if ques is True:
            ask = messagebox.askyesno("CONFIRMAR", "LA CONEXIÓN DEL HOST ANTERIOR SE ELIMINARÁ,\n "
                                                   "¿DESEAS CONTINUAR?")
            if ask is True:
                f = open("database_data.txt", "wb")
                f.truncate(0)
                messagebox.showinfo("ÉXITO!!!", "SE HA ELIMINADO EL HOST CORRECTAMENTE.")

                root = Toplevel()
                Frontend.connect_database.ConnectDatabase(root)
                self.root.withdraw()
                root.deiconify()


def win():
    root = tk.ThemedTk()
    root.get_themes()
    root.set_theme("arc")
    Login(root)
    root.mainloop()


if __name__ == '__main__':
    win()
