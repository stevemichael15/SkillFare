# backend/utils/pdf_utils.py
from xhtml2pdf import pisa
from flask import render_template
from io import BytesIO

def generate_pdf_from_html(template_name, context):
    html = render_template(template_name, **context)
    pdf_buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=pdf_buffer)
    if pisa_status.err:
        return None
    pdf_buffer.seek(0)
    return pdf_buffer
