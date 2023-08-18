
from fpdf import FPDF
import pandas as pd

from to_pdf.excel_to_invoice import ExcelToInvoice
from to_pdf.multi_file_converter import MultiFileConverter
from to_pdf.text_to_pdf import TextToPdf

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font(family='Times', style='B', size=12)
# h or height is recommended to be set the same size as font size
pdf.cell(w=0, h=12, txt='Hello there', align='L', ln=1)
pdf.set_font(family='Times', style='B', size=10)
pdf.cell(w=0, h=12, txt='Hey there', align='L', ln=1)

pdf.add_page()
pdf.set_font(family='Times', style='B', size=12)
# h or height is recommended to be set the same size as font size
pdf.cell(w=0, h=12, txt='Hello there', align='L', ln=1)
pdf.set_font(family='Times', style='B', size=10)
pdf.cell(w=0, h=12, txt='Hey there', align='L', ln=1)

pdf.output('output.pdf')

pdf = FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    # h or height is recommended to be set the same size as font size
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    pdf.line(10, 21, 200, 21)

    # setting footer
    pdf.ln(265)
    pdf.set_font(family='Times', style='B', size=8)
    pdf.set_text_color(180, 180, 180)
    # h or height is recommended to be set the same size as font size
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)

    for i in range(row['Pages']-1):
        pdf.add_page()

        pdf.ln(277)
        pdf.set_font(family='Times', style='B', size=8)
        pdf.set_text_color(180, 180, 180)
        # h or height is recommended to be set the same size as font size
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=1)

pdf.output('output.pdf')

MultiFileConverter('invoices/*.xlsx').convert_and_save(ExcelToInvoice)
MultiFileConverter('Text Files/*.txt').convert_and_save(TextToPdf)
