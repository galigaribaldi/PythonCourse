import socket
import json
class Cliente():
    
    s = socket.socket()
    ip = "192.168.0.241"
    port = 9000
        
    def connectCliente(self):
        self.s.connect((self.ip, self.port))
        while True:
            mensaje = input("Mensaje || ")
            self.s.send(mensaje.encode())
            if mensaje == "adios":
                self.acabarSesion()
            respuesta = self.s.recv(1024).decode()
            print("Respuesta del servidor: ", respuesta)
    def comprar(self, carrito):
        pass
    
    def eliminar(self, carrito):
        pass
    
    def mantenerSesion(self):
        pass
    
    def acabarSesion(self):
        self.s.close()