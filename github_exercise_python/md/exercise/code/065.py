def string_to_dict(string):
    d = {}
    for kv in string.split("|"):
        k, v = kv.split(":")
        v = int(v)
        d[k] = v
    return d


string = "k:1|k1:2|k2:3|k3:4"
print(string_to_dict(string))
