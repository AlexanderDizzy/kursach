import struct
import PI
import PID
import socket

class Manager:
    def __init__(self):
        self.UDP_receive = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP_send = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = "127.0.0.1"
        self.addr_receive = (self.host, 25000)
        self.addr_send = (self.host, 25001)
        self.addr_snd = (self.host, 25002)
        self.UDP_receive.bind(self.addr_receive)
        self.T = 0.0001
        self.t = 0
        self.x1 = 0
        self.x2 = 0
        self.h = 0
        self.data_send = 0
        self.data_snd = 0
        self.data_matlab = 0
        self.pi_calc = PI.PI()
        self.pid_calc = PID.PID()
        self.f = open('f.csv', 'w')

    def send(self, data, addr):
        return self.UDP_send.sendto(data, addr)

    def kill_all(self):
        self.UDP_send.close()
        self.UDP_receive.close()
        self.f.close()


    def run(self):
        X = float(input("enter desire value: "))
        while True:
            data, addr = self.UDP_receive.recvfrom(1024)
            print("receiving...\n")
            self.data_matlab = struct.unpack('3d', data)
            self.t = self.data_matlab[0]
            self.x1 = self.data_matlab[1]
            self.x2 = self.data_matlab[2]
            self.h = self.t - self.T
            y1 = self.pi_calc.run(self.h, self.x1, X)
            y2 = self.pi_calc.run(self.h, self.x2, X)
            self.T = self.t

            self.data_send = struct.pack('d', y1)
            self.data_snd = struct.pack('d', y2)

            self.send(self.data_send, self.addr_send)
            self.send(self.data_snd, self.addr_snd)
            print('sending...\n')

            self.f.write(str(self.t) + ';' + str(self.x1) + ';' + str(self.x2) + '\n')

            if self.t == 4:
                break

        self.kill_all()