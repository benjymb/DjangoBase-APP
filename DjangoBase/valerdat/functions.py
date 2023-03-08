def longest_word(word : str, to_choose : list) -> str:
    matches = {}
    for w in to_choose:
        original_word = word
        for i, c in enumerate(w):
            if c in word:
                word = word.replace(c, "", 1)
            else:
                break
            if i == len(w) - 1:
                matches[len(w)] = w
        word = original_word
    if matches:
        return matches[max(matches.keys())]
    else:
        return None
            
