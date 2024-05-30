# Proyecto Intermedio

Objetivo: Reafirmar y corroborar los conocimientos aprendidos durante el curso intermedio de python.

## Temas a explorar (Básico)

- Control de Flujo
- Módulos
- Programación Orientada a objetos
- Documentación Básica



## Temas a explorar (intermedio):

- Excepciones
- Librerías WEB (SMTP)
- Lectura de Archivos (CSV)
- Almacenamiento de Datos (modelado de una BD)
- Entornos Virtuales
- Interfaz Gráfica (opcional)
- Expresiones Regulares (opcional)



## Desarrollo del Proyecto

Se hará una simulación acerca de una tienda de libros. El cual tendrá 2 roles, sus acciones se especificarán a continuación

- **Administrador**: Dichas operaciones se harán sobre la BD principal
  - Actualizar y cambiar libros y autores
  - Eliminar libros y autores
- **Cliente**: Tener en cuenta que las operaciones no se irán sobre la BD principal, si no sobre el carrito de compra
  - Comprar: Añadir al carrito para después comprar.
  - Eliminar: Quitar del carrito (si no hay ninguno, esta acción quedará no útil)

### Temática general

- Se podrá mandar correos a los autores cuando se compre un libro.

- La base de datos tendrá que tener 20 registros.

- El cliente y el administrador serán simulados a través de Sockets (cliente y servidor respectivamente)

- La base de datos deberá cargarse con el archivo CSV llamado LibroData.csv para la tabla libro.

- La base de datos deberá cargarse con el archivo CSV llamado AutorData.csv para la tabla autor.

- Todos los archivos del código deberán ir comentados con los 3 encabezados principales

  - ```python
    """
    @autor:
    @date:
    @description:
    """
    ```





### Temática específica (aspectos de programación)