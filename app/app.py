from flask import Flask, render_template, request,session,redirect,url_for,g

def create_app():
    app = Flask(__name__,template_folder="templates",static_folder="static")
    
    @app.route('/')
    def index():
        return 'Hello, Bruce Pater!'
    
    @app.route('/about',methods = ['GET'])
    def about():
        return render_template('about.html')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port = 5000, debug = True)