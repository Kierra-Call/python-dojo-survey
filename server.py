from flask import Flask, render_template, redirect, request, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'anything you want'

#THIS WILL MOVE LOCATIONS LATER -- (controller file)
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def get_info():
    return render_template('index.html')
#*******************************

@app.route('/results', methods=['POST'])
def display_data():
    session['data'] = {**request.form}
    return redirect('/display_info')

@app.route('/display_info')
def display_info():
    return render_template('thanks.html')



#This is always at the bottom!
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.