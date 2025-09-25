<<<<<<< HEAD
# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can't go back!**

If you aren't satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you're on your own.

You don't have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn't feel obligated to use this feature. However we understand that this tool wouldn't be useful if you couldn't customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
=======
# 📩 AI Research Digest Newsletter System

A Django + React application that delivers daily topic summaries and insights in multiple domains (AI, Cybersecurity, Finance, Health, Science, Technology, and more).

Users can:

Subscribe to categories of interest

Receive automated daily newsletters via email (powered by Gemini API)

Browse an archive of past articles

Bookmark and manage personal collections

Update preferences via a responsive dashboard

## 🚀 Features

🔐 User authentication with JWT (login, register, logout)

⚙️ Personalized preferences (select categories, email frequency)

📰 Daily newsletter generation using Gemini API

📧 Automated email delivery system (SMTP + cron jobs)

📂 Archive browsing with search & filtering

⭐ Bookmarking system for favorite articles

📱 Responsive React dashboard (modern UI/UX with TailwindCSS)

🌙 Optional dark mode

## 🛠 Tech Stack

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


## ⚙️ Setup Instructions
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

# 📬 Email Newsletter

Daily cron job fetches articles from Gemini API

Stores them in database

Sends personalized HTML emails to users.

⚙️ Preferences

# 📌 Roadmap

 Add more categories (Sports, Entertainment, Business)

 Add dark mode toggle

 Add notifications (in-app + push)

 Multi-language support

🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you’d like to change.

>>>>>>> 345933bb1ebf8ca18b4d76260079bbd5ae77b8c9
