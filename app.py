from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__== '__main__':
    app.debug= True
    app.run()

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        #print(customer,dealer,rating,comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please complete all required fields')
    return render_template('success.html')

if __name__ == '__main__':
    app.debug = True
    app.run()