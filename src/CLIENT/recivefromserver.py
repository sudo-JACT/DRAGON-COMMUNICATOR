from rich.console import Console

console = Console()

#create a function to recive the message from server
def recv_from_server(clsock,FLAG):
    
    while True:
        #decode the message
        data=clsock.recv(1024).decode()
        
        if data=="q":
            console.print(f"[bold red][WARNING!] CLOSING CONNECTION[/bold red]")
            console.print(f"[bold red][WARNING!] CONNECTION CLOSED[/bold red]")
            console.print(f"[bold red][WARNING!] QUITTED[/bold red]")
            FLAG==True
            break
        
        console.print(f"[bold blue][SERVER] [/bold blue]{data}")  #--> print the message
        
        #playsound("91011.wav")--> if you want to play sound when the message is recived