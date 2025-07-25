from flask import Blueprint, session, render_template, request, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if request.method == 'POST':
        selected_domains = request.form.getlist('domains')
        session['domains'] = selected_domains
        return redirect(url_for('ml.analysis'))
    return render_template('dashboard.html')