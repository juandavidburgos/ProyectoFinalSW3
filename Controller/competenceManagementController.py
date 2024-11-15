
from flask import jsonify, request
from Model.connection import Connection
from Model.competence import competence

#class CompetenciaController:
class competenceManagementController:
    def __init__(self, app):
        # Inicializar la conexión a la base de datos usando la clase Connection
        self.mysql = Connection.init_database(app)

    def create_competence(self):
        """Crear una nueva competencia (de programa o de asignatura)"""
        data = request.json
        description = data.get("description")
        type_ = data.get("type")
        level = data.get("level")
        parent_id = data.get("parent_id", None)  # Este valor es opcional

        # Insertar competencia en la base de datos
        cursor = self.mysql.connection.cursor()
        query = """
            INSERT INTO TBL_COMPETENCIA (COMP_DESCRIPCION, COMP_TIPO, COMP_NIVEL, COMP_IDPROGRAMA )
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (description, type_, level, parent_id))
        self.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Competencia creada exitosamente"}), 201

    def update_competence(self, id):
        """Actualizar una competencia existente"""
        data = request.json
        description = data.get("description")
        type_ = data.get("type")
        level = data.get("level")
        parent_id = data.get("parent_id", None)

        # Actualizar competencia en la base de datos
        cursor = self.mysql.connection.cursor()
        query = """
            UPDATE TBL_COMPETENCIA
            SET COMP_DESCRIPCION = %s, COMP_TIPO = %s, COMP_NIVEL = %s, COMP_IDPROGRAMA = %s
            WHERE COMP_ID = %s
        """
        cursor.execute(query, (description, type_, level, parent_id, id))
        self.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Competencia actualizada exitosamente"}), 200

    def get_competencias_by_type(self, type_):
        """Obtener todas las competencias de un tipo específico (programa o asignatura)"""
        cursor = self.mysql.connection.cursor()
        query = "SELECT * FROM TBL_COMPETENCIA WHERE COMP_TIPO = %s"
        cursor.execute(query, (type_,))
        rows = cursor.fetchall()
        cursor.close()

        # Convertir resultados a una lista de competencias
        competences = [competence(id=row[0], description=row[2], type_=row[3], level=row[4], parent_id=row[1]).to_dict() for row in rows]
        return jsonify(competences), 200

    def get_linked_competences(self, parent_id):
        """Obtener competencias de asignatura vinculadas a una competencia de programa"""
        cursor = self.mysql.connection.cursor()
        query = "SELECT * FROM TBL_COMPETENCIA WHERE COMP_IDPROGRAMA = %s"
        cursor.execute(query, (parent_id,))
        rows = cursor.fetchall()
        cursor.close()

        # Convertir resultados a una lista de competencias
        linked_competences = [competence(id=row[0], description=row[2], type_=row[3], level=row[4], parent_id=row[1]).to_dict() for row in rows]
        return jsonify(linked_competences), 200
