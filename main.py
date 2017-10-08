from flask import Flask
from flask import request

app = Flask(__name__)
app.config['DEBUG'] = True

def index():
    return form

@app.route("/hello", methods = ['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '<h1>'



time_form = """
    <style>
        .error {{color:red;}}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input names="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type = "submit" name = "action" value="Validate" />
    </form>
    """

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',minutes='',minutes_error='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods = ['POST'])
def validate_time():

    #name = request.form['name']
    hours = request.form["hours"]
    minutes = request.form["minutes"]

    hours_error = ''
    minutes_error = ''


    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer   '
    
    else:
        hours = int(hours)
        if hours > 23 or hours  < 0:
            hours_error = 'Hour value out of range (0 to 23)'
            hours = ''

        if not is_integer(minutes):
            minutes_error = 'Not a valid integer'
            minutes = ''
        else:
            minutes = int(minutes)
            if minutes > 59 or minutes < 0:
                minutes_error = 'Minutes value out of range (0-59)'
                minutes = ''

        if not minutes_error and not hours_error:
            return "Success!"
        else:
            return time_form.format(hour_error = hours_error, minutes_error = minutes_error, hours = hours, minutes = minutes )



    

app.run()