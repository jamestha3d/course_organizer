def EmailReplace(template, key_dict:dict):
    key_list = list(key_dict.keys())

    for item in key_list:
        if dict[item] is None:
            dict[item] = ''

        template = template.replace("["+item+"]", dict[item])

    return template