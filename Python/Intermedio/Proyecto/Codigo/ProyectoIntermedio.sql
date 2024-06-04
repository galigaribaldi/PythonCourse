--
-- ER/Studio 8.0 SQL Code Generation
-- Company :      UNAM
-- Project :      ModeloIntermedio.DM1
-- Author :       galigaribaldi
--
-- Date Created : Friday, May 31, 2024 23:05:24
-- Target DBMS : Oracle 11g
--

-- 
-- TABLE: AUTOR 
--

CREATE TABLE AUTOR(
    AUTOR_ID        INTEGER     PRIMARY KEY,
    NACIONALIDAD    VARCHAR2(40)     NOT NULL,
    EDAD            INTEGER          NOT NULL,
    CORREO          VARCHAR2(40)     NOT NULL,
    NOMBRE          VARCHAR2(40)     NOT NULL
);

-- 
-- TABLE: LIBRO 
--

CREATE TABLE LIBRO(
    LIBRO_ID        INTEGER         PRIMARY KEY,
    CALIFICACION    VARCHAR2(40)     NOT NULL,
    PRECIO          NUMBER(32, 0)     NOT NULL,
    EDITORIAL       VARCHAR2(40)     NOT NULL,
    AUTOR_ID        VARCHAR2(40)     NOT NULL
);



-- 
-- TABLE: COMPRA 
--

CREATE TABLE COMPRA(
    COMPRA_ID    INTEGER          PRIMARY KEY,
    TICKET       VARCHAR2(40)     NOT NULL,
    FECHA        VARCHAR2(40)     NOT NULL,
    LIBRO_ID     INTEGER          NOT NULL
    CONSTRAINT LIBRO_ID_FK REFERENCES LIBRO(LIBRO_ID)
);

INSERT INTO libro(libro_id, nombre, calificacion, precio, editorial, autor_id) VALUES(?, ?, ?, ?, ?, ?)
INSERT INTO autor(autor_id, nacionalidad, edad, correo, nombre) VALUES(?, ?, ?, ?, ?)