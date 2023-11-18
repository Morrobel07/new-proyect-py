class Cajero:
    def __init__(self,saldo_inicial,numero_cuenta):
        self.saldo_inicial = saldo_inicial
        self.numero_cuenta = numero_cuenta
        self.transacciones = []
        
    def mostrar_saldo(self):
        #for saldo_inicial in self.saldo_inicial:
            #print (saldo_inicial)
        return self.saldo_inicial    

    def depositar_saldo(self,monto):
      #saldo_inicial = int(input("haz tu primer deposito en la cuenta numero",numero_cuenta,"con el monto de:"))
        #self.transacciones.append(saldo_inicial += 1)
        if monto >= 0:
            self.saldo_inicial += monto  #saldo_inicial = saldo_inicial + monto 
            #self.transacciones.append(int(input(f"Desposita:"+ monto))) 
            monto = int(input("deposita: "))
            self.transacciones.append(float(  + monto))
            return True
         
        else:
            print("error: El monto debe ser mayor que 0")
            return False
    
    def retirar_saldo(self,monto):
        if monto > 0 and monto <= self.saldo_inicial:
            self.saldo_inicial -= monto
            monto = int(input("retirar: "))
            self.transacciones.append(float(- monto))
            return True
        elif monto <= 0:
            print("error: El monto debe ser mayor que 0")
            return False
        else:
            print("Error fondos insuficientes")
            return False
        
def main ():
    numero_cuenta = "xxxxxxx"
    saldo_inicial = 10000      
    cajero = Cajero(saldo_inicial,numero_cuenta)
    
    while True:
        print("\nMenu")
        print("1.consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. salir")
        
        opcion = int(input("seleccione una opcion: "))
        
        if opcion == 1 :  
            print("saldo actual:",cajero.mostrar_saldo())
            
        elif opcion == 2 :
            monto_deposito =float(input("ingrese el monto a depositar: "))
            cajero.depositar_saldo(monto_deposito)
            
        elif opcion == 3 :
            monto_retiro = float(input("ingrese el monto a retiro: "))
            cajero.retirar_saldo(monto_retiro)  
                
        elif opcion == 4 :
            print("bye!!!!!")
            break
        
        else : 
            print("opcion no vlaida. por favor, selecciones una valida")
        
if __name__ == "__main__":
    main()                      
       






          

