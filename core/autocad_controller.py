import random
from time import sleep

from pyautocad import Autocad, APoint
from pyautocad.contrib.tables import Table
import pandas as pd


class AutocadController:
    """
    A class to control AutoCAD
    :param project_path: path to the AutoCAD project
    """
    def __init__(self):
        self._autocad_instance = None
        self._active_document = None
        self._active_document_name = None

    def start_autocad(self, visible=True):
        """
        Start AutoCAD
        create_if_not_exist: if AutoCAD doesn’t run, then new instanse will be crated
        :param visible: new AutoCAD instance will be visible if True (default)
        :return: a string message with the result of the operation
        """
        try:
            self._autocad_instance = Autocad(create_if_not_exists=True, visible=visible)
        except Exception as e:
            message = f"Error from `start_autocad`: {e}"
            return message
        return 'success'

    def open_document(self, path):
        """
        Open a document in AutoCAD
        :param path: path to the document
        :return: a string message with the result of the operation
        """
        try:
            self._autocad_instance.app.Documents.Open(path)
        except Exception as e:
            message = f"Error from `open_document`: {e}"
            return message
        return 'success'

    def get_active_document(self):
        """
        Get the active document and set it to the active_document attribute
        :return: a string message with the result of the operation
        """
        try:
            self._active_document = self._autocad_instance.doc
        except Exception as e:
            message = f"Error from `get_active_document`: {e}"
            return message
        return 'success'

    def get_active_document_name(self):
        """
        Get the active document name and set it to the active_document_name attribute
        :return: a string message with the result of the operation
        """
        try:
            self._active_document_name = self._active_document.Name
        except Exception as e:
            message = f"Error from `get_active_document`: {e}"
            return message
        return 'success'

    def save_active_document(self):
        """
        Save the active document
        :return: a string message with the result of the operation
        """
        try:
            self._active_document.Save()
        except Exception as e:
            message = f"Error from `save_active_document`: {e}"
            return message
        return 'success'

    def close_active_document(self):
        """
        Close the active document
        :return: a string message with the result of the operation
        """
        try:
            self._active_document.Close()
        except Exception as e:
            message = f"Error from `close_active_document`: {e}"
            return message
        return 'success'

    def print_in_autocad(self, text):
        """
        Print a text in AutoCAD
        :param text: the text to print
        :return: a string message with the result of the operation
        """
        try:
            self._autocad_instance.prompt(text)
        except Exception as e:
            message = f"Error from: `get_active_document`: {e}"
            return message
        return 'success'

    def draw_random_circle(self):
        """
        Draw a random circle in AutoCAD
        :return: a string message with the result of the operation
        """
        try:
            random_x = random.randint(0, 100)
            random_y = random.randint(0, 100)
            center = APoint(random_x, random_y)
            radius = 10.0
            self._autocad_instance.model.AddCircle(center, radius)
        except Exception as e:
            message = f"Error from `draw_circle`: {e}"
            return message
        return 'success'

    def close_autocad(self):
        """
        Close AutoCAD
        :return: a string message with the result of the operation
        """
        try:
            self._autocad_instance.app.Quit()
        except Exception as e:
            message = f"Error from `close_autocad`: {e}"
            return message
        return 'success'

    def extract_text_to_excel(self):
        """
        WIP
        """
        excel = 'test.xlsx'
        data = []

        try:
            for obj in self._autocad_instance.iter_objects('Text'):
                x, y, z = obj.InsertionPoint
                data.append([obj.TextString, x, y, z])

            df = pd.DataFrame(data, columns=['Text', 'X', 'Y', 'Z'])
            df.to_excel(excel, index=False)

        except Exception as e:
            message = f"{e}"
            return message
        return 'success'

    def sequence(self, path):
        """
        Execute a sequence of operations
        :return: a string message with the result of the operation
        """
        try:
            self.start_autocad()
            sleep(5)
            self.open_document(path)
            sleep(5)
            self.get_active_document()
            sleep(5)
            self.get_active_document_name()
            sleep(5)
            self.draw_random_circle()
            sleep(5)
            self.save_active_document()
            sleep(5)
            self.close_active_document()
            sleep(5)
            self.close_autocad()
        except Exception as e:
            message = f"Error from `sequence`: {e}"
            return message
        return 'success'
