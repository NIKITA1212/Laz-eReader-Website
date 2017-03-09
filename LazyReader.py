from flask import Flask, render_template,redirect,url_for,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    #return redirect(url_for('index.html'))
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
   # app.run(debug=False, port=port, host='0.0.0.0')
    app.run(debug=False, port=port, host='127.0.0.1')
