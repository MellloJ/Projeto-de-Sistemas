from django.contrib.auth import authenticate, login

class loginUser:
    def auth(request, email, password, remember):
        usuarioLogado = authenticate(request, username=email, password=password)

        return usuarioLogado
    
    def login(request, usuarioAutenticado):
        try:
            return login(request, usuarioAutenticado)
        except:
            return False