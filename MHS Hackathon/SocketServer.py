import socket
import time
import MasterProgram
framerate = 1
HOST = ""   # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

print(socket.gethostname())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            #Download camera feed
            with open("Camerafeed.png", "wb") as file:
                while True:
                    data = conn.recv(8192)
                    if data == b"DONE":
                        print("done recieving.")
                        break
                    file.write(data)
                    print("Recieved load")

            #Run AI
            MasterProgram.analysePicture()
            time.sleep(1/5)

            #Upload the annotated output
            with open("annotatedoutput.png", "rb") as file:
                data = file.read(8192)
                while data:
                    conn.sendall(data)
                    print("sent a load")
                    data = file.read(8192)
                    time.sleep(1/5)
                conn.sendall(b"DONE")
                print("sent done")

            #Upload the prices document
            with open("prices.txt", "rb") as file:
                data = file.read(8192)
                while data:
                    conn.sendall(data)
                    print("sent a load")
                    data = file.read(8192)
                    time.sleep(1/5)
                conn.sendall(b"DONE")
                print("sent done")
            
            #Upload the items document
            with open("itemsrecognized.txt", "rb") as file:
                data = file.read(8192)
                while data:
                    conn.sendall(data)
                    print("sent a load")
                    data = file.read(8192)
                    time.sleep(1/5)
                conn.sendall(b"DONE")
                print("sent done")
            