import socket
import os
FLAGS = None
class SendSocket():

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def socket_send(self):
        current_size=0
        total_size=0
        data_send=0
        end=0

        file_name= input("Input your file name : ")

        self.socket.sendto(FLAGS.ip.encode(), (FLAGS.ip, FLAGS.port))#ip

        self.socket.sendto(file_name.encode(), (FLAGS.ip, FLAGS.port))#file_name

        print("File Transmit Start....")

        f = open(file_name, 'rb')

        total_size = os.path.getsize(file_name)
        self.socket.sendto(str(total_size).encode(), (FLAGS.ip, FLAGS.port))#size
        try:
            data = f.read(1024)
            while data:
                current_size += 1024
                if current_size>total_size:
                   current_size=total_size
                self.socket.sendto(str(current_size).encode(), (FLAGS.ip, FLAGS.port))#current_size  
                
                data_send += self.socket.sendto(data, (FLAGS.ip, FLAGS.port))#file
                
                s=str("current_size / total_size = "+str(current_size)+"/"+str(total_size)+","+ str((current_size/total_size)*100)+"%")
                print(s)
                self.socket.sendto(s.encode(), (FLAGS.ip, FLAGS.port))#current/total
                data = f.read(1024)

        except Exception as e:
               print(e)
        print("ok")
        print("file_send_end")      

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
