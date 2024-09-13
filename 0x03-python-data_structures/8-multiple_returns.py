#!/usr/bin/python3
def multiple_returns(sentence):
    Tuple = ()
    if len(sentence) == 0:
        Tuple = 0, "None"
    else:
        Tuple = len(sentence), sentence[0]
    return Tuple
