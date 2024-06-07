--Statement Autor
CREATE TABLE autor(
                    AUTOR_ID            INTEGER          PRIMARY KEY,
                    NACIONALIDAD        VARCHAR2(40)     NOT NULL,
                    EDAD                INTEGER          NOT NULL,
                    CORREO              VARCHAR2(40)     NOT NULL,
                    NOMBRE              VARCHAR2(40)     NOT NULL
                )
--Statement Libro
CREATE TABLE libro(
                    LIBRO_ID        INTEGER         PRIMARY KEY,
                    NOMBRE          VARCHAR2(40)     NOT NULL,
                    CALIFICACION    VARCHAR2(40)     NOT NULL,
                    PRECIO          NUMBER(32, 0)     NOT NULL,
                    EDITORIAL       VARCHAR2(40)     NOT NULL,
                    AUTOR_ID        INTEGER          NOT NULL,
                    CONTRAINT   autor_id_fk REFERENCES autor(autor_id)     
                )
