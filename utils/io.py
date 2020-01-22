def read_from_file(scr):
    with open(scr) as file:
        data = file.read()
    return data


def save_oasm_to_file(string, args):
    src = args["<output>"]
    with open(src, "w") as file:
        file.write(string)


def save_or1_to_file(list, args):
    debug = args["-d"]
    if debug == True:
        src = args["<output>"]
        with open(src, "w") as file:
            for item in list:
                file.write(str(item))
                file.write(" ")
    else:
        raise BaseException("binary mode is not implemented")