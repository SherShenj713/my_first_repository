class User:
    def __init__(self, user_id, name, age, email):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email

def get_user_info(user: User) -> str:
    return f'Возраст пользователя {user.name} - {user.age}, ' \
           f'а email - {user.email}'


user_1 = User(42, 'Vasiliy', 23, 'vasya_pupkin@pochta.ru')
print(get_user_info(user_1))