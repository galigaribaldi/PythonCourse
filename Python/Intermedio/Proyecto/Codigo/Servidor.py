import socket

class Servidor():
    
    s = socket.socket()
    sesion = True
    conn = None
    ip = "192.168.0.241"
    port = 9000
        
    def connectServidor(self):
        self.s.bind((self.ip, self.port))
        self.s.listen(1)
        self.conn, addr = self.s.accept()
        print("Iniciando el servidor")
        print("Cliente conectado desde: ", addr[0], ": ", addr[1])
        while True:
            recibido = self.conn.recv(5000).decode()
            self.conn.send(input("Ingresa tu mensaje >> ").encode())
            if recibido == "adios":
                self.acabarSesion()
        
    def actualizar_libro(self):
        pass

    def actualizar_autor(self):
        pass
    
    def eliminar_libro(self):
        pass
    
    def eliminar_autor(self):
        pass

    def checar_compra(self):
        pass

    def anular_compra(self):
        pass

    def actualizar_compra(self):
        pass
    
    def acabarSesion(self):
        self.s.close()