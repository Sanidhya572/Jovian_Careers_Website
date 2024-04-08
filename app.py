from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        'id':1,
        'title': "Data Analyst",
        'Location': "Bengaluru, India",
        'Salary': 'Rs. 10,00,000'
    },

        {
        'id':2,
        'title': "Data Scientist ",
        'Location': "Pune, India",
        'Salary': 'Rs. 12,00,000'
    },

        {
        'id':3,
        'title': "Power BI Analyst",
        'Location': "Indore, India",
        'Salary': 'Rs. 5,00,000'
    },

        {
        'id':4,
        'title': "Front End Developer",
        'Location': "Mumbai, India",
        'Salary': 'Rs. 11,00,000'
    },

        {
        'id':5,
        'title': "Backend Developer",
        'Location': "Bengaluru, India",
        'Salary': 'Rs. 13,00,000'
    },

    {
        'id':6,
        'title': "UI/UX Designer",
        'Location': "Remote",
        'Salary': 'Rs. 7,00,000'
    },


     {
        'id':7,
        'title': "Enterprise Architect",
        'Location': "Bengaluru, India",
        'Salary': 'Rs. 25,00,000'
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
