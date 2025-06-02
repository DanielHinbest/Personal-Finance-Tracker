import os

from flask import Flask, render_template, request, flash
import app.database as db

app = Flask(__name__)
app.secret_key = 'my-portfolio-secret-key'
app.config['DATABASE'] = os.path.abspath(os.path.join(app.root_path, '..', 'data', 'data.sqlite'))
db.init_app(app)

@app.route('/')
def index():
    data = db.get_db()
    error = None
    expenses = None

    if error is None:
        try:
            expenses = data.execute("SELECT * FROM expenses").fetchall()
        except:
            error = "Database error"

    flash(error)

    return render_template('index.html', expenses=expenses)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    return render_template('add_expense.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
