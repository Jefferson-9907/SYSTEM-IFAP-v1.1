import random
from datetime import datetime, date
from tkinter import *

from PIL import ImageTk
from ttkthemes import themed_tk as tk
from tkinter import messagebox

import Model_class.database_connected
import Model_class.users_registration
import Model_class.auditoria_u_registration
import Frontend.connect_database
import Frontend.database_connected
import Backend.connection

from Frontend.Admin.Principal_Window_A import Principal
from Frontend.Secretary.Principal_Window_S import Principal_S
from Frontend.Facturation.Principal_Window_F import Principal_F

"""
    from Frontend.Facturation.Principal_Window import Principal_S
"""


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
        self.user = StringVar()
        self.passw = StringVar()

        self.username_label = Label(self.Manage_Frame_login, text="USUARIO ", bg="#a27114", fg="Black",
                                    font=("Cooper Black", 12))
        self.username_label.place(x=140, y=75)

        self.username_entry = Entry(self.Manage_Frame_login, textvariable=self.user, highlightthickness=0, relief=FLAT,
                                    bg="#D3D3D3",
                                    fg="#4f4e4d", font=("Cooper Black", 12))
        self.username_entry.place(x=140, y=110, width=250)
        self.username_entry.focus()

        # ========================================================================
        # ===========================Contraseña===================================
        # ========================================================================

        self.password_label = Label(self.Manage_Frame_login, text="CONTRASEÑA ", bg="#a27114", fg="Black",
                                    font=("Cooper Black", 12))
        self.password_label.place(x=140, y=155)

        self.password_entry = Entry(self.Manage_Frame_login, textvariable=self.passw, highlightthickness=0,
                                    relief=FLAT, bg="#D3D3D3", fg="#4f4e4d", font=("Cooper Black", 12), show="*")
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
        username = self.username_entry.get()
        userpassword = self.password_entry.get()
        self.tipo1 = 'Administrador'
        self.tipo2 = 'Secretaría'
        self.tipo3 = 'Caja'
        tipo1 = self.tipo1
        tipo2 = self.tipo2
        tipo3 = self.tipo3

        """
            Valida si las entradas de nombre de usuario/contraseña existen en la base de datos o no, si
            existen y coinciden con el usuario contraseña, les permite iniciar sesión llamando a otro método,
            BaseException se maneja con el fin de evitar cualquier error en tiempo de ejecución
        """
        if self.username_entry.get() == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "POR FAVOR INGRESE SU USUARIO")
            self.username_entry.focus()

        elif self.password_entry.get() == "":
            messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA!!!)", "POR FAVOR INGRESE SU CONTRASEÑA")
            self.password_entry.focus()

        else:
            obj_login_users = Model_class.database_connected.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_login_users.get_database())

            query = "select * from usuarios where usuario=%s;"
            values = username
            data = self.db_connection.search(query, (values,))

            if data:
                query = "select * from usuarios where contrasena=%s;"
                values = userpassword
                data = self.db_connection.search(query, (values,))

                self.f_username = []
                self.f_password = []
                self.f_email = []
                for values in data:
                    current_list = values[2]
                    f_username_list = values[1]
                    f_password_list = values[3]
                    f_email_list = values[2]
                    self.f_email.append(f_email_list)
                    self.f_username.append(f_username_list)
                    self.f_password.append(f_password_list)
                    Login.current_user.clear()
                    Login.current_user.append(current_list)

                if data:
                    self.accion = "INGRESO (USUARIO ADMIN)"
                    query = "select * from usuarios where usuario=%s AND contrasena=%s AND tipo=%s;"
                    values = (username, userpassword, tipo1)
                    data = self.db_connection.search(query, values)

                    if data:
                        messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", f"REGISTRO DE INGRESO (USUARIO)\n"
                                                                             f"USUARIO: {self.username_entry.get()}\n"
                                                                             f"ACCIÓN: {self.accion}\n"
                                                                             f"FECHA: {self.fecha}\n"
                                                                             f"HORA: {self.hora}")
                        self.audi_users()
                        root = Toplevel()
                        Principal(root)
                        self.root.withdraw()
                        root.deiconify()

                    else:
                        self.accion = "INGRESO (USUARIO SECRETARÍA)"
                        query = "select * from usuarios where usuario=%s AND contrasena=%s AND tipo=%s;"
                        values = (username, userpassword, tipo2)
                        data = self.db_connection.search(query, values)

                        if data:
                            messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", f"REGISTRO DE INGRESO (USUARIO)\n"
                                                                                 f"USUARIO: {self.username_entry.get()}\n"
                                                                                 f"ACCIÓN: {self.accion}\n"
                                                                                 f"FECHA: {self.fecha}\n"
                                                                                 f"HORA: {self.hora}")
                            self.audi_users()
                            root = Toplevel()
                            Principal_S(root)
                            self.root.withdraw()
                            root.deiconify()

                        else:
                            self.accion = "INGRESO (USUARIO CAJA)"
                            query = "select * from usuarios where usuario=%s AND contrasena=%s AND tipo=%s;"
                            values = (username, userpassword, tipo3)
                            data = self.db_connection.search(query, values)

                            if data:
                                messagebox.showinfo("SYST_CONTROL(IFAP®)-->(ÉXITO)", f"REGISTRO DE INGRESO (USUARIO)\n"
                                                                                     f"USUARIO: {self.username_entry.get()}\n"
                                                                                     f"ACCIÓN: {self.accion}\n"
                                                                                     f"FECHA: {self.fecha}\n"
                                                                                     f"HORA: {self.hora}")
                                self.audi_users()
                                root = Toplevel()
                                Principal_F(root)
                                self.root.withdraw()
                                root.deiconify()
                else:
                    messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA)", f"CONTRASEÑA NO VÁLIDA")
                    self.passw.set("")
                    self.password_entry.focus()

            else:
                messagebox.showwarning("SYST_CONTROL(IFAP®)-->(ADVERTENCIA)", f"USUARIO NO VÁLIDO")
                self.user.set("")
                self.username_entry.focus()

    def audi_users(self):
        today = date.today()
        username = self.username_entry.get()
        accion = self.accion
        fecha = f"{today.year}/{today.month}/{today.day}"
        hour = datetime.now()
        hora = f"{hour.hour}:{hour.minute}:{hour.second}"

        try:
            obj_aud_user_database = Model_class.auditoria_u_registration.GetDatabase('use ddbb_sys_ifap;')
            self.db_connection.create(obj_aud_user_database.get_database())

            query = 'insert into auditoria_usuarios(usuario, accion, fecha, hora) values (%s, %s, %s, %s);'
            values = (username, accion, fecha, hora)

            self.db_connection.insert(query, values)

        except BaseException as msg:
            messagebox.showerror("SYST_CONTROL(IFAP®)-->(ERROR)", f"NO FUÉ POSIBLE CONECTARSE CON EL SERVIDOR,\n"
                                                                  f"REVISE LA CONEXIÓN: {msg}")

    def click_database(self):
        """"
            Cuando haga clic en el botón Cambiar base de datos, les pedirá que confirmen el cambio de dirección de host,
            y también les informará que esta confirmación eliminará las credenciales de host actuales, después de
            : devuelve True, luego se abre una nueva ventana guiándolos para configurar su host nuevamente
        """
        ques = messagebox.askyesno("ADVERTENCIA!!!", "¿ESTÁS SEGURO/A DE CAMBIAR DE HOST?")
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

    def login_success(self):
        """after successful login new admin dashboard will open by fetching the current logged in user"""
        root = Toplevel()
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
