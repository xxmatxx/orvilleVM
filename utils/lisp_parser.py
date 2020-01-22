from utils.sl_types import Symbol, SlException
from parsy import char_from, regex, seq, alt, string, generate, ParseError


whitespace1p = char_from("\n\r\t ").at_least(1).desc("at lest 1 white space character")
whitespace0p = char_from("\n\r\t ").many().desc("zero or more white space characters")
floatp = regex(r"-?\d+\.\d+").map(float).desc("float")
integerp = regex(r"-?\d+").map(int).desc("integer")


def symbolpMap(result):
    return Symbol(result)


symbolp = regex(r"[^\s\[\]\{\}\(\'\"\`\,\;\)]+").map(symbolpMap).desc("symbol")
emptyListp = seq(string( "(" ),whitespace0p,string( ")" )).result(list()).desc("empty list")
atomp = alt(floatp, integerp, symbolp).desc("atom")


@generate("list")
def listp(): 
    yield string( "(" ) 
    yield whitespace0p.desc("zero or more white space characters")
    result = yield formp.sep_by(whitespace1p).desc("form")
    yield whitespace0p.desc("zero or more white space characters")
    yield string( ")" )
    return result


formp = alt(listp, emptyListp, atomp)


def read_str(source):
    try:
        return formp.parse(source)
    except ParseError as error:
        raise SlException(error)
