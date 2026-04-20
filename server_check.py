import os

# Адреса, яку будемо перевіряти
hostname = "8.8.8.8" 

print(f"--- Перевірка зв'язку з {hostname} ---")

# Виконуємо команду ping
response = os.system(f"ping -n 1 {hostname}" if os.name == "nt" else f"ping -c 1 {hostname}")

# Перевіряємо результат
if response == 0:
    print(f"\nУспіх! Сервер {hostname} доступний.")
else:
    print(f"\nПомилка! Не вдалося з'єднатися з {hostname}.")