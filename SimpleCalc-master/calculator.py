import re

def add(nums):
     if len(nums)==0:
        return 0
     else:
       
       # num_list = re.split('; |, |\n|,|4|,|/|,|;|',nums)
        #num_list = list(filter(None, num_list))
        num_list = re.findall(r"\d+|-\d+", nums)

        sum=0
        print(num_list)
        for number in num_list:
            if int(number)<=1000:
                if int(number) < 0:
                    raise Exception("ERROR: negatives not allowed -1,-2")
                number = int(number)
                sum +=  number
            #print(i)
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