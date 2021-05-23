#!/bin/python3
import json

# A multiline JSON String Object
json_string = """
{
"users" : [
  {
    "userId": 1,
    "id": 1,
    "title": ["English", "Fench"],
    "completed": false
  },
  {
    "userId": 1,
    "id": 2,
    "title": "quis ut nam facilis et officia qui",
    "completed": false
  },
  {
    "userId": 8,
    "id": 149,
    "title": "animi voluptas quod perferendis est",
    "completed": false
  },
  {
    "userId": 8,
    "id": 150,
    "title": "eos amet tempore laudantium fugit a",
    "completed": false
  },
  {
    "userId": 8,
    "id": 151,
    "title": "accusamus adipisci dicta qui quo ea explicabo sed vero",
    "completed": true
  },
  {
    "userId": 8,
    "id": 152,
    "title": "odit eligendi recusandae doloremque cumque non",
    "completed": false
  },
  {
    "userId": 8,
    "id": 153,
    "title": "ea aperiam consequatur qui repellat eos",
    "completed": false
  },
  {
    "userId": 8,
    "id": 154,
    "title": "rerum non ex sapiente",
    "completed": true
  },
  {
    "userId": 8,
    "id": 155,
    "title": "voluptatem nobis consequatur et assumenda magnam",
    "completed": true
  },
  {
    "userId": 8,
    "id": 156,
    "title": "nam quia quia nulla repellat assumenda quibusdam sit nobis",
    "completed": true
  },
  {
    "userId": 8,
    "id": 157,
    "title": "dolorem veniam quisquam deserunt repellendus",
    "completed": true
  },
  {
    "userId": 8,
    "id": 158,
    "title": "debitis vitae delectus et harum accusamus aut deleniti a",
    "completed": true
  },
  {
    "userId": 8,
    "id": 159,
    "title": "debitis adipisci quibusdam aliquam sed dolore ea praesentium nobis",
    "completed": true
  },
  {
    "userId": 8,
    "id": 160,
    "title": "et praesentium aliquam est",
    "completed": false
  },
  {
    "userId": 9,
    "id": 161,
    "title": "ex hic consequuntur earum omnis alias ut occaecati culpa",
    "completed": true
  },
  {
    "userId": 9,
    "id": 162,
    "title": "omnis laboriosam molestias animi sunt dolore",
    "completed": true
  },
  {
    "userId": 10,
    "id": 191,
    "title": "temporibus atque distinctio omnis eius impedit tempore molestias pariatur",
    "completed": true
  },
  {
    "userId": 10,
    "id": 192,
    "title": "ut quas possimus exercitationem sint voluptates",
    "completed": false
  },
  {
    "userId": 10,
    "id": 193,
    "title": "rerum debitis voluptatem qui eveniet tempora distinctio a",
    "completed": true
  },
  {
    "userId": 10,
    "id": 194,
    "title": "sed ut vero sit molestiae",
    "completed": false
  },
  {
    "userId": 10,
    "id": 195,
    "title": "rerum ex veniam mollitia voluptatibus pariatur",
    "completed": true
  },
  {
    "userId": 10,
    "id": 196,
    "title": "consequuntur aut ut fugit similique",
    "completed": true
  },
  {
    "userId": 10,
    "id": 197,
    "title": "dignissimos quo nobis earum saepe",
    "completed": true
  },
  {
    "userId": 10,
    "id": 198,
    "title": "quis eius est sint explicabo",
    "completed": true
  },
  {
    "userId": 10,
    "id": 199,
    "title": "numquam repellendus a magnam",
    "completed": true
  },
  {
    "userId": 10,
    "id": 200,
    "title": "ipsam aperiam voluptates qui",
    "completed": false
  }
]
}
"""

json_dict = json.loads(json_string)

# Print the number of times userId with 8 occured
counter = 0

for user in json_dict['users']:
    if user['userId'] == 8:
        counter += 1
# Output: Users with ID 8 = 12
print ("Users with ID " + str(user['userId']) + " = " + str(counter))

# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for user in json_dict['users']:
    if user["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[user["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[user["userId"]] = 1

todos_json = json.dumps(todos_by_user, indent=4, sort_keys=True)

# Output will be a dict type object
# {8: 7, 9: 2, 10: 7}
print(todos_by_user)

# Output will be a JSON
# {
#     "8": 7,
#     "9": 2,
#     "10": 7
# }
print(todos_json)
