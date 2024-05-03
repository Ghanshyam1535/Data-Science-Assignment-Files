from flask import Flask, url_for

app = Flask(__name__)

# Define routes with endpoint names
@app.route('/')
def index():
    return 'Welcome to the Home Page!'

@app.route('/about')
def about():
    return 'This is the About Page.'

@app.route('/contact')
def contact():
    return 'Contact us at: example@example.com'

if __name__ == '__main__':
    with app.test_request_context():
        # Generate URLs using url_for() function
        print("URL for index():", url_for('index'))
        print("URL for about():", url_for('about'))
        print("URL for contact():", url_for('contact'))
