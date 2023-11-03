# CSV Merger with Column Addition

This Python script efficiently processes a collection of CSV files that share a common structure, by appending two new columns derived from each file's name, then merging them into a single, comprehensive CSV file.

### Features:

- **Dynamic File Handling**: Automatically processes all CSV files within a specified directory.
- **Filename Parsing**: Extracts state and internet type information directly from the file names.
- **Column Addition**: Adds 'state' and 'internet_type' columns to each file's data based on the filename.
- **Data Consolidation**: Combines all individual CSV files into a single CSV for ease of analysis.
- **User-friendly**: Easy to use with clear output messaging.

### How It Works:

1. The script reads each CSV file from a predefined directory.
2. Parses the filename to determine the 'state' and 'internet_type'.
3. Adds these as columns to the data within the CSV.
4. Merges all the individual files into one combined file, without losing any data.
5. Outputs the merged file in the same directory.

### Prerequisites:

To run this script, you'll need Python installed on your system along with the `pandas` library. You can install `pandas` using pip:

```sh
pip install pandas
```

### Usage:

Place the script in the root of the directory containing your CSV files and run:

```sh
python csv_merger.py
```

The script will create a `combined_data.csv` in the same directory containing the merged data from all CSV files.

### Example Directory Structure Before Running Script:

```
states_unzipped/
├── az_cable.csv
├── az_copper.csv
├── az_fiber.csv
...
```

### Example Directory Structure After Running Script:

```
states_unzipped/
├── az_cable.csv
├── az_copper.csv
├── az_fiber.csv
...
└── combined_data.csv
```
