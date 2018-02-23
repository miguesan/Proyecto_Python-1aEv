from distutils.core import setup

setup (name="Transportes Python",
       version="1.00",
       description="Aplicacion para la empresa de transportes Python",
       long_description="""Aplicacion para la gestion,
       envio, y asigancion de paquetes
       con remitente y destinatario
       por base de datos""",
       author = "Miguel",
       author_email ="msanchezblanco@danielcastelao.org",
       url="www.transportespython.es",
       keywords="transportes,envios,furgones,python",
       platforms="Linux,MacOS",
       packages =['paquete'],
       scripts=['lanzador']
       )