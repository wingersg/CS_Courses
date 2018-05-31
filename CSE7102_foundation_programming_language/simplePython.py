# simplyPython.py - a python program to
# 1. define a function max() using if else
# 2. max_of_three()
# 3. compute the length of the string
# 4. write a function that takes a character and return True
# 5. sum() and multiply() that sums and multiplies all the numbers in a list
# 6. reverse() of a string
# 7. is_palindrome()
# 8. is_member()
# 9. overlapping() using two nested loops, use is_member and in
# 10. generate_n_chars()
# 11. find_longest_word()
# 12. filter_longer_word()
# 13. char_freq()
# SMU ID:47502277
# Name: Zhengwen Zhang
# Class: CSE 7105
def main():
    print '1.*****testing the max_of_two*****'
    max_of_two()
    print '2.*****testing the max_of_three*****'
    max_of_three()
    print '3.*****testing get string length*****'
    getstrlen()
    print '4.*****testing getting a character*****'
    onechar()
    print '5.*****testing sum and multiply of list*****'
    sumandmultiply()
    print '6.*****reverse a string*****'
    revstr()
    print '7.*****check for palindrome*****'
    ispalindrome()
    print '8.*****check for is_member*****'
    ismem()
    print '9.*****check for overlap*****'
    overlap()
    print '10.*****generate_n_char*****'
    genchar()
    print '11.*****length of longest name in a list*****'
    length_of_longest()
    print '12.*****filter a list*****'
    filter_long_words()
    print '13.*****convert a string to a dictionary*****'
    char_freq()

def max_of_two():
    x = int(raw_input('Enter an integer:'))
    y = int(raw_input('Enter another integer:'))
    if x > y:
        print 'maximum of',x,'and',y,'is',x,'\n'
    elif x == y:
        print x,'is equal to',y,'\n'
    else:
        print 'maximum of',x,'and',y,'is',y,'\n'


def max_of_three():
    x = int(raw_input('Enter the 1st integer:'))
    y = int(raw_input('Enter the 2nd integer:'))
    z = int(raw_input('Enter the 3rd integer:'))

    if x > y:
        max2 = x
    else:
        max2 = y

    if z > max2:
        print 'max of','(',x,y,z,')','is',z,'\n'
    else:
        print 'max of','(',x,',',y,',',z,')','is',max2,'\n'

def getstrlen():
    strin = raw_input('Enter a string:')
    n = 0
    for i in strin:
        n += 1

    print 'the length of the string is', n
    print '\n'

def onechar():
    charin = raw_input('Enter a character:')

    if charin.isalpha() and len(charin) == 1:
       print 'Yes,the input string is only a character:',charin,'\n'
    elif charin.isalpha() and len(charin) != 1:
       print 'No,It is a string(size>1)\n'
    else:
        print 'No,not a character'

def sumandmultiply():
    list=[1,2,3,4]
    vsum = 0
    vmultiply = 1
    for i in range(len(list)):
        vsum += list[i]
        vmultiply *=list[i]
    print 'the sum of the list is:',vsum
    print 'the multiply of the list is:',vmultiply,'\n'

def revstr():
    strin = raw_input('Enter a string to be reversed:')
    reversed =''
    for i in range(len(strin)):
        reversed += strin[len(strin)-1-i]
    print reversed

def ispalindrome():
    strin = raw_input('is this string palindrome?')

    reversed =''
    for i in range(len(strin)):
        reversed += strin[len(strin)-1-i]

    newstr = reversed

    if strin == newstr:
        print 'True'
    else:
        print 'False'

def ismem():
    bstr = raw_input('enter a big string(>5)')
    mem = raw_input('enter a small string(<5)')

    for i in range(len(bstr)):
        if mem == bstr[i]:
            print mem,'is a member of',bstr
            break
        elif i == len(bstr)-1:
            print 'not a member'
        else:
            continue

def overlap():
    list1 = raw_input('Enter the 1st list')
    list2 = raw_input('Enter the 2nd list')
    k = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                k += 1

    if k>=1:
        print 'True'
    else:
        print 'False'

def genchar():
    n = int(raw_input('Enter an integer:'))
    c = raw_input('Enter a character:')
    output = ''
    for i in range(n):
        output += c
    print output

def length_of_longest():
    list=['forest_park','dallas_zoo','inwood','university_boulevard','lovers_lane','skillman','downtown_dallas']
    print 'The input list of names are:',list
    lenlist = []
    for i in range(len(list)):
        lenlist.append((len(list[i])))

    maxindex = lenlist.index(max(lenlist))
    print 'The longest name is',list[maxindex]
    print 'It has a length of:',max(lenlist)

def filter_long_words():

    list = ['forest_park','dallas_zoo','inwood','university_boulevard','lovers_lane','skillman','downtown_dallas']
    print 'The input list of names are:', list
    newlist = []
    for i in range(len(list)):
        # define n=10
        if len(list[i])>10:
            newlist.append(list[i])

    print 'The list with name length larger than 10 is',newlist

def char_freq():
    list = 'abbabcbdbabdbdbabababcbcbab'
    print 'The input string is',list

    keylist = ''.join(set(list))
    d = {}
    for i in range(len(keylist)):
        d.update({keylist[i]: list.count(keylist[i])})
    print 'The dictionary is:',d

if __name__ == "__main__":
    main()