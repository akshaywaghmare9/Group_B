# json to yaml format:








# import yaml

# data={

  
#   "Vegetable": "Carrot", 
#   "Meat": "Chicken", 
#   "Liquid": "Water", 



#   "Fruits":
#    [
#     "Orange", 
#     "Apple", 
#     "Banana"
#   ], 
   
#   "Vegetables":
#    [
#     "Carrot", 
#     "Potato", 
#     "Tomato"
#   ], 
#   "Banana":
#   {
#     "Carbs": "27 g", 
#     "Calories": 62, 
#     "Fat": "0.4 g"
#   }
# }


# print(type(data))
# print(data)


# print(yaml.dump(data))










# import yaml


# s={'raincoat': 1, 'coins': 5, 'books': 23, 'spectacles': 2, 'chairs': 12, 'pens': 6}

# print(s)
# print(yaml.dump(s))














# Dict format to yaml:





# import yaml

# data={'Name':'Akshay',
#       'age':25,
#       'handles':{'instagram': 'akshay_waghmare',
#       'github': 'akshaywaghmare9',
#       'facebook': 'akshay waghmare'},
#       'languages':{'markup': ['HTML','XML','AIML'],
#       'programming':['c','c++','python','java','None',True]}
#         }               



# print(type(data))
# print(data)

# print(yaml.dump(data))














# json to yaml:

# Dict vs list vs list of dict:




# import yaml

# d=[
#   {
#     "Transmission": "Automatic", 
#     "Car": {
#       "Model": "Urus", 
#       "Name": "Lamborghini"
#     }, 
#     "Price": "3.10 Crore", 
#     "color": "Black"
#   }, 
#   {
#     "Transmission": "Automatic", 
#     "Car": {
#       "Model": "R8", 
#       "Name": "Audi"
#     }, 
#     "Price": "2.07 Crore", 
#     "color": "Green"
#   }, 
#   {
#     "Transmission": "Automatic", 
#     "Car": {
#       "Model": "Huracan", 
#       "Name": "Lamborghini"
#     }, 
#     "Price": "3.22 Crore", 
#     "color": "Yellow"
#   }, 
#   {
#     "Transmission": "Automatic", 
#     "Car": {
#       "Model": "F8 Tributo", 
#       "Name": "Ferrari"
#     }, 
#     "Price": "4.02 Crore", 
#     "color": "Blue"
#   }, 
#   {
#     "Transmission": "Automatic", 
#     "Car": {
#       "Model": "Bentayga V8 Petrol", 
#       "Name": "Bentley"
#     }, 
#     "Price": "4.10 Crore", 
#     "color": "Alpha Green"
#   }
# ]


# data=yaml.dump(d)
# print(data)

# print(yaml.safe_load(data))
# print(type(data))










