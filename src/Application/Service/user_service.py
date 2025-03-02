from Domain.user import create_user
from Infrastructure.Models.user import save_user_model

def save(usuario):
    user = create_user(usuario)
    save_user_model(user)
    return