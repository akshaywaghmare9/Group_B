# yaml module:





# Serialization :



# import yaml


# s={'raincoat': 1, 'coins': 5, 'books': 23, 'spectacles': 2, 'chairs': 12, 'pens': 6}
# with open('items.yaml','w') as f:
# 	data=yaml.dump(s,f)










# Deserialization




# import yaml

# with open('items.yaml') as f:
# 	data= yaml.safe_load(f)     # data=yaml.load(f,Loader=yaml.Fullloader)
# 	print(data)











# we can sort keys also




# import yaml

# with open('items.yaml') as f:
    
#     data = yaml.load(f, Loader=yaml.FullLoader)
#     print(data)

#     sorted = yaml.dump(data, sort_keys=True)
#     print(sorted)


