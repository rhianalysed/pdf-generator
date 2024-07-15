from fpdf import FPDF
import pandas as pd

# Set page settings
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    # Adding a page
    pdf.add_page()
    # Adding items to the page
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(0, 0, 102)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=22, x2=200, y2=22)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

pdf.output("output.pdf")
