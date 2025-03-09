# **Recruit AI**  

Recruit AI is an **AI-driven recruitment tool** designed to simplify the hiring process by integrating resume parsing, job description (JD) analysis, and recruitment automation. The project is built using **Flask** and multiple Python scripts, allowing users to perform **data-driven hiring analysis** with ease.  

## **Project Setup**  

### **Step 1: Extract the ZIP File**  
1. Download the provided ZIP file.  
2. Extract it to your preferred directory.  

### **Step 2: Set Up the Virtual Environment**  
Navigate to the project folder and run the following commands:  

```sh
# Create a virtual environment (if not already present)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Step 3: Running the Project**  
#### **Method 1: Using Flask Run (Preferred)**  
```sh
flask run
```
#### **Method 2: Running app.py Directly**  
If the above command doesn’t work, try:  
```sh
python app.py
```
After running either of these commands, **a local host link will be generated**. Click on it to access the **Recruit AI web interface**.  

## **Project Structure**  

```
RecruitAI/
│── __pycache__/             # Compiled Python files
│── .venv/                   # Virtual environment
│── CV's and JD's/           # Resumes and job descriptions
│── JD Form Template/        # JD input templates
│── src/                     # Core application source code
│── static/                  # Static files (CSS, JS, images)
│── templates/               # HTML templates for Flask
│── video/                   # Video assets (if any)
│── .env                     # Environment variables for secure API integration
│── .gitignore               # Excludes sensitive files
│── app.py                   # Main application entry point
│── issue-relay-tokens.py    # Handles token management
│── requirements.txt         # Dependencies
│── variable_loader.py       # Loads environment variables
│── README.md                # Project documentation
```

## **Technologies Used**  
- **Python** (Flask)  
- **HTML, CSS, JavaScript** (for the frontend)  
- **Virtual Environment (venv)**  
- **Git for version control**  


---

Let me know if you want any additional modifications! 🚀
