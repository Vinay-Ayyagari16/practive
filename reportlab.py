from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

# Output PDF path
pdf_path = "/home/thrymr/Downloads/pest_control_invoice1.pdf"

# Create canvas
c = canvas.Canvas(pdf_path, pagesize=A4)
width, height = A4

# Title
c.setFont("Helvetica-Bold", 20)
c.drawString(50, height - 50, "LOHITHA PEST CONTROL SERVICES")
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 70, "Serviceman Address :")
c.setFont("Helvetica", 12)
c.drawString(50, height - 85, "Shop number 8-3-228/481, Rahmath nagar")
c.drawString(50, height - 97, "Yousufguda-500045 (Rahmath nagar Circle)")
# Date and customer address heading
c.setFont("Helvetica-Bold", 12)
c.drawString(50, height - 130, "Customer Address :")
c.drawRightString(width - 50, height - 100, "Date: 24-05-2025")
c.setFont("Helvetica", 10)
# Customer address details
address_lines = [
    "XILINX INDIA TECHNOLOGY SERVICES PVT LTD,",
    "OCTAVE 2A, AND 2B, PARCEL 4.11 TO 17TH FLOOR,",
    "SALARPURIA SATTVA KNOWLEDGE CITY, SURVEY",
    "NO 83/1, RAIDURG, Serlingampally Circle No 30, Hyderabad,",
    "Telangana – 500081"
]

y = height - 162
for line in address_lines:
    c.drawString(50, y, line)
    y -= 12

# Table Data
data = [
    ["Sl.No", "Service Area", "Chemical Name", "Chemical Qty", "Chemical Quality"],
    ["1", "Tea counter\n8×10=80 sq ft", "Delta Flow\n(Deltamethrin 2.5% SC)", "250ml", "100% Pure"],
    ["2", "Tea counter\n8×10=80 sq ft", "Propaxure", "200 ml", "100% Pure"]
]

# Create Table with formatting

table = Table(data, colWidths=[40, 120, 150, 80, 100])
table.setStyle(TableStyle([
    ("BOX", (0, 0), (-1, -1), 1, colors.black),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
]))

# Table placement
table.wrapOn(c, width, height)
table.drawOn(c, 50, y - 100)
c.setFont("Helvetica", 15)
# Signature line
c.drawString(50, y - 500, "Customer sign: ---------------------------")

# Finalize PDF
c.save()