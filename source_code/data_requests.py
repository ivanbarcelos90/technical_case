# Import package
import requests
from clint.textui import progress
import os


def download_file(filepath):
    print("Downloading " + filepath)
    r = requests.get(filepath, stream=True)
    destination_path = '../trips/' + filepath.split('/')[-1]

    with open(destination_path, 'wb') as f:
        length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=4096), expected_size=(length / 4096) + 1):
            if chunk:
                f.write(chunk)
                f.flush()

if __name__ == '__main__':
    # Get the data from the hyperlinks and storage at the variables
    files = ['https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json',
             'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json',
             'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json',
             'https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json']

    for file in files:
        os.makedirs('../trips/', exist_ok=True)
        download_file(file)
