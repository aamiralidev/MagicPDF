from pathlib import Path

import pandas as pd

from fonts.font import Font
from to_pdf.Converter import Converter
from to_pdf.excel_to_pdf import ExcelToPdf


class ExcelToInvoice(Converter):

    def __init__(self, filename, converter=None, font=None):
        self.converter = converter if converter is not None else ExcelToPdf(
            font=font if font is not None else Font()
        )
        self.filename = filename
        self.df = self.get_data()

    def get_data(self):
        return pd.read_excel(self.filename)

    def write_header(self):
        invoice_nr, date = Path(self.filename).stem.split('-')
        self.converter.pdf.cell(w=50, h=8, txt=f'Invoice nr.{invoice_nr}', ln=1)
        self.converter.pdf.cell(w=50, h=8, txt=f'Date: {date}', ln=1)

    def get_column_titles(self):
        return [item.replace('-', ' ').title() for item in self.df.columns]

    def write_data(self):
        self.converter.set_font_size(10)
        self.converter.pdf.set_text_color(80, 80, 80)
        self.converter.set_columns(self.get_column_titles(), 35, 8, ln=True, border=1)
        self.converter.set_rows(self.df.columns, self.df, 35, 8)

    def write_footer(self):
        total_sum = self.df['total_price'].sum()

        self.converter.pdf.cell(w=30, h=8, txt=f'The total price is {total_sum}', ln=1)

        self.converter.pdf.cell(w=25, h=8, txt=f'PythonHow')
        self.converter.pdf.image('pythonhow.png', w=10)

    def get_output_filepath(self):
        return f'PDFs/{Path(self.filename).stem}.pdf'

    def get_pdf(self):
        return self.converter.pdf

