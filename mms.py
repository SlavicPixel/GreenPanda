from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.get("/")
@app.get("/home")
def home():
    return render_template('home.html', title='Green Panda')

@app.get("/recipes")
def recipes():
    return render_template('recipes.html', title='Recipes')

@app.get("/exercises")
def exercises():
    return render_template('exercises.html', title='Exercises')

@app.get("/protein")
def protein():
    return render_template('protein.html', title='Protein')

@app.get("/supplements")
def supplements():
    return render_template('supplements.html', title='Supplements')

@app.get("/about")
def about():
    return render_template('about.html', title='About Us')

if __name__ == '__main__':
    app.run(debug=True)