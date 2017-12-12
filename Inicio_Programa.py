import gi

import Empresa_Transportes

import sqlite3 as dbapi


print (dbapi.apilevel)
print (dbapi.threadsafety)
print (dbapi.paramstyle)

gi.require_version('Gtk','3.0')

from gi.repository import Gtk

class ventanaPrincipalPrograma (Gtk.Window): #crea una ventana

    def clickear(self, boton):
        try:
            bbdd = dbapi.connect("envios.db")
            print("Conectado con Exito")
            self.botonInPrograma.set_sensitive(True) #activa el boton
        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error (OperationalError): ")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def cambioVent(self, boton):
        Empresa_Transportes.ventanaPrograma()
        self.destroy()

    def bSalir(self, boton): #sale del programa y cierra la base de datos
        try:
            bbdd = dbapi.connect("envios.db")
            print("Cerrando Base de Datos...")
            bbdd.close()
            print("Saliendo del programa...")
            Gtk.main_quit()
            print("Cerrado con Exito")
        except:
            print("Error en el Cierre")

    def __init__(self):

        # crear la ventana principal
        Gtk.Window.__init__(self, title="Iniciando Transportes Python - Nº 6122")
        self.set_border_width(10)
        self.set_default_size(450, 250)

        # crear la caja principal, la base de la ventana
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaPrincipal)

        # titulo para el programa dentro de la ventana
        lbtitulo = Gtk.Label(xalign=0)  # para la posicion
        lbtitulo.set_markup("<b>Transportes Python S.L.</b>")
        cajaPrincipal.add(lbtitulo)


# PARTE DE LA VENTANA:

        #agregar el frame
        finicioPrograma = Gtk.Frame(label="Iniciar el Servicio de Transportes Python")
        #para agregar una caja vertical 1 dentro del frame para tener posicionado
        cajaInvisibleVert1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        finicioPrograma.add(cajaInvisibleVert1)


        #añadir contenidos
        lbliniciarBase = Gtk.Label("Paso 1 - Iniciar la Base de Datos:", xalign=0)
        cajaInvisibleVert1.add(lbliniciarBase)
        botonInBase = Gtk.Button("INCIAR BASE")
        botonInBase.connect("clicked", self.clickear)
        cajaInvisibleVert1.add(botonInBase)

        lblProgramaPrin = Gtk.Label("Paso 2 - Abrir el Programa Principal", xalign=0)
        cajaInvisibleVert1.add(lblProgramaPrin)
        self.botonInPrograma = Gtk.Button("INICIAR PROGRAMA")
        self.botonInPrograma.set_sensitive(False) #inicia con el boton desactivado
        self.botonInPrograma.connect("clicked", self.cambioVent)

        cajaInvisibleVert1.add(self.botonInPrograma)

        lblsalir = Gtk.Label("SALIR DEL PROGRAMA", xalign=0)
        cajaInvisibleVert1.add(lblsalir)
        botonsalir = Gtk.Button("SALIR")
        botonsalir.connect("clicked", self.bSalir)
        cajaInvisibleVert1.add(botonsalir)




        cajaPrincipal.add(finicioPrograma)  # agrega la primera parte a la ventana principal


        #self.connect("delete-event", Gtk.main_quit)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
                                #para que se muestre la ventana




if __name__ == "__main__":
    ventana = ventanaPrincipalPrograma()
    Gtk.main()