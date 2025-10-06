import os


class FileManager:

    @staticmethod
    def read_txt(*args):
        path = os.path.join(*args)
        if not path.endswith('.txt'):
            path += '.txt'
        with open(path, 'r', encoding='UTF-8') as file:
            return file.read()

    @staticmethod
    def read_bytes(path: str):
        with open(path, 'rb') as file:
            return file.read()

    @staticmethod
    def write_txt(*args, data: str):
        path = os.path.join(*args)
        if not path.endswith('.txt'):
            path += '.txt'
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(data)

    @staticmethod
    def write_bytes(path: str, data: bytes):
        with open(path, 'wb') as file:
            file.write(data)
