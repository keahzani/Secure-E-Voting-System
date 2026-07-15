# Secure E-Voting System

A secure, accessible, and user-friendly electronic voting web application built using **Python and Django**.  
This system is designed to facilitate transparent elections by enabling users to register, log in, vote, and verify results within a secure environment.

---

## 📌 Features

### 👤 User Features
- User Registration & Login  
- Secure Authentication  
- View Available Elections  
- Cast a Vote (only once per election)  
- View Election Results  

### 🗳️ Admin Features
- Create & Manage Elections  
- Add and Manage Candidates  
- Open & Close Voting Sessions  
- Monitor Voter Participation  
- View and Export Results  
- Audit Logs and Vote Verification  

### 🔐 Security Features
- Protected routes for voters & admins  
- Vote integrity checks  
- Prevention of multiple voting  
- Clean separation of business logic & templates  

---

## 📁 Project Structure



Secure-E-Voting-System/
│
├── SecureEVoting/ # Core project folder
│ ├── users/ # User authentication & user management
│ ├── elections/ # Election & candidate management
│ ├── voting/ # Vote casting and validation logic
│ ├── audit/ # Audit & verification logic
│ └── templates/ # Django HTML templates
│
├── manage.py # Django project entry point
└── .gitignore # Ignored files


---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/keahzani/Secure-E-Voting-System.git
cd Secure-E-Voting-System

2️⃣ Install dependencies

Make sure Python 3.x and pip are installed.

If you have a requirements.txt file:

pip install -r requirements.txt


Or manually install Django:

pip install django

3️⃣ Apply database migrations
python manage.py migrate

4️⃣ Start the development server
python manage.py runserver

5️⃣ Access the application

Visit the system in your browser:
👉 http://localhost:8000/

🧭 System Workflow
🔹 Voter Workflow

Register & log in

View active elections

Vote for a candidate

Wait for admin to close the election

View verified results

🔹 Admin Workflow

Log in as admin

Create an election

Add candidates

Open / close elections

Track voting activity

Verify and export results

🔧 Future Enhancements

End-to-end encrypted ballots

Role-based access control (Admin, Auditor, Voter)

Improved responsive UI

Blockchain-backed vote immutability

Multi-factor authentication

Detailed audit logs with anomaly detection

🤝 Contributing

Contributions are welcome!
To contribute:

Fork the repository

Create a new feature branch

Commit your changes

Open a pull request

📜 License

You may add your preferred license here (MIT is recommended).
If you want, I can create a LICENSE file for you.

📧 Contact

Developer: Ronald Zani
Email: ronaldzani@gmail.com

GitHub: https://github.com/keahzani

⭐ Support the Project

If you find this project useful, kindly give it a star ⭐ on GitHub to support visibility!


---

If you want a version **with GitHub badges**, **screenshots**, or a **project banner**, just tell me!
