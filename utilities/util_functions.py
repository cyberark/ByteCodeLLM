import json

def find_closest_match(data,index,value):
    for i in range(index,len(data)):
        if data[i].startswith(value):
            return i
    return None

def reduce_indent_by_one(data):
    # only if the first character is a tab or 4 spaces
    for i in range(len(data)):
        if data[i].startswith('    '):
            data[i] = data[i][4:]
        elif data[i].startswith('\t'):
            data[i] = data[i][1:]
    return data

def increase_indent_by_one(data):
    for i in range(len(data)):
        data[i] = '    ' + data[i]
    return data

def convert_indent_to_spaces(data):
    is_bytes = isinstance(data[0],bytes)
    for i in range(len(data)):
        if not is_bytes:
            data[i] = data[i].replace('\t','    ')
        else:
            data[i] = data[i].replace(b'\t',b'    ')
    return data

def convert_spaces_to_indent(data):
    for i in range(len(data)):
        data[i] = data[i].replace('    ','\t')
    return data

def is_valid_json(string):
    try:
        json.loads(str(string))
        return True
    except ValueError:
        return False