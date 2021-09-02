# Import Modules
from _datetime import datetime
from tkinter import *
from tkinter import messagebox, ttk


class Reports:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›REPORTES")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('./recursos/ICONO_SIST_CONTROL (IFAP®)2.0.ico')

        imagenes = {
            'nuevo': PhotoImage(file='./recursos/icon_export.png'),
        }

        self.barra1 = Label(self.root)
        self.barra1.config(bg='black', padx=681, pady=20)
        self.barra1.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.barra2 = Label(self.root)
        self.barra2.config(bg="#a27114", padx=681, pady=10)
        self.barra2.grid(row=0, column=0, sticky='w', padx=0, pady=0)
        self.texto1 = Label(self.root, text='SYSTEM CONTROL (REPORTES)')
        self.texto1.config(font=("Britannic", 20, "bold"), fg='black', bg="#a27114")
        self.texto1.grid(row=0, column=0, sticky='w', padx=455, pady=0)

        # =============================================================
        # CREACIÓN DE LA BARRA DE MENÚ
        # =============================================================
        self.menubarra = Menu(self.root)

        # =============================================================
        # CREACIÓN DEL MENÚ
        # =============================================================
        self.menubarra.add_cascade(label='ALUMNOS')
        self.root.config(menu=self.menubarra)
        self.menus = Menu(self.root)
        self.Column1 = Menu(self.menus, tearoff=0)
        self.cuaderno = ttk.Notebook(self.root, width=1340, height=625)
        self.cuaderno.grid(row=1, column=0, sticky='nw', padx=10, pady=5)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ PRINCIPAL
        # =============================================================
        self.menus.add_cascade(label='INICIO', menu=self.Column1)
        self.Column1.add_command(label='Menú Inicio', command=self.principal_btn)
        self.Column2 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # AÑADIENDO OPCIONES AL MENÚ ALUMNO
        # =============================================================
        self.menus.add_cascade(label='ALUMNOS', menu=self.Column2)
        self.Column2.add_command(label='Menú Alumnos', command=self.student_btn)
        self.Column2.add_command(label='Matriculación', command=self.matricula_btn)
        self.Column3 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL MENÚ ASESORES
        # =============================================================
        self.menus.add_cascade(label='ASESORES', menu=self.Column3)
        self.Column3.add_command(label='Menú Asesores', command=self.assesor_btn)
        self.Column4 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ CURSOS
        # =============================================================
        self.menus.add_cascade(label='CURSOS', menu=self.Column4)
        self.Column4.add_command(label='Menú Cursos', command=self.courses_btn)
        self.Column5 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ FACTURACIÓN
        # =============================================================
        self.menus.add_cascade(label='FACTURACIÓN', menu=self.Column5)
        self.Column5.add_command(label='Menú Facturación', command=self.facturation_btn)
        self.Column6 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ REPORTES
        # =============================================================
        self.menus.add_cascade(label='REPORTES', menu=self.Column6)
        self.Column7 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ AYUDA
        # =============================================================
        self.menus.add_cascade(label='USUARIOS', menu=self.Column7)
        self.Column7.add_command(label='Cambiar Usuario', command=self.logout)
        self.Column7.add_command(label='Cambiar Contraseña', command=self.pass_btn)
        self.Column7.add_separator()
        self.Column7.add_command(label='Cerrar Sesión', command=self.salir_principal)
        self.Column7.add_separator()
        self.Column8 = Menu(self.menus, tearoff=0)
        self.root.config(menu=self.menus)

        # =============================================================
        # CREACIÓN DEL DE MENÚ INFO
        # =============================================================
        self.menus.add_cascade(label='INFO', menu=self.Column8)
        self.Column8.add_command(label='Sobre IFAP®', command=self.caja_info_ifap)
        self.Column8.add_separator()
        self.Column8.add_command(label='Sobre SIST_CONTROL (IFAP®)', command=self.caja_info_sist)
        self.Column8.add_separator()
        self.root.config(menu=self.menus)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y   %H:%M:%S %p "
        self.footer = Label(self.root, text='  FECHA Y HORA DE INGRESO: ', font=("Cooper Black", 10), bg='Honeydew2',
                            relief=RIDGE)
        self.footer.place(x=0, y=703)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='Honeydew2',
                              relief=RIDGE)
        self.footer_1.place(x=212, y=704)
        self.footer_4 = Label(self.root, text='DESING® | Derechos Reservados 2021', width=195, bg='black', fg='white')
        self.footer_4.place(x=0, y=725)

        self.Manage_Frame_report = Frame(self.root, relief=RIDGE, bd=4, bg='#0d1e24')
        self.Manage_Frame_report.place(x=25, y=75, width=1310, height=605)

        m_title_p = Label(self.Manage_Frame_report, text="-ADMINISTAR REPORTES-",
                          font=("Copperplate Gothic Bold", 16, "bold"), bg='#0d1e24', fg="White")
        m_title_p.grid(column=0, row=0, columnspan=2, padx=485, pady=10)

        # Button Frame
        self.btn_frame_report = Frame(self.Manage_Frame_report, bg='#0d1e24')
        self.btn_frame_report.place(x=25, y=75, width=450)

        self.l_gen_report = Label(self.btn_frame_report, text='REPORTE GENERAL DE ESTUDIANTES', width='40',
                                  font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report.grid(row=0, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                     text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"))
        self.gen_report_btn.image = imagenes['nuevo']
        self.gen_report_btn.grid(row=0, column=1, padx=15, pady=10, sticky="E")

        self.gen_report_btn1 = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                      text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"))
        self.gen_report_btn1.image = imagenes['nuevo']
        self.gen_report_btn1.grid(row=1, column=0, padx=15, pady=10, sticky="W")

    def logout(self):
        self.root.destroy()

        from Frontend.login_form import Login
        st_root = Tk()
        Login(st_root)
        st_root.mainloop()

    def principal_btn(self):
        self.root.destroy()

        from Frontend.Principal_Window_A import Principal
        st_root = Tk()
        Principal(st_root)
        st_root.mainloop()

    def student_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Student_Window_A import Student
        st_root = Tk()
        Student(st_root)
        st_root.mainloop()

    def matricula_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Matricula_Window_A import Matricula
        st_root = Tk()
        Matricula(st_root)
        st_root.mainloop()

    def assesor_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Assesor_Window_A import Assesor
        st_root = Tk()
        Assesor(st_root)
        st_root.mainloop()

    def courses_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Course_Window_A import Course
        st_root = Tk()
        Course(st_root)
        st_root.mainloop()

    def facturation_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Facturation_Window_A import Ventana_Principal
        st_root = Tk()
        Ventana_Principal(st_root)
        st_root.mainloop()

    def pass_btn(self):
        self.root.destroy()

        from Frontend.Administrador.Password_Window_A import Password
        st_root = Tk()
        Password(st_root)
        st_root.mainloop()

    def salir_principal(self):
        self.sa = messagebox.askyesno('CERRAR SESIÓN', 'CERRAR SYST_CONTROL(IFAP®)')
        if self.sa:
            exit()

    # =============================================================
    # FUNCIÓN CAJA DE INFORMACIÓN DEL INSTITUTO(INFO)
    # =============================================================
    def caja_info_ifap(self):
        self.men1 = messagebox.showinfo('SIST_CONTROL (IFAP®)', 'INSTITUTO DE FORMACIÓN ACADEMICA PROEZAS(IFAP®)')

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
                                        'total o parcial.\n\n\n© 2021 BJM DESING®. Todos los derechos reservados')


if __name__ == '__main__':
    root = Tk()
    application = Reports(root)
    root.mainloop()
