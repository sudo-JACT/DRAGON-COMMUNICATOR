def send_to_server(clsock,FLAG):
   
    while True:
        if FLAG==True:
            break
        send_msg=input("")
        clsock.sendall(send_msg.encode())  #-->encode the message and sent it to server