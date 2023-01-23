is_equal = True

def compare_json(json1, json2):
    global is_equal
    for key, value in json1.items():
        if type(value) == dict:
            compare_json(value, json2[key])
        else:
            if value != json2[key]:
                is_equal = False
                break
    return is_equal

