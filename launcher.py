from design import Ui_MainWindow
from results import Ui_Results
import os
import sys
from PySide2 import QtWidgets
from time import sleep
from pathlib import Path
#import psutil

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
        # PROCNAME = "GameClient.exe"
        #
        # for proc in psutil.process_iter():
        #     # check whether the process name matches
        #     if proc.name() == PROCNAME:
        #         proc.kill()
        for filepath in self.clients:
            os.startfile(filepath)
            sleep(3)





    def select_files(self):
        # Находим файл
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Open File")
        # Добавляем файл в листвиджет и в список клиентов, отрезаем от названий все лишнее
        self.listWidget.addItem(str(file).strip('(').strip("'")[:-19])
        self.clients.append(str(file).strip('(').strip("'")[:-19])

    clients = []






if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Создаем экземпляр класса лаунчер
    launcher = Launcher()
    results = Results()
    # Запуск
    sys.exit(app.exec_())


