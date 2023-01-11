#Librerias
from tkinter import *
from tkinter import messagebox
import cx_Oracle


# Cuando sea 1 → no hay conexion a base de datos
# Cuando sea 0 → Si hay conexion a base de datos


#Configuración de Ventana Principal
master=Tk()
x_ventana = master.winfo_screenwidth() // 2 - 1280 // 2
y_ventana = master.winfo_screenheight() // 2 - 720 // 2
posicion = str(1280) + "x" + str(600) + "+" + str(x_ventana) + "+" + str(y_ventana)
master.geometry(posicion)
master.resizable(1,1)
master.title("Conexiones BD Transaciones")
master.config(bg="#ECEEEF")


#Funciones


def ConexionBaseDatos():
    #user="ubdproducto",password="1234567",dsn="localhost/xe"
    user=StringVar.get(Dato_Nombre_Instancia)
    password=StringVar.get(Dato_Contrasena_Instancia)
    dsn=StringVar.get(Dato_Puerto_Instancia)
    try:
        conexiones= cx_Oracle.connect(user,password,dsn)
    except Exception as err:
        messagebox.showerror(message="Algún dato de la Conexion la introducido Incorrectamente", title="Error de Conexion")
        print("Error en la conexion a la base", err)
        return 1
    else:
        print("Conectado a Oracle Database ", conexiones.version)
        return conexiones
    



#Funciones
def ConsultaDatos():
    bandera = ConexionBaseDatos()
    if(bandera==1):
        print("Termino proceso por no conexion")  
    else:
        print("Siguiente paso")
        conexion= bandera.cursor()
        
        inserta_dato='''select SALDO from CUENTA'''
        conexion.execute(inserta_dato)
        datosAlmacenado = conexion.fetchall()
        contado=0
        for row in datosAlmacenado:
            if(contado==0):
                StringVar.set(Dato_Cuenta1,row)
            if(contado==1):
                StringVar.set(Dato_Cuenta2,row)
            contado= contado+1
        bandera.close()
        messagebox.showinfo(message="Se ha finalizado el proceso correctamente", title="Proceso")
    return 0


def TransferirTransaccional():
    bandera = ConexionBaseDatos()
    if(bandera==1):
        print("Termino proceso por no conexion")  
    else:
        print("Siguiente paso")
        conexion= bandera.cursor()
        cuentaorigen = StringVar.get(Dato_ID_Cuenta_Origen )
        cuentadestino =  StringVar.get(Dato_ID_Cuena_Destino)
        valortransferido =  StringVar.get(Dato_Valor_Transferir)
        conexion.callproc("PA_INSERTAR_TRANSACCIONAL", [cuentaorigen, cuentadestino, valortransferido])
        bandera.commit()
        bandera.close()
        messagebox.showinfo(message="Se ha finalizado el proceso correctamente", title="Proceso")
    return 0

def TransferirNoTransaccional():
    bandera = ConexionBaseDatos()
    if(bandera==1):
        print("Termino proceso por no conexion")  
    else:
        print("Siguiente paso")
        conexion= bandera.cursor()
        cuentaorigen = StringVar.get(Dato_ID_Cuenta_Origen )
        cuentadestino =  StringVar.get(Dato_ID_Cuena_Destino)
        valortransferido =  StringVar.get(Dato_Valor_Transferir)
        conexion.callproc("PA_INSERTAR_NO_TRANSACCIONAL", [cuentaorigen, cuentadestino, valortransferido])
        bandera.commit()
        bandera.close()
        messagebox.showinfo(message="Se ha finalizado el proceso correctamente", title="Proceso")
    return 0







#Contenido de la Interfaz
#Variables
Dato_Nombre_Instancia = StringVar()
Dato_Contrasena_Instancia = StringVar()
Dato_Puerto_Instancia = StringVar()
Dato_Cuenta1 = StringVar()
Dato_Cuenta2 = StringVar()
Dato_ID_Cuenta_Origen = StringVar()
Dato_ID_Cuena_Destino = StringVar()
Dato_Valor_Transferir = StringVar()

#Estilo de letra predeterminada


