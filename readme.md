# Personal Finance Tracker

A containerized personal finance application built with Flask and Docker, featuring expense tracking, categorization, user authentication, and reporting capabilities.

## 🚀 Live Demo

[View Live Application](https://personal-finance-tracker-x0ag.onrender.com) | [View Source Code](https://github.com/DanielHinbest/Personal-Finance-Tracker)

### Demo Login Credentials
```
Username: demo_user
Email: user@demo.com
Password: demo123
```

**Note:** This application is deployed on Render's free tier. Due to the limitations of the free plan, the database is reset periodically and data is not permanently saved at this time.

## 📋 Project Overview

This full-stack web application allows users to track personal expenses with comprehensive filtering, reporting features, and secure user authentication. Built as a learning project to demonstrate containerization skills, database management, user authentication, and modern web development practices.

**Key Achievements:**
- ✅ **Phase 1 Complete**: Multi-user support with authentication system
- Containerized Flask application with Docker
- SQLite database with proper schema design and user relationships
- Secure user authentication with password hashing
- Responsive web interface with server-side rendering
- Advanced search and filtering capabilities
- Date-based expense analysis and summaries
- User-specific expense isolation and session management

## ✨ Features

### Core Functionality
- **User Authentication**: Secure registration and login system with password hashing
- **Multi-User Support**: Each user has their own isolated expense data
- **Expense Management**: Add, view, and delete expenses with detailed categorization
- **Smart Categorization**: Predefined categories (Food, Transportation, Entertainment, Shopping, Bills, Healthcare, Education, Travel, Other)
- **Advanced Search**: Filter by description, category, and date ranges
- **Financial Summaries**: Real-time calculations for weekly, monthly, and total spending
- **Data Persistence**: Reliable SQLite database with proper relationships and foreign keys

### User Experience
- **Clean Interface**: Intuitive design with responsive layout
- **Session Management**: Secure login sessions with automatic logout
- **Instant Feedback**: Success/error messages with proper form validation
- **Quick Actions**: One-click expense deletion with confirmation
- **Comprehensive Reports**: Tabular view of all expenses with sorting and filtering
- **Personalized Dashboard**: Welcome messages and user-specific data views

### Security Features
- **Password Hashing**: Secure password storage using Werkzeug's PBKDF2
- **Session Protection**: Flask session management with secure cookies
- **Authentication Guards**: Protected routes requiring login
- **Input Validation**: Server-side validation for all user inputs
- **User Isolation**: Complete separation of user data

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | Flask (Python) | Web framework and API endpoints |
| **Authentication** | Flask-Login, Werkzeug | User session management and password hashing |
| **Database** | SQLite | Data persistence with user relationships |
| **Frontend** | HTML5, CSS3, JavaScript | User interface and interactions |
| **Templates** | Jinja2 | Server-side rendering with user context |
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
        └─────────────►│ Authentication  │              │
                       │   & Sessions    │              │
                       └─────────────────┘              │
                                │                       │
                       ┌─────────────────┐              │
                       │ Docker Container│◄─────────────┘
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
   - Register a new account or use demo credentials:
     - Username: `demo_user`
     - Password: `demo123`
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

The application uses a normalized SQLite database design with user authentication:

```sql
-- Users table for authentication
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Categories table
CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Expenses table with user relationship
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount DECIMAL(10,2) NOT NULL,
    description TEXT NOT NULL,
    category_id INTEGER,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

## 🔧 Key Implementation Details

### Authentication System
- **Password Security**: PBKDF2 hashing with salt for secure password storage
- **Session Management**: Flask session-based authentication with secure cookies
- **Route Protection**: Authentication decorators to protect sensitive endpoints
- **User Context**: All expenses are isolated by user ID for complete data separation

### Docker Configuration
- **Multi-stage build** for optimized container size
- **Volume mounting** for database persistence
- **Environment variables** for configuration
- **Development vs Production** setups

### Backend Architecture
- **Route separation** for clean code organization (auth, main app routes)
- **Database connection pooling** with Flask-g context
- **Error handling** with user-friendly messages
- **Form validation** with server-side checks and CSRF protection

### Frontend Design
- **Mobile-responsive** CSS Grid and Flexbox layouts
- **Progressive enhancement** with vanilla JavaScript
- **Semantic HTML** for accessibility
- **Custom styling** without external frameworks
- **User-aware interface** with personalized content

## 📈 Development Progress & Future Enhancements

### ✅ Phase 1: User Management (COMPLETED)
**Goal**: Multi-user support with authentication

**Completed Features:**
- ✅ User registration and login system
- ✅ Session-based authentication with Flask sessions
- ✅ User-specific expense isolation
- ✅ Password hashing with Werkzeug PBKDF2
- ✅ Authentication decorators for route protection
- ✅ Updated database schema with user relationships
- ✅ Login/register templates and routes
- ✅ User-aware interface and personalized experience

---

### Phase 2: Enhanced Reporting & Analytics
**Goal**: Advanced financial insights and visualizations

**Planned Features:**
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

**Planned Features:**
- Multi-currency support with real-time conversion
- Expense comparison and trend analysis
- Advanced filtering and sorting options
- Bulk operations (delete multiple expenses)
- Data backup and restore functionality
- Performance optimizations
- Email notifications for budgets and reminders

**Technical Implementation:**
- Integrate currency conversion APIs
- Add database indexing for performance
- Implement batch operations with database transactions
- Create automated backup system
- Add caching for frequently accessed data
- Optimize database queries and add pagination
- Implement email service integration

**Deployment & DevOps:**
- Enhanced deployment with proper CI/CD
- Set up monitoring and logging
- Implement database backups
- Add performance monitoring
- Create comprehensive API documentation

**Learning Objectives:**
- Third-party API integration
- Production deployment and DevOps
- Application monitoring and maintenance
- CI/CD pipeline setup
- Performance optimization techniques

---

### Phase 4: Team & Enterprise Features
**Goal**: Multi-user collaboration and advanced functionality

**Planned Features:**
- Team/family expense sharing
- Role-based access control (admin, user, viewer roles)
- Expense approval workflows
- Audit trails and activity logging
- Advanced reporting with custom dashboards
- Administrative panel for user management

**Technical Implementation:**
- Implement complex permission system
- Add workflow engine for approvals
- Create dashboard builder interface
- Build comprehensive notification system
- Add extensive activity logging
- Implement data privacy controls

**Learning Objectives:**
- Enterprise application architecture
- Complex permission systems
- Workflow automation
- Advanced security considerations
- Multi-tenant data architecture

## 🌟 Dream Goals & Future Possibilities

*These are ambitious features that would transform this into a comprehensive financial platform:*

### Mobile Application
- **React Native mobile app** with full feature parity
- **Offline capability** with local storage and sync
- **Receipt photo upload** with OCR text extraction
- **Push notifications** for spending limits and reminders

### Artificial Intelligence Features
- **Smart expense categorization** using machine learning
- **Spending pattern analysis** with predictive insights
- **Anomaly detection** for unusual spending behavior
- **Natural language processing** for expense descriptions

### Advanced Integrations
- **Bank account integration** with secure financial APIs
- **Integration with accounting software** (QuickBooks, etc.)
- **Automated recurring expense templates**
- **Third-party app data imports**

## 🎯 Portfolio Highlights

This project demonstrates:

### Technical Skills
- **Full-Stack Development**: Complete web application from database to UI
- **User Authentication**: Secure login system with password hashing and sessions
- **Database Design**: Normalized schema with proper relationships and foreign keys
- **Containerization**: Docker expertise for development and deployment
- **Web Security**: Authentication, input validation, and data protection
- **UI/UX Design**: Clean, responsive interface with user-centric design

### Problem-Solving Approach
- **Iterative Development**: Built MVP first, then systematically added authentication
- **Security-First Mindset**: Implemented proper authentication from the ground up
- **User-Centric Design**: Focused on practical, everyday use cases
- **Scalable Architecture**: Designed for future enhancements and multi-user growth

### Project Management
- **Phased Development**: Clear milestones with measurable outcomes
- **Goal-Oriented Planning**: Systematic approach to feature implementation
- **Technology Selection**: Pragmatic choices balancing learning and functionality
- **Documentation**: Comprehensive README with progress tracking

## 🤝 Contributing

This project welcomes contributions! Please feel free to:
- Report bugs or suggest features
- Submit pull requests for improvements
- Share feedback on user experience
- Contribute to documentation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ as a learning project to demonstrate modern web development, authentication systems, and containerization skills.**