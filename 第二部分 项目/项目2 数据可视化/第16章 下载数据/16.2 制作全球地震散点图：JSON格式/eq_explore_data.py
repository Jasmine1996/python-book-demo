import json

# 探索数据的结构。
filename = '../data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = '../data/test.json'

with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)