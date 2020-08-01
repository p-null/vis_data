import json



with open('emissions.json') as f:
    loaded_json = json.load(f)

new_items = []
for json_item in loaded_json:
    year = int(json_item['year'])
    if year > 1945:
        new_item = json_item
        new_item['year'] = str(year + 60)
        new_items.append(new_item)

with open('new_emissions.json', '+w') as fo:
    json.dump(new_items, fo, indent=2)
