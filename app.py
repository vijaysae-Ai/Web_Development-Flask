from flask import Flask, render_template ,jsonify

app = Flask(__name__)

jobs_data = [
    {'id': 1, 'title': 'Data Analyst', 'salary': 12333, 'location': 'Bengaluru'},
    {'id': 2, 'title': 'Data', 'salary': 193039, 'location': 'Bengaluru'},
    {'id': 3, 'title': 'Data Scientist', 'salary': 123, 'location': 'Bengaluru'},
    {'id': 4, 'title': 'Data Engineer', 'salary': 10983, 'location': 'Bengaluru'}
]

@app.route('/')
def home():
    return render_template('home.html', jobs=jobs_data)

@app.route('/api/jobs')
def get_jobs():
    return jsonify(jobs_data)




if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
