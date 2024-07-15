from fpdf import FPDF
import pandas as pd

# Set page settings
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Adding a page
    pdf.add_page()

    # Creating the header
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 102)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # Creating the lined page
    for y in range(20, 298, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # Creating the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        # Creating the lined page
        for y in range(20, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)


pdf.output("output.pdf")
