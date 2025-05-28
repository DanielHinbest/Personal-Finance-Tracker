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

INSERT INTO categories VALUES (1, 'test');
INSERT INTO expenses (id, amount, description, category_id, expense_date) VALUES (1, 5.99, 'test', 1, '2025-05-27');
