#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len == 0:
        char_at_one = None
        result = (str_len, char_at_one)
        return (result)
    else:
        char_at_one = sentence[0]
        result = (str_len, char_at_one)
        return (result)
