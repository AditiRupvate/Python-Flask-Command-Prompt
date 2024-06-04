from flask import Flask,request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def Home():
    html= ''' 

    
    <form action="/about" method="POST">
      <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname"><br>
  
  <input type="submit" value="Submit">
    </form>
    
    '''
    return html
   


@app.route('/about', methods=['POST'])
def About():
    
    if request.method=='POST' :
        fname=request.form['fname']
        return "<p>Hello {} !</p>".format(fname)
    else :
     print ("NOT POST")
    
    return "About us"
