from fpdf import FPDF
import pandas as pd


# load data
df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():

    # create header page
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # adds lines after the underlining header
    # comment out to remove, add lines fcn?
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # set footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # add pages equal to "Pages" col - 1
    # first page with header already printed above
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # set footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        # adds lines after the underlining header
        # comment out to remove, add lines fcn?
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")
