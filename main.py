import sys

from PyQt5.QtWidgets import QApplication

from core.autocad_controller import AutocadController
from frontend.pyqt_controller import FrontendWindow


name_of_app = 'AutoCAD Controller'


if __name__ == '__main__':
    # 1. Create an instance of the AutoCAD controller
    autocad_controller = AutocadController()

    # 2. Create an instance of the GUI and pass the AutoCAD controller to it
    gui = QApplication(sys.argv)
    gui_window = FrontendWindow(name_of_app, autocad_controller)

    # 3. Execute the GUI
    gui_window.show()
    sys.exit(gui.exec_())
