# Implement an exponent function

def exponent(num, raised_to):
    result = 1
    start = 1
    end = raised_to

    while start <= end:
        if start == end:
            result *= num
            return result

        result = result * num * num

        start += 1
        end -= 1

    return result


print(exponent(3, 4))
