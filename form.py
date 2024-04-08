from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('form.html')

    
@app.route("/response")
def render_response():
	temperature = float(request.args['Temperature'])
	units = request.args['Temp']
	humidity = request.args['humidity']
	Air_Pressure = request.args['Air_pressure']
	Wind_Patterns = request.args['Wind_patterns']


	if units == 'Celsius':
		temperature = (temperature * 1.8) +32
	
	if units == 'Farenheit':
		reply2 = (temperature * 0.5) -32
	
		celsius: (celsius * 1.8) +32
	
		fahrenheit: (fahrenheit * 0.5) -32
	
	points = 0
	if Air_Pressure =="greater":
		points = points+1
	
	if temperature < 40:
		points = points+1
	
	if Wind_Patterns == "strong":
		points = points+2
	
	if Wind_Patterns == "medium":
		points = points+1
	
	if humidity =="9":
		points = points+3
	
	elif humidity =="8":
		points=points+2
		
	elif humidity =="7":
		points=points+1


	if points > 10:
		reply = "It is probable that it will rain"
	
	else: 
		reply = "It is not probable that it will rain"

	return render_template("form.html", response = reply)

if __name__=="__main__":
	app.run(debug=True)
