class TreeNode:

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def insert(root: TreeNode, value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root


def search(root: TreeNode, target: int) -> bool:
    if root is None:
        return False
    if root.value == target:
        return True

    if target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)


def inorder(root: TreeNode, result=None) -> list:
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result


def find_min(root: TreeNode) -> TreeNode:
    current = root
    while current.left is not None:
        current = current.left
    return current


def delete(root: TreeNode, value: int) -> TreeNode:
    if root is None:
        return root

    if value < root.value:
        root.left = delete(root.left, value)
    elif value > root.value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_min(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)

    return root


if __name__ == "__main__":
    tree_root = None

    for val in [50, 30, 70, 20, 40, 60, 80]:
        tree_root = insert(tree_root, val)

    print("Дерево инициализировано начальными числами: [50, 30, 70, 20, 40, 60, 80]")
    print(f"Текущий симметричный обход (в порядке возрастания): {inorder(tree_root)}")

    while True:
        print("\n--- Меню работы с Бинарным Деревом Поиска (BST) ---")
        print("1. Добавить новое число в дерево")
        print("2. Найти число в дереве")
        print("3. Вывести все числа (Inorder обход)")
        print("4. Удалить число из дерева (Вариативная часть)")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ").strip()

        if choice == "1":
            try:
                num = int(input("Введите целое число для вставки: "))
                tree_root = insert(tree_root, num)
                print(f"Число {num} успешно добавлено.")
            except ValueError:
                print("Ошибка: Введите корректное целое число!")

        elif choice == "2":
            try:
                num = int(input("Введите число для поиска: "))
                if search(tree_root, num):
                    print(f"Результат: Число {num} НАЙДЕНО в дереве!")
                else:
                    print(f"Результат: Число {num} НЕ найдено.")
            except ValueError:
                print("Ошибка: Введите корректное целое число!")

        elif choice == "3":
            print(f"Элементы дерева по возрастанию: {inorder(tree_root)}")

        elif choice == "4":
            try:
                num = int(input("Введите число для удаления: "))
                if search(tree_root, num):
                    tree_root = delete(tree_root, num)
                    print(f"Число {num} успешно удалено из дерева.")
                else:
                    print(f"Ошибка: Числа {num} нет в дереве, удаление невозможно.")
            except ValueError:
                print("Ошибка: Введите корректное целое число!")

        elif choice == "5":
            print("Работа программы завершена.")
            break
        else:
            print("Неверный ввод, попробуйте еще раз.")