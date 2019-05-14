import socket
import os
FLAGS = None
class SendSocket():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def socket_send(self):
        total_size=0;
        current_size=0
        self.socket.bind(('',4000))
        data, addr =self.socket.recvfrom(2000)#ip
        print("file recv start from "+data.decode())
        data, addr =self.socket.recvfrom(2000)#file_name
        f = open(data, 'wb')
        print("File Name: "+data.decode())
        data, addr =self.socket.recvfrom(2000)#file_size
        total_size=data.decode()

        print("File Size: "+total_size)

        total_size=int(total_size)
        
        try:
            while current_size<total_size:
                data, addr =self.socket.recvfrom(2000)#current_size
                current_size=int(data.decode())

                data, addr =self.socket.recvfrom(2000)#file
                f.write(data)

                data, addr =self.socket.recvfrom(2000)#current/total
                print(data.decode())
                
                
        except Exception as e:
               print(e)

        
        

    def main(self):
        self.socket_send()
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--ip', type=str, default='localhost')

    parser.add_argument('-p', '--port', type=int, default=8080)



    FLAGS, _ = parser.parse_known_args()

    send_socket = SendSocket()
    send_socket.main()
