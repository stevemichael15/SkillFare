from flask import Blueprint, request, jsonify, render_template
from backend.ml.ml_logic import generate_analysis

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/analysis', methods=['POST'])
def analyze():
    try:
        data = request.get_json()

        domains = data.get('domains', [])
        skill_level = data.get('skillLevel', 'Beginner')  # default to Beginner

        if not domains:
            return jsonify({"error": "No domains provided"}), 400

        result = generate_analysis(domains, skill_level)
        return jsonify({"status": "success", "analysis": result}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


# Optionally, if you want to support form POSTs as well:
@analysis_bp.route('/analysis', methods=['GET', 'POST'])
def analysis_form():
    if request.method == 'POST':
        selected_domains = request.form.getlist('domains')
        skill_level = request.form.get('skillLevel', 'Beginner')
        analysis = generate_analysis(selected_domains, skill_level)
        return render_template('analysis.html', analysis=analysis, skill_level=skill_level)
    return render_template('analysis.html')