#Primera Linea
TituloNombreInstacia= Label(master, text="Nombre de Usuario de Oracle",fg="#31303E",font=('Times New Roman',18)).place(x=55 , y=20)
Entrada_Nombre_Instancia=Entry(master,textvariable=Dato_Nombre_Instancia,bg="#FFFFFF",width=38,font=('Times New Roman',18)).place(x=420 , y=20)
TituloValorSegun= Label(master, text="Valor según su instalación",fg="#218ADC",font=('Times New Roman',18)).place(x=900 , y=20)
#Intermedio
TituloContrasena= Label(master, text="Contraseña del Usuario de Oracle",font=('Times New Roman',18)).place(x=55 , y=60)
Entrada_Contrasena=Entry(master,textvariable=Dato_Contrasena_Instancia,bg="#FFFFFF",width=38,font=('Times New Roman',18)).place(x=420 , y=60)
TituloContrasena= Label(master, text="Valor según su instalación",fg="#218ADC",font=('Times New Roman',18)).place(x=900 , y=60)
#Segunda Linea
TituloPuertoInstancia= Label(master, text="Puerto de la instancia SQL SERVER",font=('Times New Roman',18)).place(x=55 , y=100)
Entrada_PuertoInstancia=Entry(master,textvariable=Dato_Puerto_Instancia,bg="#FFFFFF",width=38,font=('Times New Roman',18)).place(x=420 , y=100)
TituloPuertoTipico= Label(master, text="Valor según su instalación",fg="#218ADC",font=('Times New Roman',18)).place(x=900 , y=100)
#Tercera Linea
TituloTransaccion= Label(master, text="Transacción: Transferencia bancaria",font=('Times New Roman',18)).place(x=460 , y=150)
#Cuarto Linea
TituloCuenta1= Label(master, text="Cuenta 1[ID en Base de datos = 1]:",font=('Times New Roman',18)).place(x=55 , y=220)
Entrada_Cuenta1=Entry(master,textvariable=Dato_Cuenta1,bg="#FFFFFF",width=19,font=('Times New Roman',18)).place(x=420 , y=220)

#Button Intermedio
Calcular_Buton= Button(master,bg="MistyRose3", text="Consultar Saldo",height=2,width=15,font=('Times New Roman',18),command=lambda:ConsultaDatos()).place(x=800 , y=238)

#Quinto Linea
TituloCuenta2= Label(master, text="Cuenta 2[ID en Base de datos = 2]:",font=('Times New Roman',18)).place(x=55 , y=300)
Entrada_Cuenta2=Entry(master,textvariable=Dato_Cuenta2,bg="#FFFFFF",width=19,font=('Times New Roman',18)).place(x=420 , y=300)


#Sexto Linea
TituloIDorigen= Label(master, text="ID de la cuenta origen",font=('Times New Roman',18)).place(x=55 , y=400)
Entrada_IDorigen=Entry(master,textvariable=Dato_ID_Cuenta_Origen,bg="#FFFFFF",font=('Times New Roman',18)).place(x=280 , y=400)
TituloIDdestino= Label(master, text="ID de la cuenta destino",font=('Times New Roman',18)).place(x=600 , y=400)
Entrada_IDdestino=Entry(master,textvariable=Dato_ID_Cuena_Destino,bg="#FFFFFF",font=('Times New Roman',18)).place(x=835 , y=400)

#Septimo Linea
TituloValorTranferir= Label(master, text="Valor a transferir",font=('Times New Roman',18)).place(x=55 , y=450)
Entrada_ValorTranferir=Entry(master,textvariable=Dato_Valor_Transferir,bg="#FFFFFF",font=('Times New Roman',18)).place(x=280 , y=450)

#Octavo Linea
Calcular_Buton= Button(master,bg="MistyRose3", text="Transferir (Modo no transaccional)",font=('Times New Roman',18),command=lambda:TransferirNoTransaccional).place(x=275 , y=535)
Calcular_Buton= Button(master,bg="MistyRose3", text="Transferir (Modo transaccional)",font=('Times New Roman',18),command=lambda:TransferirTransaccional()).place(x=675 , y=535)

mainloop()


