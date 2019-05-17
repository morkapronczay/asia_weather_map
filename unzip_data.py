import zipfile
import os

with open('data/countries.txt', 'r') as fp:
    countries = [f.strip('\n') for f in fp.readlines()]

for c in countries:
    path_to_zip_file = f'data/{c}.zip'
    directory_to_extract_to = 'data/'
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
    os.unlink(path_to_zip_file)
	
print('files unzipped.')