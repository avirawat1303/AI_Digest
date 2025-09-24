📩 AI Research Digest Newsletter System

A Django + React application that delivers daily topic summaries and insights in multiple domains (AI, Cybersecurity, Finance, Health, Science, Technology, and more).

Users can:

Subscribe to categories of interest

Receive automated daily newsletters via email (powered by Gemini API)

Browse an archive of past articles

Bookmark and manage personal collections

Update preferences via a responsive dashboard

🚀 Features

🔐 User authentication with JWT (login, register, logout)

⚙️ Personalized preferences (select categories, email frequency)

📰 Daily newsletter generation using Gemini API

📧 Automated email delivery system (SMTP + cron jobs)

📂 Archive browsing with search & filtering

⭐ Bookmarking system for favorite articles

📱 Responsive React dashboard (modern UI/UX with TailwindCSS)

🌙 Optional dark mode

🛠 Tech Stack

Backend (Django + DRF):

Django 4.2

Django REST Framework

SimpleJWT (authentication)

SQLite (development DB)

django-crontab (scheduling)

python-dotenv (environment management)

Frontend (React):

React 18

React Router

Axios (API calls with JWT interceptor)

TailwindCSS (UI framework)

Other Tools:

Git + GitHub (version control)

Render/Heroku (backend deployment)

Vercel/Netlify (frontend deployment)

⚙️ Setup Instructions
1. Clone the repo
git clone https://github.com/your-username/ai-digest.git
cd ai-digest

2. Backend (Django)

Create a virtual environment and install dependencies:

cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt


Create .env file in backend/ folder:

SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
GEMINI_API_KEY=your-gemini-api-key


Run migrations:

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


Add cron job (for newsletter scheduling):

python manage.py crontab add
python manage.py crontab show

3. Frontend (React)
cd frontend
npm install
npm start


React dev server will start at http://localhost:3000.

📬 Email Newsletter

Daily cron job fetches articles from Gemini API

Stores them in database

Sends personalized HTML emails to users

🖼 Screenshots

🔑 Login/Register

📊 Dashboard (daily articles)

📂 Archive with filters

⭐ Bookmarks page

⚙️ Preferences

🚀 Deployment

Backend (Django) → Render / Heroku

Frontend (React) → Vercel / Netlify

Database → SQLite (dev), PostgreSQL (prod recommended)

📌 Roadmap

 Add more categories (Sports, Entertainment, Business)

 Add dark mode toggle

 Add notifications (in-app + push)

 Multi-language support

🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you’d like to change.

📄 License

This project is licensed under the MIT License.
