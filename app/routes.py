from app import app


from flask import render_template

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/gentop5')
def gentopPage():
    return render_template('gentop5.html')


@app.route('/movtop5')
def movtopPage():
    movies = [
        {
            'Title' : 'Goonies'
        },
        {
            'Title': 'Pulp Fiction'
        },
        {
            'Title': 'Gone Girl'
        },
        {
            'Title': 'Nightmare Before Christmas'
        },
        {
            'Title': 'Sandlot'
        }
    ]
    return render_template('movtop5.html', movies=movies)