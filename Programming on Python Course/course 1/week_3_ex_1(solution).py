class FileReader:

    """
    Класс FileReader помогает читать из файла
    """

    def __init__(self, way_to_file):
        self._way_to_file = way_to_file

    def read(self):
        try:
            with open(self._way_to_file, 'r') as file:
                return file.read()
        except IOError:
            return ''
