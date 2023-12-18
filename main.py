import random
from time import sleep

from pyautocad import Autocad, APoint


path = r'C:\Users\User\Desktop\MK\assembly_version2 - Copy.dwg'


def start_autocad():
    # create_if_not_exists – if AutoCAD doesn’t run, then new instanse will be crated
    # visible – new AutoCAD instance will be visible if True (default)
    try:
        autocad_instance = Autocad(create_if_not_exists=True, visible=True)
    except Exception as e:
        print(f"Error from `start_autocad`: {e}")
        return None
    return autocad_instance


def open_document(autocad_instance, path):
    try:
        autocad_instance.app.Documents.Open(path)
    except Exception as e:
        print(f"Error from `open_document`: {e}")
        return None
    return True


def get_active_document(autocad_instance):
    try:
        active_document = autocad_instance.doc
    except Exception as e:
        print(f"Error from `get_active_document`: {e}")
        return None
    return active_document


def get_active_document_name(autocad_instance):
    try:
        active_document_name = autocad_instance.doc.Name
    except Exception as e:
        print(f"Error from `get_active_document`: {e}")
        return None
    return active_document_name


def save_active_document(autocad_instance):
    try:
        autocad_instance.doc.Save()
    except Exception as e:
        print(f"Error from `save_active_document`: {e}")
        return None
    return True


def close_active_document(autocad_instance):
    try:
        autocad_instance.doc.Close()
    except Exception as e:
        print(f"Error from `get_active_document`: {e}")
        return None
    return True


def print_in_autocad(autocad_instance, text):
    try:
        autocad_instance.prompt(text)
    except Exception as e:
        print(f"Error from: `get_active_document`: {e}")
        return None
    return True


def draw_circle(autocad_instance):
    random_x = random.randint(0, 100)
    random_y = random.randint(0, 100)

    # create a new circle
    try:
        # center = APoint(0, 0)
        center = APoint(random_x, random_y)
        radius = 10.0
        circle = autocad_instance.model.AddCircle(center, radius)
    except Exception as e:
        print(f"Error from `draw_circle`: {e}")
        return None
    return circle


def close_autocad(autocad_instance):
    try:
        autocad_instance.app.Quit()
    except Exception as e:
        print(f"Error from `close_autocad`: {e}")
        return None
    return True


def main():
    ac = start_autocad()
    sleep(5)
    open_document(ac, path)
    sleep(5)

    doc = get_active_document(ac)
    sleep(5)
    if doc:
        print(f'{doc} - {type(doc)}')

        name = get_active_document_name(ac)
        print(f'{name} - {type(name)}')
        sleep(5)

        circle = draw_circle(ac)
        print(f'{circle} - {type(circle)}')
        sleep(5)

        save_active_document(ac)
        sleep(5)

        close_active_document(ac)

    sleep(7)
    close_autocad(ac)


main()
