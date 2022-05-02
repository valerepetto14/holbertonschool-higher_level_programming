#!/usr/bin/python3
def multiple_returns(sentence):
    if(!sentence):
        return None
    new_tuple = (len(sentence), sentence[0])
    return (new_tuple)
