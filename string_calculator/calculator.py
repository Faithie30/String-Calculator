import re 

def add(numbers):
   
    if len(numbers) == 0:
        return 0

    nums = re.findall(r"\d+|-\d+", numbers)
    sum = 0
    negatives = []
    for num in nums:
        num = int(num)
        if num < 0:
            negatives.append(num)
        if num <= 1000:
            sum = sum + int(num)
               
    if len(negatives) > 0:
        message = "negatives not allowed! "
        for i in range(len(negatives)):
            if i != len(negatives)-1:
                message += str(negatives[i]) + ", "
            else:
                message += str(negatives[i]) + "."
        raise Exception(message)

    return sum



print(add(""))
#// should return 0

print(add("1"))
#// should return 1

print(add("1,1"))
#// should return 2

print(add("1,2,3,4"))
# answer is 10

print(add("1\n2,3" ))
#// should return 6

print(add("//;\n1;2"))
#// should return 3

print(add("//4\n142"))
#// should return 3

print(add("//***\n1***2***3"))
#// should return 6

print(add("//[:D][%]\n1:D2%3"))
#// should return 6

print(add("//[***][%%%]\n1***2%%%3"))
#// should return 6

print(add("//[(-_-')][%]\n1(-_-')2%3"))
#// should return 6

print(add("//[abc][777][:(]\n1abc27773:(1"))
#// should return 7

print(add("-1,-2,3,4"))