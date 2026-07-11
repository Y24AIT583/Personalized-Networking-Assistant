from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
