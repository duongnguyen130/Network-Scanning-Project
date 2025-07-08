# Network Scanning Project

## Frontend

# 🌐 Network Scanning Admin UI (Frontend)

This is the **frontend** of the Network Scanning project, built using **Vue 3**, **Vite**, and **Tailwind CSS**.

## 🧱 Features

- Sidebar navigation with routing
- Dashboard for initiating network scans
- Device Discovery (Ping Scan)
- Detailed Network Scan
- Result tables for each scan
- Responsive and clean UI

## 📁 Project Structure

```
frontend/
├── index.html
├── package.json
├── vite.config.js
├── postcss.config.js
├── tailwind.config.js
├── /public
├── /src
│   ├── main.js
│   ├── App.vue
│   ├── /assets
│   │   └── tailwind.css, logo.png
│   ├── /components
│   │   ├── Sidebar.vue
│   │   ├── Dashboard.vue
│   │   ├── DeviceDiscovery.vue
│   │   └── DetailedScan.vue
│   └── /router
│       └── index.js
```

## 🚀 Getting Started

```bash
cd frontend
npm install
npm run dev
```

Visit: http://localhost:5173

## 🛠 Build for Production

```bash
npm run build
npm run serve
```

---

## 📦 Technologies

- Vue 3
- Vite
- Tailwind CSS
- Vue Router
- Axios

## Backend

# 🔧 Network Scanning API (Backend)

This is the **backend** for the Network Scanning project. It provides REST APIs for:

- Ping scan (Device Discovery)
- Detailed scan

## ⚙️ Tech Stack

- Python 3.10+
- Django or Flask (based on your setup)
- nmap / scapy for scanning (optional)
- Django REST Framework or Flask-Restful

## 📁 Project Structure (Django example)

```
backend/
├── manage.py
├── requirements.txt
├── /backend
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── /scanner
│   ├── views.py
│   ├── urls.py
│   └── detailed_scan.py
│   └── ping_scan.py
│   └── type_find.py
│   └── os_find.py
  
```

## 🚀 Getting Started

```bash
cd backend
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
python manage.py runserver
```

APIs will be available at: http://localhost:8000/api/

## 🔍 API Endpoints

- `/api/ping-scan/` → Device Discovery
- `/api/detailed-scan/` → Detailed Network Scan

---

## ✅ Dependencies

Include in `requirements.txt`:

```
Django>=4.0
djangorestframework
python-nmap
```