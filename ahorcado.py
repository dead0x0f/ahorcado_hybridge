#!/usr/bin/env python3
#Autor: Roberto

#Importamos los dibujos
from dibujo_ahorcado import dibujo_ahorcado
#Para escoger un directorio de forma aleatoria
import random 
#Para esperar un tiempo, por ejemplo segundos
import time
#Para ejecutar comandos del sistema
import subprocess
#Para identificar el tipo de sistema operativo
import os


def limpiar_pantalla():

    #Con exepciones de errores comprobamos si es posible ejecutar un comando del sistema
    try:
        #Determinar el sistema operativo para usar el comando correcto
        comando_limpiar_pantalla = 'cls' if os.name == 'nt' else 'clear'
        #Limpiar el terminal
        codigo_salida = subprocess.call(comando_limpiar_pantalla, shell=True)
        
        #Si el codigo del sistema es diferente a 0 imprimir 100 saltos de linea para simular una limpeza de pantalla
        #La razón de imprimir 100 saltos de línea es por que Thonny no acepta comandos del sistema
        if codigo_salida != 0:
            print('\n' * 100)

    except Exception:
        #Si da un error al intertar correr el comando, recurrir a imprimir 100 saltos de linea
        print('\n' * 100)


def palabra_tablero(palabra, letras_coleccionadas):
    
    #Crear un tablero dependiendo la palabra auque tenga espacios
    tablero = ''
    for letra in palabra:
        if letra in letras_coleccionadas:
            tablero += letra + ' '
        else:
            if letra == ' ':
                tablero += '  '
            else:
                tablero += '_ '
    
    return tablero


def main():

    #Directorios de los archivos con palabras
    directorios_archivos = {
            1: "filosofos.txt",
            2: "lenguajes_programacion.txt",
            3: "calculo.txt"
        }
    
    #Seleccionamos un archivo de manera aleatoria
    archivo_aleatorio = directorios_archivos[random.randint(1,3)]
    #Abro un archivo y guardo una sola de sus palabras
    archivo = open(archivo_aleatorio, "r")
    palabra = random.choice(archivo.readlines())
    palabra = palabra.replace('\n', '')
    archivo.close()
 
    #Creando una serie de tips para el jugador
    if archivo_aleatorio == directorios_archivos[1]:
        tips = "Piensa en un filosofo"
    if archivo_aleatorio == directorios_archivos[2]:
        tips = "Piensa en un lenguaje de programación"
    if archivo_aleatorio == directorios_archivos[3]:
        tips = "Piensa en un concepto básico del Cálculo"
   
    #Creando lógica del juego
    juego = False
    vidas = 7
    letras_coleccionadas = ''

    limpiar_pantalla()

    while vidas != 0:

        #Imprimimos la bienvenida
        print("\t\033[1;31m¡¡¡Bienvenido al juego del ahorcado!!!\033[1;0m")
       
       #Imprimimos el dibujo del ahorcado
        print(dibujo_ahorcado[vidas])
        
        #Imprimimos tips para intertar adivinar palabras
        print(tips)
    
        #Esta varuable guarda nuestro tablero de palabras
        tablero = palabra_tablero(palabra, letras_coleccionadas)
        
        #Si los caracteres "_ " no estan el el tablero, sifnifican que todas las palabras han sido adivinadas
        if '_ ' not in tablero:
            juego = True
            break 
        
        #Imprimimos el tablero
        print(tablero)

        letra_usuario = input("Ingrese una letra: ")
       
        #Verificamos que el usuario no ingrese mas de una letra
        if len(letra_usuario) > 1:
            print("Solo puedes ingresar una letra :( ")
            vidas -= 1
            time.sleep(2)

        #Verificamos que el usuario no haya ingresado la misma letra dos veces
        if letra_usuario in letras_coleccionadas:
            print("Esa letra ya la habias ingresado :( ")
            vidas -= 1
            time.sleep(2)
        
        #Agregamos las letras del usuario a un string que colecciona las letras
        letras_coleccionadas += letra_usuario
        
        #Verificamos si la letra es incorrecta
        if letra_usuario not in palabra:
            print("!!Esta letra es incorrecta!!")
            vidas -= 1
            time.sleep(2)
        
        #Limpiamos la pantalla para la presentación
        limpiar_pantalla()
   
    
    if juego:
        #Los caracteres especiales son para añadir colores 
        print("\033[7;31m¡¡Felicidases, has ganado al juego!!\033[1;30m")
    else:
        print("\033[7;33m¡¡Malas noticias, has perdido el juego!!\033[1;30m")

    

main()
