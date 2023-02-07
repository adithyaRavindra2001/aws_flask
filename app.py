

from flask import Flask, request, redirect, render_template
import boto3

app = Flask(__name__)
us="adithya"
pw="secret"
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    pwd=request.form['password']
    
    if user==us and pwd==pw:

        return redirect(f'/greet/{user}')
    return 'Invalid username or password'

@app.route('/greet/<user>')
def greet(user):
    return render_template('greet.html', user=user)



@app.route('/upload', methods=['POST'])
def upload():
       
    s3 = boto3.client('s3')

    file = request.files['file']
    
    try:

        s3.upload_fileobj(file, 'ec2-s3-full-access-bucket-2', file.filename)

        return 'File uploaded successfully.'
    except:
        return 'File not selected / Not able to upload file '



if __name__ == '__main__':
    app.run(debug=True)
