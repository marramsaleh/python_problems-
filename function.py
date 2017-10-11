# problem number 4
def duplicated_str(inputstr):
     result=""
     i=0
     length = len(inputstr)
     while i< length:
         result = result +inputstr[i]+inputstr[i]
         i=i+1
     return  result

newword =duplicated_str('the')
print(newword)

#  problem number 1 /function  def arrayCheck(nums):
def arrayCheck(nums):
    if (1 in nums):
        if (2 in nums):
            if (3 in nums):
                return True
    return False
my_array = [1,2,4,4,5,]
print(arrayCheck(my_array))

# problem number 2 def stringBits(str): function
def stringBits(str):
     print(str[::2])

stringBits('hello')
#  problem number  3def end_other(a, b):

def end_other(a, b):
   first = a.lower()
   second = b.lower()
   if (first in second):
       print('true')
   elif (second in first):
       print('true')
   else:
       print('false')

end_other('thk','morfg')
end_other('AbC', 'HiaBc')
# problem number 5 def fix_teen(n):


def fix_teen(n):
    if (n in range(0,15)) or (n in range(17,20)):
        n = 0
        return n
    else:
        return n




    # problem number 5 def no_teen_sum(a, b , c):
sum = 0
def no_teen_sum(a, b, c):
    n1 = fix_teen(a)
    n2 = fix_teen(b)
    n3 = fix_teen(c)
    sum = n1 + n2 + n3
    print(sum)

no_teen_sum(2, 13, 1)
# problem number 6 def count_evens(nums):

def count_evens(nums):
    count = 0
    for i in nums:
        if i%2 == 0:
            count= count+1
    print (count)

array_to_test = [2, 1, 2, 3, 4]
count_evens(array_to_test)
