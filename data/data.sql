DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
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

INSERT INTO expenses (id, amount, description, category_id, expense_date, created_at) VALUES
(12345, 45.32, 'Grocery shopping at Walmart', 1, '2025-05-28', '2025-05-28 14:30:00'),
(23456, 12.50, 'Coffee and pastry', 1, '2025-06-01', '2025-06-01 08:15:00'),
(34567, 65.00, 'Gas fill-up', 2, '2025-05-30', '2025-05-30 16:45:00'),
(45678, 89.99, 'Monthly gym membership', 5, '2025-06-01', '2025-06-01 09:00:00'),
(56789, 25.75, 'Movie tickets', 3, '2025-05-25', '2025-05-25 19:30:00'),
(67890, 150.00, 'Electricity bill', 4, '2025-05-15', '2025-05-15 10:00:00'),
(78901, 32.48, 'Lunch with friends', 1, '2025-05-20', '2025-05-20 12:30:00'),
(89012, 78.90, 'New running shoes', 6, '2025-05-18', '2025-05-18 15:20:00'),
(90123, 15.99, 'Netflix subscription', 3, '2025-05-01', '2025-05-01 00:05:00'),
(01234, 42.00, 'Uber rides', 2, '2025-05-22', '2025-05-22 18:45:00');