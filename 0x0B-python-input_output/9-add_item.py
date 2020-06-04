#!/usr/bin/python3
"""  + args to python list save to file """


from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


if __name__ == "__main__":

    try:
        js = load_from_json_file("add_item.json")
    except Exception:
        js = []

    arg = 1

    while(arg < len(argv)):
        js.append(argv[arg])
        arg += 1
    save_to_json_file(js, "add_item.json")
