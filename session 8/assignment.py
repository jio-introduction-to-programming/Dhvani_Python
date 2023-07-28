import json
import os
import pickle
import cv2
import pandas as pd

def persist_data(data, filename):
    # pass  # Use Python built-in functions to write 'data' to 'filename'
    with open(filename, 'w') as file:
            file.write(data)

def read_file(filename):
    # pass  # Use Python built-in functions to read contents of 'filename' and print them to screen
    with open(filename, 'r') as file:
        data = file.read()
        print(data)

def write_file(filename, data):
    # pass  # Use Python built-in functions to write 'data' to 'filename'
    with open(filename, 'w') as file:
        file.write(data)

def delete_file(filename):
    # pass  # Use Python built-in functions to delete 'filename'
    os.remove(filename)

def overwrite_file(filename, data):
    # pass  # Use Python built-in functions to overwrite 'filename' with 'data'
    with open(filename, 'w') as file:
        file.write(data)

def append_file(filename, data):
    # pass  # Use Python built-in functions to append 'data' to 'filename'
    with open(filename, 'a') as file:
        file.write(data)

def write_binary_file(filename, data):
    # pass  # Use Python built-in functions to write 'data' as binary to 'filename'
    with open(filename, "wb") as file:
        file.write(data)

def read_image_file(filename):
    # pass  # Use OpenCV to read 'filename' as an image
    image = cv2.imread(filename)
    cv2.imshow("Input Image", image)

def read_csv_file(filename):
    # pass  # Use Pandas to read 'filename' as a csv
    with open(filename,'r'):
        df = pd.read_csv(filename)
        print(df)

def write_csv_file(filename, df):
    # pass  # Use Pandas to write dataframe 'df' to 'filename'
    with open(filename,'w'):
        df.to_csv(filename, index=False)

def read_json_file(filename):
    # pass  # Use json to read 'filename' as a json
    with open(filename, 'r'):
        data = json.load(filename)
        print(data)

def write_json_file(filename, data):
    # pass  # Use json to write 'data' to 'filename'
    with open(filename, 'w'):
        json.dump(data, filename)

def write_pickle_file(filename, data):
    # pass  # Use pickle to write 'data' to 'filename'
    with open("data.pkl", "wb") as file:
        pickle.dump(data, filename)

def read_pickle_file(filename):
    # pass  # Use pickle to read 'filename'
    with open(filename,'rb'):
        data = pickle.load(filename)
        print(data)
