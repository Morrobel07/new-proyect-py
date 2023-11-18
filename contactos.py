class Contacto:
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
       return f"{self.nombre}-{self.telefono}-{self.email}"  
    


class GestorContactos:
    def __init__(self):
       self.contactos = []

    def agregar_contactos(self,contacto):
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        for contacto in self.contactos:
            print(contacto)
            

def main():
        gestor = GestorContactos()

        while True:
            print("\n!Gestor de Contactos!")
            print("1.agregar contacto")
            print("2.mostrar contacto")
            print("3.salir")

            opcion = input("seleccione una opcion")

            if opcion == "1":
                nombre = input("ingrese el nombre de contacto: ")
                telefono = input("Ingrese el telefono de contacto: ")
                email = input("ingrese el email del contacto: ")

                nuevo_contacto = Contacto(nombre,telefono,email)
                gestor.agregar_contactos(nuevo_contacto)
                print("contacto agregado correctamente")


            elif opcion == "2":
                print("\nLista de Contactos")  
                gestor.mostrar_contactos()

            elif opcion == "3":
                print("hasta luego")
                break

            else:
                print("Opcion no valida")

if __name__ =="__main__":
        main()                        



    

