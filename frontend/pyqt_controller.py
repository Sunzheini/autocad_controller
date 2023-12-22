from time import sleep

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class FrontendWindow(QMainWindow):
    """
    The main window of the application that inherits from QMainWindow

    self.setGeometry(200, 200, 300, 300)  # x, y, width, height of where the window is on the screen
    self.label1.move(40, 20)  # x, y of where the label is on the window
    """
    def __init__(self, name_of_app, autocad_controller_object):
        super().__init__()

        # The controller object that will be used to call the methods
        self._autocad_controller = autocad_controller_object

        # The path of the selected file
        self._selected_file_path = ''

        # Set the window properties
        self.setGeometry(400, 200, 300, 300)
        self.setWindowTitle(name_of_app)

        # Call the method that will initialize the UI
        self._init_ui()

    def _init_ui(self):
        """
        Initialize the UI of the window
        """
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText('Използвай бутоните за команди към AutoCAD')
        self.label1.setMinimumWidth(250)
        self.label1.move(25, 20)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center

        self.button_select_file = QtWidgets.QPushButton(self)
        self.button_select_file.setText('Избери файл')
        self.button_select_file.setMinimumWidth(150)
        self.button_select_file.move(75, 60)
        self.button_select_file.clicked.connect(self.select_file_click)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Стартирай AutoCAD')
        self.button1.setMinimumWidth(150)
        self.button1.move(75, 100)
        self.button1.clicked.connect(self.start_autocad_click)

        self.button2 = QtWidgets.QPushButton(self)
        self.button2.setText('Затвори AutoCAD')
        self.button2.setMinimumWidth(150)
        self.button2.move(75, 140)
        self.button2.clicked.connect(self.close_autocad_click)

        self.button9 = QtWidgets.QPushButton(self)
        self.button9.setText('Последователност')
        self.button9.setMinimumWidth(150)
        self.button9.move(75, 180)
        self.button9.clicked.connect(self.sequence_click)

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText('Статус: очакване на команда')
        self.label2.setMinimumWidth(250)
        self.label2.move(25, 250)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)  # Align text to the center

    def _update_status(self, status_text):
        """
        Update the status label
        :param status_text:
        """
        self.label2.setText(status_text)
        self.update()

    def select_file_click(self):
        """
        Open a file dialog to select a file
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_dialog = QFileDialog()
        file_dialog.setOptions(options)
        file_dialog.setWindowTitle("Избери файл")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("AutoCAD Drawing Files (*.dwg)")

        if file_dialog.exec_() == QFileDialog.Accepted:
            self._selected_file_path = file_dialog.selectedFiles()[0]

        # update the status label
        status_text = f'Избран файл: ...{self._selected_file_path[-20:]}' if self._selected_file_path else 'Не е избран файл'
        self._update_status(status_text)

    def start_autocad_click(self):
        """
        Start AutoCAD and open the selected file
        """
        try:
            self._autocad_controller.start_autocad()
            sleep(5)
            self._autocad_controller.open_document(self._selected_file_path)
            sleep(5)
            self._autocad_controller.get_active_document()
            sleep(5)
            self._autocad_controller.get_active_document_name()
            sleep(5)
        except Exception as e:
            print(f"Error from `button1_click`: {e}")

        # update the status label
        function = self.button1.text()      # get the text attribute of the button
        status_text = f'Статус: `{function}` изпълнено'
        self._update_status(status_text)

    def close_autocad_click(self):
        """
        Save and close the active document and close AutoCAD
        """
        try:
            self._autocad_controller.save_active_document()
            sleep(5)
            self._autocad_controller.close_active_document()
            sleep(5)
            self._autocad_controller.close_autocad()
            sleep(5)
        except Exception as e:
            print(f"Error from `button2_click`: {e}")

        # update the status label
        function = self.button2.text()      # get the text attribute of the button
        status_text = f'Статус: `{function}` изпълнено'
        self._update_status(status_text)

    def sequence_click(self):
        """
        Run the sequence method
        """
        try:
            self._autocad_controller.sequence(self._selected_file_path)
        except Exception as e:
            print(f"Error from `button9_click`: {e}")

        # update the status label
        function = self.button9.text()      # get the text attribute of the button
        status_text = f'Статус: `{function}` изпълнено'
        self._update_status(status_text)

    def update(self):
        # adjust size to hold the text inside
        self.label1.adjustSize()
