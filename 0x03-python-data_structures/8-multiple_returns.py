#!/usr/bin/python3
def multiple_returns(sentence):
    """Get the length of string and first char
    of a sentence
    
    Args: sentence - The sentence to mentioned

    Return: Tuple with len and first char
    """

    if not sentence:
        return (len(sentencs), None)
    return (len(sentence), sentence[0])
