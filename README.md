# meg2tidy
A Python utility to parse [MEGA](https://www.megasoftware.net/) (.meg) pairwise distance matrices into a long-format (tidy) CSV file. This tool converts wide-format matrices into a column-based structure suitable for data visualization and analysis in tools like [Cytoscape](https://cytoscape.org/).
## Features
- Parses standard MEGA distance matrix files (.meg). 1.2.5
- Outputs a three-column CSV: sample1, sample2, distance
- Command-line interface (CLI) for easy integration into bioinformatics pipelines.
## Installation
Ensure you have Python 3.x and pandas installed.
```bash
git clone https://github.com/caladov/mega-matrix-to-column.git
```
## Usage
```bash
python matrix2col.py input_file.meg
```
## Output
The script generates a CSV file named pairwise_distances.csv in the directory where the input MEG file is located.
```
sample1 sample2 distance
sampleA sampleB     38.0
sampleA sampleC     52.0
sampleB sampleC     16.0
```


