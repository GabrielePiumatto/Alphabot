#SERVER ALPHABOT
#DiNicola Luca      Piumatto Gabriele

#Importazione librerie
import socket
import AlphaBot
import time
import sqlite3

#stabilisce la connessione con il database
con = sqlite3.connect("./TabellaRaspberryPi.db")
cur = con.cursor()
#variabile per gestire l'alphabot utilizzando la 
#libreria dedicata all'alphabot
alpha = AlphaBot.AlphaBot()

#funzione per ricevere i dati dal database ed interpretarli
def MovimentoDatabase(dato):
    #prende la stringa corrispondente all'id passato dal client
    res = cur.execute(f"SELECT Movimento FROM TABELLA_MOVIMENTI WHERE ID={dato}")
    #divide la stringa ogni volta che trova ';' in modo da ottenere
    #delle stringhe pronte per essere prese in input
    dati =str(res.fetchone()[0]).split(";")
    #scorre i dati
    for dato in dati:
        #divide la lettera dal numero
        dati = dato.split(",")
        #li stampa 
        print(dato,dati)
        #prende la lettera
        dizio[dati[0]]()
        #prende il numero trovato come il tempo 
        time.sleep(float(dati[1]))
        #ferma l'alphabot
        alpha.stop()
        #attende mezzo secondo
        time.sleep(0.5)

#dizionario dove vengono salvate le corrispondenze tra le lettere lette in input e i movimenti 
#utilizzando la libreria dell'alphabot
dizio = {"s": alpha.stop,"f":alpha.forward,"b":alpha.backward,"l":alpha.left,"r":alpha.right}
def main():
    #creazione del socket utilizzando TCP e IPv4 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #connessione al client
    s.bind(("0.0.0.0",5000))
    print("Sto ascoltando...")
    #mette il server in ascolto per ricevere comandi
    s.listen()
    connection,address = s.accept()
    #in loop
    while True:
        #riceve e stampa i dati ricevuti dal client
        dato = connection.recv(4096).decode().lower()
        print(dato)
        #controlla che sia presente la virgola 
        if "," in dato:
            #se si splitta il dato e lo esegue
            #tramite la funzione MovimentoDatabase()
            dati = dato.split(",")
            print("1")
            if dati[0]== "id":
                    print("2")
                    MovimentoDatabase(int(dati[1]))
            else:
                    dizio[dati[0]]()
                    time.sleep(float(dati[1]))
                    dizio["s"]()
        else:
                #se no ferma l'alphabot
                time.sleep(float(dati[1]))
                dizio["s"]()
    #chiusura socket
    s.close()
        
if __name__=="__main__":
    main()