import json
import math


with open('rain-flow.json') as f:
    loaded_json = json.load(f)

new_items = []
for json_item in loaded_json:

    new_item = json_item
    new_item['flow'] = math.ceil(int(json_item['flow']))
    rain = math.ceil(int(json_item['rain']))
    if new_item['flow'] > 0:
        new_item['rain'] = rain + 1
    else:
        new_item['rain'] = rain
    new_items.append(new_item)

with open('ceil_flow_train.json', '+w') as fo:
    json.dump(new_items, fo, indent=2)
