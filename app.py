from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': '1',
    'title': 'Data Analyst',
    'location': 'kegalle, Sri Lanka',
    'salary': 'Rs. 10,000,000'
}, {
    'id': '2',
    'title': 'Data Scientist',
    'location': 'Matara, Sri Lanka',
    'salary': 'Rs. 10,000,000'
}, {
    'id': '3',
    'title': 'System Administor',
    'location': 'Anuradhapura, Sri Lanka',
    'salary': 'Rs. 10,000,000'
}, {
    'id': '4',
    'title': 'Network Engineer',
    'location': 'Colombo, Sri Lanka',
    'salary': 'Rs. 10,000,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080)
