import os

# 1. Створюємо список адрес для перевірки
targets = ["8.8.8.8", "1.1.1.1", "google.com","8.8.4.4"]

print("--- Починаємо масову перевірку серверів ---")

# 2. Починаємо цикл: для кожного "target" у списку "targets"
for target in targets:
    print(f"\nПеревіряю: {target}...")
    
    # Виконуємо команду ping (враховуємо Windows та Linux)
    response = os.system(f"ping -n 1 {target}" if os.name == "nt" else f"ping -c 1 {target}")

    # Перевіряємо результат для кожної конкретної адреси
    if response == 0:
        print(f"Результат: {target} ПРАЦЮЄ")
    else:
        print(f"Результат: {target} НЕ ДОСТУПНИЙ")

print("\n--- Перевірку завершено ---")