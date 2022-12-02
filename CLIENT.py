#CLIENT ALPHABOT
#DiNicola Luca      Piumatto Gabriele

#Importazione librerie
import socket

def main():
    #creazione del socket utilizzando TCP e IPv4 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connessione all'alphabot
    s.connect(("192.168.0.131",5000))
    print("COMANDI  f b l r s id")

    #in loop
    while True:
        #prende in input uno dei comandi prima elencati + , + un tempo in secondi
        #nel caso della scelta id il numero dopo la virgola indica l'indice del comando 
        #corrispondente del database
        comando = input("inserisci comando e tempo con vigola: ")
        #Invia al server le informazioni
        s.sendall("".join(comando).encode())

if __name__ == "__main__":
    main()