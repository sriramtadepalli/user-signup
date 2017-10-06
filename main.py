from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

app.run()

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
            <input type = "submit" value="Validate" />
        </form>
        """

@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',minutes='',minutes_error='')



if not is_integer(hours):
    hours_error = 'Not a valid integer'
else:
    hours = int(hours)
    if hours > 23 or hours  < 0:
        hours_error = 'Hour value out of range (0 to 23)'

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
    else:
        minutes = int(minutes)

app.run()
#        if minutes > 59: