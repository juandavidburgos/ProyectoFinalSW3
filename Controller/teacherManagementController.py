from flask import jsonify, request
from Model.connection import Connection
from Model.teacher import Teacher

#* CONTROLADOR GESTION DE PROFESORES
class TeacherManagementController:
    def __init__(self, app):
        # Inicializar la conexión a la base de datos usando la clase Connection
        self.app = app
    
    def create_teacher(self):
        """Crear un nuevo profesor"""
        data = request.json
        teTypeIdentification = data.get("teTypeIdentification")
        teIdentification = data.get("teIdentification")
        teTypeTeacher = data.get("teTypeTeacher")
        teName = data.get("teName")
        teLastName = data.get("teLastName")
        teLastTitle = data.get("teLastTitle")
        teEmail = data.get("teEmail")

        cursor = self.app.mysql.connection.cursor()
        query = """
            INSERT INTO TBL_Docente (teTypeIdentification, teIdentification, teTypeTeacher, teName, teLastName, teLastTitle, teEmail)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (teTypeIdentification, teIdentification, teTypeTeacher, teName, teLastName, teLastTitle, teEmail))
        self.app.mysql.connection.commit()
        cursor.close()
    
        return jsonify({"message": "Profesor creado exitosamente"}), 201
    
    def update_teacher(self, teId):
        """Actualizar un profesor existente"""
        data = request.json
        teTypeIdentification = data.get("teTypeIdentification")
        teIdentification = data.get("teIdentification")
        teTypeTeacher = data.get("teTypeTeacher")
        teName = data.get("teName")
        teLastName = data.get("teLastName")
        teLastTitle = data.get("teLastTitle")
        teEmail = data.get("teEmail")

    def delete_teacher(self, teId):
        """Eliminar un profesor existente"""
        cursor = self.app.mysql.connection.cursor()
        query = "DELETE FROM TBL_Docente WHERE teId = %s"
        cursor.execute(query, (teId,))
        self.app.mysql.connection.commit()
        cursor.close()
        return jsonify({"message": "Profesor eliminado exitosamente"}), 200
    
    def search_allTeacher(self):
        """Obtener todos los profesores"""
        cursor = self.app.mysql.connection.cursor()
        query = "SELECT * FROM TBL_Docente"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        # Convertir resultados a una lista de profesores
        teacher_list = [Teacher(teId=row[0], teTypeIdentification=row[1], teIdentification=row[2], teTypeTeacher=row[3], teName=row[4], teLastName=row[5], teLastTitle=row[6], teEmail=row[7]).to_dict() for row in rows]
        return jsonify(teacher_list), 200
    
    def search_byIdentification(self, teIdentification):
        """Obtener un profesor por su número de identificación"""
        cursor = self.app.mysql.connection.cursor()
        query = "SELECT * FROM TBL_Docente WHERE teIdentification = %s"
        cursor.execute(query, (teIdentification,))
        row = cursor.fetchone()
        cursor.close()
        # Convertir resultado a un profesor
        teacher = Teacher(teId=row[0], teTypeIdentification=row[1], teIdentification=row[2], teTypeTeacher=row[3], teName=row[4], teLastName=row[5], teLastTitle=row[6], teEmail=row[7]).to_dict()
        return jsonify(teacher), 200
    

    