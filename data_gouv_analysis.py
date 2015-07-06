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
    print 'Loading {url}'.format(url=url)
    local_filename = url.split('/')[-1]
    write_path = os.path.join('.cache_csv', local_filename)
    if not os.path.isfile(write_path):
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(write_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
    return write_path


def download_all():
    list_url = 'https://www.data.gouv.fr:443/api/1/datasets/?sort=created&format=csv&page_size=20'
    max_pages = 100
    while max_pages > 0:
        max_pages -= 1
        page = requests.get(list_url).json()
        list_url = page['next_page']
        data = page['data']
        
        for i in range(20):
            download_url = data[i]['resources'][0]['url']
            try:
                yield download_file(download_url)
            except:
                print 'Could not download {url}'.format(url=download_url)


if __name__ == '__main__':

    # Will erase downloaded CSV's if variable is set to True
    erase_csv_cache = False

    ####
    # Temporary storage for csv files downloaded from data.gouv
    if not os.path.isdir('.cache_csv'):
    	os.mkdir('.cache_csv')

    # Storage for the detection jsons that are generated
    if not os.path.isdir('cache_json'):
    	os.mkdir('cache_json')

    list_tests = ['ALL', '-FR.geo.code_departement']
    for file_path in download_all():

        # Open your file and run csv_detective
        with open(file_path, 'r') as file:
            inspection_results = routine(file, user_input_tests = list_tests)

        # Write your file as json
        json_path = os.path.join('cache_json', os.path.basename(file_path).replace('.csv', '.json'))
        with open(json_path, 'wb') as fp:
            json.dump(inspection_results, fp, indent=4, separators=(',', ': '), encoding="utf-8")

        if erase_csv_cache:
            os.remove(file_path)