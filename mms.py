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

@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)