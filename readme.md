# Personal Finance Tracker

A simplified personal finance tracking application designed to learn Docker while building something useful. This project focuses on core functionality with beginner-friendly technologies.

## 🎯 Project Overview

**Goal:** Build a containerized expense tracker that demonstrates Docker skills, basic web development, and database management.

**Duration:** 3-4 weeks (part-time)  
**Complexity:** Beginner-Intermediate  
**Learning Focus:** Docker, Python web development, database basics

## 🛠️ Tech Stack

| Component              | Technology                       | Why This Choice |
|------------------------|----------------------------------|-----------------|
| Backend                | **Flask** (Python)              | Much simpler than FastAPI, lots of tutorials |
| Database               | **SQLite** only                  | No database server needed, file-based |
| Frontend               | **Basic HTML + CSS + vanilla JS** | No frameworks to learn |
| Templates              | **Jinja2** (built into Flask)   | Simple server-side rendering |
| Charts                 | **Skip initially** or simple HTML tables | Avoid Chart.js complexity |
| Container              | **Docker** with simple setup    | Core learning objective |

## 📁 Project Structure

```
expense-tracker/
├── app/
│   ├── app.py                 # Main Flask application (everything in one file initially)
│   ├── database.py            # Simple SQLite setup
│   ├── templates/             # HTML templates
│   │   ├── base.html
│   │   ├── index.html         # Home page with expense list
│   │   ├── add_expense.html   # Form to add expense
│   │   └── reports.html       # Simple reports page
│   └── static/                # CSS and images
│       ├── style.css
│       └── images/
├── data/                      # SQLite database file goes here
├── Dockerfile                 # Single, simple Dockerfile
├── docker-compose.yml         # Simple setup
├── requirements.txt           # Python dependencies
├── .env.example              # Environment variables
├── README.md
└── .gitignore
```

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Basic understanding of Python and web development

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd expense-tracker
   ```

2. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```

3. **Access the application:**
   Open your browser and go to `http://localhost:5000`

### Development Setup

For development with live code reloading:

```bash
# Build the container
docker-compose build

# Run in development mode
docker-compose up
```

The application will automatically reload when you make changes to the code.

## 🐳 Docker Commands

### Basic Commands
```bash
# Build the image
docker-compose build

# Run the application
docker-compose up

# Run in background
docker-compose up -d

# Stop the application
docker-compose down

# View logs
docker-compose logs

# Rebuild and run
docker-compose up --build
```

### Database Persistence
The SQLite database is stored in the `./data` directory and persists between container restarts thanks to Docker volume mounting.

## 📋 Features

### Core Features (MVP)

1. **Simple Expense Tracking**
   - Add expenses with: amount, description, category, date
   - View list of all expenses
   - Edit and delete expenses
   - Basic search by description

2. **Categories**
   - Pre-defined categories: Food, Transportation, Entertainment, Shopping, Bills, Other
   - Simple dropdown selection (no custom categories initially)

3. **Basic Reports**
   - Total spent this month
   - Spending by category (simple table, no charts initially)
   - Monthly totals

4. **Data Persistence**
   - SQLite database (simple, no PostgreSQL complexity)
   - Basic CSV export

## 💾 Database Schema

```sql
-- categories table
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- expenses table  
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
```

## 🔄 Development Phases

### Phase 1: Basic Flask App (Week 1)
- [x] Create simple Flask app that runs locally
- [x] Set up SQLite database with basic tables
- [x] Create HTML form to add expenses
- [x] Display list of expenses on home page
- [x] Learn basic Docker commands

**Docker Goal:** Get the app running in a container

### Phase 2: Docker Integration (Week 2)  
- [ ] Write Dockerfile that works
- [ ] Create docker-compose.yml
- [ ] Make database persist between container restarts
- [ ] Learn Docker volume mounting
- [ ] Practice rebuilding containers

**Docker Goal:** Comfortable with basic Docker workflow

### Phase 3: Features & Polish (Week 3)
- [ ] Add edit/delete functionality
- [ ] Simple search feature
- [ ] Basic monthly totals
- [ ] CSV export
- [ ] Improve styling

**Docker Goal:** Multi-stage builds or production setup

### Phase 4: Optional Enhancements (Week 4)
- [ ] Simple charts (if feeling ambitious)
- [ ] Date filtering
- [ ] Better responsive design
- [ ] Deploy to cloud service

## 📚 Learning Resources

### Flask (Easy to Learn)
- Official Flask Tutorial: https://flask.palletsprojects.com/tutorial/
- Flask in 20 minutes: YouTube has many short tutorials
- Much simpler than FastAPI for beginners

### Docker Basics
- Official Docker Tutorial: https://docs.docker.com/get-started/
- "Docker for Beginners" courses on YouTube
- Focus on: `docker build`, `docker run`, `docker-compose up`

### SQLite (Very Simple)
- Built into Python, no server setup needed
- Simple SQL queries only
- DB Browser for SQLite (GUI tool to view your data)

## 💡 Success Strategy

### Start Super Simple
1. **First:** Get Flask app working locally (no Docker)
2. **Second:** Get same app working in Docker container
3. **Third:** Add one feature at a time
4. **Fourth:** Learn more Docker features as you go

### Docker Learning Milestones
- [ ] "Hello World" Flask app in container
- [ ] App with database in container
- [ ] Data persists when container restarts
- [ ] Can rebuild and update app easily
- [ ] Understand difference between development and production setups

## 🔄 Expansion Path

Once comfortable with basics, you can easily add:
- User authentication (session-based, not JWT)
- PostgreSQL (using Docker container)
- Simple budgets
- Basic charts
- More advanced Docker features

But start simple and build confidence first!

## 📖 Portfolio Value

Even this simplified version shows:
- **Python web development** (Flask)
- **Database skills** (SQLite, basic SQL)
- **Containerization** (Docker fundamentals)
- **Full-stack thinking** (HTML, CSS, backend)
- **Problem-solving** (building something useful)

## 🤝 Contributing

This is a learning project, but feel free to suggest improvements or report issues!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).