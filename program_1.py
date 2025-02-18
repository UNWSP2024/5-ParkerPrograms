# Nathan Parker
# 2/17/25
# Program #1: Kilometer Converter


# define a function that converts kilometers to miles
def converter_from_km_to_mi(kilometers):
    miles = kilometers * 0.6214
    return miles

# get the distance in kilometers from the user
distance_in_km = float(input('Enter a distance in kilometers: '))

# run the function and set the result to the variable distance_in_mi
distance_in_mi = converter_from_km_to_mi(distance_in_km)

# display the result
print(f'That is equal to {distance_in_mi} miles.')

