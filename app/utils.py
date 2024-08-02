from io import BytesIO  # Import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from django.http import FileResponse
from .models import Vehicle

def generate_receipt(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    elements = []

    data = [
        ["Field", "Value"],
        ["Plate Number", vehicle.plate_number],
        ["Driver Name", vehicle.driver_name],
        ["Entry Weight (kg)", vehicle.entry_weight],
        ["Exit Weight (kg)", vehicle.exit_weight],
        ["Net Weight (kg)", vehicle.net_weight],
        ["Entry Time", vehicle.entry_time],
        ["Exit Time", vehicle.exit_time],
    ]

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ]))

    elements.append(table)
    doc.build(elements)
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='receipt.pdf')

