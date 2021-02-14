import requests                 	# Para obtener datos de la pagina _____
from bs4 import BeautifulSoup as bs # Para ordenar esos datos de manera legible

# Descargar la pagina web ______________________________________________________
def get_page(aniurl):
    """
    Utilzamos beautiful soup y request para obtener la url y obtener la pagina
    como texto separado por linea dentro de una lista, esta funcion devuelve una
    lista
    """
    #descargamos la pagina
    page = requests.get(aniurl)
    #la ordenamos
    soup = bs(page.content, 'html.parser')

    # separamos cada linea en elementos de una lista
    page = str(soup).split("\n")

    return page

# Buscador de palabras ________________________________________________________ <3
def grep(texto, buscar, imprimir = False, counter = 0, sep = False):
    """
    #Comparador de Lineas
    ingrese string en el texto y buscar, en caso de que el texto contenga la palabra
    que reemplazo por buscar, se imprimira la linea donde aparecio

    >> grep("hola \\n como estas","estas") -> "como estas"

    la opcion counter se saltara tantos matches

    >> grep("hola caracola \\n hola tu","estas", counter = 0) -> "hola caracola"
    >> grep("hola caracola \\n hola tu","estas", counter = 1) -> "hola tu"
	
	De usar la opcion "imprimir=True", se convierte en algo solo para debugging, la funcion no retornara nada

    """
    if sep:
        #De darle la opcion, separara el texto en Lineas, esto es util si no solo le das la pagina sin procesar
		#Por default las funcion get_page ya lo hace, asi que esta opcion en grep viene por default desactivada
        texto = str(texto).split("\n")

    for linea in texto: #buscar entre las lineas
        if buscar in linea: #de haber matche

            if counter == 0:        #revisamos el counter, de no existir el counter solo nos dara el primer match
									#y la funcion acabara de ejecutarse
                if imprimir:
                    print(linea)
                else:
                    return linea

            counter = counter - 1 	# de haber visto un match, restamos uno al counter
                					#de manera que el siguiente pueda caer con counter 0 y ser ejecutado
            if imprimir:
				print(linea) #imprimimos una de las lineas que hallo, es bueno para ver si funciona correctamente
