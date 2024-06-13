from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Pune, India',
        'salary': 'Rs. 13,00,000'
    },
    {
        'id': 3,
        'title': 'Cyber security',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Python developer ',
        'location': 'Mumbai, India',
        'salary': 'Rs. 9,00,000'
    },
]


@app.route("/")
def hello():
  return render_template("index.html", Jobs=JOBS)


@app.route("api/jobs")
def job_list():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
