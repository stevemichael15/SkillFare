
from flask import Blueprint, request, session, render_template, make_response, redirect, url_for
from flask import send_file
from backend.ml.ml_logic import generate_analysis
from backend.utils.pdf_utils import generate_pdf_from_html
import pdfkit
pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
ml_bp = Blueprint("ml", __name__)

@ml_bp.route("/")
def index():
    return render_template("index.html")
  

@ml_bp.route("/analysis", methods=["POST", "GET"])
def analysis():
    from_pdf = request.args.get("from_pdf") == "true"

    if request.method == "POST":
        domains = request.form.getlist("domains")
        skill_level = request.form.get("skill_level", "Beginner")
        user_text = request.form.get("user_text", None)

        results = generate_analysis(domains=domains, skill_level=skill_level, user_text=user_text)
        predicted = None
        if user_text:
            predicted = list(results.keys())[0]

        # Save to session
        session["analysis_results"] = results
        session['selected_domains'] = domains
        session["skill_level"] = skill_level
        session['predicted_domain'] = predicted

        return render_template(
            "analysis_pdf.html" if from_pdf else "analysis.html",
            analysis=results,
            skill_level=skill_level,
            predicted=predicted,
            from_pdf=from_pdf
        )

    # On GET (fallback or direct visit), check if analysis exists
    analysis_results = session.get("analysis_results")
    skill_level = session.get("skill_level", "Beginner")
    predicted = session.get("predicted_domain")

    if not analysis_results:
        return redirect("/home")

    return render_template(
        "analysis_pdf.html" if from_pdf else "analysis_pdf.html",
        analysis=analysis_results,
        skill_level=skill_level,
        predicted=predicted,
        from_pdf=from_pdf
    )

@ml_bp.route("/download-pdf")
def download_pdf():
    analysis_data = session.get("analysis_results")
    skill_level = session.get("skill_level", "Beginner")
    predicted = session.get("predicted_domain")

    if not analysis_data:
        return "No analysis data found in session", 400

    rendered = render_template("analysis_pdf.html",
                               analysis=analysis_data,
                               skill_level=skill_level,
                               predicted=predicted,
                               from_pdf=True)

    # Use configuration here
    pdf = pdfkit.from_string(rendered, False, configuration=pdfkit_config)

    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=skillfare_analysis.pdf"

    return response

