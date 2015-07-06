# Enriching data.gouv metadata using csv_detective (WORK IN PROGRESS)

This project is a direct usecase of `csv_detective` (see [here](https://github.com/SGMAP-AGD/csv_detective)). The goal is to automatically detect content of the 20K or so tables in data.gouv. This helps with cross-analyses.

## How ?

This requires installing `csv_detective`:

```
git clone https://github.com/SGMAP-AGD/csv_detective
cd csv_detective
python setup.py install
```

Then clone this package and run the script

```
git clone https://github.com/Leobouloc/data.gouv-exploration
cd data.gouv-exploration
python data_gouv_analysis.py
```

This will download CSV files from data.gouv (btw, you can change `erase_csv_cache` to False to save space) and analyse them with csv_detective. Results will be stored in cache_json.
