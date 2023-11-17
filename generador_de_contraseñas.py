import random
import string

def generador_de_contraseñas(longitud):
 caracteres = string.ascii_letters + string.digits + string.punctuation
 contraseña =  ''.join(random.choice(caracteres) for i in range(longitud))
 return contraseña

#print(generador_de_contraseñas)

def main ():
    print ("Welcome ")

    longitud = int(input("longitud de la contraseña:"))

    nueva_contraseña = generador_de_contraseñas(longitud)

    print(f"\ntu nueva contraseña generada es:{nueva_contraseña}")

if __name__ == '__main__':
   main()    


  


