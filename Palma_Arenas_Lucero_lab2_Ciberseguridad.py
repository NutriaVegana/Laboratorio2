#Laboratorio 2

#Jorge Arenas
#Diego Palma
#Sebastian Lucero
import hashlib
import os
def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)

        alfabeto_a_usar = alfabeto
        limite = 97  
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto

        codificado += alfabeto_a_usar[posicion]
    return codificado


def decodificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    decodificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            decodificado += letra
            continue
        valor_letra = ord(letra)

        alfabeto_a_usar = alfabeto
        
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite - rotaciones) % longitud_alfabeto

        decodificado += alfabeto_a_usar[posicion]
    return decodificado

LETRAS = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def vigenere(mensaje,accion,myKey):

    if accion==1:
        traducido=cifrar_mensaje(myKey,mensaje)
    elif accion==2:
        traducido=descifrar_mensaje(myKey,mensaje)
    return traducido

def cifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'encriptar')

def descifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'descifrar')

def traductor_mensaje(clave,mensa,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=LETRAS.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=LETRAS.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=LETRAS.find(clave[indice_clave])
            num%=len(LETRAS)
            if symbol.isupper():
                traducido.append(LETRAS[num])
            elif symbol.islower():
                traducido.append(LETRAS[num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)


def sha256(fichero):
    fp = open(fichero, "rb")
    buffer = fp.read()
    # sha256
    hashObj = hashlib.sha256()
    hashObj.update(buffer)
    lastHash = hashObj.hexdigest().upper()
    sha256 = lastHash
    fp.close()
    return fichero,sha256

def limpiarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
        
def proceso_cifrado(m):
    m=codificar(m,8)
    m=vigenere(m,1,"SEGUNDOLAB")
    m=codificar(m,12)
    return m

def proceso_descifrado(m):
    m=decodificar(m,12)
    m=vigenere(m,2,"SEGUNDOLAB")
    m=decodificar(m,8)
    return m
while True:
    print("------------- MENÚ ------------- ")
    print("[1] Encryptar fichero con SHA256")
    print("[2] Desencryptar fichero SHA256")
    print("[3] Salir")
    opcion = int(input("Introduzca una opción: "))
    limpiarPantalla()
    if opcion == 1:
        ficheroElegido = "mensajedeentrada.txt"
        print("=" * 40)
        fichero, ultimoHash = sha256(ficheroElegido)
        print("Fichero: " + fichero)
        print("SHA256: " + ultimoHash)
        print("=" * 40)
        
        f = open ('mensajedeentrada.txt','r')
        mensaje = f.read()
        mensaje_cifrado=proceso_cifrado(mensaje)
        f.close()
        
        f = open ('mensajeseguro.txt','w')
        f.write(mensaje_cifrado+"EEESDMC"+ultimoHash)
        f.close()

    elif opcion == 2:
        ficheroElegido = "mensajeseguro.txt"      
        f = open ('mensajeseguro.txt','r')
        mensaje = f.read()
        mensaje=mensaje.split("EEESDMC")
        mensaje_seguro=mensaje[0]
        comparador_hash=mensaje[1]
        mensaje_descifrado=proceso_descifrado(mensaje_seguro)
        
        ficheroElegido = "mensajeseguro.txt"      
        f = open ('mensajeseguro.txt','w')
        f.write(mensaje_descifrado)
        f.close()
        print("=" * 40)
        fichero, ultimoHash = sha256(ficheroElegido)
        if(ultimoHash==comparador_hash):
            print("EL ARCHIVO ES INTEGRO")
        else:
            print("EL ARCHIVO NO ES INTEGRO")
        print("=" * 40)
    else:
        break
    
