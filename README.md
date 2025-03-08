# **Recruit AI**  

🚀 **Recruit AI** is an AI-driven recruitment tool designed to streamline and automate candidate analysis. It integrates multiple Python files, utilizes environment variables, and runs within a **VS Code** development environment.  

## **Project Structure**  

```
RecruitAI/
│── __pycache__/
│── .venv/
│── CV's and JD's/            # Contains resumes (CVs) and job descriptions (JDs)
│── JD Form Template/         # Predefined templates for JDs
│── src/                      # Core source files
│── static/                   # Static assets (CSS, JS, images)
│── templates/                # HTML templates for rendering
│── video/                    # Video-related assets (if any)
│── .env                      # Environment variables
│── .gitignore                # Git ignore file
│── app.py                    # Main application file (Flask server)
│── issue-relay-tokens.py      # Script for handling tokens
│── requirements.txt           # Project dependencies
│── variable_loader.py         # Handles environment variable loading
```

## **Tech Stack**  

- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS, JavaScript  
- **APIs & Libraries:** OpenAI API, Pandas, Flask, and more  

## **Installation & Setup**  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/RecruitAI.git
   cd RecruitAI
   ```

2. **Create & activate a virtual environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**  
   - Create a `.env` file in the project root.  
   - Add necessary API keys and configuration settings.  

5. **Run the application:**  
   ```bash
   flask run
   ```
   If Flask does not work, try:  
   ```bash
   python app.py
   ```

6. **Access the application:**  
   - The app runs on **`http://127.0.0.1:5000/`**  
   - Click the localhost link to access the website.  

## **Features**  

✅ AI-powered candidate screening  
✅ Job description and CV analysis  
✅ User-friendly web interface  
✅ Secure token-based authentication  

## **Contributing**  

Feel free to fork the repo, submit issues, or contribute improvements!  

## **License**  

📝 MIT License  