import json
# Load the original file
with open("US_recipes_null.json", "r", encoding="utf-8") as infile:
    data = json.load(infile)
# Convert dict-of-dicts to list
recipes_list = list(data.values())
# Save to new file
with open("recipes_fixed.json", "w", encoding="utf-8") as outfile:
    json.dump(recipes_list, outfile, indent=4)
print("✅ JSON fixed and saved to recipes_fixed.json")
