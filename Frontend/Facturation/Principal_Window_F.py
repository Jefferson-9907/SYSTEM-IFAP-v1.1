# Import Modules
from _datetime import datetime
from tkinter import *
from tkinter import messagebox


class Principal_F:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›Principal")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('../recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)

        self.txt = "SYSTEM CONTROL (INICIO)"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=450)

        """self.texto1 = Label(self.root, text='SYSTEM CONTROL (INICIO)')
        self.texto1.config(font=("Britannic", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=455, pady=0)"""

        # =============================================================
        # CREACIÓN DE LA BARRA DE MENÚ
        # =============================================================
        self.menubarra = Menu(self.root)

        # =============================================================
        # CREACIÓN DEL MENÚ ALUMNO
        # =============================================================
        self.menubarra.add_cascade(label='ALUMNOS')
        self.root.config(menu=self.menubarra)
        self.menus = Menu(self.root)
        self.Column1 = Menu(self.menus, tearoff=0)

        # =============================================================
        # CREACIÓN DEL DE MENÚ FACTURACIÓN
        # =============================================================
        self.menus.add_cascade(label='FACTURACIÓN', menu=self.Column1)
        self.Column1.add_command(label='Menú Facturación', command=self.facturation_btn)
        self.Column2 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column2)
        self.Column2.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column2.add_command(label='Cambiar Contraseña', command=self.pass_btn)
        self.Column2.add_separator()
        self.Column2.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column2.add_separator()
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column3)
        self.Column3.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column3.add_separator()
        self.root.config(menu=self.menus)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10), bg='Honeydew2',
                            relief=RIDGE)
        self.footer.place(x=0, y=703)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10),
                              bg='Honeydew2',
                              relief=RIDGE)
        self.footer_1.place(x=212, y=704)

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=195, bg='black',
                              fg='white')
        self.footer_4.place(x=0, y=725)

    def logout(self):
        self.root.destroy()

        from Frontend.login_form import Login
        st_root = Tk()
        Login(st_root)
        st_root.mainloop()

    def facturation_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Facturation_Window_A import Ventana_Principal
        st_root = Tk()
        Ventana_Principal(st_root)
        st_root.mainloop()

    def pass_btn(self):
        self.root.destroy()

        from Frontend.Facturacion.Password_Window_F import Password_F
        st_root = Tk()
        Password_F(st_root)
        st_root.mainloop()

    def salir_principal(self):
        self.sa = messagebox.askyesno('CERRAR SESIÓN', 'CERRAR SYST_CONTROL(IFAP®)')
        if self.sa:
            exit()

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL SISTEMA(INFO)
    # =============================================================
    def caja_info_sist(self):
        self.men2 = messagebox.showinfo('SIST_CONTROL (IFAP®)',
                                        'SIST_CONTROL (IFAP®) v2.0\n'
                                        'El uso de este software queda sujeto a los términos y condiciones del '
                                        'contrato "BJM DESING®-CLIENTE".    \n'
                                        'El uso de este software queda sujeto a su contrato. No podrá utilizar '
                                        'este software para fines de distribución\n'
                                        'total o parcial.\n\n\n© 2021 J.C.F DESING®. Todos los derechos reservados')


if __name__ == '__main__':
    root = Tk()
    application = Principal_F(root)
    root.mainloop()
