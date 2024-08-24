import json
from flask import Flask, render_template, request

app = Flask(__name__)

FILE_PATH = "user_data.json"

@app.route('/', methods=['GET', 'POST'])
def index():
    errors = {}
    user_data = {}

    if request.method == "POST":
        
        uName = request.form['uName']
        uPhone = request.form['uPhone']
        uEmail = request.form['uEmail']
        
        print("User Name =", uName)
        print("User Phone =", uPhone)
        print("User Email =", uEmail)

        user_data={
            'Name':uName,
            'Phone':uPhone,
            'Email':uEmail,
        }

        if not uName[0].isalpha():
            errors['uName'] = ['User name should start with an alphabet']

        if not errors:
            save_data_to_file(user_data)
    
    return render_template('home.html.j2', errors=errors)  


def save_data_to_file(data):
    try:
        with open(FILE_PATH, 'a') as f:
            f.write(json.dumps(data) + "\n")
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50100, debug=True)
