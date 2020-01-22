def remove_space(s: str):
    return s.replace(" ", "")


def group_n_char(s: str, n: int):
    s = remove_space(s)
    return ' '.join([s[i:i+5] for i in range(0, len(s), n)])
