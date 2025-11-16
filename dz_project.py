from pydantic import BaseModel


class SystemUser(BaseModel):
    id: int
    username: str
    email: str
    password: str
    surname: str
    name: str
    is_active: bool
    address: dict
    contacts: list


# --- Створення об’єкта і збереження у файл ---

user = SystemUser(
    id=1,
    username="sergiy2025",
    email="sergiy@example.com",
    password="qwerty123",
    surname="Іванов",
    name="Сергій",
    is_active=True,
    address={"city": "Kyiv", "street": "Khreshchatyk", "house": 10},
    contacts=["+380991112233", "backup@example.com"]
)

# Перетворюємо у JSON і записуємо у файл
with open("system_user.json", "w", encoding="utf-8") as file:
    file.write(user.model_dump_json(indent=4))


# --- Зчитування з файлу і відновлення об’єкта ---

with open("system_user.json", "r", encoding="utf-8") as file:
    json_content = file.read()

# Перетворюємо JSON → назад у об’єкт SystemUser
loaded_user = SystemUser.model_validate_json(json_content)

# Виводимо у консоль
print(loaded_user)
print()
