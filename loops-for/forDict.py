def reverse_dict(dict):
    B = {}
    for key, value in dict.items():
        B[value] = key
    print(B)
    # swap keys and values within dict and return dict