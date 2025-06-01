from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    return render_template('add_expense.html')

@app.route('/reports')
def reports():
    # expenses = get_expenses_from_db()  # Your data logic
    return render_template('reports.html')
    # return render_template('reports.html', expenses=expenses)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
