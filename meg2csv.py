from io import StringIO
import os 
import pandas as pd
import argparse

def convert_meg_to_csv(input_matrix):
    """
    Converts a MEGA pairwise matrix MEG file into a long-format (tidy) CSV file.
    Output CSV file will be saved on the same directory as the input MEG file.

    Args:
        input_matrix (list of lists): Path to the pairwise distance matrix MEG file created by MEGA
    
    Returns:
        None
    """
    try:
        with open(input_matrix, mode='r') as file:
            text = file.read()
            no_header = text.split(';')[-1] # remove file header
            sample_dict = {} # dictionary to save sample names
            dictionary_data = True
            count_empty_lines = 0
            dataset_rows = []
            for line in no_header.splitlines():
                if line.strip() == '':
                    count_empty_lines += 1
                    if count_empty_lines > 2:
                        dictionary_data = False
                elif dictionary_data:
                    line_split = line.split('#')
                    key = line_split[0].replace('[', '').replace(']', '').strip()
                    value = line_split[1].strip()
                    sample_dict[key] = value
                else: 
                    dataset_rows.append(','.join(line.replace('[', '').replace(']', '').split()))
            dataset_rows[0] = '0,' + dataset_rows[0] # column fix
            dataset = StringIO('\n'.join(dataset_rows))
            df = pd.read_csv(dataset)
            df['0'] = df['0'].astype(str).map(sample_dict) # replace row numbers with sample names
            df.set_index('0', inplace=True)
            df.columns = [sample_dict[col] for col in df.columns] # replace col numbers with sample names
            long_df = df.stack(future_stack=True).reset_index()
            long_df.columns = ['sample1', 'sample2', 'distance']
            long_df.dropna(subset=['distance'], inplace=True)
            long_df['distance'] = long_df['distance']
            dirname = os.path.dirname(os.path.abspath(input_matrix))
            output_csv = os.path.join(dirname, 'pairwise_distances.csv')
            long_df.to_csv(output_csv, index=False)
            print(f'Successfully parsed {input_matrix} into {output_csv}')
    except Exception as e:
        print(f'Failed to parse {input_matrix} into {output_csv}')
        print('Error:', e)


def main():
    parser = argparse.ArgumentParser(description='Parse a MEGA pairwise distance matrix MEG file into a tidy CSV file called "pairwise_distances.csv" located in the same directory as the input MEG file')
    parser.add_argument('input', type=str, help='Path to the input MEG file created by MEGA')
    args = parser.parse_args()
    convert_meg_to_csv(args.input)
    

if __name__ == '__main__':
    main()
