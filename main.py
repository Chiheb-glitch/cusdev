import os

from flask import Flask, render_template, request, redirect, url_for, flash, send_file, jsonify

app = Flask(__name__)
app.secret_key = 'Test6690'

@app.route("/")
def index():
    return send_file('src/index.html')



@app.route('/submit', methods=['POST'])
def submit():
 
    flash('Form submitted successfully!', 'success')
    return jsonify({"age": request.form.get('age'),
    "gender": request.form.get('gender'),
    "status": request.form.get('status'),
    "first_q": request.form.get('first_q'),
    "second_q": request.form.get('second_q'),
    "third_q": request.form.get('third_q'),
    "fourth_q": request.form.get('fourth_q'),
    "fifth_q": request.form.get('fifth_q'),
    "sixth_q": request.form.get('sixth_q'),
    "seventh_q": request.form.get('seventh_q'),
    "eighth_q": request.form.get('eighth_q'),
    "ninth_q": request.form.get('ninth_q'),
    "tenth_q": request.form.get('tenth_q'),
    "eleventh_q": request.form.get('eleventh_q'),   },)
def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
