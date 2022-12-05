def calc_nscore(iscore, rscore, peak):
    if iscore < 0.00001 and rscore <= 0.00001:
        return 0.0

    if peak > 400.:
        b = 0.
    elif peak < 150.:
        b = 0.5
    else:
        b = 0.5 * (400. - peak) / 250.
    
    x = (b * iscore) + ((1. - b) * rscore)
    return x