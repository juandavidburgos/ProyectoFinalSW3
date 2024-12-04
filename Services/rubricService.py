from Model.rubric import Rubric
from Model.connection import db
from Model.evaluator import Evaluator
from Model.connection import db

class RubricService:
    @staticmethod
    def create_rubric(data):
        print(f"Datos recibidos en el servicio: {data}")
        # Validacion de los datos requeridos
        if not data.get('evaluation_id') or not data.get('rub_name') \
            or not data.get('rub_score') or not data.get('criterion_description')\
            or not data.get('rub_level'):
            return None, "Todos los campos son requeridos"
        
        # Crear un nueva rubrica
        new_rubric = Rubric(
            evaluation_id= ['evaluation_id'],
            rub_name=data['rub_name'],
            rub_score=data['rub_score'],
            criterion_description=data['criterion_description'],
            rub_level=data['rub_level']   
        )
        
        try:
            db.session.add(new_rubric)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, f"Ha ocurrido un error en la base de datos: {str(e)}"

        return new_rubric, None
    
    @staticmethod
    def get_all_Rubric():
        #*Obtiene todos las rubricas
        try:
            # Consultar todos los rubricas 
            # Consultar solo los campos requeridos
            rubrics = db.session.query(Rubric.rub_id,Rubric.rub_name,Rubric.criterion_description, Rubric.rub_level,Rubric.rub_score).all()

            if not rubrics:
                return [], "No se encontraron rubricas."
            # Convertir las tuplas resultantes en una lista de diccionarios
            rubric_dict = [{"rub_id": rubric.rub_id, "rub_name": rubric.rub_name, "criterion_description": Rubric.criterion_description,"rub_level": Rubric.rub_level,"rub_score": Rubric.rub_score } for rubric in rubrics]
        
            print(rubric_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return rubric_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener los rubricas: {str(e)}"
         
    @staticmethod
    def search_by_rub_level(rub_level):
        try:
            #Buscar todos las rubricas por el nivel de desempeño
            rubric = Rubric.query.filter_by(rub_level=rub_level).all()
            if rubric:
                return rubric, None
            return None, "No se encontraron rubricas con ese nivel especificado"
        except Exception as e:
            return None, f"Error al buscar la rubrica {str(e)}"
        
    @staticmethod
    def search_by_criterion_description(criterion_description):
        try:
            #Buscar todoas las rubricas por la descripción del criterio
            rubric = Rubric.query.filter_by(criterion_description=criterion_description).all()
            if rubric:
                return rubric, None
            return None, "No se encontraron rubricas con esa descripción"
        except Exception as e:
            return None, f"Error al buscar la rubrica {str(e)}"
        
    @staticmethod
    def search_by_name(rub_name):
        try:
            #Buscar todoas las rubricas por la descripción del criterio
            rubric = Rubric.query.filter_by(rub_name=rub_name).first()
            if rubric:
                return rubric, None
            return None, "No se encontraron rubricas con esa descripción"
        except Exception as e:
            return None, f"Error al buscar la rubrica {str(e)}"
    
    @staticmethod
    def edit_rubric(rub_name,data):
        try:
            #Buscar la rubrica por el nombre
            rubric = Rubric.query.filter_by(rub_name=rub_name).equal()
            if not rubric:
                return None, "No se encontró la rubrica"
            
            rubric.rub_name = data.get['rub_name']
            rubric.rub_score = data['rub_score']
            rubric.criterion_description = data['criterion_description']
            rubric.rub_level = data['rub_level']

            db.session.commit()
            return rubric, None
        except Exception as e:
            db.session.rollback()
            return None, f"Error al editar la rubrica {str(e)}"
        
