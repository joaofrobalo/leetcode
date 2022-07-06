
def main():
    print(romanToInt("MMCCCXCIX"))

def romanToInt(s: str) -> int:
    """
    gets a string of roman numerals, returns an int of their sum
    """
    sum = 0
    ignore_next = False
    last_number = False
    for i, n in enumerate(s):

            # if previous number was a subtraction, ignore this current number
            if ignore_next:
                ignore_next = False
                continue
            
            # if it's the last number in the string, then don't check the out of bounds index
            if len(s) == i + 1:
                last_number = True

            match n:
                case "M":
                    sum += 1000
                case "D":
                    sum += 500
                case "C":
                    if not last_number and s[i + 1] == "D":
                        sum += 400
                        ignore_next = True
                    elif not last_number and s[i + 1] == "M":
                        sum += 900
                        ignore_next = True
                    else:
                        sum += 100
                case "L":
                    sum += 50
                case "X":
                    if  not last_number and s[i + 1] == "L":
                        sum += 40
                        ignore_next = True
                    elif not last_number and s[i + 1] == "C":
                        sum += 90
                        ignore_next = True
                    else:
                        sum += 10
                case "V":
                    sum += 5
                case "I":
                    if not last_number and s[i + 1] == "V":
                        sum += 4
                        ignore_next = True
                    elif not last_number and s[i + 1] == "X":
                        sum += 9
                        ignore_next = True
                    else:
                        sum += 1
    return sum



main()