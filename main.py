#must run: pip install country_converter package, flask, requests
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import requests
import country_converter as coco

#function to convert country code to country name
def getCountryNameFromCode(code):
    return coco.convert(names=code, to='name_short')

#main function
app = Flask(__name__)

#first endpoint
@app.route('/jokes/')
#showJoke() is a function that renders the template 'jokes.html'
def showJokes():
    #get the category from the url
    query = request.args.get('category')
    apiurl = f"https://api.chucknorris.io/jokes/search?query={query}"
    jokes = []
    #get the jokes from the api
    response = requests.get(apiurl)
    data = response.json()
    #append the jokes to the list
    for ele in data['result']:
        jokes.append(ele['value'])
    
    #render the template
    return render_template('jokes.html', jokes=jokes, category=query)

#second endpoint
@app.route('/nationbyname/')
#guessYourNationalityByYourName() is a function that renders the template 'nationbyname.html'
def guessYourNationalityByYourName():
    #get the name from the url
    name = request.args.get('name')
    #get the countries from the api
    apiurl = f"https://api.nationalize.io/?name={name}"
    response = requests.get(apiurl)
    data = response.json()
    countries = []
    #append the countries to the list
    for country in data['country']:
        #get the country name from the country code
        countries.append(getCountryNameFromCode(country['country_id']))
    
    #render the template
    return render_template('nationality.html', countries=countries, name=name)

if __name__ == "__main__":
    #run the app in debug mode in port 5005
    app.run(host='0.0.0.0', port=5005, debug=True)
