import glob
import argparse
import os
import json


def load_files(path):
    files = {}
    data_files = glob.glob(f"{path[0]}/*.json")

    for data_file_path in data_files:
        with open(data_file_path, "r", encoding="utf-8") as raw:
            json_file = json.load(raw)
            files[f"{data_file_path}"] = json_file

    return files


def main():
    parser = argparse.ArgumentParser(description="Directory path.")
    parser.add_argument(
        "file_path",
        nargs="+",
        metavar="FILE_PATH",
        help="Provide correct directory path.",
    )

    date_fields = ["orderFromDate", "orderToDate", "orderStartDate", "orderEndDate"]
    args = parser.parse_args()
    files = load_files(args.file_path)

    for path, file in files.items():
        format_date(date_fields, file)
        save_file(path, file)


def save_file(fullpath, file):
    path_arr = os.path.split(fullpath)
    filename = path_arr[1]
    dirpath = path_arr[0]
    output_path = f"{dirpath}/output"
    print(dirpath)
    print(filename)
    if not os.path.exists(output_path):
        os.mkdir(f"{dirpath}/output")
    with open(f"{output_path}/{filename}", "w") as jsonfile:
        json.dump(file, jsonfile)


def format_date(date_fields, file):
    data = file["data"]
    for obj in data:
        for order in obj["orders"]:
            for date_field in date_fields:
                attr_value = order.get(date_field, None)
                if attr_value != None:
                    value = convert_to_date(attr_value)
                    order.update({date_field: value})
    print(file)


def convert_to_date(value):
    year = value.get("year")
    month = add_zero(int(value.get("month")))
    day = add_zero(int(value.get("day")))
    return f"{year}-{month}-{day}"


def add_zero(period):
    if period > 9:
        return str(period)
    else:
        return f"0{period}"


if __name__ == "__main__":
    main()
