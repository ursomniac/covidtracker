

def calc_vscore(num_cases_to_date, population, full_vac, rscore):
    t1 = full_vac / 0.8
    t2 = 0.5 * num_cases_to_date / population
    t3 = rscore
    vscore = 0.5 * ((t1 + t2)+ t3)
    return vscore

