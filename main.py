import requests as rq
from flask import Flask, render_template, request

app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static'  # Name of directory for static files
)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/americanCuisine')
def americanCuisine():
  complete_api_link = "https://api.spoonacular.com/recipes/complexSearch?&apiKey=a546a5f813484419b635524722f42c1b&cuisine=american"

  print(complete_api_link)
  api_link = rq.get(complete_api_link)

  api_data = api_link.json()
  print("---------------------")
  result = ""
  for i in range(10):
    print(i + 1, ". ", api_data['results'][i]['title'])
    print('')
    result += str(i + 1) + '. ' + api_data['results'][i]['title'] + '\n'
  img = api_data['results'][0]['image']
  return render_template('americanCuisine.html', results=result, image=img)

@app.route('/indianCuisine')
def indianCuisine():
  complete_api_link = "https://api.spoonacular.com/recipes/complexSearch?&apiKey=a546a5f813484419b635524722f42c1b&cuisine=indian"

  print(complete_api_link)
  api_link = rq.get(complete_api_link)

  api_data = api_link.json()
  print("---------------------")
  result = ""
  for i in range(10):
    print(i + 1, ". ", api_data['results'][i]['title'])
    print('')
    result += str(i + 1) + '. ' + api_data['results'][i]['title'] + "\n"
  img = api_data['results'][0]['image']
  return render_template('indianCuisine.html', results=result, image=img)

@app.route('/chineseCuisine')
def chineseCuisine():
  complete_api_link = "https://api.spoonacular.com/recipes/complexSearch?&apiKey=a546a5f813484419b635524722f42c1b&cuisine=chinese"

  print(complete_api_link)
  api_link = rq.get(complete_api_link)

  api_data = api_link.json()
  print("---------------------")
  result = ""
  for i in range(10):
    print(i + 1, ". ", api_data['results'][i]['title'])
    print('')
    result += str(i + 1) + '. ' + api_data['results'][i]['title'] + "\n"
  img = api_data['results'][0]['image']
  return render_template('chineseCuisine.html', results=result, image=img)

@app.route('/mexicanCuisine')
def mexicanCuisine():
  complete_api_link = "https://api.spoonacular.com/recipes/complexSearch?&apiKey=a546a5f813484419b635524722f42c1b&cuisine=mexican"

  print(complete_api_link)
  api_link = rq.get(complete_api_link)

  api_data = api_link.json()
  print("---------------------")
  result = ""
  for i in range(10):
    print(i + 1, ". ", api_data['results'][i]['title'])
    print('')
    result += str(i + 1) + '. ' + api_data['results'][i]['title'] + "\n"
  img = api_data['results'][0]['image']
  return render_template('mexicanCuisine.html', results=result, image=img)

@app.route('/italianCuisine')
def italianCuisine():
  complete_api_link = "https://api.spoonacular.com/recipes/complexSearch?&apiKey=a546a5f813484419b635524722f42c1b&cuisine=italian"

  print(complete_api_link)
  api_link = rq.get(complete_api_link)

  api_data = api_link.json()
  print("---------------------")
  result = ""
  for i in range(10):
    print(i + 1, ". ", api_data['results'][i]['title'])
    print('')
    result += str(i + 1) + '. ' + api_data['results'][i]['title'] + "\n"
  img = api_data['results'][0]['image']
  return render_template('italianCuisine.html', results=result, image=img)

@app.route('/userChoice')
def userChoice():
  return render_template('userChoice.html')

@app.route("/input", methods=['POST'])
def showChoice():
  try:
    choice_data = request.form['Cuisine']
    print(choice_data)
    complete_api_link = "https://api.spoonacular.com/recipes/complexSearch?&apiKey=a546a5f813484419b635524722f42c1b&cuisine=" + choice_data
    api_link = rq.get(complete_api_link)
  
    api_data = api_link.json()
    print("---------------------")
    result = ""
    for i in range(10):
      print(i + 1, ". ", api_data['results'][i]['title'])
      print('')
      result += str(i + 1) + '. ' + api_data['results'][i]['title'] + "\n"
      img = api_data['results'][0]['image']
    return render_template('choice.html', results=result, image = img)
  except:
    return render_template('error.html')

if __name__ == "__main__": 
  app.run(  # Starts the site
    host='0.0.0.0', port=5000)
