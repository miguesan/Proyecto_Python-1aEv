from setuptools import setup

ficheiros = ["arquivos/*"]
setup (name="Transportes Python",version="1.00",
       description="Aplicacion para la empresa de transportes Python",
       long_description="""Aplicacion para la gestion,
       envio, y asigancion de paquetes
       con remitente y destinatario
       por base de datos""",
       author = "Miguel",
       author_email ="msanchezblanco@danielcastelao.org",
       url="www.transportespython.es",
       keywords="Transportes,envios,furgones",
       platforms="Linux,MacOs",
       packages =["paquete"],
       package_data= {'paquete':ficheiros},
       scripts=["lanzador"]
       )