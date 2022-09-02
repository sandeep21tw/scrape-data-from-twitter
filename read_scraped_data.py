from pprint import pprint
import json


with open("testing.json", "r") as f:
	data = json.load(f)

print(type(data))

pprint(data)





















"""
# Earlier, the logic was different, modified version a bit now.

# since there are many twitter object in testing.json, we need to convert them to list and then use a loop on 
# them
data = data.split(",qseroiurewfijdei")
data = data[:-1]    # last item is just ,qseroiurewfijdei

"""



# length is showing greater than 100 but how could this be possible, i need to learn more about cursor
# and .search_tweets from twitter api or tweepy
# haha, it's because we are writing in append mode, idiot!!!
#but the problem is the first tweet object is weird and giving idk why for what reason giving error!
# NOw, fixed on its own, dk what is happening AHHHHHH
#pprint((tweet))


# ---------EARLIER THERE WAS ERROR BELOW -------

# tweet = data[-1]
# pprint((tweet))

# earlier, it was i think just a single tweet and hence only dictionary when converted to str. but this time
# is dict inside list inside str
# SOLVED:
"""
earlier, i have manually added the opening([) and closing(]) brackets in testing.json, idk why what am i thinking
i thought it will be a list but i forget, when reading it will be loaded as string and we need to use split
not list, if we use list, it will create a list for every character in string which is kinda wrong.!!!
"""