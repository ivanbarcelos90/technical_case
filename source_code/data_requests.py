# Import package
import requests

# Get the data from the hyperlinks and storage at the variables
r1 = requests.get('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2009-json_corrigido.json')
r2 = requests.get('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2010-json_corrigido.json')
r3 = requests.get('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2011-json_corrigido.json')
r4 = requests.get('https://s3.amazonaws.com/data-sprints-eng-test/data-sample_data-nyctaxi-trips-2012-json_corrigido.json')

# Write the data at the local repository
with open(r'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2009-json_corrigido.json', 'wb') as f1:
    f1.write(r1.content)

with open(r'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2010-json_corrigido.json', 'wb') as f2:
    f2.write(r2.content)

with open(r'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2011-json_corrigido.json', 'wb') as f3:
    f3.write(r3.content)

with open(r'C:\PersonalProjects/technical_case/trips/data-sample_data-nyctaxi-trips-2012-json_corrigido.json', 'wb') as f4:
    f4.write(r4.content)
