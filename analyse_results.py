import os
import json
from pprint import pprint

import pandas as pd 

all_file_paths = [os.path.join('cache_json', x) for x in os.listdir('cache_json')]
result_dict = dict()

# Number of files
print 'There is a total of {num_files} json files'.format(num_files=len(all_file_paths))
result_dict['num_files'] = len(all_file_paths)

result_dict['num_errors'] = 0
result_dict['num_valid'] = 0
result_dict['columns_detected'] = 0
result_dict['propositions_made'] = 0
result_dict['unique_detections'] = 0

result_dict['column_count'] = {}


for file_path in all_file_paths:
	with open(file_path, 'rb') as f:
		data = json.load(f)
	if 'error' in data.keys():
		result_dict['num_errors'] += 1
	elif 'columns' in data.keys():
		result_dict['num_valid'] += 1
		columns = data['columns']
		for key, values in columns.iteritems():
			result_dict['columns_detected'] += 1
			if len(values) == 1:
				result_dict['unique_detections'] += 1
			for val in values:
				result_dict['propositions_made'] += 1
				if val in result_dict['column_count'].keys():
					result_dict['column_count'][val] += 1
				else:
					result_dict['column_count'][val] = 1

pprint(result_dict)
import pdb
pdb.set_trace()
