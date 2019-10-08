from design import Ui_MainWindow
from results import Ui_Results
import os
import sys
from PySide2 import QtWidgets
from time import sleep
import psutil

# Окошко с результатом проверки
class Results(QtWidgets.QWidget, Ui_Results):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirmation_button.clicked.connect(self.confirm)
        self.results_label.setText("Тут информация о прошедших обновлениях")

    def confirm(self):
        self.close()

# Основное окно программы
class Launcher(QtWidgets.QMainWindow, Ui_MainWindow, Results):
    def __init__(self):
        super().__init__()
        # Создание формы и Ui (дизайн)
        self.setupUi(self)
        # Показать наше окно
        self.show()
        # Инитим кнопки
        self.check_updates_button.clicked.connect(self.check_updates)
        self.select_files_button.clicked.connect(self.select_files)

    # Определяем функции кнопок
    def check_updates(self):
        # Задаем процесс, за которым будем охотиться
        PROCNAME = "notepad.exe"
        # Создаем цикл запуска и убийства процесса
        with open(r'C:\Users\Admin\Desktop\Python projects\Pyside2 GUI\clients.txt') as clients_kill:
            clients_kill_splitted = [line.rstrip('\n') for line in clients_kill]
            for line in clients_kill_splitted:
                os.startfile(line)
                sleep(3)
                for process in psutil.process_iter():
                    if process.name() == PROCNAME:
                        process.kill()





    def select_files(self):
        # Находим файл
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        # отрезаем от названия все лишнее
        added_file = str(file).strip('(').strip("'")[:-19]
        # Проверяем, есть ли файл в списке клиентов и если нет, добавляем его в листвиджет
        with open(r'C:\Users\Admin\Desktop\Python projects\Pyside2 GUI\clients.txt', 'r') as clients_check:
            if added_file not in clients_check.read():
                self.listWidget.addItem(added_file)
        # Проверяем, есть ли файл в списке клиентов и если нет, добавляем его в список клиентов, чтобы с ним можно было работать
        with open(r'C:\Users\Admin\Desktop\Python projects\Pyside2 GUI\clients.txt', 'a') as clients:
            with open(r'C:\Users\Admin\Desktop\Python projects\Pyside2 GUI\clients.txt', 'r') as clients_check:
                if added_file not in clients_check.read():
                    clients.write(added_file + '\n')
        self.clients.append(added_file)


    # Список клиентов, которые будут запускаться
    clients = []






if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Создаем экземпляр класса лаунчер
    launcher = Launcher()
    results = Results()
    # Запуск
    sys.exit(app.exec_())


