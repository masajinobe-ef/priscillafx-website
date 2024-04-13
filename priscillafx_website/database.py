import aiosqlite


# Подключение к базе данных
async def connect_to_db():
    return await aiosqlite.connect('database/priscillafx.db')


# Авторизация пользователя
async def authenticate_user(username: str, password: str) -> bool:
    db = await connect_to_db()
    try:
        cursor = await db.cursor()
        query = "SELECT password FROM users WHERE username = ?"
        await cursor.execute(query, (username,))
        result = await cursor.fetchone()
        if result and result[0] == password:
            return True
        return False
    finally:
        await db.close()
