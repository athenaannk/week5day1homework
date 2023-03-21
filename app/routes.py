from app import app


@app.route('/home')
def homePage():
    return {
        'Oh hello': 'Athena'
    }
@app.route('/')
def landingPage():
    return {
        'Landing': 'Woo!'
    }

@app.route('/test')
def testPage():
    return {
        'test': 'test'
    }   