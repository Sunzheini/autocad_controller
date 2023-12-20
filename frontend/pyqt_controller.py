from time import sleep

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow


class FrontendWindow(QMainWindow):
    """
    The main window of the application that inherits from QMainWindow

    self.setGeometry(200, 200, 300, 300)  # x, y, width, height of where the window is on the screen
    self.label1.move(40, 20)  # x, y of where the label is on the window
    """
    def __init__(self, name_of_app, autocad_controller_object):
        super().__init__()

        self.autocad_controller = autocad_controller_object

        self.setGeometry(400, 200, 300, 300)
        self.setWindowTitle(name_of_app)
        self.init_ui()

    def init_ui(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Използвай бутоните за команди към AutoCAD')
        self.label1.setMinimumWidth(250)
        self.label1.move(25, 20)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Стартирай AutoCAD')
        self.button1.setMinimumWidth(150)
        self.button1.move(75, 70)
        self.button1.clicked.connect(self.button1_click)

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText('Затвори AutoCAD')
        self.button2.setMinimumWidth(150)
        self.button2.move(75, 110)
        self.button2.clicked.connect(self.button2_click)

        self.button9 = QtWidgets.QPushButton(self)
        self.button9.setText('Последователност')
        self.button9.setMinimumWidth(150)
        self.button9.move(75, 150)
        self.button9.clicked.connect(self.button9_click)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('Статус: очакване на команда')
        self.label2.setMinimumWidth(250)
        self.label2.move(25, 250)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center

    def button1_click(self):
        try:
            self.autocad_controller.start_autocad()
            sleep(5)
            self.autocad_controller.open_document()
            sleep(5)
            self.autocad_controller.get_active_document()
            sleep(5)
            self.autocad_controller.get_active_document_name()
            sleep(5)
        except Exception as e:
            print(f"Error from `button1_click`: {e}")

        function = self.button1.text()      # get the text attribute of the button
        status_text = f'Статус: {function} изпълнена'
        self.label2.setText(status_text)
        self.update()

    def button2_click(self):
        try:
            self.autocad_controller.save_active_document()
            sleep(5)
            self.autocad_controller.close_active_document()
            sleep(5)
            self.autocad_controller.close_autocad()
            sleep(5)
        except Exception as e:
            print(f"Error from `button2_click`: {e}")

        function = self.button2.text()      # get the text attribute of the button
        status_text = f'Статус: {function} изпълнена'
        self.label2.setText(status_text)
        self.update()

    def button9_click(self):
        try:
            self.autocad_controller.sequence()
        except Exception as e:
            print(f"Error from `button9_click`: {e}")

        function = self.button9.text()      # get the text attribute of the button
        status_text = f'Статус: {function} изпълнена'
        self.label2.setText(status_text)
        self.update()

    def update(self):
        self.label1.adjustSize()    # adjust size to hold the text inside
