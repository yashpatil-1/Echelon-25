from flask import Flask, render_template,session
from src.jd_maker import jd_maker_bp
from src.ai_interview import ai_interview_bp
from src.cv_analyzer import cv_analyzer_bp
from src.utilities import utilities_bp
from flask_session import Session

app = Flask(__name__)

app.register_blueprint(jd_maker_bp, url_prefix='/jd_maker')
app.register_blueprint(ai_interview_bp,url_prefix='/ai_interview')
app.register_blueprint(cv_analyzer_bp,url_prefix='/cv_analyzer')
app.register_blueprint(utilities_bp, url_prefix='/utilities')

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404

@app.route('/')
def login():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/heygen')
def heygen():
    return render_template('heygen.html')

@app.route('/jd_maker')
def jd_maker():
    return render_template('jd_maker.html')

@app.route('/cv_analyzer')
def cv_analyzer():
    return render_template('cv_analyzer.html')

@app.route('/interview')
def interview():
    return render_template('interview.html')

if __name__ == '__main__':
    app.run()