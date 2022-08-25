import re


def is_float(float_value):
    try:
        float(float_value)
        return True
    except ValueError:
        return False


def format_value(value_type):
    value_type = re.split("\s*#", value_type)[0]
    boolean_values = {
        "yes": True,
        "true": True,
        "on": True,
        "false": False,
        "off": False,
        "no": False,
    }
    if value_type.isdigit():
        return int(value_type)
    elif value_type.lower() in boolean_values:
        return boolean_values[value_type.lower()]
    elif is_float(value_type):
        return float(value_type)

    return value_type


def get_config_values(file):
    config_values = {}
    for line in file:
        line = re.sub("\s*\n$", "", line)
        if not re.search("^\s*#", line):
            try:
                (key, value) = re.split('\s*=\s*', line, maxsplit=1)
            except ValueError:
                continue
            config_values[key] = format_value(value)
    return config_values


def get_config(configs):
    input_config = "Get Config Value, type 'quit' to end\n"
    config_name = input(input_config)
    while config_name != "quit":
        if config_name not in configs:
            print("Invalid Config Name")
        else:
            print('Config Value: ' + str(configs[config_name]))
            print('Config Value Type: ' + str(type(configs[config_name])))

        config_name = input(input_config)


# Gets configs
def get_file_configs(file_path=None):
    if file_path is None:
        file_path = input("Path to file\n")
    try:
        f = open(file_path, "r")
    except FileNotFoundError:
        print('Invalid File')
        exit()

    config_values = get_config_values(f)

    f.close()

    return config_values