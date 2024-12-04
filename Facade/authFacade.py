from Services.authService import AuthService

class AuthFacade:
    def __init__(self):
        self.auth_service = AuthService()

    def login_user(self, data):
        """
        Maneja la lógica de inicio de sesión.
        :param data: Diccionario con email y contraseña del usuario.
        :return: Token y rol si tiene éxito, mensaje de error en caso contrario.
        """
        return self.auth_service.login_user(data)