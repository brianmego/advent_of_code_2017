def validate_passphrase(input_str, allow_anagrams=True):
    input_str = str(input_str)
    words = input_str.split()
    if not allow_anagrams:
        words = [''.join(sorted(x)) for x in words]
    if len(words) == len(set(words)):
        return True
    return False
