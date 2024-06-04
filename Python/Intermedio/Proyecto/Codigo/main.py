from Data.Carga import CargaLibro
from Data.Carga import CargaAutor

#c = CargaLibro()
#listaDatos = c.leerDatos('Data/LibroData.csv')
#print(listaDatos)

d = CargaAutor()
listaAutor = d.leerDatos('Data/AutorData.csv')
print(listaAutor)
d.crearTablaAutor()
d.cargarDatosAutor(listaDatos)