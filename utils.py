

def isfloat(v):
    try:
        float(v)
        return True
    except ValueError:
        return False


def ischar(s):
    return type(s) == str and len(s) == 1


def interpret_type(s):
    s = s.strip()
    if s.lower() in ["true", "false"]:
        return bool
    elif s.isnumeric():
        return int
    elif isfloat(s):
        return float
    elif s:
        return str 
    else:
        return None
