from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from faker import Faker
import random

# Initialize
fake = Faker()
styles = getSampleStyleSheet()

# Create document
doc = SimpleDocTemplate("enterprise_sales_report.pdf", pagesize=letter)
elements = []

# ---------- Helper Functions ----------

def currency(val):
    return "${:,.2f}".format(val)

def generate_kpis():
    revenue = random.randint(50000, 500000)
    orders = random.randint(200, 2000)
    avg_order = revenue / orders
    growth = round(random.uniform(-5, 20), 2)

    return [
        ["Metric", "Value"],
        ["Total Revenue", currency(revenue)],
        ["Total Orders", str(orders)],
        ["Avg Order Value", currency(avg_order)],
        ["Growth %", str(growth) + "%"]
    ]

def generate_sales_table(rows=25):
    data = [["Date", "Customer", "Region", "Product", "Qty", "Unit Price", "Revenue"]]

    for _ in range(rows):
        qty = random.randint(1, 10)
        price = round(random.uniform(20, 500), 2)
        revenue = qty * price

        data.append([
            fake.date(),
            fake.name(),
            fake.state(),
            fake.word().capitalize(),
            str(qty),
            currency(price),
            currency(revenue)
        ])
    return data

def styled_table(data):
    table = Table(data, repeatRows=1)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.grey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (4, 1), (-1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ]))

    return table

# ---------- Cover Page ----------
elements.append(Paragraph("Global Sales Performance Report", styles["Title"]))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Prepared by: Analytics Team", styles["Normal"]))
elements.append(Paragraph("Generated on: " + fake.date(), styles["Normal"]))
elements.append(PageBreak())

# ---------- Generate 100 Pages ----------
for page in range(100):

    # Title
    elements.append(Paragraph("Sales Report - Section {}".format(page + 1), styles["Heading2"]))
    elements.append(Spacer(1, 10))

    # Executive Summary
    elements.append(Paragraph("Executive Summary", styles["Heading3"]))
    elements.append(Paragraph(fake.paragraph(nb_sentences=5), styles["Normal"]))
    elements.append(Spacer(1, 12))

    # KPI Table
    elements.append(Paragraph("Key Performance Indicators", styles["Heading3"]))
    elements.append(styled_table(generate_kpis()))
    elements.append(Spacer(1, 12))

    # Sales Table
    elements.append(Paragraph("Detailed Sales Data", styles["Heading3"]))
    elements.append(styled_table(generate_sales_table(25)))

    # Footer Note
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "Note: This is a system-generated report for analytics and testing purposes.",
        styles["Italic"]
    ))

    elements.append(PageBreak())

# ---------- Build PDF ----------
doc.build(elements)

print("100-page enterprise sales PDF generated successfully.")