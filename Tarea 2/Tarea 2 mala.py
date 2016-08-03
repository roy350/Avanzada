from poker import Tablero, Carta, Baraja
from poker import obtenerApuestaRobot, compararJugadas
print("                                           Bienvenido al juego de Poker Texas Hold'em")
print("El juego consiste en que te enfrentaras contra un computador nivel Dios para el Poker, aca partiras con 2 cartas y deberias hacer la ")
print("mejor combinacion de 5 cartas entre tus dos cartas mas 3 de la mesa, 3 de tu mano mas 2 de la mesa, 4 de tu mano mas 1 de la mesa, solo")
print("tu mano o solo la mesa, se partira con $1000 pesos, asi que si ya estas preparado")
input("presiona <ENTER> para continuar: ")
i=1
t=Tablero()
c=Carta()
b=Baraja()
b.barajar()
bote=0
dinero_humano=1000
dinero_robot=1000
apuesta_robot=0
cm=[]
ch1=b.obtenerCarta()
ch2=b.obtenerCarta()
cr1=b.obtenerCarta()
cr1.definirEstado("oculto")
cr2=b.obtenerCarta()
cr2.definirEstado("oculto")
cm1=b.obtenerCarta()
cm2=b.obtenerCarta()
cm3=b.obtenerCarta()
cm4=b.obtenerCarta()
cm5=b.obtenerCarta()
t.dibujarCarta(ch1,3,11)
t.dibujarCarta(ch2,13,11)
t.dibujarCarta(cr1,28,11)
t.dibujarCarta(cr2,38,11)
t.dibujarBorde(26,1,53,8)
t.dibujarBorde(0,10,23,9)
t.dibujarBorde(25,10,23,9)
t.escribirMensaje("Poker Texas Hold'em",0,1)
t.escribirMensaje("___________________",0,2)
t.escribirMensaje("-------------------",0,3)
t.escribirMensaje("Bote: "+str(bote),0,4)
t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
t.escribirMensaje("$"+str(dinero_humano),9,18)
t.escribirMensaje("$"+str(dinero_robot),34,18)
t.escribirMensaje("Mesa",51,1)
t.escribirMensaje("Jugador 0",7,10)
t.escribirMensaje("Jugador 1",33,10)
print(t)
apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
while apuesta_humano>dinero_humano:
    print("Su dinero es inferior a la apuesta asi que ingrese otra")
    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
