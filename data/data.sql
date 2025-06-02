DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS categories;
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

INSERT INTO categories VALUES (1, 'Food');
INSERT INTO categories VALUES (2, 'Transportation');
INSERT INTO categories VALUES (3, 'Entertainment');
INSERT INTO categories VALUES (4, 'Utilities');
INSERT INTO categories VALUES (5, 'Healthcare');
INSERT INTO categories VALUES (6, 'Shopping');
INSERT INTO categories VALUES (7, 'Education');
INSERT INTO categories VALUES (8, 'Travel');
INSERT INTO categories VALUES (9, 'Other');