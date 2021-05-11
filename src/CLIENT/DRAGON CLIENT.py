import sys
import playsound
from socket import *
import threading
from playsound import playsound
import banner
from rich.console import Console
import sendtoserver
import recivefromserver

#specific console = Console()
console = Console()

#create variable coll FLAG
FLAG=False


#create the main funcion 
def main():
    #create a list of threads
    threads=[]
    #specific the HOST where the client needs to connect
    HOST="192.168.5.14"
    #specific the PORT where the client can liste
    PORT=5555
    
    #create the socket
    clientSocket=socket(AF_INET,SOCK_STREAM)
    
    #coonect the socket to the server
    clientSocket.connect((HOST,PORT))
    
    #print the dragon head
    banner
    
    #create the target of the thread 
    recv=recivefromserver.recv_from_server
    send=sendtoserver.send_to_server
    
    
    
    #print the initial message
    console.print(f"[bold green][SISTEM] Il client si sta connetendo a un server![/bold green]")
    
    #playsound("1234.wav")-->if you want to play sound when the sistem is running
    
    
    #print the seconds message
    console.print(f"[bold green][SISTEM] Il client si è connesso a un server![/bold green]")
    
    #create the thread and start it
    t_send=threading.Thread(target=send,args=(clientSocket,FLAG))
    t_rcv=threading.Thread(target=recv,args=(clientSocket,FLAG,))
    threads.append(t_send)
    threads.append(t_rcv)
    t_send.start()
    t_rcv.start()
    t_send.join()
    t_rcv.join()
    
    #closing connection
    sys.exit()
    
    #start the programm
if __name__=="__main__":
    main()