bote+=apuesta_humano
dinero_humano-=(apuesta_humano)
apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
while True:
    if apuesta_robot==0:
        print("El robot se a retirado asi que tu ganaste")
        dinero_humano+=bote
        if dinero_humano<10:
            print("ya no puede seguir jugando porque su saldo es inferior a $10")
            break
        else:
            p=input("¿Quieres volver a jugar?(si/no): ")
            if p=="si":
                t.borrarTablero()
                b=Baraja()
                b.barajar()
                bote=0
                dinero_robot=1000
                apuesta_robot=0
                ch1=b.obtenerCarta()
                ch2=b.obtenerCarta()
                cr1=b.obtenerCarta()
                cr1.definirEstado("oculto")
                cr2=b.obtenerCarta()
                cr2.definirEstado("oculto")
                t.dibujarCarta(ch1,3,11)
                t.dibujarCarta(ch2,13,11)
                t.dibujarCarta(cr1,28,11)
                t.dibujarCarta(cr2,38,11)
                t.dibujarBorde(26,1,53,8)
                t.dibujarBorde(0,10,23,9)
                t.dibujarBorde(25,10,23,9)
                t.escribirMensaje("Poker Texas Hold'em",0,1)
                t.escribirMensaje("___________________",0,2)
                t.escribirMensaje("-------------------",0,3)
                t.escribirMensaje("Bote: "+str(bote),0,4)
                t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                t.escribirMensaje("$"+str(dinero_humano),9,18)
                t.escribirMensaje("$"+str(dinero_robot),34,18)
                t.escribirMensaje("Mesa",51,1)
                t.escribirMensaje("Jugador 0",7,10)
                t.escribirMensaje("Jugador 1",33,10)
                print(t)
                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                while apuesta_humano>dinero_humano:
                    print("Su dinero es inferior a la apuesta asi que ingrese otra")
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                bote+=apuesta_humano
                dinero_humano-=apuesta_humano
                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
            if p=="no":
                print("Hasta luego")
                break
    elif apuesta_robot==apuesta_humano:
        if i==1:
            bote+=apuesta_robot
            dinero_robot-=apuesta_robot
            print("El robot iguala")
            t.dibujarCarta(cm1,28,2)
            t.dibujarCarta(cm2,38,2)
            t.dibujarCarta(cm3,48,2)
            t.escribirMensaje("Bote: "+str(bote),0,4)
            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
            t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
            t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
            cm=[cm1,cm2,cm3]
            print(t)
            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
            while apuesta_humano>dinero_humano:
                print("Su dinero es inferior a la apuesta asi que ingrese otra")
                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
            bote+=apuesta_humano
            dinero_humano-=apuesta_humano
            t.escribirMensaje("Bote: "+str(bote),0,4)
            t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
            t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
            t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
            i+=1
        if i==2:
            bote+=apuesta_robot
            dinero_robot-=apuesta_robot
            print("El robot iguala")
            t.dibujarCarta(cm4,58,2)
            t.escribirMensaje("Bote: "+str(bote),0,4)
            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
            t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
            t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
            cm=[cm1,cm2,cm3,cm4]
            print(t)
            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
            while apuesta_humano>dinero_humano:
                print("Su dinero es inferior a la apuesta asi que ingrese otra")
                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
            bote+=apuesta_humano
            dinero_humano-=apuesta_humano
            t.escribirMensaje("Bote: "+str(bote),0,4)
            t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
            t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
            t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
            i+=1
        if i==3:
            bote+=apuesta_robot
            dinero_robot-=apuesta_robot
            print("El robot iguala")
            t.dibujarCarta(cm5,68,2)
            t.escribirMensaje("Bote: "+str(bote),0,4)
            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
            t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
            t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
            cm=[cm1,cm2,cm3,cm4,cm5]
            print(t)
            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
            while apuesta_humano>dinero_humano:
                print("Su dinero es inferior a la apuesta asi que ingrese otra")
                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
            bote+=apuesta_humano
            dinero_humano-=apuesta_humano
            t.escribirMensaje("Bote: "+str(bote),0,4)
            t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
            t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
            t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
            i+=1
    elif apuesta_robot>apuesta_humano:
        bote+=apuesta_robot
        dinero_robot-=apuesta_robot
        print("el robot a aumentado la apuesta ")
        t.escribirMensaje("Bote: "+str(bote),0,4)
        t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
        t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
        t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
        print(t)
        if dinero_humano<apuesta_robot:
            print("No puedes seguir jugando")
            if dinero_humano<10:
                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                break
            else:
                p=input("¿Quieres volver a jugar?(si/no): ")
                if p=="si":
                    t.borrarTablero()
                    b=Baraja()
                    b.barajar()
                    bote=0
                    dinero_robot=1000
                    apuesta_robot=0
                    ch1=b.obtenerCarta()
                    ch2=b.obtenerCarta()
                    cr1=b.obtenerCarta()
                    cr1.definirEstado("oculto")
                    cr2=b.obtenerCarta()
                    cr2.definirEstado("oculto")
                    t.dibujarCarta(ch1,3,11)
                    t.dibujarCarta(ch2,13,11)
                    t.dibujarCarta(cr1,28,11)
                    t.dibujarCarta(cr2,38,11)
                    t.dibujarBorde(26,1,53,8)
                    t.dibujarBorde(0,10,23,9)
                    t.dibujarBorde(25,10,23,9)
                    t.escribirMensaje("Poker Texas Hold'em",0,1)
                    t.escribirMensaje("___________________",0,2)
                    t.escribirMensaje("-------------------",0,3)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano),9,18)
                    t.escribirMensaje("$"+str(dinero_robot),34,18)
                    t.escribirMensaje("Mesa",51,1)
                    t.escribirMensaje("Jugador 0",7,10)
                    t.escribirMensaje("Jugador 1",33,10)
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                if p=="no":
                        print("Hasta luego")
                        break
        else:
            p1=input("¿Que desea hacer?(retirar,igualar o aumentar): ")
            if p1=="retirar":
                dinero_robot+=bote
                print("Se ha rendido, suerte para la proxima")
                if dinero_humano<10:
                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                    break
                else:
                    p=input("¿Quieres volver a jugar?(si/no): ")
                    if p=="si":
                        t.borrarTablero()
                        b=Baraja()
                        b.barajar()
                        bote=0
                        dinero_robot=1000
                        apuesta_robot=0
                        ch1=b.obtenerCarta()
                        ch2=b.obtenerCarta()
                        cr1=b.obtenerCarta()
                        cr1.definirEstado("oculto")
                        cr2=b.obtenerCarta()
                        cr2.definirEstado("oculto")
                        t.dibujarCarta(ch1,3,11)
                        t.dibujarCarta(ch2,13,11)
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        t.dibujarBorde(26,1,53,8)
                        t.dibujarBorde(0,10,23,9)
                        t.dibujarBorde(25,10,23,9)
                        t.escribirMensaje("Poker Texas Hold'em",0,1)
                        t.escribirMensaje("___________________",0,2)
                        t.escribirMensaje("-------------------",0,3)
                        t.escribirMensaje("Bote: "+str(bote),0,4)
                        t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                        t.escribirMensaje("$"+str(dinero_humano),9,18)
                        t.escribirMensaje("$"+str(dinero_robot),34,18)
                        t.escribirMensaje("Mesa",51,1)
                        t.escribirMensaje("Jugador 0",7,10)
                        t.escribirMensaje("Jugador 1",33,10)
                        print(t)
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                        while apuesta_humano>dinero_humano:
                            print("Su dinero es inferior a la apuesta asi que ingrese otra")
                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                        bote+=apuesta_humano
                        dinero_humano-=apuesta_humano
                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                    if p=="no":
                        print("Hasta luego")
                        break
            elif p1=="igualar":
                if i==1:
                    bote+=apuesta_robot
                    dinero_humano-=apuesta_robot
                    t.dibujarCarta(cm1,28,2)
                    t.dibujarCarta(cm2,38,2)
                    t.dibujarCarta(cm3,48,2)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
                    t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
                    cm=[cm1,cm2,cm3]
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                    i+=1
                if i==2:
                    bote+=apuesta_robot
                    dinero_humano-=apuesta_robot
                    t.dibujarCarta(cm4,58,2)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
                    t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
                    cm=[cm1,cm2,cm3,cm4]
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                    i+=1
                if i==3:
                    bote+=apuesta_robot
                    dinero_humano-=apuesta_robot
                    t.dibujarCarta(cm5,68,2)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
                    t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
                    cm=[cm1,cm2,cm3,cm4,cm5]
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                    i+=1
            if p1=="aumentar":
                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                while apuesta_humano>dinero_humano:
                    print("Su dinero es inferior a la apuesta asi que ingrese otra")
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                bote+=apuesta_humano
                t.escribirMensaje("Bote: "+str(bote),0,4)
                t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
                t.escribirMensaje("$"+str(dinero_humano)+" ",9,18)
                t.escribirMensaje("$"+str(dinero_robot)+" ",34,18)
                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
    if len(cm)==5:
        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
        cr1.definirEstado("visible")
        cr2.definirEstado("visible")
        t.dibujarCarta(cr1,28,11)
        t.dibujarCarta(cr2,38,11)
        if final=="empate":
            print(t)
            print("Ha sido un empate")
            if dinero_humano<10:
                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                break
            else:
                p=input("¿Quieres volver a jugar?(si/no): ")
                if p=="si":
                    t.borrarTablero()
                    b=Baraja()
                    b.barajar()
                    bote=0
                    dinero_robot=1000
                    apuesta_robot=0
                    ch1=b.obtenerCarta()
                    ch2=b.obtenerCarta()
                    cr1=b.obtenerCarta()
                    cr1.definirEstado("oculto")
                    cr2=b.obtenerCarta()
                    cr2.definirEstado("oculto")
                    t.dibujarCarta(ch1,3,11)
                    t.dibujarCarta(ch2,13,11)
                    t.dibujarCarta(cr1,28,11)
                    t.dibujarCarta(cr2,38,11)
                    t.dibujarBorde(26,1,53,8)
                    t.dibujarBorde(0,10,23,9)
                    t.dibujarBorde(25,10,23,9)
                    t.escribirMensaje("Poker Texas Hold'em",0,1)
                    t.escribirMensaje("___________________",0,2)
                    t.escribirMensaje("-------------------",0,3)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano),9,18)
                    t.escribirMensaje("$"+str(dinero_robot),34,18)
                    t.escribirMensaje("Mesa",51,1)
                    t.escribirMensaje("Jugador 0",7,10)
                    t.escribirMensaje("Jugador 1",33,10)
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                if p=="no":
                    print("Hasta luego")
                    break
        elif final=="gana_humano":
            print(t)
            print("¡Felicidades has ganado!")
            if dinero_humano<10:
                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                break
            else:
                p=input("¿Quieres volver a jugar?(si/no): ")
                if p=="si":
                    t.borrarTablero()
                    b=Baraja()
                    b.barajar()
                    bote=0
                    dinero_robot=1000
                    apuesta_robot=0
                    ch1=b.obtenerCarta()
                    ch2=b.obtenerCarta()
                    cr1=b.obtenerCarta()
                    cr1.definirEstado("oculto")
                    cr2=b.obtenerCarta()
                    cr2.definirEstado("oculto")
                    t.dibujarCarta(ch1,3,11)
                    t.dibujarCarta(ch2,13,11)
                    t.dibujarCarta(cr1,28,11)
                    t.dibujarCarta(cr2,38,11)
                    t.dibujarBorde(26,1,53,8)
                    t.dibujarBorde(0,10,23,9)
                    t.dibujarBorde(25,10,23,9)
                    t.escribirMensaje("Poker Texas Hold'em",0,1)
                    t.escribirMensaje("___________________",0,2)
                    t.escribirMensaje("-------------------",0,3)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano),9,18)
                    t.escribirMensaje("$"+str(dinero_robot),34,18)
                    t.escribirMensaje("Mesa",51,1)
                    t.escribirMensaje("Jugador 0",7,10)
                    t.escribirMensaje("Jugador 1",33,10)
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                if p=="no":
                    print("Hasta luego")
                    break
        elif final=="gana_robot":
            print(t)
            print("Lo sentimos ha ganado el robot")
            if dinero_humano<10:
                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                break
            else:
                p=input("¿Quieres volver a jugar?(si/no): ")
                if p=="si":
                    t.borrarTablero()
                    b=Baraja()
                    b.barajar()
                    bote=0
                    dinero_robot=1000
                    apuesta_robot=0
                    ch1=b.obtenerCarta()
                    ch2=b.obtenerCarta()
                    cr1=b.obtenerCarta()
                    cr1.definirEstado("oculto")
                    cr2=b.obtenerCarta()
                    cr2.definirEstado("oculto")
                    t.dibujarCarta(ch1,3,11)
                    t.dibujarCarta(ch2,13,11)
                    t.dibujarCarta(cr1,28,11)
                    t.dibujarCarta(cr2,38,11)
                    t.dibujarBorde(26,1,53,8)
                    t.dibujarBorde(0,10,23,9)
                    t.dibujarBorde(25,10,23,9)
                    t.escribirMensaje("Poker Texas Hold'em",0,1)
                    t.escribirMensaje("___________________",0,2)
                    t.escribirMensaje("-------------------",0,3)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(dinero_humano),9,18)
                    t.escribirMensaje("$"+str(dinero_robot),34,18)
                    t.escribirMensaje("Mesa",51,1)
                    t.escribirMensaje("Jugador 0",7,10)
                    t.escribirMensaje("Jugador 1",33,10)
                    print(t)
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>dinero_humano:
                        print("Su dinero es inferior a la apuesta asi que ingrese otra")
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    bote+=apuesta_humano
                    dinero_humano-=apuesta_humano
                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,dinero_robot,apuesta_robot,apuesta_humano)
                if p=="no":
                    print("Hasta luego")
                    break










