from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def Home():
    html= ''' 
    <p>hello</p>
    <a href="/about"> about </a>
    
    '''
    return html
   


@app.route('/about')
def About():
    return "About us"
