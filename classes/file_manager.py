class FileManager:

    @staticmethod
    def read_txt(path: str):
        if not path.endswith('.txt'):
            path += '.txt'
        with open(path, 'r', encoding='UTF-8') as file:
            return file.read()

    @staticmethod
    def read_bytes(path: str):
        with open(path, 'rb') as file:
            return file.read()

    @staticmethod
    def write_txt(path: str, data: str):
        with open(path, 'w', encoding='UTF-8') as file:
            file.write(data)

    @staticmethod
    def write_bytes(path: str, data: bytes):
        with open(path, 'wb') as file:
            file.write(data)
