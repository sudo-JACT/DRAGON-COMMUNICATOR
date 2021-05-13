from rich.console import Console
console = Console()

def send_to_server(clsock,FLAG):
   
    while True:
        if FLAG==True:
            break
        send_msg=console.input(f"[bold gray]CLIENT: [/bold gray]")
        clsock.sendall(send_msg.encode())  #-->encode the message and sent it to server
