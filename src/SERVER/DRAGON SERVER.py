import sys
import playsound
from socket import *
import threading
from playsound import playsound
import banner
import sendtoclient
import recivefromclient
from rich.console import Console

#specific console = Console()
console = Console()

#create variable coll FLAG
FLAG=False


#create the main function
def main():
    #create a list of threads
    threads=[]
    #specific FLAG is global
    global FLAG
    
    #specific the HOST where the server is running
    HOST="192.168.5.14"
    
    #specific the PORT where the server is listening
    serverPort=5555
    
    #create the socket and bind it to the server address and port
    serverSocket=socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((HOST,serverPort))
    
    #open the connection
    serverSocket.listen(1)
    
    
    #print the dragon head
    banner     
    
        
    #print the initial message
    console.print(f"[bold green][SISTEM] The server is connecting with a client[/bold green]")
    
    #playsound("1234.wav")-->if you want to play sound when the sistem is running
    
    #accept the connection
    connectinSocket, addr=serverSocket.accept()
    
    #print the seconds message
    console.print(f"[bold green][SISTEM] The server is connected with a client\n[/bold green]")
    
    
    #create the target of the thread and start the thread
    send=sendtoclient.send_to_client
    recive=recivefromclient.recv_from_client
    
    
    t_rcv=threading.Thread(target=recive,args=(connectinSocket,addr,FLAG))
    t_send=threading.Thread(target=send,args=(connectinSocket,addr,FLAG))
    
    #append to the list of threads
    threads.append(t_rcv)
    threads.append(t_send)
    
    #start the thread
    t_rcv.start()
    t_send.start()
    
    
    t_rcv.join()
    t_send.join()
    
    #closing the connection
    serverSocket.close()
    
    sys.exit()
    
    #start the program 
if __name__=="__main__":
    main()
    
