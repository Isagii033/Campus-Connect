# 🎓 CampusConnect — Student-to-Student Campus Assistance Platform

CampusConnect is a modern, responsive single-file web application designed to connect university students for peer-to-peer assistance, skill-sharing, and micro-tasks across campus.

---

## ✨ Features

- **🔐 Authentication System:**
  - Full Login and Registration with department, year, skills, and password validation.
  - Quick 1-click Demo Login for test personas (**Rahul Sharma** and **Ananya Roy**).
  - Session persistence via `localStorage` with Sign Out capability.

- **🌓 Dynamic Dark Mode:**
  - One-click toggle between light mode and sleek navy/indigo dark mode.
  - Automatically persists user theme preference.

- **👥 Multi-User Identity Switcher:**
  - Instant persona switcher between Requester (Student A: Rahul Sharma) and Provider (Student B: Ananya Roy).

- **🛒 Request Marketplace:**
  - Real-time search by title and description.
  - Dynamic filtering by category, budget tier (Free, <₹200, ₹200–₹500, ₹500+), and status (`OPEN`, `ACCEPTED`, `IN_PROGRESS`, `COMPLETED`).

- **📝 4-Step Request Posting Wizard:**
  - Step 1: Visual category selection.
  - Step 2: Title, description, and optional special requirements.
  - Step 3: Date, time, and specific campus location.
  - Step 4: Budget setting with real-time fee and provider payout calculation (10% platform fee, 90% payout).

- **🤝 Request Acceptance & Workflow:**
  - Strict business rules: Users cannot accept their own requests; non-open requests cannot be re-accepted.
  - Lifecycle: `OPEN` ➔ `ACCEPTED` ➔ `IN_PROGRESS` (Provider marks done) ➔ `COMPLETED` (Requester confirms).

- **⭐ Interactive Rating & Reviews:**
  - Interactive 1–5 star rating modal with text reviews upon task completion.
  - Real-time recalculation of provider's cumulative rating.

- **📊 Dashboard & User Profiles:**
  - Stats overview (Posted, Completed, Avg Rating, Earned/Spent).
  - Dual tabs: "My Requests" and "Accepted Tasks".
  - Rich profile with bio, skills tag cloud, and student reviews.

- **🔔 Notification Center:**
  - Animated toast alerts for real-time actions.
  - Slide-out panel for notification history with unread count badge.

---

## 🛠️ Built With

- **HTML5 & CSS3** (Custom transitions, animations, glassmorphism, responsive grid)
- **Vanilla JavaScript (ES6+)** with reactive `localStorage` state management
- **[Tailwind CSS](https://tailwindcss.com/)** via CDN
- **[Font Awesome 6](https://fontawesome.com/)** via CDN
- **[Google Fonts Inter](https://fonts.google.com/specimen/Inter)**

---

## 🚀 Getting Started

1. Clone or download the repository:
   ```bash
   git clone https://github.com/Isagii033/Campus-Connect.git
   ```
2. Open `index.html` directly in any web browser:
   - Double-click `index.html`, OR
   - Serve using any static server (e.g. `npx serve` or `python -m http.server 8080`).

---

## 📄 License

MIT License. Free to use for learning, campus development, and open-source contributions.
