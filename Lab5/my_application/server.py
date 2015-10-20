from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index File!\n"

@app.route("/hello")
def hello():
    return "Hello World!\n"
    
@app.route("/user/paul")
def user():
    return "The User is Paul!\n"
    
@app.route("/post/80")
def post():
    return "Post 80!\n"
    
@app.route("/mwn")
def nurse():
    return "Mergos Wet Nurse is my Spirit Animal.\n"
    
@app.route("/rex")
def rex():
    return "Dinosaurs are Great.\n"
    
@app.route("/jess")
def rex():
    return "Today I made an Alias for Jess locally! Hurrah!.\n"
    

if __name__ == "__main__": app.run(host="0.0.0.0", port=8080,debug=True)
