-- Active: 1731345075061@@localhost@3306@bdacademic_management
--SCRIPT SOFTWARE
CREATE DATABASE bdacademic_management;
USE bdacademic_management;

-- TABLES

--! IMPORTANTE:
-- TODO: VERIFICAR SI LAS TABLAS A CONTINUACION ESTAN BIEN DEFINIDAS Y SI SON TODAS O FALTAN ALGUNAS

-- COORDINATOR TABLE
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
    description TEXT,
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
    scoreRange DECIMAL(4,2),
    evaluation_criteria_id INT, -- Relación con evaluation_criteria
    FOREIGN KEY (evaluation_criteria_id) REFERENCES evaluation_criteria(id) ON DELETE CASCADE
);



