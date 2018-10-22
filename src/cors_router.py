from flask import Flask,request
# from flask.ext.mandrill import Mandrill
try:
    from flask.ext.cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask.ext.cors import CORS
app = Flask(__name__)

app.config['MANDRILL_API_KEY'] = '...'
app.config['MANDRILL_DEFAULT_FROM']= '...'
app.config['QOLD_SUPPORT_EMAIL']='...'
app.config['CORS_HEADERS'] = 'Content-Type'

# mandrill = Mandrill(app)
cors = CORS(app)

@app.route('/email/',methods=['POST'])
def hello_world():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    description=request.form['description']

    # mandrill.send_email(
    #     from_email=email,
    #     from_name=name,
    #     to=[{'email': app.config['QOLD_SUPPORT_EMAIL']}],
    #     text="Phone="+phone+"\n\n"+description
    # )

    return '200 OK'

if __name__ == '__main__':
    app.run()