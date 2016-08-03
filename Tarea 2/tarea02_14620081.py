from poker import Tablero, Carta, Baraja
from poker import obtenerApuestaRobot, compararJugadas
print("                                           Bienvenido al juego de Poker Texas Hold'em")
print("El juego consiste en que te enfrentaras contra un robot con grandes habilidades para el Poker, aca partiras con 2 cartas y deberias hacer la")
print("mejor combinacion de 5 cartas entre todas las opciones posibles ya sea usando tus dos cartas solo 1 o ninguna en conjunto con las de la mesa,la")
print("idea es utilizar 5 cartas dentro de todas las combinaciones posibles a utilizar,el juego consta de cuatro rondas de apuestas primero con 2 cartas")
print("cada jugador y ninguna en la mesa,luego con 3 cartas en la mesa, despues con 4 y finalmente con 5, luego de que finalice esta ronda de apuesta se")
print("compara jugadas y se comprueba quien es el ganador del juego, tu simepre partes apostando si el robot o tu quedan con un saldo inferior a 10 pesos")
print("el juego se acaba, una vez que apuestas el robot opta por retirarse, igualarte o aumentar si aumenta ahora te toca a ti las mismas tres opciones   ")
print("retirarte, igualar o aumentar, se parte con un total de $5000 asi que si ya estas listo para enfrentarte al robot en este juego de Poker, por favor")
input("presiona <ENTER> para continuar: ")
class Jugador:
    def __init__(self,tipo):
        self.tipo=tipo
        self.dinero=5000
    def cartasJugador(self,a):
        self.cj1=a.obtenerCarta()
        self.cj2=a.obtenerCarta()
        return([self.cj1,self.cj2])
