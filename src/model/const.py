IKEA_NAME_CHARS = [
    " ",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "ä",
    "å",
    "ö",
]


CHAR_TO_INDEX = {c: i for i, c in enumerate(IKEA_NAME_CHARS)}
INDEX_TO_CHAR = {i: c for i, c in enumerate(IKEA_NAME_CHARS)}
VOCAB_SIZE = len(IKEA_NAME_CHARS)

MAX_LEN = 20
