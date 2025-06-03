# Personal Finance Tracker

A containerized personal finance application built with Flask and Docker, featuring expense tracking, categorization, and reporting capabilities.

## 🚀 Live Demo

[View Live Application](your-deployment-url-here) | [View Source Code](https://github.com/DanielHinbest/Personal-Finance-Tracker)

## 📋 Project Overview

This full-stack web application allows users to track personal expenses with comprehensive filtering and reporting features. Built as a learning project to demonstrate containerization skills, database management, and modern web development practices.

**Key Achievements:**
- Containerized Flask application with Docker
- SQLite database with proper schema design
- Responsive web interface with server-side rendering
- Advanced search and filtering capabilities
- Date-based expense analysis and summaries

## ✨ Features

### Core Functionality
- **Expense Management**: Add, view, and delete expenses with detailed categorization
- **Smart Categorization**: Predefined categories (Food, Transportation, Entertainment, Shopping, Bills, Other)
- **Advanced Search**: Filter by description, category, and date ranges
- **Financial Summaries**: Real-time calculations for weekly, monthly, and total spending
- **Data Persistence**: Reliable SQLite database with proper relationships

### User Experience
- **Clean Interface**: Intuitive design with responsive layout
- **Instant Feedback**: Success/error messages with proper form validation
- **Quick Actions**: One-click expense deletion with confirmation
- **Comprehensive Reports**: Tabular view of all expenses with sorting and filtering

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask (Python) | Web framework and API endpoints |
| **Database** | SQLite | Data persistence and relationships |
| **Frontend** | HTML5, CSS3, JavaScript | User interface and interactions |
| **Templates** | Jinja2 | Server-side rendering |
| **Containerization** | Docker & Docker Compose | Development and deployment |
| **Styling** | Custom CSS | Modern, responsive design |

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Browser   │◄──►│  Flask App      │◄──►│  SQLite DB      │
│   (Frontend)    │    │  (Backend)      │    │  (Data Layer)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
        │                       │                       │
        │              ┌─────────────────┐              │
        └─────────────►│ Docker Container│◄─────────────┘
                       │   Environment   │
                       └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Git

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/personal-finance-tracker.git
   cd personal-finance-tracker
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Open your browser to `http://localhost:5000`
   - Start adding expenses and exploring features

### Development Mode
```bash
# For development with auto-reload
docker-compose up --build

# View logs
docker-compose logs -f

# Rebuild after changes
docker-compose down && docker-compose up --build
```

## 📊 Database Schema

The application uses a normalized SQLite database design:

```sql
-- Categories table
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

-- Expenses table with foreign key relationship
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER NOT NULL,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories (id)
);
```

## 🔧 Key Implementation Details

### Docker Configuration
- **Multi-stage build** for optimized container size
- **Volume mounting** for database persistence
- **Environment variables** for configuration
- **Development vs Production** setups

### Backend Architecture
- **Route separation** for clean code organization
- **Database connection pooling** with Flask-g context
- **Error handling** with user-friendly messages
- **Form validation** with server-side checks

### Frontend Design
- **Mobile-responsive** CSS Grid and Flexbox layouts
- **Progressive enhancement** with vanilla JavaScript
- **Semantic HTML** for accessibility
- **Custom styling** without external frameworks

## 📈 Future Enhancements
These are concrete plans that I intend to work on over the coming months, transforming this foundation into a 
comprehensive financial management platform. 

Each phase builds systematically on the previous work, with clear technical goals and measurable outcomes.

### Phase 1: User Management
**Goal**: Multi-user support with authentication

**Features to Add:**
- User registration and login system
- Session-based authentication
- User-specific expense isolation
- Password hashing with bcrypt

**Technical Implementation:**
- Add `users` table to database schema
- Implement Flask-Login for session management
- Add user_id foreign key to expenses table
- Create login/register templates and routes
- Add authentication decorators to protect routes

**Learning Objectives:**
- Web application security fundamentals
- Session management in Flask
- Database schema migrations
- User experience design for authentication flows

---

### Phase 2: Enhanced Reporting & Analytics
**Goal**: Advanced financial insights and visualizations

**Features to Add:**
- Interactive charts and graphs (Chart.js integration)
- Monthly/yearly spending trends
- Category-based spending analysis
- Budget setting and tracking
- Expense comparison tools
- PDF report generation
- Data export functionality (CSV, Excel formats)
- Advanced search with full-text indexing

**Technical Implementation:**
- Integrate Chart.js for data visualization
- Add new database tables for budgets and spending targets
- Create API endpoints for chart data
- Implement PDF generation with ReportLab
- Add date picker components for better UX
- Create responsive chart layouts
- Build CSV/Excel export functionality with pandas
- Add full-text search with SQLite FTS extensions

**Learning Objectives:**
- Data visualization in web applications
- API design for frontend consumption
- PDF generation in Python
- Advanced SQL queries and aggregations
- File export formats and data processing

---

### Phase 3: Advanced Features & Deployment
**Goal**: Production-ready application with enhanced functionality

**Features to Add:**
- Multi-currency support with real-time conversion
- Expense comparison and trend analysis
- Advanced filtering and sorting options
- Bulk operations (delete multiple expenses)
- Data backup and restore functionality
- Performance optimizations

**Technical Implementation:**
- Integrate currency conversion APIs
- Add database indexing for performance
- Implement batch operations with database transactions
- Create automated backup system
- Add caching for frequently accessed data
- Optimize database queries and add pagination

**Deployment & DevOps:**
- Deploy to AWS/Heroku with proper CI/CD
- Set up monitoring and logging
- Implement database backups
- Add performance monitoring
- Create comprehensive documentation

**Learning Objectives:**
- Third-party API integration
- Production deployment and DevOps
- Application monitoring and maintenance
- CI/CD pipeline setup
- Performance optimization techniques

---

### Phase 4: Team & Enterprise Features
**Goal**: Multi-user collaboration and advanced functionality

**Features to Add:**
- Team/family expense sharing
- Role-based access control (admin, user, viewer roles)
- Expense approval workflows
- Audit trails and activity logging
- Advanced reporting with custom dashboards
- Email notifications for important events

**Technical Implementation:**
- Implement complex permission system
- Add workflow engine for approvals
- Create dashboard builder interface
- Build notification system with email integration
- Add comprehensive activity logging
- Implement data privacy controls

**Learning Objectives:**
- Enterprise application architecture
- Complex permission systems
- Workflow automation
- Email integration
- Security and privacy considerations

---

## 🌟 Dream Goals & Future Possibilities

*These are ambitious features that would make this a truly exceptional project, but require significant additional learning and time investment:*

### Mobile Application
- **React Native mobile app** with full feature parity
- **Offline capability** with local storage and sync
- **Receipt photo upload** with OCR text extraction
- **Push notifications** for spending limits and reminders
- **Real-time sync** between web and mobile platforms

### Artificial Intelligence Features
- **Smart expense categorization** using simple machine learning
  - Train on user's historical categorization patterns
  - Suggest categories for new expenses based on description
- **Spending pattern analysis** with predictive insights
- **Anomaly detection** for unusual spending behavior

### Advanced Integrations
- **Bank account integration** (if comfortable with financial APIs)
- **Integration with accounting software** (QuickBooks, etc.)
- **Automated recurring expense templates** for bills and subscriptions
- **Data import capabilities** from bank statements and other apps

### Enterprise & Scale Features
- **White-label customization** for different organizations
- **API for third-party integrations**
- **Advanced analytics** with business intelligence features
- **Multi-tenant architecture** for SaaS deployment

## 🎯 Portfolio Highlights

This project demonstrates:

### Technical Skills
- **Full-Stack Development**: Complete web application from database to UI
- **Containerization**: Docker expertise for development and deployment
- **Database Design**: Normalized schema with proper relationships
- **Web Security**: Input validation, error handling, and data protection
- **UI/UX Design**: Clean, responsive interface without external frameworks

### Problem-Solving Approach
- **Iterative Development**: Built MVP first, planned systematic improvements
- **User-Centric Design**: Focused on practical, everyday use cases
- **Scalable Architecture**: Designed for future enhancements and growth
- **Clean Code**: Organized, maintainable, and well-documented codebase

### Project Management
- **Goal-Oriented Planning**: Clear objectives and measurable outcomes
- **Technology Selection**: Pragmatic choices balancing learning and functionality
- **Documentation**: Comprehensive README and inline code comments

## 🤝 Contributing

This project welcomes contributions! Please feel free to:
- Report bugs or suggest features
- Submit pull requests for improvements
- Share feedback on user experience
- Contribute to documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ as a learning project to demonstrate modern web development and containerization skills.**