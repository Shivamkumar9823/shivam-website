from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
       {
           'id' : 1,
           'Title' : 'Data Analyst',
           'Location':'Bengaluru, India',
           'Salary' :'Rs 1000000',
           'email':'dt2022@gmail.com'
       },
       {
           'id' : 2,
           'Title' : 'Data Scientist',
           'Location':'Delhi, India',
           'Salary' :'Rs 1000000',
           'email':'ds2022@gmail.com'

       },
       {
           'id' : 3,
           'Title' : 'Backend Engineer',
           'Location':'california',
        #    'Salary' :'$ 12000'
           'email':'be2022@gmail.com'

       },
       {
           'id' : 4,
           'Title' : 'FrontEnd Engineer',
           'Location':'New York',
           'Salary' :'$100000',
           'email':'fe2022@gmail.com'

       } 

]



@app.route("/")

def hello_world():
    return render_template('index.html',
                           jobs=JOBS)

 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)