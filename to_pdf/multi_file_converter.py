import glob

from to_pdf.Converter import Converter


class MultiFileConverter:
    def __init__(self, path):
        self._path = path
        self.files = None

    def path(self, value=None):
        if value is None:
            return self._path
        else:
            self._path = value

    def convert(self, converter, *args, **kwargs):
        self.files = [converter(filepath, *args, **kwargs).convert() for filepath in glob.glob(self.path)]
        return self

    def save(self):
        for file in self.files:
            file.save()

    def convert_and_save(self, converter, *args, **kwargs):
        for filepath in glob.glob(self._path):
            converter(filepath, *args, **kwargs).convert().save()

