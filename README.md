<<<<<<< HEAD
# FlowMotion - Intelligent Habit and Task Management System

FlowMotion is an intelligent habit and task management system designed for Linux desktop users. It helps you track habits, manage tasks, and provides smart reminders and emotional feedback.

## Features
- **Habit Tracking**: Support for binary (Yes/No) and measurable habits.
- **Smart Scheduling**: Adaptive reminder logic that learns from your behavior.
- **Linux Notifications**: Native desktop notifications using `notify-send`.
- **AI Integration**: AI-powered task understanding and categorization.
- **Visual Analytics**: Beautiful charts using Chart.js to track your progress.
- **Emotional Feedback**: Supportive messages based on your performance.

## Tech Stack
- **Backend**: Python 3.9+, Django 4.x
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: Django REST Framework
- **Charts**: Chart.js

## Installation and Setup (Linux Ubuntu)

### 1. Install System Dependencies
Ensure you have Python 3 and `libnotify-bin` (for notifications) installed:
```bash
sudo apt update
sudo apt install python3 python3-pip libnotify-bin
```

### 2. Clone and Setup Environment
```bash
# Clone the repository (or navigate to the project folder)
cd flowmotion

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
python manage.py migrate
```

### 4. Run the Application
```bash
python manage.py runserver
```
The application will be available at `http://localhost:8000`.

## Key Components
- `habits/`: Core logic for habit management and tracking.
- `users/`: User profiles and preference management.
- `analytics/`: Data processing for charts and progress tracking.
- `flowmotion/`: Project configuration and settings.

## Note on Notifications
The application uses `notify-send` for desktop notifications. Ensure your Linux environment supports desktop notifications to see these in action.
=======
# FlowMotion  
### Your Routine. Your Flow. Smarter Every Day.

---

## 📌 Project Title  
**Routine Management System (FlowMotion)**

---

## 📖 Introduction

In today’s fast-paced world, traditional task and habit management systems often push users toward rigid productivity goals, ignoring individual routines, energy levels, and emotional well-being.

**FlowMotion** is designed to solve this problem by creating a human-centered productivity experience that adapts to the user, rather than forcing the user to adapt to the system.

FlowMotion is a smart productivity application that aligns tasks with a user’s daily routine, mental state, and energy patterns—making productivity feel natural, achievable, and sustainable.

---

## ❗ Problem Statement

Most productivity tools focus only on **what** needs to be done, not **how** or **when** a user is mentally ready to do it. This often leads to:

- Task overload  
- Burnout and loss of motivation  
- Incomplete plans  
- Abandoned to-do lists  

There is a strong need for a system that balances **productivity and motivation**, while respecting human emotions and daily rhythms.

---

## 💡 The Solution

FlowMotion intelligently organizes tasks around the user’s **daily routine and mental state**.  
Instead of enforcing strict schedules, it flows with the user’s:

- Daily habits  
- Energy levels  
- Emotional state  

By adapting in real time, FlowMotion transforms task management into a **supportive and motivating experience**, rather than a stressful one.

---

## 🚀 Why FlowMotion Works

FlowMotion combines multiple intelligent systems into one unified experience:

- **Task Management** – Organizes and prioritizes tasks efficiently  
- **Routine Intelligence** – Learns from the user’s daily behavior and patterns  
- **AI Assistance** – Provides smart suggestions and adaptive planning  
- **Emotional Persuasion** – Encourages users gently instead of pressuring them  

By addressing both **productivity and human motivation**, FlowMotion helps users not only plan tasks — but actually **complete them consistently**, day after day 📈

---

## ✨ Key Features

- Adaptive task scheduling based on routine and energy  
- Emotion-aware task recommendations  
- Smart reminders and OS-level notifications  
- AI-powered task execution assistance  
- Emotional feedback (happy / neutral / crying responses)  
- Habit history, streaks, and progress visualization  
- Home screen widgets with emotional messages  
- Minimal, user-friendly interface  

---

## 🧠 Core Innovation

When a task reminder is clicked, FlowMotion does more than open the app.

It:
- Understands the task using AI  
- Suggests **relevant AI tools** (not just ChatGPT)  
- Provides **direct website links** so users can immediately start working  

This bridges the gap between **intention and action**.

---

## 🛠 Technology Stack
```bash
🖥 FlowMotion.exe
│
├── 🧑‍💻 Frontend (React)
│ └── Screens & User Interface
│
├── ⚙ Backend (Node.js)
│ └── Application Logic
│
├── 🗄 Database (SQLite)
│ └── flowmotion.db
│
├── 🔔 Notifications
│ └── OS-level Alerts
│
└── 🤖 AI (Cloud)
└── Gemini API
```


---

## 🔄 Complete Workflow of FlowMotion

### Step 1: User Onboarding
- User installs and opens FlowMotion  
- Sets:
  - Daily routine preferences  
  - Notification timings  
  - Focus areas (health, study, work, personal)  

---

### Step 2: Habit / Task Creation
User creates a habit or task.

**Habit Types:**
- Yes / No Habit (binary)
- Measurable Habit (numeric)

**Details Collected:**
- Habit name  
- Question (manual or AI-generated)  
- Frequency (daily / weekly / custom)  
- Optional target, unit, and notes  

---

### Step 3: Smart Scheduling & Routine Intelligence
- Backend analyzes usage patterns  
- Learns user behavior  
- Adjusts reminder timing and tone  

---

### Step 4: Pre-Reminder Notification
- Gentle reminder sent **10 minutes before**
- Prepares user mentally  

---

### Step 5: Main Notification & Check-In
- OS-level notification triggered  
- Contains habit/task question and emotional tone  

---

### Step 6: App Launch
- App opens directly on notification click  
- Task becomes active immediately  

---

### Step 7: AI-Powered Task Assistance (Core Function)
- AI analyzes task description  
- Identifies task category and required tools  

**Example:**  
“Make PPT for project review”

---

### Step 8: AI Tool Recommendation
- Shows curated list of AI tools  
- Each includes:
  - Purpose  
  - Short description  
  - Direct website link  

---

### Step 9: User Response
- ✅ Completed  
- ❌ Not completed  
- ⏳ No response  

---

### Step 10: Emotional Feedback
- Completed → 😄 Happy encouragement  
- Delayed → 😐 Gentle reminder  
- Missed → 😢 Supportive emotional message  

---

### Step 11: History & Progress Visualization
- Calendar view  
- Progress graphs  
- Best & current streaks  
- Frequency overview  

---

### Step 12: Home Screen Widget Update
- Widget updates automatically  
- Displays:
  - Habit status  
  - Countdown or progress  
  - Emotional expression  

---

### Step 13: Continuous Learning
- AI improves:
  - Question phrasing  
  - Reminder timing  
  - Emotional responses  

---

## 🔁 Workflow Summary

**Plan → Remind → Assist → Act → Reflect → Encourage → Improve**

FlowMotion ensures users are not just reminded of tasks, but are **actively helped to complete them**, emotionally supported when they fail, and motivated to continue.

---

## 👥 Team

**FlowMotion**  
- Sharruk
- Nathaniel 
- Navin  

---

## 🌱 Conclusion

FlowMotion redefines productivity by putting the **human back into task management**.  
By flowing with the user’s routine, emotions, and energy levels, it creates a sustainable, intelligent, and motivating productivity system for everyday life.

> *Smarter productivity begins when your tools understand you.*

>>>>>>> 7e4750c7faa12c9d12e9aeb0919f6e3145b6a316
