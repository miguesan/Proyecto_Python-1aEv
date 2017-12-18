import gi

import sqlite3 as dbapi

import random
import Ventana_Furgon
from Inicio_Programa import ventanaPrincipalPrograma

print (dbapi.apilevel)
print (dbapi.threadsafety)
print (dbapi.paramstyle)

gi.require_version('Gtk','3.0')

from gi.repository import Gtk


class ventanaPrograma (Gtk.Window): #crea una ventana

    def cambioVentFurgon(self, boton):
        Ventana_Furgon.ventanaFurgon()
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

    def comprobarCheck1(self, boton):
        self.CheckButton1.set_sensitive(True)
        self.CheckButton2.set_sensitive(False)
        self.txtpagarcontrarrembolso.set_sensitive(False)

    def comprobarCheck2(self, boton):
        self.CheckButton1.set_sensitive(False)
        self.CheckButton2.set_sensitive(True)
        self.txtpagarcontrarrembolso.set_sensitive(True)

    def bLimpiarEnvio(self,boton): #vacia los campos del envio
        try:
            print("Vaciando campos del Envio...")
            self.txtNombreenvio.set_text("")
            self.txtdirecciondestino.set_text("")
            self.txtestado.set_text("")
            self.txtpoblacion.set_text("")
            str(self.txtcp.set_text(""))
            str(self.txttelf.set_text(""))
            str(self.txtmovil.set_text(""))
            print("...............")
            print("Limpado el Envio con Exito")
        except:
            print("Error en el Vaciado del Envio")

    def bLimpiarRemitente(self,boton): #vacia los campos del remitente
        try:
            print("Vaciando campos del Remitente...")
            self.txtNombreremitente.set_text("")
            self.txtdireccionremitente.set_text("")
            self.txtestadoremitente.set_text("")
            self.txtpoblacionremitente.set_text("")
            str(self.txtcpremitente.set_text(""))
            str(self.txttelfremitente.set_text(""))
            print("...............")
            print("Limpado el Remitente con Exito")
        except:
            print("Error en el Vaciado del Remitente")

    def bComprobarEnvio(self,boton):
        try:
            bbdd = dbapi.connect("envios.db")
            print("Conmprobando Datos de Envio ...")

            cursorEnvio = bbdd.cursor()

            cursorEnvio.execute("SELECT * FROM envios")
            for rexistro in cursorEnvio.fetchmany(2):
                self.txtNombreenvio.set_text(rexistro[1])
                self.txtdirecciondestino.set_text(rexistro[2])
                self.txtestado.set_text(rexistro[3])
                self.txtpoblacion.set_text(rexistro[4])
                str(self.txtcp.set_text(rexistro[5]))
                str(self.txttelf.set_text(rexistro[6]))
                str(self.txtmovil.set_text(rexistro[7]))
            cursorEnvio.close()  # cierra el cursor
            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Comprobar los Datos del Envio (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")



    def bComprobarRemite(self,boton):
        try:
            bbdd = dbapi.connect("envios.db")
            print("Comprobando Datos de Remitente...")

            cursorRemitente = bbdd.cursor()

            cursorRemitente.execute("SELECT * FROM remitente")
            for rexistro in cursorRemitente.fetchmany(2):
                self.txtNombreremitente.set_text(rexistro[1])
                self.txtdireccionremitente.set_text(rexistro[2])
                self.txtestadoremitente.set_text(rexistro[3])
                self.txtpoblacionremitente.set_text(rexistro[4])
                str(self.txtcpremitente.set_text(rexistro[5]))
                str(self.txttelfremitente.set_text(rexistro[6]))
            cursorRemitente.close()  # cierra el cursor
            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Comprobar los Datos del Remitente (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def bAñadirEnvio(self,boton):

        n = random.randint(10,50)  # genera un numero aleatorio entre 10 y 50
        idE = n

        try:
            bbdd = dbapi.connect("envios.db")
            print("Procesando...")

            cursorAñadirE = bbdd.cursor()
            datosEnvio = (
            idE,
            self.txtNombreenvio.get_text(),
            self.txtdirecciondestino.get_text(),
            self.txtestado.get_text(),
            self.txtpoblacion.get_text(),
            str(self.txtcp.get_text()),
            str(self.txttelf.get_text()),
            str(self.txtmovil.get_text())
            )

            cursorAñadirE.execute("INSERT INTO envios VALUES(?,?,?,?,?,?,?,?)",datosEnvio)

            cursorAñadirE.close()  # cierra el cursor
            bbdd.commit() #guarda los cambios

            print("Exito al Añadir Envio")

            self.txtNombreenvio.set_text("")
            self.txtdirecciondestino.set_text("")
            self.txtestado.set_text("")
            self.txtpoblacion.set_text("")
            str(self.txtcp.set_text(""))
            str(self.txttelf.set_text(""))
            str(self.txtmovil.set_text(""))
            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Añadir los Datos del Envio (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")



    def bAñadirRemite(self,boton):
        n = random.randint(10,50) #genera un numero aleatorio entre 10 y 50
        idR = n

        try:
            bbdd = dbapi.connect("envios.db")
            print("Procesando...")

            cursorAñadirR = bbdd.cursor()
            datosRemite = (
            idR,
            self.txtNombreremitente.get_text(),
            self.txtdireccionremitente.get_text(),
            self.txtestadoremitente.get_text(),
            self.txtpoblacionremitente.get_text(),
            str(self.txtcpremitente.get_text()),
            str(self.txttelfremitente.get_text())
            )
            cursorAñadirR.execute("INSERT INTO remitente VALUES(?,?,?,?,?,?,?)",datosRemite)

            cursorAñadirR.close()  # cierra el cursor
            bbdd.commit() #guarda los cambios

            print("Exito al Añadir Remitente")

            print("Vaciando campos del Remitente...")
            self.txtNombreremitente.set_text("")
            self.txtdireccionremitente.set_text("")
            self.txtestadoremitente.set_text("")
            self.txtpoblacionremitente.set_text("")
            str(self.txtcpremitente.set_text(""))
            str(self.txttelfremitente.set_text(""))

            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Añadir los Datos del Remitente (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def bAñadirPago(self, boton):

        try:
            bbdd = dbapi.connect("envios.db")
            print("Procesando...")

            cursorAñadirP = bbdd.cursor()
            datosPago = (
                self.comboBox.get_active_text(),
                self.txtpagarcontrarrembolso.get_text()
            )
            cursorAñadirP.execute("INSERT INTO pago VALUES(?,?)", datosPago)

            cursorAñadirP.close()  # cierra el cursor
            bbdd.commit()  # guarda los cambios

            print("Exito al Añadir Pago")

            bbdd.close()

        # excepcion

        except dbapi.OperationalError:
            print("Ups.. Error al Añadir los Datos del Pago (OperationalError)")
        except dbapi.DatabaseError:
            print("Error en la Base de Datos")

    def __init__(self):

        #crear la ventana principal
        Gtk.Window.__init__(self, title="Transportes Python - Nº 6122")
        self.set_border_width(10)
        self.set_default_size(450, 250)

        #crear la caja principal, la base de la ventana
        cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(cajaPrincipal)

        #titulo para el programa dentro de la ventana
        lbtitulo = Gtk.Label(xalign=0) #para la posicion
        lbtitulo.set_markup("<b>Transportes Python S.L.</b>")
        cajaPrincipal.add(lbtitulo)




#PRIMERA PARTE DE LA VENTANA:

        #agregar el frame
        fdatos = Gtk.Frame(label="Datos de Envio")
        #para agregar una caja vertical 1 dentro del frame para tener posicionado
        cajaInvisibleVert1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        fdatos.add(cajaInvisibleVert1)
        cajaInvisibleHor1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHor2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHor3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleVert2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)


        #añadir contenidos
        lblNombreenvio = Gtk.Label("Nombre Destinatario:", xalign=0)
        cajaInvisibleVert1.add(lblNombreenvio)
        self.txtNombreenvio = Gtk.Entry()
        cajaInvisibleVert1.add(self.txtNombreenvio)

        lbldirecciondestino = Gtk.Label("Dirección Destino:", xalign=0)
        cajaInvisibleVert1.add(lbldirecciondestino)
        self.txtdirecciondestino = Gtk.Entry()
        cajaInvisibleVert1.add(self.txtdirecciondestino)


        # para agregar una caja horizontal dentro del frame para tener posicionado

        lblestado = Gtk.Label("Estado ", xalign=0)
        cajaInvisibleHor1.add(lblestado)
        self.txtestado = Gtk.Entry()
        cajaInvisibleHor1.add(self.txtestado)

        lblpoblacion = Gtk.Label("Población ", xalign=0)
        cajaInvisibleHor1.add(lblpoblacion)
        self.txtpoblacion = Gtk.Entry()
        cajaInvisibleHor1.add(self.txtpoblacion)

        lblcp = Gtk.Label("C.P. ", xalign=0)
        cajaInvisibleHor1.add(lblcp)
        self.txtcp = Gtk.Entry()
        cajaInvisibleHor1.add(self.txtcp)

        lbltelf = Gtk.Label("Telf. ", xalign=0)
        cajaInvisibleHor2.add(lbltelf)
        self.txttelf = Gtk.Entry()
        cajaInvisibleHor2.add(self.txttelf)

        lblmovil = Gtk.Label("Movil ", xalign=0)
        cajaInvisibleHor2.add(lblmovil)
        self.txtmovil = Gtk.Entry()
        cajaInvisibleHor2.add(self.txtmovil)

        bComprobarEnvio = Gtk.Button("Comprobar Datos")
        bComprobarEnvio.connect("clicked", self.bComprobarEnvio)
        cajaInvisibleHor3.add(bComprobarEnvio)

        bAñadirEnvio = Gtk.Button("Añadir Datos")
        bAñadirEnvio.connect("clicked", self.bAñadirEnvio)
        cajaInvisibleHor3.pack_start(bAñadirEnvio, False, False, 100)
        cajaInvisibleHor3.add(bAñadirEnvio)

        bLimpiarEnvio = Gtk.Button("Limpiar Campos")
        bLimpiarEnvio.connect("clicked", self.bLimpiarEnvio)
        cajaInvisibleHor3.pack_end(bLimpiarEnvio, False, False, 0)
        cajaInvisibleHor3.add(bLimpiarEnvio)

#SEGUNDA PARTE DE LA VENTANA:

        # agregar el frame
        fremitente = Gtk.Frame(label="Remitente")
        # para agregar una caja vertical dentro del frame para tener posicionado
        cajaInvisibleVert3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleHorizontal4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        fremitente.add(cajaInvisibleVert3)
        fremitente.add(cajaInvisibleHorizontal4)
        fremitente.add(cajaInvisibleHorizontal5)
        fremitente.add(cajaInvisibleHorizontal6)

        # añadir contenidos
        lblNombreremitente= Gtk.Label("Nombre Remitente/Nombre de Empresa:", xalign=0)
        cajaInvisibleVert3.add(lblNombreremitente)
        self.txtNombreremitente = Gtk.Entry()
        cajaInvisibleVert3.add(self.txtNombreremitente)

        lbldireccionremitente = Gtk.Label("Dirección Remitente:", xalign=0)
        cajaInvisibleVert3.add(lbldireccionremitente)
        self.txtdireccionremitente = Gtk.Entry()
        cajaInvisibleVert3.add(self.txtdireccionremitente)


        lblestadoremitente = Gtk.Label("Estado ", xalign=0)
        cajaInvisibleHorizontal4.add(lblestadoremitente)
        self.txtestadoremitente = Gtk.Entry()
        cajaInvisibleHorizontal4.add(self.txtestadoremitente)

        lblpoblacionremitente = Gtk.Label("Población ", xalign=0)
        cajaInvisibleHorizontal4.add(lblpoblacionremitente)
        self.txtpoblacionremitente = Gtk.Entry()
        cajaInvisibleHorizontal4.add(self.txtpoblacionremitente)

        lblcpremitente = Gtk.Label("C.P. ", xalign=0)
        cajaInvisibleHorizontal4.add(lblcpremitente)
        self.txtcpremitente = Gtk.Entry()
        cajaInvisibleHorizontal4.add(self.txtcpremitente)

        lbltelfremitente = Gtk.Label("Telf. ", xalign=0)
        cajaInvisibleHorizontal5.add(lbltelfremitente)
        self.txttelfremitente = Gtk.Entry()
        cajaInvisibleHorizontal5.add(self.txttelfremitente)

        bComprobarRemitente = Gtk.Button("Comprobar Datos")
        bComprobarRemitente.connect("clicked", self.bComprobarRemite)
        cajaInvisibleHorizontal6.add(bComprobarRemitente)

        bAñadirRemite = Gtk.Button("Añadir Datos")
        bAñadirRemite.connect("clicked", self.bAñadirRemite)
        cajaInvisibleHorizontal6.pack_start(bAñadirRemite, False, False, 100)
        cajaInvisibleHorizontal6.add(bAñadirRemite)

        bLimpiarRemitente = Gtk.Button("Limpiar Campos")
        bLimpiarRemitente.connect("clicked", self.bLimpiarRemitente)
        cajaInvisibleHorizontal6.pack_end(bLimpiarRemitente, False, False, 0)
        cajaInvisibleHorizontal6.add(bLimpiarRemitente)

# TERCERA PARTE DE LA VENTANA:

        # agregar el frame
        fenvio = Gtk.Frame(label="Envio")
        # para agregar una caja vertical dentro del frame para tener posicionado
        cajaInvisibleVert4 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        cajaInvisibleHorizontal7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal9 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal10 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        cajaInvisibleHorizontal11 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        fenvio.add(cajaInvisibleVert4)
        fenvio.add(cajaInvisibleHorizontal7)
        fenvio.add(cajaInvisibleHorizontal8)
        fenvio.add(cajaInvisibleHorizontal9)
        fenvio.add(cajaInvisibleHorizontal10)
        fenvio.add(cajaInvisibleHorizontal11)

        #añadir el comboBox
        lbltipoenvio = Gtk.Label("Tipo de Envio",xalign=0)
        cajaInvisibleHorizontal7.add(lbltipoenvio)
        self.comboBox = Gtk.ComboBoxText()
        self.comboBox.insert(0,"0","24h")
        self.comboBox.insert(1, "1", "48h")
        self.comboBox.insert(2, "2", "72h")
        cajaInvisibleHorizontal7.add(self.comboBox )

        cajaInvisibleVert5 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        fenvio.add(cajaInvisibleVert4)
        lblcontrareembolso = Gtk.Label("¿Contrareembolso?",xalign=0)
        cajaInvisibleVert5.add(lblcontrareembolso)

                # añadir los checkbutton
        self.CheckButton1 = Gtk.CheckButton("Ninguno")
        self.CheckButton1.connect("clicked", self.comprobarCheck1)
        cajaInvisibleVert5.pack_start(self.CheckButton1, False, False, 10)
        cajaInvisibleVert5.add(self.CheckButton1)

        self.CheckButton2 = Gtk.CheckButton("Si, a pagar ")
        self.CheckButton2.connect("clicked", self.comprobarCheck2)
        cajaInvisibleVert5.pack_start(self.CheckButton2, False, False, 10)
        cajaInvisibleVert5.add(self.CheckButton2)

        self.txtpagarcontrarrembolso = Gtk.Entry()
        self.txtpagarcontrarrembolso.set_sensitive(False)
        cajaInvisibleHorizontal10.add(self.txtpagarcontrarrembolso)

        self.bPago = Gtk.Button("Añadir Datos")
        self.bPago.connect("clicked", self.bAñadirPago)
        cajaInvisibleHorizontal11.pack_start(self.bPago, False, False, 0)
        cajaInvisibleHorizontal11.add(self.bPago)

        botonVerFurgon= Gtk.Button("Abrir los Furgones")
        botonVerFurgon.connect("clicked", self.cambioVentFurgon)
        cajaInvisibleHorizontal11.pack_start(botonVerFurgon, False, False, 100)
        cajaInvisibleHorizontal11.add(botonVerFurgon)

        botonsalir = Gtk.Button("SALIR")
        botonsalir.connect("clicked", self.bSalir)
        cajaInvisibleHorizontal11.pack_end(botonsalir, False, False, 0)
        cajaInvisibleHorizontal11.add(botonsalir)

        cajaInvisibleVert1.add(cajaInvisibleHor1)#añade la caja horizontal 1 con la vertical 1
        cajaInvisibleVert1.add(cajaInvisibleHor2)  # añade la caja horizontal 2 con la vertical 1
        cajaInvisibleVert1.add(cajaInvisibleHor3)  # añade la caja horizontal 3 con la vertical 1
        cajaInvisibleVert1.add(cajaInvisibleVert2)#añade la caja vertical 2 con la vertical 1
        cajaInvisibleVert3.add(cajaInvisibleHorizontal4) #añade la caja horizontal 4 con la vertical 3
        cajaInvisibleVert3.add(cajaInvisibleHorizontal5)  # añade la caja horizontal 5 con la vertical 3
        cajaInvisibleVert3.add(cajaInvisibleHorizontal6)  # añade la caja horizontal 6 con la vertical 3
        cajaInvisibleVert4.add(cajaInvisibleHorizontal7) # añade la caja horizontal 7 con la vertical 4
        cajaInvisibleVert4.add(cajaInvisibleHorizontal8) # añade la caja horizontal 8 con la vertical 4
        cajaInvisibleVert4.add(cajaInvisibleHorizontal9) # añade la caja horizontal 9 con la vertical 4
        cajaInvisibleVert4.add(cajaInvisibleVert5) # añade la caja vertical 5 con la vertical 4
        cajaInvisibleVert4.add(cajaInvisibleHorizontal10)  # añade la caja horizontal 10 con la vertical 4
        cajaInvisibleVert4.add(cajaInvisibleHorizontal11)  # añade la caja horizontal 11 con la vertical 4

        cajaPrincipal.add(fdatos)#agrega la primera parte a la ventana principal
        cajaPrincipal.add(fremitente)#agrega la segunda ventana a la principal
        cajaPrincipal.add(fenvio)  # agrega la tercera ventana a la principal










        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
                                #para que se muestre la ventana
if __name__ == "__main__":
    ventana = ventanaPrincipalPrograma()
    Gtk.main()