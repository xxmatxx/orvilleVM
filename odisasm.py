from parsy import char_from, regex, generate

def read_from_file(scr):
    with open(scr) as file:
        data = file.read()
    return data

def parse(string):
    pass

whitespace1p = char_from("\n\r\t ").desc("at lest 1 white space character").at_least(1)
integerp = regex(r"-?\d+").map(int).desc("integer")

@generate
def debug_format():
    result = yield integerp
    yield whitespace1p
    return result


test = debug_format.many().parse("15 15 15 ")
print(test)