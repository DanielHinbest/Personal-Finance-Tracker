import datetime
import os
import random

from flask import Flask, render_template, request, flash, redirect, url_for
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
    if request.method == 'POST':
        id = random.randint(10000, 99999)
        amount = request.form['amount']
        description = request.form['description']
        category_name = request.form['category']
        expense_date = request.form['expense_date']
        created_at = datetime.datetime.now()
        data = db.get_db()

        errors = []
        if not amount:
            errors.append("Please enter an amount")
        if not description:
            errors.append("Please enter a description")
        if not category_name:
            errors.append("Please select a category")
        if not expense_date:
            errors.append("Please select an expense date")

        if errors:
            for error in errors:
                flash(error)
            return render_template('add_expense.html')

        try:
            category_row = data.execute("SELECT id FROM categories WHERE name = ?", (category_name,)).fetchone()
            if category_row is None:
                flash("Invalid category")
                return render_template("add_expense.html")

            category_id = category_row['id']
            data.execute(
                "INSERT INTO expenses (id, amount, description, category_id, expense_date, created_at) VALUES (?, ?, ?, ?, ?, ?)",
                (id, amount, description, category_id, expense_date, created_at)
            )
            data.commit()
            flash(f"{description} added to expenses", category="success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Database error: {str(e)}", category="danger")
    return render_template('add_expense.html')

@app.route('/reports')
def reports():
    data = db.get_db()
    error = None
    expenses = None

    if error is None:
        try:
            expenses = data.execute("SELECT * FROM expenses, categories WHERE category_id=categories.id").fetchall()
            categories = data.execute("SELECT * FROM categories").fetchall()
        except:
            error = "Database error"

    flash(error)
    return render_template('reports.html', expenses=expenses, categories=categories)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
