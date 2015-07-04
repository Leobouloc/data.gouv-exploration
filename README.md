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