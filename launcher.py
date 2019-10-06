from design import Ui_MainWindow
from results import Ui_Results
import os
import sys
from PySide2 import QtWidgets
from time import sleep
from pathlib import Path

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
        # results.show()
        # for file in listWidget:
        #    os.startfile(file)
        for filename in os.listdir(os.getcwd()):
            os.startfile(os.getcwd() + '\\' + filename)
            sleep(3)





    def select_files(self):
        # Если в списке что-то было, сбрасываем его
        self.listWidget.clear()
        # Задаем переменную для папки с клиентами для обновления
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if folder:
            for file in os.listdir(folder):
                self.listWidget.addItem(file)









if __name__ == '__main__':
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    # Создаем экземпляр класса лаунчер
    launcher = Launcher()
    results = Results()
    # Запуск
    sys.exit(app.exec_())


