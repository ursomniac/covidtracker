import pandas as pd

def calc_iscore(cases, peak):
    if cases < 0.001:
        return 1.0
    p = 150. if peak < 150. else peak
    imp = 1. - (cases/p)
    if cases > 100.:
        x = 0.6 * (300 - cases) / 200.
        if x < 0:
            x = 0
        return x
    # A
    if imp > 0.9:
        score = imp
    # B
    elif imp > 0.75:
        x = (imp - 0.75) / 0.15
        score = 0.8 + (x/10.)
    # C
    elif imp > 0.50:
        x = (imp - 0.5) / 0.25
        score = 0.7 + (x/10.)
    # D
    elif imp > 0.25:
        x = (imp - 0.25) / 0.25
        score = 0.6 + (x/10.)
    # F
    else:
        score = imp * 0.6 / 0.25

    # Bonuses
    if peak < 6.0:
        r = 1. - (peak/6.)
        b = 0.1 + 0.05 * r
        score += b
    elif peak < 10.0:
        r = 1. - (peak - 6.) / 4.
        b = 0.025 + 0.075 * r
        score += b

    score = 1. if score > 1. else score
    return score

def calc_raw_iscore(cases, peak):
    return 1. - cases/peak