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

-- Insert categories
INSERT INTO categories VALUES (1, 'Food');
INSERT INTO categories VALUES (2, 'Transportation');
INSERT INTO categories VALUES (3, 'Entertainment');
INSERT INTO categories VALUES (4, 'Utilities');
INSERT INTO categories VALUES (5, 'Healthcare');
INSERT INTO categories VALUES (6, 'Shopping');
INSERT INTO categories VALUES (7, 'Education');
INSERT INTO categories VALUES (8, 'Travel');
INSERT INTO categories VALUES (9, 'Other');

-- Insert sample expenses for demo user (user_id = 1)
INSERT INTO expenses (amount, description, category_id, expense_date, user_id) VALUES
-- Recent expenses (last 2 weeks)
(12.50, 'Lunch at downtown cafe', 1, '2025-06-02', 1),
(45.20, 'Grocery shopping at Superstore', 1, '2025-06-01', 1),
(15.75, 'Coffee and pastry', 1, '2025-05-31', 1),
(8.50, 'Bus fare for the week', 2, '2025-05-30', 1),
(25.00, 'Movie tickets', 3, '2025-05-29', 1),
(120.50, 'Monthly internet bill', 4, '2025-05-28', 1),
(67.30, 'New running shoes', 6, '2025-05-27', 1),
(18.90, 'Lunch with colleagues', 1, '2025-05-26', 1),
(9.99, 'Netflix subscription', 3, '2025-05-25', 1),
(32.40, 'Gas for car', 2, '2025-05-24', 1),

-- Older expenses (last month)
(95.75, 'Weekly groceries', 1, '2025-05-20', 1),
(200.00, 'Electricity bill', 4, '2025-05-15', 1),
(75.50, 'Dinner at Italian restaurant', 1, '2025-05-12', 1),
(40.00, 'Uber rides', 2, '2025-05-10', 1),
(150.00, 'New winter jacket', 6, '2025-05-08', 1),
(85.20, 'Pharmacy prescription', 5, '2025-05-05', 1),
(22.30, 'Book for learning Python', 7, '2025-05-03', 1),
(180.00, 'Weekend getaway hotel', 8, '2025-05-01', 1),

-- Mix of categories to show variety
(13.45, 'Fast food lunch', 1, '2025-04-28', 1),
(5.50, 'Coffee shop', 1, '2025-04-25', 1),
(35.00, 'Concert tickets', 3, '2025-04-22', 1),
(110.00, 'Phone bill', 4, '2025-04-20', 1),
(45.60, 'Clothing store purchase', 6, '2025-04-18', 1),
(60.00, 'Doctor visit co-pay', 5, '2025-04-15', 1),
(28.75, 'Online course subscription', 7, '2025-04-12', 1),
(250.00, 'Flight booking', 8, '2025-04-10', 1),
(15.99, 'Miscellaneous household items', 9, '2025-04-08', 1);