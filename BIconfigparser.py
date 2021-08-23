def readConfig(filepath):
    dictionary =  {}
    with open(filepath, "r") as f:
        for line in f:
            parsed_param = line.strip().split("=")
            if len(parsed_param) == 2:
                param = parsed_param[0]
                if parsed_param[1] == 'TRUE':
                    val = True
                elif parsed_param[1] == 'FALSE':
                    val = False
                else:
                    val = float(parsed_param[1])
                dictionary[parsed_param[0]] = val
        return dictionary
