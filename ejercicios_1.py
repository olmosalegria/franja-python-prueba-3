#Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000
#en un archivo llamado numeros_prueba.txt. Luego debe leer desde el
#archivo esos números y agregarlos a una lista, modifique o cree
#una nueva lista que contenga solo los nñumeros impares.
#Finalmente con numpy determinar la dimensión de la lista.
#Imprimir por consola la lista final y su dimensión.



#escribir un programa que escriba 20 numeros
import random

def main ():
    escribir_archivo()
    numeros_impares=leer_numeros()
def escribir_archivo():
    nombre_archivo="./archivos/numeros_prueba-.txt"
    with open(nombre_archivo,"w+", encoding="utf-8") as file:
        for i in range(1,21):
            numero_aleatorio= random.randint(100,1000)
            linea=str(numero_aleatorio)
            file.write(linea)
            file.write("\n")

#lectura de numeros en archivo
def leer_numeros():
    numeros=[]
    nombre_archivo="./archivos/numeros_prueba-.txt"
    with open(nombre_archivo,"r", encoding="utf-8") as file:
        for linea in file:
            numeros.append(int(linea))
        numeros_impares=[]
        for n in numeros:
            if n%2!=0:
                numeros_impares.append(n)
        print(numeros_impares)

if __name__=='__main__':
    main()

    

#Con numpy determinar la dimensión de la lista.

















