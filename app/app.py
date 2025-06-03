import datetime
import os

from flask import Flask, render_template, request, flash, redirect, url_for, session, g
import app.database as db
from app.auth import bp as auth_bp, login_required

app = Flask(__name__)
app.secret_key = 'my-portfolio-secret-key'
app.config['DATABASE'] = os.path.abspath(os.path.join(app.root_path, '..', 'data', 'data.sqlite'))
db.init_app(app)
app.register_blueprint(auth_bp)


@app.route('/')
@login_required
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
            user_id = session.get('user_id')
            expenses = data.execute("""
                                    SELECT *
                                    FROM expenses
                                    WHERE user_id = ?
                                    ORDER BY expense_date DESC
                                    """, (user_id,)).fetchall()

            total = data.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,)).fetchone()[0] or 0
            total = f"{total:.2f}"

            monthly_total = data.execute("""
                                         SELECT SUM(amount)
                                         FROM expenses
                                         WHERE user_id = ?
                                           AND strftime('%Y', expense_date) = ?
                                           AND strftime('%m', expense_date) = ?
                                         """, (user_id, str(current_year), f"{current_month:02d}")).fetchone()[0] or 0
            monthly_total = f"{monthly_total:.2f}"

            weekly_total = data.execute("""
                                        SELECT SUM(amount)
                                        FROM expenses
                                        WHERE user_id = ?
                                          AND strftime('%Y', expense_date) = ?
                                          AND strftime('%W', expense_date) = ?
                                        """, (user_id, str(current_year), current_week)).fetchone()[0] or 0
            weekly_total = f"{weekly_total:.2f}"
        except Exception as e:
            error = f"Database error: {str(e)}"

    if error:
        flash(error)

    return render_template('index.html', expenses=expenses, total_expenses=total, monthly_total=monthly_total,
                           weekly_total=weekly_total)


@app.route('/add_expense', methods=['GET', 'POST'])
@login_required
def add_expense():
    try:
        data = db.get_db()
        categories = data.execute("SELECT * FROM categories").fetchall()
    except Exception as e:
        flash(f"Database error: {str(e)}", category="danger")
        categories = []

    if request.method == 'POST':
        amount = request.form['amount']
        description = request.form['description']
        category_name = request.form['category']
        expense_date = request.form['expense_date']
        created_at = datetime.datetime.now()
        user_id = session.get('user_id')  # Get current user
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
            return render_template('add_expense.html', categories=categories)

        try:
            category_row = data.execute("SELECT id FROM categories WHERE name = ?", (category_name,)).fetchone()
            if category_row is None:
                flash("Invalid category")
                return render_template("add_expense.html", categories=categories)

            category_id = category_row['id']
            data.execute(
                "INSERT INTO expenses (amount, description, category_id, expense_date, created_at, user_id) VALUES (?, ?, ?, ?, ?, ?)",
                (amount, description, category_id, expense_date, created_at, user_id)
            )
            data.commit()
            flash(f"{description} added to expenses", category="success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Database error: {str(e)}", category="danger")

    return render_template('add_expense.html', categories=categories, today=datetime.date.today().isoformat())


@app.route('/delete/<int:expense_id>', methods=['POST'])
@login_required
def delete_expense(expense_id):
    if request.method == 'POST':
        data = db.get_db()
        user_id = session.get('user_id')
        try:
            data.execute("DELETE FROM expenses WHERE id = ? AND user_id = ?", (expense_id, user_id))
            data.commit()
            flash("Expense deleted", category="success")
            return redirect(url_for('index'))
        except Exception as e:
            flash(f"Database error: {str(e)}", category="danger")
    return redirect(url_for('index'))


@app.route('/reports', methods=['GET'])
@login_required
def reports():
    data = db.get_db()
    error = None
    expenses = None
    categories = []
    user_id = session.get('user_id')

    search_query = request.args.get('q', '').strip()
    selected_category = request.args.get('category', '').strip()
    start_date = request.args.get('start_date', '').strip()
    end_date = request.args.get('end_date', '').strip()

    total_amount = 0
    category_totals = {}

    if error is None:
        try:
            categories = data.execute("SELECT * FROM categories").fetchall()

            search_sql = """
                         SELECT expenses.*, categories.name as category_name
                         FROM expenses
                                  JOIN categories ON expenses.category_id = categories.id
                         WHERE expenses.user_id = ? \
                         """
            params = [user_id]

            if search_query:
                search_sql += " AND (expenses.description LIKE ? OR categories.name LIKE ?)"
                params += [f"%{search_query}%", f"%{search_query}%"]

            if selected_category:
                search_sql += " AND categories.name = ?"
                params.append(selected_category)

            if start_date:
                search_sql += " AND expense_date >= ?"
                params.append(start_date)

            if end_date:
                search_sql += " AND expense_date <= ?"
                params.append(end_date)

            search_sql += " ORDER BY expense_date DESC"

            expenses = data.execute(search_sql, params).fetchall()

            if expenses:
                total_amount = sum(expense['amount'] for expense in expenses)

                for expense in expenses:
                    category = expense['category_name']
                    if category in category_totals:
                        category_totals[category] += expense['amount']
                    else:
                        category_totals[category] = expense['amount']

        except Exception as e:
            error = f"Database error: {str(e)}"
            expenses = []
            categories = []

    if error:
        flash(error)

    return render_template('reports.html',
                           expenses=expenses,
                           categories=categories,
                           search_query=search_query,
                           selected_category=selected_category,
                           start_date=start_date,
                           end_date=end_date,
                           total_amount=total_amount,
                           category_totals=category_totals)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)