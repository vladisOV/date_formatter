import glob
import argparse
import os
import json


def load_files(path):
    files = {};
    data_files = glob.glob(f"{path[0]}/*.json")

    for data_file_path in data_files:
        with open(data_file_path, "r", encoding="utf-8") as raw:
            json_file = json.load(raw)
            files[f'{data_file_path}'] = json_file
    
    return files


def main():
    parser = argparse.ArgumentParser(description='Directory path.')
    parser.add_argument("file_path",
                        nargs='+', metavar='FILE_PATH',
                        help="Provide correct directory path.")

    date_fields = ["orderFromDate"]
    args = parser.parse_args()
    files = load_files(args.file_path)

    for path, file in files.items():
        format_date(date_fields, file)
        save_file(path, file)
        

def save_file(filepath, file):
    filename = os.path.split(filepath)[1]
    with open(filename, "w") as jsonfile:
        json.dump(file, jsonfile)


def format_date(date_fields, file):
    for field in date_fields:
        file["data"][0]["orderFromDate"] = "123"
        print(file)
        # file["orderFromDate"] = "123"

if __name__ == "__main__":
    main()