import abc
from pathlib import Path


class Converter(abc.ABC):
    def convert(self):
        self.write_header()
        self.write_data()
        self.write_footer()
        return self

    def save(self):
        self.get_pdf().output(self.get_output_filepath())
        return self

    def convert_and_save(self):
        self.convert()
        self.save()

    @abc.abstractmethod
    def write_header(self):
        pass

    @abc.abstractmethod
    def write_data(self):
        pass

    @abc.abstractmethod
    def write_footer(self):
        pass

    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def get_output_filepath(self):
        pass

    @abc.abstractmethod
    def get_pdf(self):
        pass
