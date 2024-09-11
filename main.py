import math
### enthalpy, entropy, Gibbs free energy

## Enthalpy
user_command = input("What would you like to calculate? ")

if user_command == "Enthalpy" or "enthalpy" or "entalpy":
    internal_energy = float(input("What is the value for the Internal Energy? "))
    pressure = float(input("What is the value for the Pressure? "))
    volume = float(input("What is the value for the Volume? "))
    enthalpy = internal_energy + (pressure * volume)
    print(enthalpy)
elif user_command == "Entropy" or "entropy" or "entrpy":
    q_rev = float(input("Enter the reversible heat exchange (q_rev) in joules: "))
    T = float(input("Enter the temperature (T) in Kelvin: "))
    # Check if the temperature is above absolute zero
    if T <= 0:
        print("Temperature must be greater than 0 K.")
    elif T>0:
        # Entropy calculation
        delta_S = q_rev / T
        print(f"The change in entropy (ΔS) is: {delta_S} J/K")
elif user_command == "gibbs" or "Gibbs Free Energy" or "Free Energy":
    # Input section
    delta_H = float(input("Enter the change in enthalpy (ΔH) in joules: "))
    T = float(input("Enter the temperature (T) in Kelvin: "))
    delta_S = float(input("Enter the change in entropy (ΔS) in J/K: "))

# Check if temperature is above absolute zero
if T <= 0:
    print("Temperature must be greater than 0 K.")
else:
    # Gibbs free energy calculation
    delta_G = delta_H - T * delta_S
    print(f"The change in Gibbs free energy (ΔG) is: {delta_G} J")






