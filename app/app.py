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
    total = None
    monthly_total = None
    weekly_total = None
    now = datetime.datetime.now()
    current_year = now.year
    current_month = now.month
    current_week = now.strftime("%W")

    if error is None:
        try:
            expenses = data.execute("SELECT * FROM expenses ORDER BY expense_date DESC").fetchall()
            total = data.execute("SELECT SUM(amount) FROM expenses").fetchone()[0] or 0
            total = f"{total:.2f}"

            monthly_total = data.execute("""
                                         SELECT SUM(amount) 
                                         FROM expenses 
                                         WHERE strftime('%Y', expense_date) = ? 
                                           AND strftime('%m', expense_date) = ?
                                             """, (str(current_year), f"{current_month:02d}")).fetchone()[0]
            monthly_total = f"{monthly_total:.2f}"

            weekly_total = data.execute("""
                                        SELECT SUM(amount)
                                        FROM expenses
                                        WHERE strftime('%Y', expense_date) = ?
                                          AND strftime('%W', expense_date) = ?
                                        """, (str(current_year), current_week)).fetchone()[0]
            weekly_total = f"{weekly_total:.2f}"
        except:
            error = "Database error"

    flash(error)

    return render_template('index.html', expenses=expenses, total_expenses=total, monthly_total=monthly_total, weekly_total=weekly_total)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    try:
        data = db.get_db()
        categories = data.execute("SELECT * FROM categories").fetchall()
    except Exception as e:
        flash(f"Database error: {str(e)}", category="danger")
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

    return render_template('add_expense.html', categories=categories)

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    if request.method == 'POST':
        data = db.get_db()
        try:
            data.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
            data.commit()
            flash("Expense deleted", category="success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Database error: {str(e)}", category="danger")
    return redirect(url_for('index'))

@app.route('/reports', methods=['GET'])
def reports():
    data = db.get_db()
    error = None
    expenses = None
    categories = []

    search_query = request.args.get('q', '').strip()
    selected_category = request.args.get('category', '').strip()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()

    if error is None:
        try:
            categories = data.execute("SELECT * FROM categories").fetchall()

            search_sql = """
                SELECT expenses.*, categories.name as category_name
                FROM expenses 
                JOIN categories ON expenses.category_id = categories.id
                WHERE 1=1
            """
            params = []

            if search_query:
                search_sql += " AND (expenses.description LIKE ? OR categories.name LIKE ?)"
                params += [f"%{search_query}%", f"%{search_query}%"]

            if selected_category:
                search_sql += "AND categories.name = ?"
                params.append(selected_category)

            if start_date:
                search_sql += " AND expense_date >= ?"
                params.append(start_date)

            if end_date:
                search_sql += " AND expense_date <= ?"
                params.append(end_date)

            search_sql += " ORDER BY expense_date DESC"

            expenses = data.execute(search_sql, params).fetchall()
        except:
            error = "Database error"
            expenses = []
            categories = []

    flash(error)
    return render_template('reports.html', expenses=expenses, categories=categories, search_query=search_query, selected_category=selected_category, start_date=start_date, end_date=end_date)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
