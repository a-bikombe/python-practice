groceries = {'fruits': ['mangoes', 'bananas', 'kiwis'],
            'protein': ['beef', 'pork', 'salmon'],
            'carbs': ['rice', 'pasta', 'bread'],
            'veggies': ['lettuce', 'cabbage', 'onions']}

party_planning = {'Yes': 10,
					'No': 15,
					'Maybe': 30,
					'Location': 'Our Backyard',
					'Date': '2022/05/01'}

party_planning['Location'] # returns 'Our Backyard'
party_planning['Location'] = 'At the park'
party_planning['Location'] # prints 'At the park'

party_planning['Dress Code'] = 'Casual'

len(party_planning) # returns 5

# .update()
shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}

shopping_list1.update(shopping_list2)

print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}

# .keys() and .values()
shopping_list = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}

shopping_list.keys() # returns dict_keys(['jewelry', 'clothes', 'budget'])
shopping_list.values() # returns dict_values(['earrings', 'jeans', 200])