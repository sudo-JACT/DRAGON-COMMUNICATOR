import playsound
import sys
import playsound
import sys
import playsound
from socket import *
import threading
from rich.console import Console

console = Console()


#create a function to recive the message from client
def recv_from_client(conn,addr,FLAG):
    
    try:
        
        while True:
            if FLAG==True:
                break
            #decode the message we have recived from client
            message=conn.recv(1024).decode()
            
            #if we recive a message to close the connection we send to client to close the connection
            if message=="q":
                conn.send("q".encode())
                console.print(f"[bold red][WARNING!] CLOSING CONNECTION[/bold red]")
                console.print(f"[bold red][WARNING!] CONNECTION CLOSED[/bold red]")
                console.print(f"[bold red][WARNING!] QUITTED[/bold red]")
                conn.close()
                FLAG=True
                break
        
            console.print(f"[bold blue][CLIENT] [/bold blue]{message}")   #-->print the message we have recived from client
            #playsound("5678.wav")--> if you want to play sound when the message is recived
    except:
        conn.close()  #-->clos connection
        
