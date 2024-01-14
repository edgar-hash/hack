from flask import Flask, render_template, request
from csv_1 import csvChecker
app = Flask(__name__)

# Sample options array
options_array = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_food', methods=['POST'])
def submit_food():
    food_item = request.form.get('foodInput')
    dining_hall = request.form.get('diningHall')
    

    # Example processing: You can use food_item and dining_hall as needed
    options_array = csvChecker(dining_hall, food_item)
    # Pass the options array to the result template
    return render_template('result.html', food_item=food_item, dining_hall=dining_hall, options_array=options_array)

if __name__ == '__main__':
    app.run(debug=True)
