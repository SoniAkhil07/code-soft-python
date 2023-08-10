from flask import Flask,render_template,request
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        try:
            url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=5aa7cb94e1d41f17061b3f662b6eeec5'
            city=request.form['city']
            r=requests.get(url.format(city)).json()
            weather={
                'city': city,
                'temperature':round(r['main']['temp']-273.15),
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon'] ,
                'humidity':r['main']['humidity'],
                'wind':r['wind']['speed']
            }
            print(weather)
            return render_template('weather.html',weather=weather)
        except Exception as e:
            return "<h1>You entered Incorrect City Or You havent enterded any thing plz enter and try again</h1>"
    else:
        return render_template('index.html')
if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)