class ControlJuego:
    def Juego(self,h,r):
        z=0
        i=1
        t=Tablero()
        c=Carta()
        b=Baraja()
        b.barajar()
        bote=0
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
        t.escribirMensaje("$"+str(h.dinero),9,18)
        t.escribirMensaje("$"+str(r.dinero),34,18)
        t.escribirMensaje("Mesa",51,1)
        t.escribirMensaje("Jugador 0",7,10)
        t.escribirMensaje("Jugador 1",33,10)
        print(t)
        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
        while apuesta_humano>h.dinero:
            print("Su dinero es inferior a la apuesta asi que ingrese otra")
            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
        if apuesta_humano>r.dinero:
            print("¡Felicidades has ganado!")
        bote+=apuesta_humano
        h.dinero-=(apuesta_humano)
        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
        while z==0:
            if apuesta_robot==0:
                print("El robot se a retirado asi que tu ganaste")
                h.dinero+=bote
                if h.dinero<10:
                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                    z+=1
                    break
                else:
                    x=0
                    while x==0:
                        y=0
                        while y==0:
                            p=input("¿Quieres volver a jugar?(si/no): ")
                            if p=="si":
                                i=1
                                t.borrarTablero()
                                b=Baraja()
                                b.barajar()
                                bote=0
                                apuesta_robot=0
                                cm=[]
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
                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                t.escribirMensaje("Mesa",51,1)
                                t.escribirMensaje("Jugador 0",7,10)
                                t.escribirMensaje("Jugador 1",33,10)
                                print(t)
                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                while apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                if apuesta_humano>r.dinero:
                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                    h.dinero+=bote
                                    if h.dinero<10:
                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                        y+=1
                                        x+=1
                                        z+=1
                                        break
                                    else:
                                        y+=1
                                else:
                                    bote+=apuesta_humano
                                    h.dinero-=apuesta_humano
                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                    y+=1
                                    x+=1
                            if p=="no":
                                print("Hasta luego")
                                y+=1
                                x+=1
                                z+=1
            elif apuesta_robot==apuesta_humano:
                if i==1:
                    bote+=apuesta_robot
                    r.dinero-=apuesta_robot
                    print("El robot iguala")
                    t.dibujarCarta(cm1,28,2)
                    t.dibujarCarta(cm2,38,2)
                    t.dibujarCarta(cm3,48,2)
                    t.borrarZona(9,18,5,1)
                    t.borrarZona(34,18,5,1)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                    t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                    cm=[cm1,cm2,cm3]
                    print(t)
                    if r.dinero==0 and h.dinero==0:
                        print("ambos jugadores se han quedado sin dinero asi que se repartiran cartas a la mesa y se encontrar al ganador")
                        t.dibujarCarta(cm4,58,2)
                        t.dibujarCarta(cm5,68,2)
                        cm=[cm1,cm2,cm3,cm4,cm5]
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=(bote_medio)+1
                                h.dinero+=bote_medio
                            else:
                                r.dinero+=(bote_medio)
                                h.dinero+=bote_medio
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                    elif r.dinero<=0:
                        print("Has dejado al robot sin dinero asi que ya no se puede jugar")
                        z+=1
                        break
                    elif h.dinero==0:
                        print("Te has quedado sin dinero asi que ya no podras jugar")
                        z+=1
                        break
                    if apuesta_robot>h.dinero:
                        print("Tu saldo es menor que la apuesta del robot, has perdido")
                        r.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            x=0
                            while x==0:
                                y=0
                                while y==0:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                y+=1
                                                x+=1
                                                z+=1
                                                break
                                            else:
                                                y+=1
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            y+=1
                                            x+=1
                                    if p=="no":
                                        print("Hasta luego")
                                        y+=1
                                        x+=1
                                        z+=1
                                        break
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>h.dinero or apuesta_humano<apuesta_robot:
                        if apuesta_humano>h.dinero:
                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                        elif apuesta_humano<apuesta_robot:
                            apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                    if apuesta_humano>r.dinero:
                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                        h.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            x=0
                            while x==0:
                                y=0
                                while y==0:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                y+=1
                                                x+=1
                                                z+=1
                                                break
                                            else:
                                                y+=1
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            y+=1
                                            x+=1
                                    if p=="no":
                                        print("Hasta luego")
                                        y+=1
                                        x+=1
                                        z+=1
                    else:
                        bote+=apuesta_humano
                        h.dinero-=apuesta_humano
                        t.borrarZona(9,18,5,1)
                        t.borrarZona(34,18,5,1)
                        t.escribirMensaje("Bote: "+str(bote),0,4)
                        t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
                        t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                        t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                        i+=1
                elif i==2:
                    bote+=apuesta_robot
                    r.dinero-=apuesta_robot
                    print("El robot iguala")
                    t.dibujarCarta(cm4,58,2)
                    t.borrarZona(9,18,5,1)
                    t.borrarZona(34,18,5,1)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                    t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                    cm=[cm1,cm2,cm3,cm4]
                    print(t)
                    if r.dinero==0 and h.dinero==0:
                        print("ambos jugadores se han quedado sin dinero asi que se repartiran las cartas para decidir al ganador")
                        t.dibujarCarta(cm5,68,2)
                        cm=[cm1,cm2,cm3,cm4,cm5]
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=(bote_medio)+1
                                h.dinero+=bote_medio
                            else:
                                r.dinero+=(bote_medio)
                                h.dinero+=bote_medio
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                    elif r.dinero<=0:
                        print("Has dejado al robot sin dinero asi que ya no se puede jugar")
                        z+=1
                        break
                    elif h.dinero==0:
                        print("Te has quedado sin dinero asi que ya no podras jugar")
                        z+=1
                        break
                    if apuesta_robot>h.dinero:
                        print("Tu saldo es menor que la apuesta del robot, has perdido")
                        r.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            x=0
                            while x==0:
                                y=0
                                while y==0:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                y+=1
                                                x+=1
                                                z+=1
                                                break
                                            else:
                                                y+=1
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            y+=1
                                            x+=1
                                    if p=="no":
                                        print("Hasta luego")
                                        y+=1
                                        x+=1
                                        z+=1
                                        break
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>h.dinero or apuesta_humano<apuesta_robot:
                        if apuesta_humano>h.dinero:
                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                        elif apuesta_humano<apuesta_robot:
                            apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                    if apuesta_humano>r.dinero:
                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                        h.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            x=0
                            while x==0:
                                y=0
                                while y==0:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                y+=1
                                                x+=1
                                                z+=1
                                                break
                                            else:
                                                y+=1
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            y+=1
                                            x+=1
                                    if p=="no":
                                        print("Hasta luego")
                                        y+=1
                                        x+=1
                                        z+=1
                    else:
                        bote+=apuesta_humano
                        h.dinero-=apuesta_humano
                        t.borrarZona(9,18,5,1)
                        t.borrarZona(34,18,5,1)
                        t.escribirMensaje("Bote: "+str(bote),0,4)
                        t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
                        t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                        t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                        i+=1
                elif i==3:
                    bote+=apuesta_robot
                    r.dinero-=apuesta_robot
                    print("El robot iguala")
                    t.dibujarCarta(cm5,68,2)
                    t.borrarZona(9,18,5,1)
                    t.borrarZona(34,18,5,1)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                    t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                    cm=[cm1,cm2,cm3,cm4,cm5]
                    print(t)
                    if r.dinero==0 and h.dinero==0:
                        print("ambos jugadores se han quedado sin dinero asi que se repartiran las cartas para decidir al ganador")
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)+1
                            else:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                    elif r.dinero<=0:
                        print("Has dejado al robot sin dinero asi que ya no se puede jugar")
                        z+=1
                        break
                    elif h.dinero==0:
                        print("Te has quedado sin dinero asi que ya no podras jugar")
                        z+=1
                        break
                    if apuesta_robot>h.dinero:
                        print("Tu saldo es menor que la apuesta del robot, has perdido")
                        r.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            x=0
                            while x==0:
                                y=0
                                while y==0:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                y+=1
                                                x+=1
                                                z+=1
                                                break
                                            else:
                                                y+=1
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            y+=1
                                            x+=1
                                    if p=="no":
                                        print("Hasta luego")
                                        y+=1
                                        x+=1
                                        z+=1
                                        break
                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                    while apuesta_humano>h.dinero or apuesta_humano<apuesta_robot:
                        if apuesta_humano>h.dinero:
                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                        elif apuesta_humano<apuesta_robot:
                            apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                    if apuesta_humano>r.dinero:
                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                        h.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            x=0
                            while x==0:
                                y=0
                                while y==0:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                y+=1
                                                x+=1
                                                z+=1
                                                break
                                            else:
                                                y+=1
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            y+=1
                                            x+=1
                                    if p=="no":
                                        print("Hasta luego")
                                        y+=1
                                        x+=1
                                        z+=1
                    else:
                        bote+=apuesta_humano
                        h.dinero-=apuesta_humano
                        t.borrarZona(9,18,5,1)
                        t.borrarZona(34,18,5,1)
                        t.escribirMensaje("Bote: "+str(bote),0,4)
                        t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
                        t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                        t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                        i+=1
            elif apuesta_robot>apuesta_humano:
                bote+=apuesta_robot
                r.dinero-=apuesta_robot
                print("el robot ha aumentado la apuesta ")
                t.borrarZona(9,18,5,1)
                t.borrarZona(34,18,5,1)
                t.escribirMensaje("Bote: "+str(bote),0,4)
                t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                print(t)
                if r.dinero<=0 and h.dinero==0:
                    print("ambos jugadores se han quedado sin dinero asi que se repartiran las cartas para decidir al ganador")
                    if len(cm)==0:
                        t.dibujarCarta(cm1,28,2)
                        t.dibujarCarta(cm2,38,2)
                        t.dibujarCarta(cm3,48,2)
                        t.dibujarCarta(cm4,58,2)
                        t.dibujarCarta(cm5,68,2)
                        cm=[cm1,cm2,cm3,cm4,cm5]
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)+1
                            else:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                    elif len(cm)==3:
                        t.dibujarCarta(cm4,58,2)
                        t.dibujarCarta(cm5,68,2)
                        cm=[cm1,cm2,cm3,cm4,cm5]
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)+1
                            else:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                    elif len(cm)==4:
                        t.dibujarCarta(cm5,68,2)
                        cm=[cm1,cm2,cm3,cm4,cm5]
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)+1
                            else:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                    elif len(cm)==5:
                        cm=[cm1,cm2,cm3,cm4,cm5]
                        final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                        cr1.definirEstado("visible")
                        cr2.definirEstado("visible")
                        t.dibujarCarta(cr1,28,11)
                        t.dibujarCarta(cr2,38,11)
                        if final=="empate":
                            print(t)
                            print("Ha sido un empate")
                            bote_medio=bote//2
                            bote-=2*bote_medio
                            if bote==1:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)+1
                            else:
                                r.dinero+=bote_medio
                                h.dinero+=(bote_medio)
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                                            break
                        elif final=="gana_humano":
                            print(t)
                            print("¡Felicidades has ganado!")
                            break
                        elif final=="gana_robot":
                            print(t)
                            print("Lo sentimos ha ganado el robot")
                            break
                elif r.dinero==0:
                    print("Has dejado al robot sin dinero asi que ya no se puede jugar")
                    z+=1
                    break
                elif h.dinero==0:
                    print("Te has quedado sin dinero asi que ya no podras jugar")
                    z+=1
                    break
                elif h.dinero<apuesta_robot:
                    print("Tu dinero es inferior a la apuesta del robot, asi que has perdido")
                    r.dinero+=bote
                    if h.dinero<10:
                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                        z+=1
                        break
                    else:
                        p=input("¿Quieres volver a jugar?(si/no): ")
                        if p=="si":
                            i=1
                            t.borrarTablero()
                            b=Baraja()
                            b.barajar()
                            bote=0
                            apuesta_robot=0
                            cm=[]
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
                            t.escribirMensaje("$"+str(h.dinero),9,18)
                            t.escribirMensaje("$"+str(r.dinero),34,18)
                            t.escribirMensaje("Mesa",51,1)
                            t.escribirMensaje("Jugador 0",7,10)
                            t.escribirMensaje("Jugador 1",33,10)
                            print(t)
                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                            while apuesta_humano>h.dinero:
                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                            if apuesta_humano>r.dinero:
                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                h.dinero+=bote
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    z+=1
                                    break
                                else:
                                    x=0
                                    while x==0:
                                        y=0
                                        while y==0:
                                            p=input("¿Quieres volver a jugar?(si/no): ")
                                            if p=="si":
                                                i=1
                                                t.borrarTablero()
                                                b=Baraja()
                                                b.barajar()
                                                bote=0
                                                apuesta_robot=0
                                                cm=[]
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
                                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                                t.escribirMensaje("Mesa",51,1)
                                                t.escribirMensaje("Jugador 0",7,10)
                                                t.escribirMensaje("Jugador 1",33,10)
                                                print(t)
                                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                while apuesta_humano>h.dinero:
                                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                if apuesta_humano>r.dinero:
                                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                    h.dinero+=bote
                                                    if h.dinero<10:
                                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                        y+=1
                                                        x+=1
                                                        z+=1
                                                        break
                                                    else:
                                                        y+=1
                                                else:
                                                    bote+=apuesta_humano
                                                    h.dinero-=apuesta_humano
                                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                    y+=1
                                                    x+=1
                                            if p=="no":
                                                print("Hasta luego")
                                                y+=1
                                                x+=1
                                                z+=1
                            bote+=apuesta_humano
                            h.dinero-=apuesta_humano
                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                        if p=="no":
                                print("Hasta luego")
                                z+=1
                else:
                    p1=input("¿Que desea hacer?(retirar,igualar o aumentar): ")
                    if p1=="retirar":
                        r.dinero+=bote
                        print("Se ha rendido, suerte para la proxima")
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            break
                        else:
                            p=input("¿Quieres volver a jugar?(si/no): ")
                            if p=="si":
                                i=1
                                t.borrarTablero()
                                b=Baraja()
                                b.barajar()
                                bote=0
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
                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                t.escribirMensaje("Mesa",51,1)
                                t.escribirMensaje("Jugador 0",7,10)
                                t.escribirMensaje("Jugador 1",33,10)
                                print(t)
                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                while apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                if apuesta_humano>r.dinero:
                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                    h.dinero+=bote
                                    if h.dinero<10:
                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                        z+=1
                                        break
                                    else:
                                        x=0
                                        while x==0:
                                            y=0
                                            while y==0:
                                                p=input("¿Quieres volver a jugar?(si/no): ")
                                                if p=="si":
                                                    i=1
                                                    t.borrarTablero()
                                                    b=Baraja()
                                                    b.barajar()
                                                    bote=0
                                                    apuesta_robot=0
                                                    cm=[]
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
                                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                                    t.escribirMensaje("Mesa",51,1)
                                                    t.escribirMensaje("Jugador 0",7,10)
                                                    t.escribirMensaje("Jugador 1",33,10)
                                                    print(t)
                                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                    while apuesta_humano>h.dinero:
                                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                    if apuesta_humano>r.dinero:
                                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                        h.dinero+=bote
                                                        if h.dinero<10:
                                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            break
                                                        else:
                                                            y+=1
                                                    else:
                                                        bote+=apuesta_humano
                                                        h.dinero-=apuesta_humano
                                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                        y+=1
                                                        x+=1
                                                if p=="no":
                                                    print("Hasta luego")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                bote+=apuesta_humano
                                h.dinero-=apuesta_humano
                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                            if p=="no":
                                print("Hasta luego")
                                z+=1
                    elif p1=="igualar":
                        if i==1:
                            bote+=apuesta_robot
                            h.dinero-=apuesta_robot
                            t.dibujarCarta(cm1,28,2)
                            t.dibujarCarta(cm2,38,2)
                            t.dibujarCarta(cm3,48,2)
                            t.borrarZona(9,18,5,1)
                            t.borrarZona(34,18,5,1)
                            t.escribirMensaje("Bote: "+str(bote),0,4)
                            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                            t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                            t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                            cm=[cm1,cm2,cm3]
                            print(t)
                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                            while apuesta_humano>h.dinero or apuesta_humano<apuesta_robot:
                                if apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                elif apuesta_humano<apuesta_robot:
                                    apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                            if apuesta_humano>r.dinero:
                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                h.dinero+=bote
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    z+=1
                                    break
                                else:
                                    x=0
                                    while x==0:
                                        y=0
                                        while y==0:
                                            p=input("¿Quieres volver a jugar?(si/no): ")
                                            if p=="si":
                                                i=1
                                                t.borrarTablero()
                                                b=Baraja()
                                                b.barajar()
                                                bote=0
                                                apuesta_robot=0
                                                cm=[]
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
                                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                                t.escribirMensaje("Mesa",51,1)
                                                t.escribirMensaje("Jugador 0",7,10)
                                                t.escribirMensaje("Jugador 1",33,10)
                                                print(t)
                                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                while apuesta_humano>h.dinero:
                                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                if apuesta_humano>r.dinero:
                                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                    h.dinero+=bote
                                                    if h.dinero<10:
                                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                        y+=1
                                                        x+=1
                                                        z+=1
                                                        break
                                                    else:
                                                        y+=1
                                                else:
                                                    bote+=apuesta_humano
                                                    h.dinero-=apuesta_humano
                                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                    y+=1
                                                    x+=1
                                            if p=="no":
                                                print("Hasta luego")
                                                y+=1
                                                x+=1
                                                z+=1
                            bote+=apuesta_humano
                            h.dinero-=apuesta_humano
                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                            i+=1
                        elif i==2:
                            bote+=apuesta_robot
                            h.dinero-=apuesta_robot
                            t.dibujarCarta(cm4,58,2)
                            t.borrarZona(9,18,5,1)
                            t.borrarZona(34,18,5,1)
                            t.escribirMensaje("Bote: "+str(bote),0,4)
                            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                            t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                            t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                            cm=[cm1,cm2,cm3,cm4]
                            print(t)
                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                            while apuesta_humano>h.dinero or apuesta_humano<apuesta_robot:
                                if apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                elif apuesta_humano<apuesta_robot:
                                    apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                            if apuesta_humano>r.dinero:
                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                h.dinero+=bote
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    z+=1
                                    break
                                else:
                                    x=0
                                    while x==0:
                                        y=0
                                        while y==0:
                                            p=input("¿Quieres volver a jugar?(si/no): ")
                                            if p=="si":
                                                i=1
                                                t.borrarTablero()
                                                b=Baraja()
                                                b.barajar()
                                                bote=0
                                                apuesta_robot=0
                                                cm=[]
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
                                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                                t.escribirMensaje("Mesa",51,1)
                                                t.escribirMensaje("Jugador 0",7,10)
                                                t.escribirMensaje("Jugador 1",33,10)
                                                print(t)
                                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                while apuesta_humano>h.dinero:
                                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                if apuesta_humano>r.dinero:
                                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                    h.dinero+=bote
                                                    if h.dinero<10:
                                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                        y+=1
                                                        x+=1
                                                        z+=1
                                                        break
                                                    else:
                                                        y+=1
                                                else:
                                                    bote+=apuesta_humano
                                                    h.dinero-=apuesta_humano
                                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                    y+=1
                                                    x+=1
                                            if p=="no":
                                                print("Hasta luego")
                                                y+=1
                                                x+=1
                                                z+=1
                            bote+=apuesta_humano
                            h.dinero-=apuesta_humano
                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                            i+=1
                        elif i==3:
                            bote+=apuesta_robot
                            h.dinero-=apuesta_robot
                            t.dibujarCarta(cm5,68,2)
                            t.borrarZona(9,18,5,1)
                            t.borrarZona(34,18,5,1)
                            t.escribirMensaje("Bote: "+str(bote),0,4)
                            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                            t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                            t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                            cm=[cm1,cm2,cm3,cm4,cm5]
                            print(t)
                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                            while apuesta_humano>h.dinero or apuesta_humano<apuesta_robot:
                                if apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                elif apuesta_humano<apuesta_robot:
                                    apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                            if apuesta_humano>r.dinero:
                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                h.dinero+=bote
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    z+=1
                                    break
                                else:
                                    x=0
                                    while x==0:
                                        y=0
                                        while y==0:
                                            p=input("¿Quieres volver a jugar?(si/no): ")
                                            if p=="si":
                                                i=1
                                                t.borrarTablero()
                                                b=Baraja()
                                                b.barajar()
                                                bote=0
                                                apuesta_robot=0
                                                cm=[]
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
                                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                                t.escribirMensaje("Mesa",51,1)
                                                t.escribirMensaje("Jugador 0",7,10)
                                                t.escribirMensaje("Jugador 1",33,10)
                                                print(t)
                                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                while apuesta_humano>h.dinero:
                                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                if apuesta_humano>r.dinero:
                                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                    h.dinero+=bote
                                                    if h.dinero<10:
                                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                        y+=1
                                                        x+=1
                                                        z+=1
                                                        break
                                                    else:
                                                        y+=1
                                                else:
                                                    bote+=apuesta_humano
                                                    h.dinero-=apuesta_humano
                                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                    y+=1
                                                    x+=1
                                            if p=="no":
                                                print("Hasta luego")
                                                y+=1
                                                x+=1
                                                z+=1
                            bote+=apuesta_humano
                            h.dinero-=apuesta_humano
                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                            i+=1
                    if p1=="aumentar":
                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                        while apuesta_humano>h.dinero or apuesta_humano<=apuesta_robot:
                            if apuesta_humano>h.dinero:
                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                            elif apuesta_humano<apuesta_robot:
                                apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                            elif apuesta_humano==apuesta_robot:
                                apuesta_humano=int(input("Su apuesta es igual a la apuesta actual asi que ingrese otra: "))
                        if apuesta_humano>r.dinero:
                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                            h.dinero+=bote
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                z+=1
                                break
                            else:
                                x=0
                                while x==0:
                                    y=0
                                    while y==0:
                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                        if p=="si":
                                            i=1
                                            t.borrarTablero()
                                            b=Baraja()
                                            b.barajar()
                                            bote=0
                                            apuesta_robot=0
                                            cm=[]
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
                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                            t.escribirMensaje("Mesa",51,1)
                                            t.escribirMensaje("Jugador 0",7,10)
                                            t.escribirMensaje("Jugador 1",33,10)
                                            print(t)
                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                            while apuesta_humano>h.dinero:
                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                            if apuesta_humano>r.dinero:
                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                h.dinero+=bote
                                                if h.dinero<10:
                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    break
                                                else:
                                                    y+=1
                                            else:
                                                bote+=apuesta_humano
                                                h.dinero-=apuesta_humano
                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                y+=1
                                                x+=1
                                        if p=="no":
                                            print("Hasta luego")
                                            y+=1
                                            x+=1
                                            z+=1
                        h.dinero-=apuesta_humano
                        bote+=apuesta_humano
                        t.borrarZona(9,18,5,1)
                        t.borrarZona(34,18,5,1)
                        t.escribirMensaje("Bote: "+str(bote),0,4)
                        t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
                        t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                        t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
            while len(cm)==5:
                if apuesta_robot==0:
                    print("El robot se a retirado asi que tu ganaste")
                    h.dinero+=bote
                    if h.dinero<10:
                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                        cm=[]
                        z+=1
                        break
                    else:
                        x=0
                        while x==0:
                            y=0
                            while y==0:
                                p=input("¿Quieres volver a jugar?(si/no): ")
                                if p=="si":
                                    i=1
                                    t.borrarTablero()
                                    b=Baraja()
                                    b.barajar()
                                    bote=0
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
                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                    t.escribirMensaje("Mesa",51,1)
                                    t.escribirMensaje("Jugador 0",7,10)
                                    t.escribirMensaje("Jugador 1",33,10)
                                    print(t)
                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                    while apuesta_humano>h.dinero:
                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                    if apuesta_humano>r.dinero:
                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                        h.dinero+=bote
                                        if h.dinero<10:
                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                            y+=1
                                            x+=1
                                            z+=1
                                            cm=[]
                                            break
                                        else:
                                            y+=1
                                    else:
                                        bote+=apuesta_humano
                                        h.dinero-=apuesta_humano
                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                        y+=1
                                        x+=1
                                        cm=[]
                                if p=="no":
                                    print("Hasta luego")
                                    y+=1
                                    x+=1
                                    z+=1
                                    cm=[]
                                    break
                elif apuesta_robot==apuesta_humano:
                    bote+=apuesta_robot
                    r.dinero-=apuesta_robot
                    print("El robot iguala")
                    t.borrarZona(9,18,5,1)
                    t.borrarZona(34,18,5,1)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                    t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                    print(t)
                    final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                    cr1.definirEstado("visible")
                    cr2.definirEstado("visible")
                    t.dibujarCarta(cr1,28,11)
                    t.dibujarCarta(cr2,38,11)
                    if final=="empate":
                        bote_medio=bote//2
                        bote-=2*bote_medio
                        if bote==1:
                            r.dinero+=bote_medio
                            h.dinero+=(bote_medio)+1
                        else:
                            r.dinero+=bote_medio
                            h.dinero+=(bote_medio)
                        print(t)
                        print("Ha sido un empate")
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            cm=[]
                            z+=1
                            break
                        else:
                            p=input("¿Quieres volver a jugar?(si/no): ")
                            if p=="si":
                                i=1
                                t.borrarTablero()
                                b=Baraja()
                                b.barajar()
                                bote=0
                                apuesta_robot=0
                                cm=[]
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
                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                t.escribirMensaje("Mesa",51,1)
                                t.escribirMensaje("Jugador 0",7,10)
                                t.escribirMensaje("Jugador 1",33,10)
                                print(t)
                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                while apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                if apuesta_humano>r.dinero:
                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                    h.dinero+=bote
                                    if h.dinero<10:
                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                        cm=[]
                                        z+=1
                                        break
                                    else:
                                        x=0
                                        while x==0:
                                            y=0
                                            while y==0:
                                                p=input("¿Quieres volver a jugar?(si/no): ")
                                                if p=="si":
                                                    i=1
                                                    t.borrarTablero()
                                                    b=Baraja()
                                                    b.barajar()
                                                    bote=0
                                                    apuesta_robot=0
                                                    cm=[]
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
                                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                                    t.escribirMensaje("Mesa",51,1)
                                                    t.escribirMensaje("Jugador 0",7,10)
                                                    t.escribirMensaje("Jugador 1",33,10)
                                                    print(t)
                                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                    while apuesta_humano>h.dinero:
                                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                    if apuesta_humano>r.dinero:
                                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                        h.dinero+=bote
                                                        if h.dinero<10:
                                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                                            break
                                                        else:
                                                            y+=1
                                                    else:
                                                        bote+=apuesta_humano
                                                        h.dinero-=apuesta_humano
                                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                        y+=1
                                                        x+=1
                                                        cm=[]
                                                if p=="no":
                                                    print("Hasta luego")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    cm=[]
                                                    break
                                else:
                                    bote+=apuesta_humano
                                    h.dinero-=apuesta_humano
                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                    cm=[]
                            if p=="no":
                                print("Hasta luego")
                                cm=[]
                                z+=1
                                break
                    elif final=="gana_humano":
                        h.dinero+=bote
                        print(t)
                        print("¡Felicidades has ganado!")
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            z+=1
                            cm=[]
                            break
                        else:
                            p=input("¿Quieres volver a jugar?(si/no): ")
                            if p=="si":
                                i=1
                                t.borrarTablero()
                                b=Baraja()
                                b.barajar()
                                bote=0
                                apuesta_robot=0
                                cm=[]
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
                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                t.escribirMensaje("Mesa",51,1)
                                t.escribirMensaje("Jugador 0",7,10)
                                t.escribirMensaje("Jugador 1",33,10)
                                print(t)
                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                while apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                if apuesta_humano>r.dinero:
                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                    h.dinero+=bote
                                    if h.dinero<10:
                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                        z+=1
                                        cm=[]
                                        break
                                    else:
                                        x=0
                                        while x==0:
                                            y=0
                                            while y==0:
                                                p=input("¿Quieres volver a jugar?(si/no): ")
                                                if p=="si":
                                                    i=1
                                                    t.borrarTablero()
                                                    b=Baraja()
                                                    b.barajar()
                                                    bote=0
                                                    apuesta_robot=0
                                                    cm=[]
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
                                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                                    t.escribirMensaje("Mesa",51,1)
                                                    t.escribirMensaje("Jugador 0",7,10)
                                                    t.escribirMensaje("Jugador 1",33,10)
                                                    print(t)
                                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                    while apuesta_humano>h.dinero:
                                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                    if apuesta_humano>r.dinero:
                                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                        h.dinero+=bote
                                                        if h.dinero<10:
                                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                                            break
                                                        else:
                                                            y+=1
                                                    else:
                                                        bote+=apuesta_humano
                                                        h.dinero-=apuesta_humano
                                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                        y+=1
                                                        x+=1
                                                        cm=[]
                                                if p=="no":
                                                    print("Hasta luego")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    cm=[]
                                else:
                                    bote+=apuesta_humano
                                    h.dinero-=apuesta_humano
                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                    cm=[]
                            if p=="no":
                                print("Hasta luego")
                                z+=1
                                cm=[]
                                break
                    elif final=="gana_robot":
                        r.dinero+=bote
                        print(t)
                        print("Lo sentimos ha ganado el robot")
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            cm=[]
                            z+=1
                            break
                        else:
                            p=input("¿Quieres volver a jugar?(si/no): ")
                            if p=="si":
                                i=1
                                t.borrarTablero()
                                b=Baraja()
                                b.barajar()
                                bote=0
                                apuesta_robot=0
                                cm=[]
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
                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                t.escribirMensaje("Mesa",51,1)
                                t.escribirMensaje("Jugador 0",7,10)
                                t.escribirMensaje("Jugador 1",33,10)
                                print(t)
                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                while apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                if apuesta_humano>r.dinero:
                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                    h.dinero+=bote
                                    if h.dinero<10:
                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                        z+=1
                                        cm=[]
                                        break
                                    else:
                                        x=0
                                        while x==0:
                                            y=0
                                            while y==0:
                                                p=input("¿Quieres volver a jugar?(si/no): ")
                                                if p=="si":
                                                    i=1
                                                    t.borrarTablero()
                                                    b=Baraja()
                                                    b.barajar()
                                                    bote=0
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
                                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                                    t.escribirMensaje("Mesa",51,1)
                                                    t.escribirMensaje("Jugador 0",7,10)
                                                    t.escribirMensaje("Jugador 1",33,10)
                                                    print(t)
                                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                    while apuesta_humano>h.dinero:
                                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                    if apuesta_humano>r.dinero:
                                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                        h.dinero+=bote
                                                        if h.dinero<10:
                                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                                            break
                                                        else:
                                                            y+=1
                                                    else:
                                                        bote+=apuesta_humano
                                                        h.dinero-=apuesta_humano
                                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                        y+=1
                                                        x+=1
                                                        cm=[]
                                                if p=="no":
                                                    print("Hasta luego")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    cm=[]
                                                    break
                                else:
                                    bote+=apuesta_humano
                                    h.dinero-=apuesta_humano
                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                    cm=[]
                            if p=="no":
                                print("Hasta luego")
                                cm=[]
                                z+=1
                                break
                elif apuesta_robot>apuesta_humano:
                    bote+=apuesta_robot
                    r.dinero-=apuesta_robot
                    print("el robot ha aumentado la apuesta ")
                    t.borrarZona(9,18,5,1)
                    t.borrarZona(34,18,5,1)
                    t.escribirMensaje("Bote: "+str(bote),0,4)
                    t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                    t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                    t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                    print(t)
                    if h.dinero<apuesta_robot:
                        print("Tu dinero es inferior a la apuesta del robot, asi que has perdido")
                        r.dinero+=bote
                        if h.dinero<10:
                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                            cm=[]
                            z+=1
                            break
                        else:
                            p=input("¿Quieres volver a jugar?(si/no): ")
                            if p=="si":
                                i=1
                                t.borrarTablero()
                                b=Baraja()
                                b.barajar()
                                bote=0
                                apuesta_robot=0
                                cm=[]
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
                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                t.escribirMensaje("Mesa",51,1)
                                t.escribirMensaje("Jugador 0",7,10)
                                t.escribirMensaje("Jugador 1",33,10)
                                print(t)
                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                while apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                if apuesta_humano>r.dinero:
                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                    h.dinero+=bote
                                    if h.dinero<10:
                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                        cm=[]
                                        z+=1
                                        break
                                    else:
                                        x=0
                                        while x==0:
                                            y=0
                                            while y==0:
                                                p=input("¿Quieres volver a jugar?(si/no): ")
                                                if p=="si":
                                                    i=1
                                                    t.borrarTablero()
                                                    b=Baraja()
                                                    b.barajar()
                                                    bote=0
                                                    apuesta_robot=0
                                                    cm=[]
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
                                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                                    t.escribirMensaje("Mesa",51,1)
                                                    t.escribirMensaje("Jugador 0",7,10)
                                                    t.escribirMensaje("Jugador 1",33,10)
                                                    print(t)
                                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                    while apuesta_humano>h.dinero:
                                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                    if apuesta_humano>r.dinero:
                                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                        h.dinero+=bote
                                                        if h.dinero<10:
                                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                                            break
                                                        else:
                                                            y+=1
                                                    else:
                                                        bote+=apuesta_humano
                                                        h.dinero-=apuesta_humano
                                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                        y+=1
                                                        x+=1
                                                        cm=[]
                                                if p=="no":
                                                    print("Hasta luego")
                                                    y+=1
                                                    x+=1
                                                    z+=1
                                                    cm=[]
                                                    break
                                else:
                                    bote+=apuesta_humano
                                    h.dinero-=apuesta_humano
                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                    cm=[]
                            if p=="no":
                                    print("Hasta luego")
                                    cm=[]
                                    z+=1
                                    break
                    else:
                        p1=input("¿Que desea hacer?(retirar,igualar o aumentar): ")
                        if p1=="retirar":
                            r.dinero+=bote
                            print("Se ha rendido, suerte para la proxima")
                            if h.dinero<10:
                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                cm=[]
                                z+=1
                                break
                            else:
                                p=input("¿Quieres volver a jugar?(si/no): ")
                                if p=="si":
                                    i=1
                                    t.borrarTablero()
                                    b=Baraja()
                                    b.barajar()
                                    bote=0
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
                                    t.escribirMensaje("$"+str(h.dinero),9,18)
                                    t.escribirMensaje("$"+str(r.dinero),34,18)
                                    t.escribirMensaje("Mesa",51,1)
                                    t.escribirMensaje("Jugador 0",7,10)
                                    t.escribirMensaje("Jugador 1",33,10)
                                    print(t)
                                    apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                    while apuesta_humano>h.dinero:
                                        apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                    if apuesta_humano>r.dinero:
                                        print("Tu apuesta es superior al dinero del robot, has ganado!")
                                        h.dinero+=bote
                                        if h.dinero<10:
                                            print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                            cm=[]
                                            z+=1
                                            break
                                        else:
                                            x=0
                                            while x==0:
                                                y=0
                                                while y==0:
                                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                                    if p=="si":
                                                        i=1
                                                        t.borrarTablero()
                                                        b=Baraja()
                                                        b.barajar()
                                                        bote=0
                                                        apuesta_robot=0
                                                        cm=[]
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
                                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                                        t.escribirMensaje("Mesa",51,1)
                                                        t.escribirMensaje("Jugador 0",7,10)
                                                        t.escribirMensaje("Jugador 1",33,10)
                                                        print(t)
                                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                        while apuesta_humano>h.dinero:
                                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                        if apuesta_humano>r.dinero:
                                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                            h.dinero+=bote
                                                            if h.dinero<10:
                                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                                y+=1
                                                                x+=1
                                                                z+=1
                                                                cm=[]
                                                                break
                                                            else:
                                                                y+=1
                                                        else:
                                                            bote+=apuesta_humano
                                                            h.dinero-=apuesta_humano
                                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                            y+=1
                                                            x+=1
                                                            cm=[]
                                                    if p=="no":
                                                        print("Hasta luego")
                                                        y+=1
                                                        x+=1
                                                        z+=1
                                                        cm=[]
                                    else:
                                        bote+=apuesta_humano
                                        h.dinero-=apuesta_humano
                                        apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                        cm=[]
                                if p=="no":
                                    print("Hasta luego")
                                    z+=1
                                    cm=[]
                                    break
                        elif p1=="igualar":
                            bote+=apuesta_robot
                            h.dinero-=apuesta_robot
                            t.borrarZona(9,18,5,1)
                            t.borrarZona(34,18,5,1)
                            t.escribirMensaje("Bote: "+str(bote),0,4)
                            t.escribirMensaje("Apuesta Actual: "+str(apuesta_robot),0,5)
                            t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                            t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                            print(t)
                            final=compararJugadas([ch1,ch2],[cr1,cr2],cm)
                            cr1.definirEstado("visible")
                            cr2.definirEstado("visible")
                            t.dibujarCarta(cr1,28,11)
                            t.dibujarCarta(cr2,38,11)
                            if final=="empate":
                                bote_medio=bote//2
                                bote-=2*bote_medio
                                if bote==1:
                                    r.dinero+=bote_medio
                                    h.dinero+=(bote_medio)+1
                                else:
                                    r.dinero+=bote_medio
                                    h.dinero+=(bote_medio)
                                print(t)
                                print("Ha sido un empate")
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    cm=[]
                                    z+=1
                                    break
                                else:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                cm=[]
                                                z+=1
                                                break
                                            else:
                                                x=0
                                                while x==0:
                                                    y=0
                                                    while y==0:
                                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                                        if p=="si":
                                                            i=1
                                                            t.borrarTablero()
                                                            b=Baraja()
                                                            b.barajar()
                                                            bote=0
                                                            apuesta_robot=0
                                                            cm=[]
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
                                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                                            t.escribirMensaje("Mesa",51,1)
                                                            t.escribirMensaje("Jugador 0",7,10)
                                                            t.escribirMensaje("Jugador 1",33,10)
                                                            print(t)
                                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                            while apuesta_humano>h.dinero:
                                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                            if apuesta_humano>r.dinero:
                                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                                h.dinero+=bote
                                                                if h.dinero<10:
                                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                                    y+=1
                                                                    x+=1
                                                                    z+=1
                                                                    cm=[]
                                                                    break
                                                                else:
                                                                    y+=1
                                                            else:
                                                                bote+=apuesta_humano
                                                                h.dinero-=apuesta_humano
                                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                                y+=1
                                                                x+=1
                                                                cm=[]
                                                        if p=="no":
                                                            print("Hasta luego")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                                            break
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            cm=[]
                                    if p=="no":
                                        print("Hasta luego")
                                        cm=[]
                                        z+=1
                                        break
                            elif final=="gana_humano":
                                h.dinero+=bote
                                print(t)
                                print("¡Felicidades has ganado!")
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    z+=1
                                    cm=[]
                                    break
                                else:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                z+=1
                                                cm=[]
                                                break
                                            else:
                                                x=0
                                                while x==0:
                                                    y=0
                                                    while y==0:
                                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                                        if p=="si":
                                                            i=1
                                                            t.borrarTablero()
                                                            b=Baraja()
                                                            b.barajar()
                                                            bote=0
                                                            apuesta_robot=0
                                                            cm=[]
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
                                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                                            t.escribirMensaje("Mesa",51,1)
                                                            t.escribirMensaje("Jugador 0",7,10)
                                                            t.escribirMensaje("Jugador 1",33,10)
                                                            print(t)
                                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                            while apuesta_humano>h.dinero:
                                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                            if apuesta_humano>r.dinero:
                                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                                h.dinero+=bote
                                                                if h.dinero<10:
                                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                                    y+=1
                                                                    x+=1
                                                                    z+=1
                                                                    cm=[]
                                                                    break
                                                                else:
                                                                    y+=1
                                                            else:
                                                                bote+=apuesta_humano
                                                                h.dinero-=apuesta_humano
                                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                                y+=1
                                                                x+=1
                                                                cm=[]
                                                        if p=="no":
                                                            print("Hasta luego")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            cm=[]
                                    if p=="no":
                                        print("Hasta luego")
                                        z+=1
                                        cm=[]
                                        break
                            elif final=="gana_robot":
                                r.dinero+=bote
                                print(t)
                                print("Lo sentimos ha ganado el robot")
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    cm=[]
                                    z+=1
                                    break
                                else:
                                    p=input("¿Quieres volver a jugar?(si/no): ")
                                    if p=="si":
                                        i=1
                                        t.borrarTablero()
                                        b=Baraja()
                                        b.barajar()
                                        bote=0
                                        apuesta_robot=0
                                        cm=[]
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
                                        t.escribirMensaje("$"+str(h.dinero),9,18)
                                        t.escribirMensaje("$"+str(r.dinero),34,18)
                                        t.escribirMensaje("Mesa",51,1)
                                        t.escribirMensaje("Jugador 0",7,10)
                                        t.escribirMensaje("Jugador 1",33,10)
                                        print(t)
                                        apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                        while apuesta_humano>h.dinero:
                                            apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                        if apuesta_humano>r.dinero:
                                            print("Tu apuesta es superior al dinero del robot, has ganado!")
                                            h.dinero+=bote
                                            if h.dinero<10:
                                                print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                z+=1
                                                cm=[]
                                                break
                                            else:
                                                x=0
                                                while x==0:
                                                    y=0
                                                    while y==0:
                                                        p=input("¿Quieres volver a jugar?(si/no): ")
                                                        if p=="si":
                                                            i=1
                                                            t.borrarTablero()
                                                            b=Baraja()
                                                            b.barajar()
                                                            bote=0
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
                                                            t.escribirMensaje("$"+str(h.dinero),9,18)
                                                            t.escribirMensaje("$"+str(r.dinero),34,18)
                                                            t.escribirMensaje("Mesa",51,1)
                                                            t.escribirMensaje("Jugador 0",7,10)
                                                            t.escribirMensaje("Jugador 1",33,10)
                                                            print(t)
                                                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                            while apuesta_humano>h.dinero:
                                                                apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                            if apuesta_humano>r.dinero:
                                                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                                h.dinero+=bote
                                                                if h.dinero<10:
                                                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                                    y+=1
                                                                    x+=1
                                                                    z+=1
                                                                    cm=[]
                                                                    break
                                                                else:
                                                                    y+=1
                                                            else:
                                                                bote+=apuesta_humano
                                                                h.dinero-=apuesta_humano
                                                                apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                                y+=1
                                                                x+=1
                                                                cm=[]
                                                        if p=="no":
                                                            print("Hasta luego")
                                                            y+=1
                                                            x+=1
                                                            z+=1
                                                            cm=[]
                                                            break
                                        else:
                                            bote+=apuesta_humano
                                            h.dinero-=apuesta_humano
                                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                            cm=[]
                                    if p=="no":
                                        print("Hasta luego")
                                        cm=[]
                                        z+=1
                                        break
                        elif p1=="aumentar":
                            apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                            while apuesta_humano>h.dinero or apuesta_humano<=apuesta_robot:
                                if apuesta_humano>h.dinero:
                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                elif apuesta_humano<apuesta_robot:
                                    apuesta_humano=int(input("Su apuesta es inferior a la apuesta actual asi que ingrese otra: "))
                                elif apuesta_humano==apuesta_robot:
                                    apuesta_humano=int(input("Su apuesta es igual a la apuesta actual asi que ingrese otra: "))
                            if apuesta_humano>r.dinero:
                                print("Tu apuesta es superior al dinero del robot, has ganado!")
                                h.dinero+=bote
                                if h.dinero<10:
                                    print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                    cm=[]
                                    z+=1
                                    break
                                else:
                                    x=0
                                    while x==0:
                                        y=0
                                        while y==0:
                                            p=input("¿Quieres volver a jugar?(si/no): ")
                                            if p=="si":
                                                i=1
                                                t.borrarTablero()
                                                b=Baraja()
                                                b.barajar()
                                                bote=0
                                                apuesta_robot=0
                                                cm=[]
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
                                                t.escribirMensaje("$"+str(h.dinero),9,18)
                                                t.escribirMensaje("$"+str(r.dinero),34,18)
                                                t.escribirMensaje("Mesa",51,1)
                                                t.escribirMensaje("Jugador 0",7,10)
                                                t.escribirMensaje("Jugador 1",33,10)
                                                print(t)
                                                apuesta_humano=int(input("su turno, ingrese una cantidad de apuesta: "))
                                                while apuesta_humano>h.dinero:
                                                    apuesta_humano=int(input("Su dinero es inferior a la apuesta asi que ingrese otra: "))
                                                if apuesta_humano>r.dinero:
                                                    print("Tu apuesta es superior al dinero del robot, has ganado!")
                                                    h.dinero+=bote
                                                    if h.dinero<10:
                                                        print("ya no puede seguir jugando porque su saldo es inferior a $10")
                                                        y+=1
                                                        x+=1
                                                        z+=1
                                                        cm=[]
                                                        break
                                                    else:
                                                        y+=1
                                                else:
                                                    bote+=apuesta_humano
                                                    h.dinero-=apuesta_humano
                                                    apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
                                                    y+=1
                                                    x+=1
                                                    cm=[]
                                            if p=="no":
                                                print("Hasta luego")
                                                y+=1
                                                x+=1
                                                z+=1
                                                cm=[]
                                                break
                            h.dinero-=apuesta_humano
                            bote+=apuesta_humano
                            t.borrarZona(9,18,5,1)
                            t.borrarZona(34,18,5,1)
                            t.escribirMensaje("Bote: "+str(bote),0,4)
                            t.escribirMensaje("Apuesta Actual: "+str(apuesta_humano),0,5)
                            t.escribirMensaje("$"+str(h.dinero)+" ",9,18)
                            t.escribirMensaje("$"+str(r.dinero)+" ",34,18)
                            apuesta_robot=obtenerApuestaRobot([cr1,cr2],cm,r.dinero,apuesta_robot,apuesta_humano)
jugador_0=Jugador("h")
jugador_1=Jugador("r")
Poker=ControlJuego()
Poker.Juego(jugador_0,jugador_1)



