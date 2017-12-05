#Query: How many website hits did Company X get during the 2nd month?


def query_original(data_file):
    data = read_file_into_array(data_file)

    #number of minutes in 2 months
    minutes_in_two_months = minutes_per_month(2)

    #number of minutes in 1 month
    minutes_in_one_month = minutes_per_month(1)

    total_website_hits = 0
    query_cost = 0  # we will add one to the cost for every value accessed
    for x in range(minutes_in_one_month, minutes_in_two_months):
        total_website_hits += data[x]
        query_cost += 1

    return {"total website hits": total_website_hits, "query cost": query_cost}


def query_wavelet(data_file):
    data = read_file_into_array(data_file)

    # number of minutes in 2 months
    minutes_in_two_months = minutes_per_month(2)

    # number of minutes in 1 month
    minutes_in_one_month = minutes_per_month(1)

    total_website_hits = 0
    query_cost = 0  # we will add one to the cost for every value accessed

    total_website_hits += data[minutes_in_two_months - 1]
    query_cost += 1

    total_website_hits -= data[minutes_in_one_month - 1]
    query_cost += 1

    return {"total website hits": total_website_hits, "query cost": query_cost}


def read_file_into_array(data_file):
    file = open(data_file,"r")
    data = []
    for line in file:
        data.append(float(line))

    file.close()
    return data

def minutes_per_month(num_months):
    days_per_month = 30
    hours_per_day = 24
    minutes_per_hour = 60
    return minutes_per_hour*hours_per_day*days_per_month*num_months

