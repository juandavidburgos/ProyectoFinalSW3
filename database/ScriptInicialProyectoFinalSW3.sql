-- SQLBook: Code
-- Active: 1731345075061@@localhost@3306@bdacademic_management
--SCRIPT SOFTWARE
CREATE DATABASE bdacademic_management;
USE bdacademic_management;

DROP TABLE competence;
DROP TABLE coordinator;
DROP TABLE evaluation_criteria;
DROP TABLE evaluator;
DROP TABLE learning_outcome;
DROP TABLE performance_level;
DROP TABLE program;
DROP TABLE rubric;
DROP TABLE subject;
DROP TABLE teacher;
-- TABLES

--! IMPORTANTE:
-- TODO: VERIFICAR SI LAS TABLAS A CONTINUACION ESTAN BIEN DEFINIDAS Y SI SON TODAS O FALTAN ALGUNAS

drop table if exists ASIG_COMP_DOCENTE;

drop table if exists RESULTAAP_RUBRICA;

drop table if exists TBL_ASIGNATURA;

drop table if exists TBL_COMPETENCIA;

drop table if exists TBL_CORDINADOR;

drop table if exists TBL_DOCENTE;

drop index TBL_EVALUADOR_PK on TBL_EVALUADOR;

drop table if exists TBL_EVALUADOR;

drop table if exists TBL_RA;

drop table if exists TBL_RUBRICA;

/*==============================================================*/
/* Table: ASIG_COMP_DOCENTE                                     */
/*==============================================================*/
create table ASIG_COMP_DOCENTE
(
   ASIG_ID              int not null,
   DOC_ID               int not null,
   COMP_ID              int not null,
   PERIODO              varchar(20),
   primary key (ASIG_ID, DOC_ID, COMP_ID)
);

/*==============================================================*/
/* Table: RESULTAAP_RUBRICA                                     */
/*==============================================================*/
create table RESULTAAP_RUBRICA
(
   RAP_ID               int not null,
   IDRUBRICA            int not null,
   primary key (RAP_ID, IDRUBRICA)
);

/*==============================================================*/
/* Table: TBL_ASIGNATURA                                        */
/*==============================================================*/
create table TBL_ASIGNATURA
(
   ASIG_ID              int not null,
   ASIG_NOMBRE          varchar(100),
   ASIG_CREDITOS        int,
   ASIG_OBJETIVOS       varchar(500),
   ASIG_SEMESTRE        int,
   primary key (ASIG_ID)
);

/*==============================================================*/
/* Table: TBL_COMPETENCIA                                       */
/*==============================================================*/
create table TBL_COMPETENCIA
(
   COMP_ID              int not null,
   COMP_DESCRIPCION     varchar(250),
   COMP_TIPO            varchar(50),
   COMP_NIVEL           varchar(50),
   COMP_IDPROGRAMA      char(10),
   primary key (COMP_ID)
);

/*==============================================================*/
/* Table: TBL_CORDINADOR                                        */
/*==============================================================*/
create table TBL_CORDINADOR
(
   COR_ID               int not null,
   DOC_ID               int,
   ASIG_ID              int,
   COMP_ID              int,
   COR_TIPOIDENTIFICACION varchar(50),
   COR_NOMBRES          varchar(100),
   COR_APELLIDOS        varchar(100),
   COR_IDENTIFICACION   varchar(100),
   COR_CORREO           varchar(100),
   primary key (COR_ID)
);

/*==============================================================*/
/* Table: TBL_DOCENTE                                           */
/*==============================================================*/
create table TBL_DOCENTE
(
   DOC_ID               int not null,
   DOC_TIPOIDENTIFICACION varchar(50),
   DOC_TIPODOCENTE      varchar(50),
   DOC_NOMBRES          varchar(100),
   DOC_APELLIDOS        varchar(100),
   DOC_IDENTIFICACION   varchar(100),
   DOC_TITULO           varchar(100),
   primary key (DOC_ID)
);

/*==============================================================*/
/* Table: TBL_EVALUADOR                                         */
/*==============================================================*/
create table TBL_EVALUADOR
(
   EVA_ID               int not null,
   EVA_TIPOIDENTIFICACION varchar(50),
   EVA_NOMBRE           varchar(100),
   EVA_APELLIDO         varchar(100),
   EVA_CORREO           varchar(100),
   EVA_IDENTIFICACION   varchar(100),
   primary key (EVA_ID)
);

/*==============================================================*/
/* Index: TBL_EVALUADOR_PK                                      */
/*==============================================================*/
create unique index TBL_EVALUADOR_PK on TBL_EVALUADOR
(
   
);

/*==============================================================*/
/* Table: TBL_RA                                                */
/*==============================================================*/
create table TBL_RA
(
   RAP_ID               int not null,
   COMP_ID              int not null,
   RAP_DESCRIPCION      varchar(250),
   primary key (RAP_ID)
);

