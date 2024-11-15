
from flask import jsonify, request
from Model.connection import Connection
from Model.competence import competence

#class CompetenciaController:
class competenceManagementController:
    def __init__(self, app):
        # Inicializar la conexión a la base de datos usando la clase Connection
        self.mysql = Connection.init_database(app)

    def create_competencia(self):
        """Crear una nueva competencia (de programa o de asignatura)"""
        data = request.json
        descripcion = data.get("descripcion")
        tipo = data.get("tipo")
        nivel = data.get("nivel")
        tbl_comp_id = data.get("tbl_comp_id", None)  # Este valor es opcional

        # Insertar competencia en la base de datos
        cursor = self.mysql.connection.cursor()
        query = """
            INSERT INTO TBL_COMPETENCIA (COMP_DESCRIPCION, COMP_TIPO, COMP_NIVEL, TBL_COMP_ID)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (descripcion, tipo, nivel, tbl_comp_id))
        self.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Competencia creada exitosamente"}), 201

    def update_competencia(self, id):
        """Actualizar una competencia existente"""
        data = request.json
        descripcion = data.get("descripcion")
        tipo = data.get("tipo")
        nivel = data.get("nivel")
        tbl_comp_id = data.get("tbl_comp_id", None)

        # Actualizar competencia en la base de datos
        cursor = self.mysql.connection.cursor()
        query = """
            UPDATE TBL_COMPETENCIA
            SET COMP_DESCRIPCION = %s, COMP_TIPO = %s, COMP_NIVEL = %s, TBL_COMP_ID = %s
            WHERE COMP_ID = %s
        """
        cursor.execute(query, (descripcion, tipo, nivel, tbl_comp_id, id))
        self.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Competencia actualizada exitosamente"}), 200

    def get_competencias_by_tipo(self, tipo):
        """Obtener todas las competencias de un tipo específico (programa o asignatura)"""
        cursor = self.mysql.connection.cursor()
        query = "SELECT * FROM TBL_COMPETENCIA WHERE COMP_TIPO = %s"
        cursor.execute(query, (tipo,))
        rows = cursor.fetchall()
        cursor.close()

        # Convertir resultados a una lista de competencias
        competencias = [competence(id=row[0], descripcion=row[2], tipo=row[3], nivel=row[4], tbl_comp_id=row[1]).to_dict() for row in rows]
        return jsonify(competencias), 200

    def get_competencias_vinculadas(self, comp_id):
        """Obtener competencias de asignatura vinculadas a una competencia de programa"""
        cursor = self.mysql.connection.cursor()
        query = "SELECT * FROM TBL_COMPETENCIA WHERE TBL_COMP_ID = %s"
        cursor.execute(query, (comp_id,))
        rows = cursor.fetchall()
        cursor.close()

        # Convertir resultados a una lista de competencias
        competencias_vinculadas = [competence(id=row[0], descripcion=row[2], tipo=row[3], nivel=row[4], tbl_comp_id=row[1]).to_dict() for row in rows]
        return jsonify(competencias_vinculadas), 200
