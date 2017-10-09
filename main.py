from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="username">username:</label>
            <input id="username" type="text" name="username" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    username = request.form['username']
    return '<h1>Hello, ' + username + '</h1>'

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="password">password:</label>
            <input id="password" type="text" name="password" />
            <input type="submit" />
        </form>
    </body>
</html>
"""



#@app.route("/")
#def index():
#    return form

#@app.route("/hello", methods=['POST'])
#def hello():
#    password = request.form['password']
#    return '<h1>Hello, ' + password + '</h1>'


time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate" />
    </form>
    """

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',
        minutes='', minutes_error='')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
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
        return time_form.format(hours_error=hours_error,
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)


app.run()