/*==============================================================*/
/* Table: TBL_RUBRICA                                           */
/*==============================================================*/
create table TBL_RUBRICA
(
   IDRUBRICA            int not null,
   EVA_ID               int,
   RUB_NOMBRE           varchar(100),
   RUB_NOTA             varchar(100),
   RUB_CRITERIODESC     varchar(100),
   RUB_NIVEL            varchar(100),
   primary key (IDRUBRICA)
);

alter table ASIG_COMP_DOCENTE add constraint FK_ASIG_COMP_DOCENTE foreign key (ASIG_ID)
      references TBL_ASIGNATURA (ASIG_ID) on delete restrict on update restrict;

alter table ASIG_COMP_DOCENTE add constraint FK_ASIG_COMP_DOCENTE2 foreign key (DOC_ID)
      references TBL_DOCENTE (DOC_ID) on delete restrict on update restrict;

alter table ASIG_COMP_DOCENTE add constraint FK_ASIG_COMP_DOCENTE3 foreign key (COMP_ID)
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table RESULTAAP_RUBRICA add constraint FK_RESULTAAP_RUBRICA foreign key (RAP_ID)
      references TBL_RA (RAP_ID) on delete restrict on update restrict;

alter table RESULTAAP_RUBRICA add constraint FK_RESULTAAP_RUBRICA2 foreign key (IDRUBRICA)
      references TBL_RUBRICA (IDRUBRICA) on delete restrict on update restrict;

alter table TBL_COMPETENCIA add constraint FK_FK_COMPETENCIAPROGRAMA foreign key ()
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table TBL_CORDINADOR add constraint FK_CORDINADOR_DOCENTE foreign key (DOC_ID)
      references TBL_DOCENTE (DOC_ID) on delete restrict on update restrict;

alter table TBL_CORDINADOR add constraint FK_REFERENCE_10 foreign key (ASIG_ID)
      references TBL_ASIGNATURA (ASIG_ID) on delete restrict on update restrict;

alter table TBL_CORDINADOR add constraint FK_REFERENCE_11 foreign key (COMP_ID)
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table TBL_RA add constraint FK_COMP_RA_PRO foreign key (COMP_ID)
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table TBL_RUBRICA add constraint FK_RUBRICA_EVALUADOR foreign key (EVA_ID)
      references TBL_EVALUADOR (EVA_ID) on delete restrict on update restrict;

----------------------------------------------------------------------------------------------------
/*-- COORDINATOR TABLE
CREATE TABLE coordinator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idType VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
    --? Como inlcuir la lista de competencias y de resultados de aprendizaje?
);

-- TEACHER TABLE
CREATE TABLE teacher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idType VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    teacherType ENUM('Catedra', 'Tiempo Completo', 'Planta') NOT NULL,
    academicDegree VARCHAR(100) NOT NULL,
    status ENUM('Activo', 'Inactivo') NOT NULL
);

-- EVALUATOR TABLE
CREATE TABLE evaluator (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idType VARCHAR(50) NOT NULL,
    name VARCHAR(100) NOT NULL,
    lastName VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- !REVISAR --------------------------------
-- TODO: SI EXISTE UNA TABLA PROGRAMAS?----
-- PROGRAM TABLE
CREATE TABLE program (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);
-- ! --------------------------------------

-- SUBJECT TABLE
CREATE TABLE subject (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,--Esta va?
    goals TEXT, 
    credits INT NOT NULL,
    semester INT NOT NULL,
    programId INT,
    FOREIGN KEY (programId) REFERENCES program(id) ON DELETE SET NULL
);

-- COMPETENCE TABLE
---? Como incluir la lista de resultados de aprendizaje?
-- ? sE INCLUYE?
CREATE TABLE competence (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    level ENUM('Basico', 'Intermedio', 'Avanzado') NOT NULL, 
    competenceType VARCHAR(100) NOT NULL
); 


--- LEARNING OUTCOME TABLE
CREATE TABLE learning_outcome (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    competence_id INT,  -- Relación con competence
    FOREIGN KEY (competence_id) REFERENCES competence(id) ON DELETE SET NULL
);

--- RUBRIC TABLE
---? Como poner la lista de CRITERIOS DE EVALUACION?
-- ? sE INCLUYE?
CREATE TABLE rubric(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    score DECIMAL(4,2) NOT NULL,
    evaluationId INT,
    FOREIGN KEY (evaluationId) REFERENCES evaluation_criteria(id)
)


--- EVALUATION CRITERIA TABLE
--? Como poner la lista de niveles de desempeño?
-- ? sE INCLUYE?
CREATE TABLE evaluation_criteria(
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    pond DECIMAL(4,2) NOT NULL
)
--- PERFORMANCE LEVEL TABLE
--? Como poner la lista de niveles de desempeño?
-- ? sE INCLUYE?
CREATE TABLE performance_level (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description TEXT,
    scoreRange DECIMAL(4,2), --Esta seria VARCHAR??
    evaluation_criteria_id INT, -- Relación con evaluation_criteria
    FOREIGN KEY (evaluation_criteria_id) REFERENCES evaluation_criteria(id) ON DELETE CASCADE
);
*/


