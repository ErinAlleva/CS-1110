# Alex Hicks (awh4kc)

def married_analysis():
    datafile = open("sleeping.csv", "r")

    married_breakdown = {}

    for line in datafile:
        split_line = line.strip().split(";")

        if split_line[2] == "Married":
            if split_line[4] in married_breakdown:
                married_breakdown[split_line[4]] += 1
            else:
                married_breakdown[split_line[4]] = 1

    return married_breakdown

def age_analysis():

    possible_responses = ['Never', 'Once a year or less', 'Once a month or less', 'A few times per month', 'A few times per week', 'Every night']

    possible_ages = ['18-29','30-44','45-60','> 60']

    for age in possible_ages:
        datafile = open("sleeping.csv", "r")
        datafile.readline()
        age_breakdown = [0,0,0,0,0,0]
        total_responses = 0
        print("-------",age,"-------")
        for line in datafile:
            split_line = line.strip().split(";")
            if split_line[4] in possible_responses and split_line[6] == age:
                index = possible_responses.index(split_line[4])
                age_breakdown[index] += 1
                total_responses += 1

        for i in range(len(possible_responses)):
            print(possible_responses[i], ":", format(100*age_breakdown[i]/total_responses, "0.2f") +"%")

print(married_analysis())
age_analysis()

