#variables globales 
cie = 0
cincuenta = 0
cien = int(cie)
cin = int(cincuenta)
#saldo 
saldo = 2520 
#arrays 
decenas = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 40, 50, 60, 70, 80, 90}
centenas = {100: "cien ", 200: "doscientos ", 300: "trescientos ", 400: "cuatrocientos ", 500: "quinientos ", 600: "seicientos ", 700: "setecientos ", 800: "ochocientos ", 900: "novecientos "}
unidades = {1: "y uno", 2: "y dos", 3: "y tres", 4: "y cuatro", 5: "y cinco", 6: "y seis", 7: "y siete", 8: "y ocho", 9: "y nueve"}
#un for para verificar las 3 veces que se puede ingresar la contraseña y el usuario 
for i in range(3): 
    #se pide el usuario y la contraseña 
    usuario = input("Bienvenido al cajero automático, ingrese su usuario porfavor ")
    pin = int(input("Por favor digite su pin "))
    #si el usuario es correcto dará acceso 
    if usuario == "BCC-2215" and pin == 225125:
        print("Elija la opción que desee, utilice números para escoger")
        print("1. Retirar dinero")
        print("2. Revisar saldo de cuenta")    
        print("3. Depositar fondos")
        print("4. Transferencia de fondos")                
        opcion = int(input())
        #esta opción te dará para elegir entre monto variable y monto fijo 
        if opcion == 1:
            print("Elija la opción que desee usando números")
            print("1. Billetes normales")
            print("2. Monto variable")
            opcion2 = int(input())
            #los montos fijos
            if opcion2 == 1: 
                print("Elija la cantidad a retirar usando números para elejir la opción")
                print("1. 100")
                print("2. 200")
                print("3. 300")
                print("4. 400")
                print("5. 500")
                opcion3 = int(input())
                #al escoger un monto se le agrega la cantidad de billetes al tipo de billete que se le va a dar
                if opcion3 == 1: 
                    cien = 1  
                elif opcion3 == 2: 
                    cien = 2
                elif opcion3 == 3: 
                    cien = 3
                elif opcion3 == 4: 
                    cien = 4
                elif opcion3 == 5: 
                    cien = 5
            #en esta opción se puede elegir el monto 
            elif opcion2 == 2: 
                monto = int(input("Ingrese el monto que desea retirar, porfavor que termine en 5 o en 0 el último dígito y que no exceda los Q2,000.00"))
                #si el monto es mayor a 100 pero menor a 2000 procederá 
                if monto >= 100 and monto < 2000:
                    #saca el residuo para contar la cantidad exacta de billetes de 100
                    residuo = monto % 100
                    cien = (monto-residuo)/100
                    #si quedan residuos los calculará aquí 
                    if residuo >= 50:
                        residuos = residuo % 50
                        cin = (residuo-residuos)/50
                        #si el monto es menor a 50 y mayor a 1 no será posible darle la cantidad de billetes solicitada
                        if residuos < 50 and residuos > 1: 
                            print("Ese monto no es posible")      
                            opcion = 3
                #si el monto original era menor a 100, entonces buscará sacar los de 50 
                elif monto >= 50 and monto < 2000:
                    if monto < 100:
                        residuo = monto % 50
                        cin = (monto-residuo)/50    
                        if residuo < 50 and residuo > 1: 
                            print("Ese monto no es posible")      
                            opcion = 3 
                #por último si no es posible, simplemente no dará nada 
                elif monto < 50: 
                    print("Ese monto no es posible")      
                    opcion = 3 
        #esta opción da el saldo que tiene la persona
        elif opcion == 2: 
            print(f"El saldo de su cuenta es igual a {saldo}")
            break 
        #en esta opción se deposita una cantidad para si mismo 
        elif opcion == 3:
            deposito = int(input("ingrese la cantidad que desea depositar"))
            palabras = input("Por favor vuelva a escribirla en letras")   
            print(f"La cantidad depositada correctamente y fue de {deposito}") 
            break                    
        #en esta opción se transfiere a otra persona
        elif opcion == 4: 
            transferencia = input("Por favor ingrese la cuenta a la que ingresar los fondos")
            ca1 = transferencia[0:3]
            cad = transferencia[4]
            cade1 = transferencia[5:6]
            caden = transferencia[7]
            cadena1 = transferencia[8:11]
            ca = ca1.isdigit()
            cade = cade1.isdigit()
            cadena = cadena1.isdigit()
            #aquí verifica si la cuenta existe y es válida 
            if ca == True and cad == "-" and cade == True and caden == "-" and cadena == True: 
                transferencia1 = int(input("ingrese la cantidad que desea transferir"))
                #si el saldo es insuficiente no podrá transferir 
                if transferencia1 > saldo: 
                    print("El saldo es insuficiente para esta transacción, intente de nuevo")
                    break 
                elif transferencia1 < saldo: 
                    saldo = saldo - transferencia1
                    print(f"La transferencia se ha realizado exitosamente, a su cuenta le quedan {saldo}")
                    break
            #si puso mal la cuenta entonces aquí lo mandará de regreso al inicio
            elif ca != True or cad != "-" or cade != True or caden != "-" or cadena != True: 
                print("La cuenta ingresada no es correcta, intente de nuevo")
                break
    #si el pin o el usuario son incorrectos lo verifica y va restando un intento 
    elif pin != 225125 or usuario != "BCC-2215": 
        i = i + 1 
        if i < 3: 
            print("incorrecto, por favor comience de nuevo")
        if i == 3: 
            print("La cantidad de intentos es excesiva")
            break
    #si el usuario es correcto, la contraseña es correcta y la opción elegida es retirar dinero, entonces dará la cantidad de billetes retirados  
    if usuario == "BCC-2215":
        if pin == 225125:  
            if opcion == 1:  
                print("la cantidad de billetes retirados fue")
                print(f"La cantidad de billetes de a 100 fue: {cien}")
                print(f"La cantidad de billetes de a 50 fue: {cin}")
                break 