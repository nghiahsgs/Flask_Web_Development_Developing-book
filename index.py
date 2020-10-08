from flask import Flask, request, make_response, redirect,abort, render_template
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    print(app.url_map)
    return 'Your user agent: %s'%user_agent,400
    
# @app.route('/user/<int:name>')
# def user(name):
#     return "<h1>Hello, %s</h1>"%name

@app.route('/user/<name>')
def user(name):
    # return "<h1>Hello, %s</h1>"%name
    name = '  <h1>nguyen ba nghia</h1> '
    list_users = ['nghia1','nghia2','nghia3']
    return render_template('user.html',name=name,list_users=list_users)

@app.route('/cookie')
def cookie():
    string = 'hello cookie'
    response = make_response(string)
    response.set_cookie('answer','42')
    return response
    # return string 

@app.route('/redirect1')
def redirect1():
    return redirect('/')

@app.route('/abort1')
def abort1():
    abort(404)

@app.route('/abort2')
def abort2():
    abort(500)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
if __name__ =="__main__":
    app.run(debug=True, port=3000)

'''
request hooks:
    before_first_request
    before_request
    after_request
    teardown_request
'''