import os


class BusStopNode:

    def __init__(self, name: str, x: float, y: float, time_to_next: int):
        self.name = name
        self.x = x
        self.y = y
        self.time_to_next = time_to_next
        self.next = None
        self.prev = None


class BusRoute:

    def __init__(self, route_number: str):
        self.route_number = route_number
        self.head = None
        self.tail = None
        self.count = 0

    def add_stop(self, name: str, x: float, y: float, time_to_next: int):
        new_stop = BusStopNode(name, x, y, time_to_next)

        if not self.head:
            self.head = new_stop
            self.tail = new_stop
        else:
            self.tail.next = new_stop
            new_stop.prev = self.tail
            self.tail = new_stop

        self.count += 1

    def calculate_total_time(self) -> int:
        total_time = 0
        current = self.head

        while current and current.next:
            total_time += current.time_to_next
            current = current.next

        return total_time

    def predict_location(self, start_stop_name: str, n_stops: int) -> str:
        current = self.head

        while current and current.name != start_stop_name:
            current = current.next

        if not current:
            return f"Ошибка: Остановка '{start_stop_name}' не найдена!"

        steps_made = 0
        while current and steps_made < n_stops:
            if current.next:
                current = current.next
                steps_made += 1
            else:
                return f"Автобус доедет до конечной '{current.name}' через {steps_made} ост. (дальше маршрута нет)."

        return f"Через {n_stops} ост. от '{start_stop_name}' автобус будет на остановке: '{current.name}'"

    def get_reverse_route_names(self) -> list:
        reverse_names = []
        current = self.tail

        while current:
            reverse_names.append(current.name)
            current = current.prev

        return reverse_names

    def save_report_to_file(self, filename: str = "route_report.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(
                f"=== ПОДРОБНЫЙ ОТЧЕТ: АВТОБУСНЫЙ МАРШРУТ №{self.route_number} ===\n"
            )
            f.write(f"Всего остановок: {self.count}\n")
            f.write("=" * 50 + "\n\n")

            current = self.head
            idx = 1
            while current:
                f.write(f" [{idx}] Остановка: {current.name}\n")
                f.write(f"     Координаты:  X: {current.x}, Y: {current.y}\n")
                if current.next:
                    f.write(
                        f"     До следующей: {current.time_to_next} мин.\n"
                    )
                else:
                    f.write(f"     Статус:       Конечная остановка\n")
                f.write("-" * 50 + "\n")

                current = current.next
                idx += 1

            f.write(
                f"\n[ИТОГ] Общее время в пути от начала до конца: {self.calculate_total_time()} минут.\n"
            )

        print(
            f"Отчет по маршруту успешно сохранен в файл: {os.path.abspath(filename)}"
        )

    def print_to_console(self):
        if not self.head:
            print("Маршрут пока пуст.")
            return

        print(f"\nСхема маршрута №{self.route_number}:")
        current = self.head
        idx = 1
        while current:
            arrow = (
                f" --({current.time_to_next} мин)--> "
                if current.next
                else " (Конечная)"
            )
            print(f"  {idx}. {current.name}{arrow}")
            current = current.next
        print(f"  Общее время пути: {self.calculate_total_time()} мин.")


if __name__ == "__main__":
    route = BusRoute("10")

    route.add_stop("Автовокзал", 0.0, 0.0, 8)
    route.add_stop("Улица Ленина", 2.5, 1.0, 5)
    route.add_stop("Парк Победы", 5.0, 3.2, 6)
    route.add_stop("ТЦ Кристалл", 7.1, 6.0, 12)
    route.add_stop("Студгородок", 10.0, 10.0, 0)

    route.print_to_console()

    print("\n" + "─" * 60)
    print("ПРОВЕРКА ФУНКЦИИ ПРОГНОЗИРОВАНИЯ (predict_location):")
    print(route.predict_location("Автовокзал", 2))
    print(route.predict_location("Улица Ленина", 3))
    print(route.predict_location("Парк Победы", 10))

    print("\n" + "─" * 60)
    print("ПРОВЕРКА СТРОЕНИЯ ОБРАТНОГО МАРШРУТА (get_reverse_route_names):")
    rev = route.get_reverse_route_names()
    print("Обратный путь: " + " -> ".join(rev))

    print("\n" + "─" * 60)
    print("Генерация отчета в текстовый файл...")
    route.save_report_to_file("bus_line_10_report.txt")