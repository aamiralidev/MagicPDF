from fpdf import FPDF

from fonts.font import Font
from to_pdf.font_owner import FontOwner

_COL_W = 30
_COL_H = 8


class ExcelToPdf(FontOwner):
    def __init__(self, pdf=None, font=None):
        super().__init__(font=font)
        self.pdf = pdf
        if self.pdf is None:
            self.pdf = FPDF(orientation='P', unit='mm', format='A4')
            self.pdf.add_page()
            self.pdf.set_font(self.font.family, self.font.style, self.font.size)

    def zip_w(self, columns, w):
        try:
            return zip(columns, w)
        except TypeError:
            return zip(columns, [w for _ in range(len(columns))])

    def set_columns(self, columns, w=_COL_W, h=_COL_H, border=None, ln=True):
        cols = self.zip_w(columns, w)
        for col, w in cols:
            self.pdf.cell(w=w, h=h, txt=str(col), border=border)
        if ln:
            self.pdf.ln(h)

    def _set_row(self, headers, row, h):
        for title, w in headers:
            # print(str(row[title]))
            self.pdf.cell(w=w, h=h, txt=str(row[title]), border=1)
        self.pdf.ln(h)

    def set_rows(self, cols, data, w=_COL_W, h=_COL_H):
        col_ids = self.zip_w(cols, w)
        for index, row in data.iterrows():
            self._set_row(col_ids, row, h=h)

    def update_font(self):
        self.pdf.set_font(style=self.font.style, family=self.font.family, size=self.font.size)
