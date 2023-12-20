import sys

from PyQt5.QtWidgets import QApplication

from core.autocad_controller import AutocadController
from frontend.pyqt_controller import FrontendWindow


# (venv) D:\Study\Projects\PycharmProjects\playground\fromdesigner>pyuic5 -x test.ui -o test.py
path = r'C:\Users\User\Desktop\MK\assembly_version2 - Copy.dwg'
name_of_app = 'AutoCAD Controller'


if __name__ == '__main__':
    # Create an instance of the AutoCAD controller
    autocad_controller = AutocadController(path)

    gui = QApplication(sys.argv)
    gui_window = FrontendWindow(name_of_app, autocad_controller)
    gui_window.show()
    sys.exit(gui.exec_())
