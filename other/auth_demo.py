import bcrypt
import jwt
import time 

SECRET_KEY = "my_super_secret_key_123"  # В реальном проекте брать из .env!
users_db = {}  # Наша "база данных" в памяти

def register(username: str, password: str):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    users_db[username] = {
        "password_hash": hashed_password.decode('utf-8')
    }
    print(f"✅ Пользователь {username} зарегистрирован")

def login(username: str, password: str) -> str | None:
    if username not in users_db:
        print("❌ Пользователь не найден")
        return None
    password_bytes = password.encode('utf-8')
    stored_hash = users_db[username]["password_hash"].encode('utf-8')
    is_valid = bcrypt.checkpw(password_bytes, stored_hash)
    
    if not is_valid:
        print("❌ Неверный пароль")
        return None
        
    print("✅ Пароль верный!")
    
    payload = {
    "username": username,
    "role": "user",
    "exp": int(time.time()) + 3600  # Unix timestamp + 1 час
}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def get_profile(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"✅ Токен валиден! Добро пожаловать, {payload['username']}")
        return payload
        
    except jwt.ExpiredSignatureError:
        print("❌ Ошибка: Срок действия токена истек")
        return None
        
    except jwt.InvalidTokenError:
        print("❌ Ошибка: Невалидный токен (подпись не совпадает или формат нарушен)")
        return None

# ==========================================
# ТЕСТОВЫЙ ПРОГОН (можешь запустить этот код)
# ==========================================
if __name__ == "__main__":
    print("--- 1. Регистрация ---")
    register("alice", "super_secret_password")
    
    print("\n--- 2. Логин (верный пароль) ---")
    token = login("alice", "super_secret_password")
    
    print("\n--- 3. Доступ к профилю ---")
    if token:
        get_profile(token)
        
    print("\n--- 4. Логин (неверный пароль) ---")
    login("alice", "wrong_password")
    
    print("\n--- 5. Подделка токена (AQA check!) ---")
    # Берем токен, меняем в нем payload вручную (имитация взлома в DevTools)
    fake_token = token[:-5] + "XXXXX" 
    get_profile(fake_token)