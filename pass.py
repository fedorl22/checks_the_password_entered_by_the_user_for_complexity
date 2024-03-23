import hashlib

def check_password(password):  
    if len(password) < 8:      # Проверяем длину пароля  
        return False  
    if not any(char.isupper() for char in password):  # Есть ли в пароле хотя бы одна латинская буква в верхнем регистре  
        return False  
    if not any(char.islower() for char in password):  # Есть ли в пароле хотя бы одна латинская буква в нижнем регистре  
        return False  
    if not any(char.isdigit() for char in password):  # Есть ли в пароле хотя бы одна цифра  
        return False  
    return True # Если все проверки пройдены успешно, возвращаем True  

password = input("Введите пароль: ")  
if check_password(password):  
    print("Пароль надежный")  
else:  
    print("Пароль ненадежный")
hash_object = hashlib.sha256(password.encode())
print(hash_object.hexdigest())

