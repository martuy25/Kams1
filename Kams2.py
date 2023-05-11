def update(STATUS_TEST: str = True, testing: bool = False, pct: bool = False) -> str:

    if not isinstance(STATUS_TEST, str) or STATUS_TEST == "":

        return "FAILURE"

 

    def data_time_formatting(data_time: str = True) -> str:

        if not isinstance(data_time, str):

            return "FAILURE"

       

        import datetime

        time = data_time[-6:]

        day = data_time.replace(time, "")

       

        exact_time = datetime.time(int(time[:2]), int(time[2:4]), int(time[4:]))

        exact_day = datetime.date(int(day[:4]), int(day[4:6]), int(day[6:]))

 

        return [exact_time, exact_day]

 

    initial_list = STATUS_TEST.split(';')

   

    new_list = [key.split('=') for key in initial_list]

 

    TEXT = {}

 

    for i in new_list:

        TEXT[i[0]] = i[1]

   

    my_values = list(TEXT.values())

 

    time_date_list = data_time_formatting(my_values[1])

 

    x = f"""

    Operating machine: {my_values[0]}

    Date of the update: {time_date_list[1]}

    Time of the update: {time_date_list[0]}

    Status of VBA script: {my_values[2]}

    Percent of reporting: {my_values[3]}"""

 

    if testing:

        return [str(my_values[0]), str(time_date_list[1]), str(time_date_list[0]),

        str(my_values[2]), str(my_values[3])]

 

    def additive_pct(percentage: bool = False, testing: bool = False) -> str:

        new_percentage = int(percentage*100)

        if 100 % (new_percentage) == 0:

            count = 1

            temp = new_percentage

            testing_list = []

            string_list = []

            while percentage <= 100:

                percentage_tracker = str(new_percentage*count)

                testing_list.append(int(percentage_tracker))

                x= f"""Operating machine : {my_values[0]}

    Date of update:  {time_date_list[1]}

    Time of update:  {time_date_list[0]}

    Status of VBA script: {my_values[2]}

    Percent of reporting: {percentage_tracker}"""

                string_list.append(x)

                count +=1

                percentage = temp*count

        if testing:

            return testing_list

        else:

            return string_list

 

    if pct:

        return additive_pct(percentage=float(my_values[3]))

 

    return x