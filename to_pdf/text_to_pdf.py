from pathlib import Path

from fpdf import FPDF

from fonts.font import Font
from to_pdf.Converter import Converter
from to_pdf.font_owner import FontOwner


class TextToPdf(FontOwner, Converter):

    def __init__(self, filename, pdf=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filename = filename
        self.pdf = pdf
        self.data = self.get_data()
        if self.pdf is None:
            self.pdf = FPDF(orientation='P', unit='mm', format='A4')
            self.pdf.add_page()
            self.pdf.set_font(self.font.family, self.font.style, self.font.size)

    def update_font(self):
        self.pdf.set_font(style=self.font.style, family=self.font.family, size=self.font.size)

    def write_header(self):
        self.pdf.cell(w=50, h=8, txt=Path(self.filename).stem.title(), ln=1)

    def write_data(self):
        line_width = int(self.pdf.w)
        page_height = int(self.pdf.h)
        lines_on_page = 0
        current_index = 0
        margin = 5
        data = self.data.split('\n')
        for line in data:
            while current_index < len(line):
                self.pdf.cell(w=50, h=8, txt=line[current_index:(current_index+line_width//2)-margin], ln=1)
                current_index += line_width//2 - margin
                lines_on_page += 1
                if lines_on_page * 8 + 8 > page_height:
                    self.pdf.add_page()
            current_index = 0

    def write_footer(self):
        pass

    def get_data(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def get_output_filepath(self):
        return f'TXTs/{Path(self.filename).stem}.pdf'

    def get_pdf(self):
        return self.pdf
