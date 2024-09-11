import subprocess
import sys
from flask import Flask, render_template, request

# Function to check if Flask is installed and install it if necessary
def install_flask():
    try:
        import flask
        print("Flask is already installed.")
    except ImportError:
        print("Flask is not installed. Installing Flask...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
        print("Flask installed successfully.")

# Ensure Flask is installed before running the Flask app
install_flask()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    user_command = request.form['command']

    result = ""
    
    # Perform calculations based on the user's command
    if user_command.lower() == "enthalpy":
        try:
            internal_energy = float(request.form['internal_energy'])
            pressure = float(request.form['pressure'])
            volume = float(request.form['volume'])
            enthalpy = internal_energy + (pressure * volume)
            result = f"Enthalpy: {enthalpy} J"
        except ValueError:
            result = "Invalid input for enthalpy calculation."

    elif user_command.lower() == "entropy":
        try:
            q_rev = float(request.form['q_rev'])
            T = float(request.form['temperature'])
            if T <= 0:
                result = "Temperature must be greater than 0 K."
            else:
                delta_S = q_rev / T
                result = f"Entropy (ΔS): {delta_S} J/K"
        except ValueError:
            result = "Invalid input for entropy calculation."

    elif user_command.lower() == "gibbs":
        try:
            delta_H = float(request.form['delta_H'])
            T = float(request.form['temperature'])
            delta_S = float(request.form['delta_S'])
            if T <= 0:
                result = "Temperature must be greater than 0 K."
            else:
                delta_G = delta_H - T * delta_S
                result = f"Gibbs Free Energy (ΔG): {delta_G} J"
        except ValueError:
            result = "Invalid input for Gibbs free energy calculation."

    else:
        result = "Invalid command."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
