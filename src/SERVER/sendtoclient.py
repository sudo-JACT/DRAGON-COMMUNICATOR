import sys
import playsound
import sys
import playsound
from socket import *
import threading
from rich.console import Console

console = Console()

#create a function to send the message to client
def send_to_client(conn,addr,FLAG):
    
    try:
        while True:
            if FLAG==True:
                break
            send_msg=input("")
            #send to client to close the connection 
            if send_msg=="q":
                conn.send("q".encode())
                
                console.print(f"[bold red][WARNING!] CLOSING CONNECTION[/bold red]")
                console.print(f"[bold red][WARNING!] CONNECTION CLOSED[/bold red]")
                console.print(f"[bold red][WARNING!] QUITTED[/bold red]")
                conn.close()
                FLAG=True
                break
            conn.send(send_msg.encode())  #-->encode the message and send it to client
    except:
        conn.close()  #-->clos connection