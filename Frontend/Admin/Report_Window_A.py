# Import Modules
import random
from _datetime import datetime
from time import strftime
from tkinter import *
from tkinter import messagebox

import Frontend.Admin.Principal_Window_A
import Frontend.login_form
import Frontend.Admin.Student_Window_A
import Frontend.Admin.Course_Window_A
import Frontend.Admin.Matricula_Window_A
import Frontend.Admin.Assesor_Window_A
import Frontend.Admin.Paralelo_Window_A
import Frontend.Admin.Implements_Window_A
import Frontend.Admin.Facturation_Window_A
import Frontend.Admin.Password_Window_A
import Frontend.Admin.Users_Window_A

from Frontend.Admin.Report_al import generarReporte_al
from Frontend.Admin.Report_as import generarReporte_as
from Frontend.Admin.Report_cs import generarReporte_cs
from Frontend.Admin.Report_pa import generarReporte_pa
from Frontend.Admin.Report_a_us import generarReporte_us




class Reports:

    def __init__(self, root):
        self.root = root
        self.root.title("SYST_CONTROL--›REPORTES")
        self.root.attributes('-fullscreen', True)
        self.root.resizable(False, False)
        self.root.iconbitmap('recursos\\ICONO_SIST_CONTROL (IFAP®)2.0.ico')
        self.root.configure(bg='#a27114')

        imagenes = {
            'nuevo': PhotoImage(file='recursos\\icon_export.png'),
        }

        self.txt = "SYSTEM CONTROL IFAP (REPORTES)"
        self.count = 0
        self.text = ''
        self.color = ["#4f4e4d", "#f29844", "red2"]
        self.heading = Label(self.root, text=self.txt, font=("Cooper Black", 35), bg="#000000",
                             fg='black', bd=5, relief=FLAT)
        self.heading.place(x=0, y=0, width=1367)

        self.slider()
        self.heading_color()

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
        self.Column7.add_command(label='Usuarios', command=self.users_btn)
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

        self.footer_4 = Label(self.root, text='J.C.F DESING® | Derechos Reservados 2021', width=195, bg='black',
                              fg='white')
        self.footer_4.place(x=0, y=725)

        data = datetime.now()
        fomato_f = " %A %d/%B/%Y"

        self.footer = Label(self.root, text='  FECHA Y HORA: ', font=("Cooper Black", 9), bg='black',
                            fg='white')
        self.footer.place(x=930, y=725)
        self.footer_1 = Label(self.root, text=str(data.strftime(fomato_f)), font=("Lucida Console", 10), bg='black',
                              fg='white')
        self.footer_1.place(x=1040, y=727)

        self.clock = Label(self.root)
        self.clock['text'] = '00:00:00'
        self.clock['font'] = 'Tahoma 9 bold'
        self.clock['bg'] = 'black'
        self.clock['fg'] = 'white'
        self.clock.place(x=1275, y=725)
        self.tic()
        self.tac()

        self.Manage_Frame_report = Frame(self.root, relief=RIDGE, bd=4, bg='#a27114')
        self.Manage_Frame_report.place(x=15, y=75, width=1330, height=640)

        m_title_p = Label(self.Manage_Frame_report, text="-ADMINISTAR REPORTES-",
                          font=("Copperplate Gothic Bold", 16, "bold"), bg='#a27114', fg="White")
        m_title_p.grid(column=0, row=0, columnspan=2, padx=485, pady=10)

        # Button Frame
        self.btn_frame_report = Frame(self.Manage_Frame_report, bg='#a27114')
        self.btn_frame_report.place(x=25, y=75, width=1000)

        self.l_gen_report_s = Label(self.btn_frame_report, text='REPORTE GENERAL DE ESTUDIANTES', width='40',
                                    font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report_s.grid(row=0, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_s_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                       text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"),
                                       command=self.report_st)
        self.gen_report_s_btn.image = imagenes['nuevo']
        self.gen_report_s_btn.grid(row=0, column=1, padx=15, pady=10, sticky="W")

        self.l_gen_report_m = Label(self.btn_frame_report, text='REPORTE GENERAL DE MATRÍCULAS', width='40',
                                    font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report_m.grid(row=1, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_m_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                       text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"),
                                       command=self.report_mt)
        self.gen_report_m_btn.image = imagenes['nuevo']
        self.gen_report_m_btn.grid(row=1, column=1, padx=15, pady=10, sticky="W")

        self.l_gen_report_a = Label(self.btn_frame_report, text='REPORTE GENERAL DE ASESORES', width='40',
                                    font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report_a.grid(row=2, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_a_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                       text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"),
                                       command=self.report_as)
        self.gen_report_a_btn.image = imagenes['nuevo']
        self.gen_report_a_btn.grid(row=2, column=1, padx=15, pady=10, sticky="W")

        self.l_gen_report_c = Label(self.btn_frame_report, text='REPORTE GENERAL DE CURSOS   ', width='40',
                                    font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report_c.grid(row=3, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_c_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                       text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"),
                                       command=self.report_cs)
        self.gen_report_c_btn.image = imagenes['nuevo']
        self.gen_report_c_btn.grid(row=3, column=1, padx=15, pady=10, sticky="W")

        self.l_gen_report_p = Label(self.btn_frame_report, text='REPORTE GENERAL DE PARALELOS ', width='40',
                                    font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report_p.grid(row=4, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_p_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                       text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"),
                                       command=self.report_pa)
        self.gen_report_p_btn.image = imagenes['nuevo']
        self.gen_report_p_btn.grid(row=4, column=1, padx=15, pady=10, sticky="W")

        self.l_gen_report_p = Label(self.btn_frame_report, text='REPORTE GENERAL DE USUARIOS ', width='40',
                                   font=("Britannic", 11, "bold"), bg='#808080')
        self.l_gen_report_p.grid(row=5, column=0, padx=1, pady=5, sticky="W")

        self.gen_report_p_btn = Button(self.btn_frame_report, image=imagenes['nuevo'],
                                       text='Generar', width=80, compound="right", font=("Britannic", 11, "bold"),
                                       command=self.report_us)
        self.gen_report_p_btn.image = imagenes['nuevo']
        self.gen_report_p_btn.grid(row=5, column=1, padx=15, pady=10, sticky="W")

    def tic(self):
        self.clock["text"] = strftime("%H:%M:%S %p")

    def tac(self):
        self.tic()
        self.clock.after(1000, self.tac)

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

    def report_st(self):
        generarReporte_al()

    def report_mt(self):
        pass

    def report_as(self):
        generarReporte_as()

    def report_cs(self):
        generarReporte_cs()

    def report_pa(self):
        generarReporte_pa()

    def report_us(self):
        generarReporte_us()

    def heading_color(self):
        """
            configures heading label
            :return: every 50 ms returned new random color.
        """
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def logout(self):
        root = Toplevel()
        Frontend.login_form.Login(root)
        self.root.withdraw()
        root.deiconify()

    def principal_btn(self):
        root = Toplevel()
        Frontend.Admin.Principal_Window_A.Principal(root)
        self.root.withdraw()
        root.deiconify()

    def student_btn(self):
        root = Toplevel()
        Frontend.Admin.Student_Window_A.Student(root)
        self.root.withdraw()
        root.deiconify()

    def matricula_btn(self):
        root = Toplevel()
        Frontend.Admin.Matricula_Window_A.Matricula(root)
        self.root.withdraw()
        root.deiconify()

    def assesor_btn(self):
        root = Toplevel()
        Frontend.Admin.Assesor_Window_A.Assesor(root)
        self.root.withdraw()
        root.deiconify()

    def courses_btn(self):
        root = Toplevel()
        Frontend.Admin.Course_Window_A.Course(root)
        self.root.withdraw()
        root.deiconify()

    def paralelos_btn(self):
        root = Toplevel()
        Frontend.Admin.Paralelo_Window_A.Paralelo(root)
        self.root.withdraw()
        root.deiconify()

    def implements_btn(self):
        root = Toplevel()
        Frontend.Admin.Implements_Window_A.Implement(root)
        self.root.withdraw()
        root.deiconify()

    def facturation_btn(self):
        root = Toplevel()
        Frontend.Admin.Facturation_Window_A.Ventana_Principal(root)
        self.root.withdraw()
        root.deiconify()

    def report_btn(self):
        root = Toplevel()
        Frontend.Admin.Report_Window_A.Reports(root)
        self.root.withdraw()
        root.deiconify()

    def pass_btn(self):
        root = Toplevel()
        Frontend.Admin.Password_Window_A.Password(root)
        self.root.withdraw()
        root.deiconify()

    def users_btn(self):
        root = Toplevel()
        Frontend.Admin.Users_Window_A.Users(root)
        self.root.withdraw()
        root.deiconify()

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
