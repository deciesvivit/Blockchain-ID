import json

data = [json.loads(line) for line in open('review.json','r')]

print(data)