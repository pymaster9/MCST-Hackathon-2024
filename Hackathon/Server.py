from flask import Flask, send_file, render_template, request


app = Flask(__name__)

@app.route("/")
def runmain():
    return send_file("index.html")

@app.route("/processedimage.jpg")
def supplyimage():
    return send_file("annotatedoutput.png")

@app.route("/prices.txt")
def supplyprices():
    return send_file("prices.txt")

@app.route("/items.txt")
def supplyitems():
    return send_file("itemsrecognized.txt")

@app.route('/get/<file>')
def index(file):
    lines = open(file,"r").readlines()
    output = ""
    for x in lines:
        output += x + "\n"
    print(output)
    return output

app.run()
#import MasterProgram