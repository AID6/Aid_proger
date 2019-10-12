def update_dictionary(d, key, value):
    try:
        d[key] == value
    except:
        return None
    d[2] = []
    d[2].append(value)

d = {}
print(update_dictionary(d, 1, -1))
print(d)
update_dictionary(d, 2, -2)
print(d)
update_dictionary(d, 1, -3)
print(d)