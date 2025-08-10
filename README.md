**🛒 THE TRADE HUB**
A Flask-based marketplace application where users can register, log in, view available items, purchase them using a virtual budget, and sell them back to the market.
Perfect as a learning project for Flask, SQLAlchemy, and Bootstrap.


**✨ Features**

**🔐 User Authentication**
Register new accounts
Log in / Log out


**🏪 Virtual Marketplace**

View available items for sale
Purchase items if you have enough budget
Sell items back to the market


**💰 Budget Tracking**

Budget decreases after a purchase
Budget increases after selling an item


**🎨 Interactive UI**

Item details via Bootstrap modals
Cart display showing owned items


🛠 Tech Stack

Backend: Flask, SQLAlchemy, Flask-Login, WTForms
Frontend: HTML, Bootstrap 5, Jinja2 Templates
Database: SQLite (default, can be switched to PostgreSQL/MySQL)


**📂 Project Structure**

THE-TRADE-HUB/
│
├── app.py                  # Main Flask app  
├── models.py               # Database models  
├── forms.py                # WTForms classes  
├── static/                 # Static files (CSS, JS, Images)  
├── templates/              # HTML templates  
│   ├── base.html  
│   ├── home.html  
│   ├── market.html  
│   ├── login.html  
│   └── register.html  
├── instance/               # SQLite database  
├── requirements.txt        # Dependencies  
└── README.md               # Project documentation  


**🚀 Installation & Usage**

1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/THE-TRADE-HUB.git
cd THE-TRADE-HUB


2️⃣ Create & activate virtual environment

bash
Copy
Edit
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate


3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt


4️⃣ Run the app

bash
Copy
Edit
flask run


5️⃣ Visit in your browser

http://127.0.0.1:5000


