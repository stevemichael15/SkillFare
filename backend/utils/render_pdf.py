# backend/utils/render_pdf.py
from playwright.sync_api import sync_playwright

def generate_pdf_from_url(url, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        page.pdf(path=output_path, format="A4", print_background=True)
        browser.close()
