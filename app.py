from flask import Flask

app = Flask(_name_)

@app.route('/')
def index():
    name = "Sree Rachnae Shyam"
    usn = "1BM20IS126"
    return f"Hello! My name is {name} and my USN is {usn}"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)