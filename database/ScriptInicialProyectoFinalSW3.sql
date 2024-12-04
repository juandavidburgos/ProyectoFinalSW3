-- SQLBook: Code
-- Active: 1731345075061@@localhost@3306@bdacademic_management
--SCRIPT SOFTWARE
CREATE DATABASE bdacademic_management;
USE bdacademic_management;
--! IMPORTANTE:
-- TODO: VERIFICAR SI LAS TABLAS A CONTINUACION ESTAN BIEN DEFINIDAS Y SI SON TODAS O FALTAN ALGUNAS

drop table if exists ASIG_COMP_DOCENTE;

drop table if exists RESULTAAP_RUBRICA;

drop table if exists TBL_ASIGNATURA;

drop table if exists TBL_COMPETENCIA;

drop table if exists TBL_CORDINADOR;

drop table if exists TBL_DOCENTE;

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
   ASIG_ID              int not null AUTO_INCREMENT,
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
   COMP_ID              int not null AUTO_INCREMENT,
   COMP_DESCRIPCION     varchar(250),
   COMP_TIPO            varchar(50),
   COMP_NIVEL           varchar(50),
   COMP_IDPROGRAMA      int,
   primary key (COMP_ID)
);

/*==============================================================*/
/* Table: TBL_CORDINADOR                                        */
/*==============================================================*/
create table TBL_CORDINADOR
(
   COR_ID               int not null AUTO_INCREMENT,
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
   DOC_ID               int not null AUTO_INCREMENT,
   DOC_TIPOIDENTIFICACION varchar(50),
   DOC_TIPODOCENTE      varchar(50),
   DOC_NOMBRES          varchar(100),
   DOC_APELLIDOS        varchar(100),
   DOC_IDENTIFICACION   varchar(100),
   DOC_TITULO           varchar(100),
   DOC_CORREO           varchar(100),
   DOC_ESTADO           varchar(50),
   primary key (DOC_ID)
);

/*==============================================================*/
/* Table: TBL_EVALUADOR                                         */
/*==============================================================*/
create table TBL_EVALUADOR
(
   EVA_ID               int not null AUTO_INCREMENT,
   EVA_TIPOIDENTIFICACION varchar(50),
   EVA_NOMBRE           varchar(100),
   EVA_APELLIDO         varchar(100),
   EVA_CORREO           varchar(100),
   EVA_IDENTIFICACION   varchar(100),
   primary key (EVA_ID)
);

/*==============================================================*/
/* Table: TBL_RA                                                */
/*==============================================================*/
create table TBL_RA
(
   RAP_ID               int not null AUTO_INCREMENT,
   COMP_ID              int not null,
   RAP_DESCRIPCION      varchar(250),
   primary key (RAP_ID)
);

/*==============================================================*/
/* Table: TBL_RUBRICA                                           */
/*==============================================================*/
create table TBL_RUBRICA
(
   IDRUBRICA            int not null AUTO_INCREMENT,
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

alter table TBL_COMPETENCIA add constraint FK_FK_COMPETENCIAPROGRAMA foreign key (COMP_IDASIGNATURA)
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table TBL_CORDINADOR add constraint FK_CORDINADOR_ASIGNATURA foreign key (ASIG_ID)
      references TBL_ASIGNATURA (ASIG_ID) on delete restrict on update restrict;

alter table TBL_CORDINADOR add constraint FK_CORDINADOR_COMPETENCIA foreign key (COMP_ID)
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table TBL_CORDINADOR add constraint FK_CORDINADOR_DOCENTE foreign key (DOC_ID)
      references TBL_DOCENTE (DOC_ID) on delete restrict on update restrict;

alter table TBL_RA add constraint FK_COMP_RA_PRO foreign key (COMP_ID)
      references TBL_COMPETENCIA (COMP_ID) on delete restrict on update restrict;

alter table TBL_RA add constraint FK_ASIG foreign key (ASIG_ID)
      references TBL_ASIGNATURA (ASIG_ID) on delete restrict on update restrict;

alter table TBL_RUBRICA add constraint FK_RUBRICA_EVALUADOR foreign key (EVA_ID)
      references TBL_EVALUADOR (EVA_ID) on delete restrict on update restrict;

----------------------------------------------------------------------------------------------------------
-- * Integración de tablas para las funcionalidades
ALTER TABLE TBL_RA
ADD RASIG_ID INT;

ALTER TABLE TBL_COMPETENCIA
CHANGE COLUMN COMP_IDPROGRAMA COMP_IDASIGNATURA int;


ALTER TABLE TBL_RA
DROP COLUMN RASIG_ID

ALTER TABLE TBL_CORDINADOR
DROP CONSTRAINT FK_CORDINADOR_DOCENTE;

ALTER TABLE TBL_CORDINADOR
DROP COLUMN  COMP_ID


ALTER TABLE TBL_COMPETENCIA 
DROP FOREIGN KEY FK_FK_COMPETENCIAPROGRAMA;

ALTER TABLE TBL_COMPETENCIA 
ADD CONSTRAINT FK_FK_COMPETENCIAPROGRAMA 
FOREIGN KEY (COMP_IDASIGNATURA) 
REFERENCES TBL_COMPETENCIA (COMP_ID)
ON DELETE CASCADE;
