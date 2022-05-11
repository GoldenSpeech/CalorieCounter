# Calorie Counter 
## _Simply Simple Calorie Counter_
_________________


You record and track the calories you consume or lose over the period of time and this app will record it for you. It also gives some advice based on your goals and refers you to sites that may be of more benefit. 

## Pre-requisites
_________________
- Install Python
- Install Flask
--  `pip install --no-cache-dir -r requirements.txt`

## Starting the App / Command lines
_________________
From the command line or terminal, start the server with the following command:
- `python Calorie.py`

Use Postamn or Curl with the links below. 
- GET http://127.0.0.1:3300//getCurrentCal
    * Gives you the current recored calorie count
- GET http://127.0.0.1:3300//CalTracker
    * Gives you the History of all the recored calorie inputs
- GET http://127.0.0.1:3300//RecommendedCal
    * Gives you the Reccomended calorie consumption
- GET http://127.0.0.1:3300//RecommendedBurn
    * Gives you the Reccomended amount of calories to burn
- POST http://127.0.0.1:3300//CaloriesAte
    * Using JSON text, you can input an "amount" you ate and it will recored it.
- POST http://127.0.0.1:3300//CalLost
     * Using JSON text, you can input an "amount" you burned and it will recored it.

## Running via Docker
_________________
- Pull Image
    * ` docker pull kaguled/hw1_api  `
- Run Image
   * ` docker run -p 127.0.0.1:3300:3300 -it kaguled/hw1_api `
- Use Postman or Curl and implement the GET/POST Commands above. 
