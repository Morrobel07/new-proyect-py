class cajero:
    def __init__(self,saldo_inicial,numero_cuenta):
        self.saldo_inicial = saldo_inicial
        self.numero_cuenta = numero_cuenta
        self.transacciones = []
        
     def  mostrar_saldo(self):
        #for saldo_inicial in self.saldo_inicial:
            #print (saldo_inicial)
        return self.saldo_inicial    

     def depositar_saldo(self,monto):
      #saldo_inicial = int(input("haz tu primer deposito en la cuenta numero",numero_cuenta,"con el monto de:"))
        #self.transacciones.append(saldo_inicial += 1)
         if monto >= 0:
            self.saldo_inicial +=0  #saldo_inicial = saldo_inicial + monto 
            #self.transacciones.append(int(input(f"Desposita:"+ monto))) 
            monto = int(input("deposita: "))
            self.transacciones.append(monto)
    
    def retirar_saldo(self):
        int(input("Cuanto deseas retirar:" ,))






          

