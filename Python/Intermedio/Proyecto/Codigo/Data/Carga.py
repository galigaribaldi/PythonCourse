"""
@author:
@date:
@description:
"""

import csv
import sqlite3
class CargaLibro():
    
    def leerDatos(self, ruta):
        listaFinal = []
        ##Lectura de datos
        with open(ruta) as autorDataFile:
            lectura = csv.reader(autorDataFile)
            for i in lectura:
                listaFinal.append(tuple(i))
        ##Limpieza
        listaFinal.pop(0)
        return listaFinal
    
    def crearTablaLibro(self):
        con = sqlite3.connect('Data/BaseProyecto.db')
        cursor = con.cursor()
        print("crear tabla libro")
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS libro(
                    LIBRO_ID        INTEGER         PRIMARY KEY,
                    NOMBRE          VARCHAR2(40)     NOT NULL,
                    CALIFICACION    VARCHAR2(40)     NOT NULL,
                    PRECIO          NUMBER(32, 0)     NOT NULL,
                    EDITORIAL       VARCHAR2(40)     NOT NULL,
                    AUTOR_ID        INTEGER          NOT NULL,
                    CONTRAINT   autor_id_fk REFERENCES autor(autor_id)     
                );''')
        except:
            print("Error")
        finally:
            con.close()
    def seleccionarDatosLibro(self):
        con = sqlite3.connect('Data/BaseProyecto.db')
        cursor = con.cursor()
        print("select a la tabla libro")
        try:
            for i in cursor.execute('SELECT * FROM libro;'):
                print(i)
            con.commit()
        except:
            print("Error")
        finally:
            con.close()        
        
    def cargarDatosLibro(self, tuplaCargar):
        con = sqlite3.connect('Data/BaseProyecto.db')
        cursor = con.cursor()
        for i in tuplaCargar:
            cursor.execute('INSERT INTO libro(libro_id, nombre, calificacion, precio, editorial, autor_id) VALUES(?, ?, ?, ?, ?, ?)', i)
        con.commit()
        con.close()

class CargaAutor():
    
    def leerDatosAutor(self, ruta):
        listaFinal = []
        ##Lectura de datos
        with open(ruta) as autorDataFile:
            lectura = csv.reader(autorDataFile)
            for i in lectura:
                listaFinal.append(tuple(i))
        ##Limpieza
        listaFinal.pop(0)
        return listaFinal

    def seleccionarDatosAutor(self):
        con = sqlite3.connect('Data/BaseProyecto.db')
        cursor = con.cursor()
        print("select a la tabla Autor")
        try:
            for i in cursor.execute('SELECT * FROM autor;'):
                print(i)
            con.commit()
        except:
            print("Error")
        finally:
            con.close()        

    def crearTablaAutor(self):
        con = sqlite3.connect('Data/BaseProyecto.db')
        cursor = con.cursor()
        print("crear tabla Autor")
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS autor(
                    AUTOR_ID            INTEGER          PRIMARY KEY,
                    NACIONALIDAD        VARCHAR2(40)     NOT NULL,
                    EDAD                INTEGER          NOT NULL,
                    CORREO              VARCHAR2(40)     NOT NULL,
                    NOMBRE              VARCHAR2(40)     NOT NULL
                );''')
            con.commit()
        except:
            print("Error")
        finally:
            con.close()

    def cargarDatosAutor(self, tuplaCargar):
        con = sqlite3.connect('Data/BaseProyecto.db')
        cursor = con.cursor()
        print("Cargar tabla autor con informacion")
        for i in tuplaCargar:
            cursor.execute('INSERT INTO autor(autor_id, nacionalidad, edad, correo, nombre) VALUES(?, ?, ?, ?, ?)', i)
        con.commit()
        con.close()