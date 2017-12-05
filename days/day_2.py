def calculate_checksum(input_str):
    input_str = str(input_str).strip()
    lines = input_str.split('\n')
    differences = []
    for line in lines:
        lowest = None
        highest = None
        line = line.strip()
        digits = line.split()
        for i in range(len(digits)):
            digit = int(digits[i])
            if lowest is None:
                lowest = digit
            if highest is None:
                highest = digit

            if int(digit) < lowest:
                lowest = digit
            elif int(digit) > highest:
                highest = digit
        differences.append(highest - lowest)
    return sum(differences)

def calculate_evenly_divisible_checksum(input_str):
    input_str = str(input_str).strip()
    lines = input_str.split('\n')
    quotients = []
    for line in lines:
        lowest = None
        highest = None
        line = line.strip()
        digits = line.split()
        for i in range(len(digits)):
            success = False
            digit = int(digits[i])
            j = i
            while j < len(digits) - 1:
                j += 1
                compare_digit = int(digits[j])
                if digit % compare_digit == 0:
                    quotients.append(int(digit / compare_digit))
                    success = True
                    break
                elif compare_digit % digit == 0:
                    quotients.append(int(compare_digit / digit))
                    success = True
                    break
            if success:
                break
    return sum(quotients)
