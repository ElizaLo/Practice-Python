import tempfile
import os.path
import random

class File:
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def __add__(self, other):
        new_file_obj = File(os.path.join(tempfile.gettempdir(), str(random.randint(0,100))))
        new_file_obj.write(self.read() + other.read())
        return new_file_obj

    def __iter__(self):
        self._current = -1
        with open(self.path, 'r') as f:
            self._lines = f.readlines()
        return self

    def __next__(self):
        if self._current + 1 >= len(self._lines):
            raise StopIteration()
        line = self._lines[self._current + 1]
        self._current += 1
        return line

    def __str__(self):
        return self.path

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)
