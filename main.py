from js import window, document

def check_py(evt=None):
    registered = document.getElementById('registered').checked
    medical = document.getElementById('medical').checked
    gradeVal = document.getElementById('grade').value
    try:
        grade = int(gradeVal) if gradeVal else None
    except Exception:
        grade = None
    section = document.getElementById('section').value.strip()
    out = document.getElementById('result')
    out.innerHTML = ''

    missing = []
    if not registered:
        missing.append('Please register online to join the Intramurals.')
    if not medical:
        missing.append('Please secure a medical clearance before joining.')
    if grade is None or grade < 7 or grade > 10:
        missing.append('Student must be in Grade 7–10 to be eligible.')

    if len(missing) == 0:
        teams = {7: 'Blue Bears', 8: 'Red Bulldogs', 9: 'Yellow Tigers', 10: 'Green Hornets'}
        team = teams.get(grade, 'Assigned Team')
        out.innerHTML = (
            f"<p class='eligible'>Congratulations! You are eligible to join the Intramurals.</p>"
            f"<p class='team'>Assigned Team: <strong>{team}</strong></p>"
            f"<p>Grade &amp; Section: {grade} - {section or 'N/A'}</p>"
        )
    else:
        lis = ''.join(f"<li>{m}</li>" for m in missing)
        out.innerHTML = (
            "<p class='ineligible'>You are not eligible to join the Intramurals.</p>"
            f"<ul>{lis}</ul>"
        )

def init_app():
    button = document.getElementById('pycheck')
    if button:
        button.addEventListener('click', check_py)

init_app()
