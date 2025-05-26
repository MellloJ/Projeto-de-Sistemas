def usuario_e_supermarket_user(request):
    user = request.user
    if not user.is_authenticated:
        return False
    try:
        return hasattr(user, 'supermarket_user') and user.supermarket_user is not None
    except Exception:
        return False
