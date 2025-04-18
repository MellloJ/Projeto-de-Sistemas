from django.contrib.auth import authenticate, login

class loginUser:
    def auth(request, email, password, remember):
        usuarioLogado = authenticate(request, username=email, password=password)

        return usuarioLogado

    def do_login(request, usuarioAutenticado):
        try:
            login(request, usuarioAutenticado)
            return True
        except Exception as e:
            print(f"Erro ao fazer login: {e}")
            return False