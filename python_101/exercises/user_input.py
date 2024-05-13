print("Distance converter: from Km to miles")

name = input("What is your name?: ")
distance_km = input("Enter the distance in km: ")
distance_mi = float(distance_km) / 1.609
print(f"Hi {name.capitalize()}! {distance_km} kilometers is equivalent to {round(distance_mi, 2)} miles.")


