from flask import Flask, redirect, render_template, request, url_for
import random
from datetime import datetime

######### INITILIAZE FLASK APPLICATION ##########

app = Flask(__name__)

######### ROUTING FOR DIFFERENT WEBPAGES ##########

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/rent')
def rent():
    return render_template('rent.html')


@app.route('/about')
def about():
    return render_template('about.html')
    
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

######### CONDITIONAL ROUTING TO DIFFERENT CAR OPTIONS ##########

@app.route('/booking')
def booking():
    book_type = request.args.get('type')
    return render_template('booking.html',book_type=book_type)

######### PAYMENT CONFIRMED PAGE WITH VALUES FROM THE FORM ##########

@app.route('/payment-confirmed', methods=['POST','GET'])
def payment():
    def __datetime(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d')
    
    order_no = random.randint(10000,99999)
    
    if request.method == 'POST':
        customer_name = request.form['name']
        start_date = request.form['start-date']
        end_date = request.form['end-date']
        
        start_date = __datetime(start_date)
        end_date = __datetime(end_date)
        
        duration = end_date - start_date
        duration = duration.days
        start_date = start_date.date()
        end_date = end_date.date()
        return render_template('payment.html',order_no=order_no,customer_name=customer_name,duration=duration,start_date=start_date,end_date=end_date)
    else:
        pass
        
if __name__ == "__main__":
    app.run(debug=True)
