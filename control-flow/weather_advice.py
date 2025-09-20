# A simple weather advice app

# Prompting user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Providing clothig recommendations

if weather == "sunny":
    clothing_recommendation = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    clothing_recommendation = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    clothing_recommendation = "Make sure to wear a warm coat and a scarf."
else:
    clothing_recommendation = "Sorry, I don't have recommendations for this weather."

# Displaying the recommendation       
print(clothing_recommendation)