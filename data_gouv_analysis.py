# -*- coding: utf-8 -*-

'''
Extract files from "data.gouv" and detect columns
'''

import os
import requests
import json

from csv_detective.explore_csv import routine


def download_file(url):
    '''Downloads file from URL unless it is in cache and returns file_path'''
    local_filename = url.split('/')[-1]
    if not isfile(os.path.join('.cache_csv', local_filename)):
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(join(download_path, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
    return os.path.join('.cache_csv', local_filename)



# Temporary storage for csv files downloaded from data.gouv
if not os.path.isdir('.cache_csv'):
	os.mkdir('.cache_csv')

# Storage for the detection jsons that are generated
if not os.path.isdir('cache_json'):
	os.mkdir('cache_json')




list_url = 'https://www.data.gouv.fr:443/api/1/datasets/?sort=created&format=csv&page_size=20'


max_pages = 100
while max_pages > 0:
    max_pages -= 1
    page = requests.get(list_url).json()
    list_url = page['next_page']
    data = page['data']
    
    for i in range(20):
        download_url = data[i]['resources'][0]['url']

        import pdb
        pdb.set_trace()
        download_file(download_url)






# for file_name in all_files:
#     print '*****************************************'
#     print file_name
#     if any([extension in file_name for extension in ['.csv', '.tsv']]):
#         file = open(join(path, file_name), 'r')
#         a = routine(file)
#         file.close()
#         if a:
#             counter += len(a)
#             with open(join(json_path, file_name.replace('.csv', '.json')), 'wb') as fp:
#                 json.dump(a, fp, indent=4, separators=(',', ': '), encoding="utf-8")
#     print '\n'
# print 'on a trouvé des matchs éventuels pour ', counter, 'valeurs'