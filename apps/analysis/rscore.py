
def calc_rscore(rate, peak, calib=300.):
    if rate < 0.01:
        return 0.
    
    if rate <= 2.0: # A
        x = rate / 2. 
        score = 1.0 - x
    elif rate <= 6.0: # B
        x = (rate - 2.) / 4.
        score = 0.9 - x
    elif rate <= 10.0: # C
        x = (rate - 6.) / 4.
        score = 0.8 - x
    elif rate <= 15.0:
        x = (rate - 10.) / 5.
        score = 0.7 - x
    else:
        x = (calib - rate) / (calib - 15.)
        score = x * 0.6
    score = 0. if score < 0. else score
    return score

