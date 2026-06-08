import string
import random


class URLShortener:

    def __init__(self):
        self.url_map = {}

    def generate_random_code(self, length: int = 4) -> str:
        characters = string.ascii_lowercase + string.digits
        return "".join(random.choice(characters) for _ in range(length))

    def add_url(self, long_url: str, custom_code: str = None) -> str:
        if custom_code:
            if self.is_code_exists(custom_code):
                print(f"Ошибка (Вариативная часть 1): Короткий код '{custom_code}' уже существует!")
                return None
            code = custom_code
        else:
            code = self.generate_random_code()
            while self.is_code_exists(code):
                code = self.generate_random_code()

        self.url_map[code] = long_url
        return code

    def get_long_url(self, code: str) -> str:
        if not self.is_code_exists(code):
            print(f"Ошибка: Код '{code}' не найден в системе!")
            return None
        return self.url_map[code]

    def is_code_exists(self, code: str) -> bool:
        return code in self.url_map

    def print_all_urls(self):
        if not self.url_map:
            print("В системе пока нет сокращенных ссылок.")
            return

        print("\n=== База данных сокращенных ссылок ===")
        for code, long_url in self.url_map.items():
            print(f"  {code} -> {long_url}")
        print("=======================================")


if __name__ == "__main__":
    shortener = URLShortener()

    shortener.add_url("https://github.com/alf1kbtw/uevos", "repo")
    shortener.add_url("https://yandex.ru", "yandex")

    print("Система инициализирована начальными данными.")
    shortener.print_all_urls()

    while True:
        print("\n--- Меню сервиса сокращения ссылок ---")
        print("1. Добавить новую ссылку (авто-код)")
        print("2. Добавить ссылку со своим коротким кодом")
        print("3. Получить длинную ссылку по коду")
        print("4. Вывести все ссылки")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            url = input("Введите длинную ссылку: ").strip()
            if url:
                code = shortener.add_url(url)
                if code:
                    print(f"Успешно! Создан автоматический код: {code}")

        elif choice == "2":
            url = input("Введите длинную ссылку: ").strip()
            code = input("Введите желаемый короткий код: ").strip()
            if url and code:
                res_code = shortener.add_url(url, code)
                if res_code:
                    print(f"Успешно! Ссылка сохранена с кодом: {res_code}")

        elif choice == "3":
            code = input("Введите короткий код для поиска: ").strip()
            long_url = shortener.get_long_url(code)
            if long_url:
                print(f"Исходная ссылка: {long_url}")

        elif choice == "4":
            shortener.print_all_urls()

        elif choice == "5":
            print("Работа программы завершена.")
            break
        else:
            print("Неверный ввод, попробуйте еще раз.")