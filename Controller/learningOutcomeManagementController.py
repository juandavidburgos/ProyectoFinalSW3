from flask import jsonify, request
from Model.connection import Connection
from Model.learningOutcome import learningOutcome

#class RAController:
class learningOutcomeManagementController:
    def __init__(self, app):
        # Inicializar la conexión a la base de datos usando la clase Connection
        self.mysql = Connection.init_database(app)

    def create_learning_outcome(self):
        """Crear un nuevo resultado de aprendizaje (RA) asociado a una competencia"""
        data = request.json
        comp_id = data.get("comp_id")  # ID de la competencia a la que se asocia el RA
        description = data.get("description")

        # Insertar RA en la base de datos
        cursor = self.mysql.connection.cursor()
        query = """
            INSERT INTO TBL_RA (COMP_ID, RAP_DESCRIPCION)
            VALUES (%s, %s)
        """
        cursor.execute(query, (comp_id, description))
        self.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "RA creado exitosamente"}), 201

    def update_learning_outcome(self, rap_id):
        """Actualizar un resultado de aprendizaje (RA) existente"""
        data = request.json
        comp_id = data.get("comp_id")  # ID de la competencia a la que se asocia el RA
        description = data.get("description")

        # Actualizar RA en la base de datos
        cursor = self.mysql.connection.cursor()
        query = """
            UPDATE TBL_RA
            SET COMP_ID = %s, RAP_DESCRIPCION = %s
            WHERE RAP_ID = %s
        """
        cursor.execute(query, (comp_id, description, rap_id))
        self.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "RA actualizado exitosamente"}), 200

    def get_learning_outcomes_by_competencia(self, comp_id):
        """Obtener todos los RA asociados a una competencia específica"""
        cursor = self.mysql.connection.cursor()
        query = "SELECT * FROM TBL_RA WHERE COMP_ID = %s"
        cursor.execute(query, (comp_id,))
        rows = cursor.fetchall()
        cursor.close()

        # Convertir resultados a una lista de RA
        lo_list = [learningOutcome(id=row[0], comp_id=row[1], description=row[2]).to_dict() for row in rows]
        return jsonify(lo_list), 200
