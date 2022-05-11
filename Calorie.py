from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)

calaries = 0 #caloriies
calorieHistory = []  

@app.route('/getCurrentCal',methods = ['GET'])# Gives the current calorie level
def getCurrentCal():
   return jsonify({"calaries":calaries});

@app.route('/CalLost',methods = ['POST'])# Records caloires you lost
def CalLost():
   global calaries
   moveMent = request.get_json()
   moveMent["type"] = "CalLost"
   moveMent["time"] = datetime.now()#when you lost it
   calaries = calaries - moveMent["amount"]
   calorieHistory.append(moveMent)
   return jsonify({"calaries":calaries});



@app.route('/CaloriesAte',methods = ['POST'])# Records calories you consumed
def CaloriesAte():
   global calaries
   moveMent = request.get_json()
   moveMent["type"] = "CaloriesAte"
   moveMent["time"] = datetime.now()#when you ate
   calaries = calaries + moveMent["amount"]
   calorieHistory.append(moveMent)
   return jsonify({"calaries":calaries});


@app.route("/RecommendedCal", methods=["GET"]) # Recommended calories to consume
def home():
    response = dict(message="The amount of Calories you should eat depends on your weight, age and gender. The average adult should eat about 2,000 calories a day. Go here for a better estimate: https://www.calculator.net/calorie-calculator.html")
    return response

@app.route("/RecommendedBurn", methods=["GET"])# Recommended calories to burn
def no():
    response = dict(message="The amount of Calories you should Burn depends on your weight, age and gender and most importanly your Goals. Go here for a better estimate: https://www.calculator.net/calorie-calculator.html")
    return response

@app.route('/CalTracker',methods = ['GET']) # Tracks what was eaten or lost through the day
def CalTracker():
   return jsonify(calorieHistory);

@app.errorhandler(404)  # Informs users that the page does not exist
def page_not_found(error):
    return dict(response="This page does not exist. Review the 'README' on the Docker File"), 404

if __name__ == '__main__':
   app.run(host="127.0.0.1", port=1942, debug = True)
