from parsy import char_from, regex, char_from, generate, alt,seq

class Label():
    def __init__(self,value):
        self.value = value[:-1]
class Keyword():
    def __init__(self,value):
        self.value = value
class Var():
    def __init__(self,value):
        self.value = value[1:]

whitespace1p = char_from("\n\r\t ").desc("at lest 1 white space character").at_least(1)
whitespace0p = char_from("\n\r\t ").desc("zero or more white space characters").many()

labelp = regex(r"[a-zA-Z0-9_]+:").map(Label).desc("label")
varp = regex(r"\$[a-zA-Z0-9_]+").map(Var).desc("var")
keywordp = regex(r"[a-zA-Z]+").map(Keyword).desc("keyword")
integerp = regex(r"-?\d+").map(int).desc("integer")
commentp = regex(r"#.*" + "\n").map(lambda a: []).desc("comment")

@generate
def label_line():
    result = yield labelp
    yield whitespace0p
    return [result]

@generate
def argp():
    yield whitespace1p
    result = yield alt(integerp,varp)
    return result

@generate
def line():
    result1 = yield keywordp
    result2 = yield argp.many()
    yield whitespace0p
    yield commentp.at_least(0)
    yield whitespace0p
    return [result1] + result2

@generate
def lines():
    result = yield alt(commentp, label_line,line).many()
    flat_result = [item for sublist in result for item in sublist]
    return flat_result


def parse(string):
    return lines.parse(string)

if __name__ == "__main__":
    string ="""#coment
label1:
test 
label2:
test 1 2 3 4
label4: 
sasa
    """
    print(parse(string))