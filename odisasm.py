from parsy import char_from, regex, generate

def read_from_file(scr):
    with open(scr) as file:
        data = file.read()
    return data

def parse_debug_or1(string):
    return debug_format.many().parse(string)

whitespace1p = char_from("\n\r\t ").desc("at lest 1 white space character").at_least(1)
integerp = regex(r"-?\d+").map(int).desc("integer")

@generate
def debug_format():
    result = yield integerp
    yield whitespace1p
    return result


test = debug_format.many().parse("7 0 13 0 13 1 1 17 20 9 11 9 10 18 2 19 0 2 9 3 9 130 18 2 19 0 2 ")
#print(test)