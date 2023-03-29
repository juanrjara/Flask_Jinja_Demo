# Flask_Jinja_Demo
Example of how to use Flask for SSR
It contains 2 endpoints: 

nationbyname: Endpoint that takes the 'name' parameter from url and try to guess the most probables nationalities for that name, rendering the nationality.html template
USAGE EXAMPLE: http://127.0.0.1:5005/nationbyname/?name=leonel 


jokes: Endpoint that takes the 'category' parameter from url and try to get multiples chuck norris jokes based on that category, rendering the jokes.html template
USAGE EXAMPLE: http://127.0.0.1:5005/jokes/?category=terminator 
