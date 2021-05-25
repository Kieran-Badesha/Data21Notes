from pprint import pprint

import pymongo

# Connecting to the MongoDB client
client = pymongo.MongoClient()
db = client['starwars']

# # Python will use snake case instead of Camel case like mongo shell
# # we use the same commands as in mongo shell but use snake case instead
#
# # find_one will allow us to print the first object it finds
# luke = db.characters.find_one({"name": "Luke Skywalker"})
# pprint(luke, sort_dicts=False)
#
# # find will just print the object id as there could be multiple objects
# luke = db.characters.find({"name": "Luke Skywalker"})
# print(luke)
#
# # for loop to print list of characters with name luke skywalker
# for char in luke:
#     print(char["name"])
#
# blue = db.chracters.find({"eye_color": "blue"})
#
# for char in blue:
#     print(char["name"])
#
# # use mapping to print list of names of characters with blue eyes
# blue_names = map(lambda x: x["name"], blue)
# pprint(list(blue_names))

# # print the names of all of the droids within the collection.
# droids = db.characters.find({"species.name": "Droid"})
#
# for droid in droids:
#     print(droid["name"])

# # Find the height of Darth Vader
# vader = db.characters.find({"name": 'Darth Vader'})
#
# for bad in vader:
#     print(bad["name"]+",", "Height =",bad['height'])

# # retrieving just the info we need to be efficient (name and height only)
# print(
#     db.characters.find_one(
#         {"name": 'Darth Vader'},
#         {"name": 1, "height": 1, "_id": 0}
#     )
# )

# # Find all chars with yellow eyes, only return the names of the chars
# yellow = db.characters.find(
#     {"eye_color": 'yellow'},
#     {"name": 1, "_id": 0}
# )
#
# for char in yellow:
#     print(char["name"])

# # Find all the male chars. Limit your results to the first 3
# male_chars = db.characters.find(
#     {"gender": "male"},
#     {"name": 1, "gender": 1, "_id": 0}
# ).limit(3)
#
# for char in male_chars:
#     print(char)

# # Find the names of all HUMANS whose homeworld is ALDERAAN
# hum_alderaan = db.characters.find(
#     {"species.name": "Human", "homeworld.name": "Alderaan"},
#     {"name": 1, "_id": 0}
# )
#
# for char in hum_alderaan:
#     print(char)

# # What is the avg height of female characters
# f_avg_height = db.characters.aggregate([
#      {"$match": {"gender": "female"}},
#      {"$group": {"_id": "$gender", "avg_height": {"$avg": "$height"}}}
# ])
#
# pprint(f_avg_height.next())

# # Which character is the tallest
# max_height = db.characters.aggregate([
#     {"$match": {"height": {"$ne": "unknown"}}},
#     {"$group": {"_id": "null", "MaximumValue": {"$max": "$height"}}}
# ]).next()["MaximumValue"]
#
# for tallest in db.characters.find({"height": max_height}):
#     print(tallest["name"], tallest["height"])
