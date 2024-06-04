
carrito = {
    "libro_id":0,
    "nombre_libro":"",
    "nombre_autor": "",
    "autor_id":0,
    "calificacion":0.0,
    "precio":0.0,
    "editorial":""
}


def get_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]