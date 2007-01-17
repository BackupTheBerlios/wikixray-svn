import dbdump
import dbanaly
import qA_conf as q

""" PASOS A SEGUIR

1. Descarga y descompresi�n del dbdump de cada idioma de Wikipedia que pretendemos analizar.

2. An�lisis de la BD de cada uno de los idiomas para
	a. Autores
	b. Art�culos
	c. Contenidos
	
3. An�lisis gr�fico y estad�stico de los resultados empleando el paquete R
	POR DESARROLLAR
"""

#Tomamos la configuracion incial del archivo
conf=q.qA_conf()

#Lista de idiomas que queremos analizar
ListaIdiomas=conf.langs
#ListaIdiomas=["eswiki", "plwiki"]

print "INICIANDO DESCOMPRESI�N DE LAS BASES DE DATOS...\n"

"""
for idioma in ListaIdiomas:
	fichero=dbdump.download_bd(conf,idioma)
	#fichero=idioma+"-latest-stub-meta-history.xml.gz"
	dbdump.unzip_bd(conf,fichero,idioma)
	print "DESCOMPRESI�N DE LAS BASES DE DATOS COMPLETADA...\n"
"""
print "INICIANDO ANALISIS DE LAS BASES DE DATOS...\n"

for idioma in ListaIdiomas:
	"""
	print "ANALISIS PARA EL IDIOMA " + idioma + "\n\n"
	dbanaly.flux_capacitor(conf,idioma)
	print "COMENZANDO ANALISIS DE AUTORES PARA EL IDIOMA " + idioma + "\n\n"
	dbanaly.info_authors(conf,idioma)
	print "FINALIZADO ANALISIS DE AUTORES PARA EL IDIOMA " + idioma + "\n\n"
	print "COMENZANDO ANALISIS DE ARTICULOS PARA EL IDIOMA " + idioma + "\n\n"
	dbanaly.info_articles(conf,idioma)
	print "FINALIZADO ANALISIS DE ARTICULOS PARA EL IDIOMA " + idioma + "\n\n"
	"""
	print "COMENZANDO ANALISIS DE CONTENIDOS PARA EL IDIOMA " + idioma + "\n\n"
	dbanaly.info_contents(conf,idioma)
	print "FINALIZADO ANALISIS DE CONTENIDOS PARA EL IDIOMA " + idioma + "\n\n"

print "ANALISIS DE LAS BASES DE DATOS COMPLETADO...\n"
print "FIN DE LA EJECUCION. BUENA SUERTE CON LA INTERPRETACION DE LOS RESULTADOS.\n"

