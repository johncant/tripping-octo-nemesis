import numpy
import json
import io

# Example dataset to use
# '../data/ASB Noise Cleansing Waste Washing/vomiting-lat-long.csv'

def ConvertToJSON(data, write_to_file):
    # This function takes a numpy array and converts it to a json
    # The output depends on the 'write_to_file' boolean
    # Args:
    #   data: csv dataset with lat and long co-ordinates
    #   write_to_file: a boolean of 'T' or 'F'
    #                  T: export to txt file
    #                  F: put into a variable
    # Returns:
    #   either a json in a txt file or into a variable
    # Usage:
    #   a = ConvertToJson('path-to-file/file.csv', 'T')
    #   Note, nothing is stored in a
    
    # Read the file as a numpy array and convert to json
    a = numpy.loadtxt(data, delimiter = ',', skiprows=1)
    a = a[numpy.where(a[:,0] != 0)]   
    lst = list(a)
    json_trial = json.dumps([dict(lat = i[0], long=i[1]) for i in lst])
    
    # Either output to file or to a variable 
    if write_to_file == 'T':
        with io.open('json_trial.txt', 'w', encoding='utf-8') as f:
            f.write(unicode(json_trial))
        return
    else:
        return json_trial
    
