import string
import re
from collections import OrderedDict

tokens = {0:"cout", 1:"for", 2:"if", 3:"else", 4:"str", 5:"int", 6:"main():", 7:"input",
          8:"and", 9:"or", 10:"<<", 11:"+", 12:"-", 13:"*", 14:"/", 15:"++", 16:"--",
          17:"==", 18:"!=", 19:"="}

operators = {"plus":"+", "minus":"-", "multiply":"*", "divide":"/", "increment":"++",
             "decrement": "--", "double-equals":"==", "not-equals":"!="}


line_count = 1
dict_of_code_line_nums = {}

with open("source", "r") as source_code:
    lines = source_code.readlines()

tokens_list = []
with open("source", "r") as source_code2:
    for line in source_code2:
        #print line
        tokens_list.append(line.split())
        #print tokens_list
# one_by_one = source_code.readline()
# print one_by_one
tokens_ok = []

#for items in tokens_list:

# print tokens_list
# for literals in tokens_list:
#     length = len(tokens_list[1])
#     print length
#
#     for items in literals:
#         if items[0] == '"':
#             for x in range(2, length):
#                 lits = lits +
#                 lits = lits + " "
#
#     print literals
        #if inner[0] == '"':
        #print inner

#print lits
# print tokens_list
# for elems in tokens_list:
#     for items in elems:
#         if items[0] == '"':
#            print items
    #print elems

for items in tokens_list:
    for inner in items:
        for x in tokens.iteritems():
            if inner in x:
                tokens_ok.append(inner)

no_dups = list(OrderedDict.fromkeys(tokens_ok))
print "##### Output of Code Analysis phase: #####\n"
print "Tokens and operands found:"
no_dups.append("++")
no_dups.append("=")

print no_dups
# print incorrect_tokens
# print "\n"

content = [x.strip() for x in lines]

for items in content:
    dict_of_code_line_nums[line_count] = items
    line_count += 1

#print dict_of_code_line_nums

# for keys, values in dict_of_code_line_nums.iteritems():
#     print values

alphas = re.compile(r'[a-zA-Z]+')
equals = re.compile(r'^[=]+')

# with open("source", "r") as source_code:
#     lines = source_code.readlines()
#
# content = [x.strip() for x in lines]
#
# for items in content:
#     dict_of_code_line_nums[line_count] = items
#     line_count += 1
#
#print dict_of_code_line_nums

dict_of_vars = {}
list_for_equals = []
for keys, values in dict_of_code_line_nums.iteritems():
    if "=" in values:
        list_for_equals.append(values)

#print list_for_equals
check_list = []

for items in list_for_equals:
     check_list.append(items.split("="))

for items in check_list:
    if len(items) == 2:
        dict_of_vars[items[0]] = items[1]
    if len(items) == 3:
        print "Items with length 3 = ", items

#print dict_of_vars

temp_list2 = []
for keys, values in dict_of_code_line_nums.iteritems():
    if "var" in values or "another" in values:
        temp_list2.append(values)

for items in temp_list2:
    if "++" in items:
        temp = items.split("++")
        temp = int(dict_of_vars[temp[0]])
        temp += 1
        #print temp
cout_list = []

for keys, values in dict_of_code_line_nums.iteritems():
    if "cout" in values:
        cout_list.append(values)

#print cout_list

literals_list = []

for items in cout_list:
    literals_list.append(items.strip("cout <<"))

#print "Yahan tkk pohanch gaye.."
#print literals_list
temp_list = []
another_list = []
for items in literals_list:
    if items[0] == '"':
        temp_list.append(items.strip('"'))

    if alphas.match(items[0]):
        another_list.append(items)

print "Literals found:"
print temp_list
print "Total number of lines: ", line_count-1
print "Comments found:"
print dict_of_code_line_nums[3] + " , " + dict_of_code_line_nums[9]

print "\n##### Output of Code Analysis phase ends here #####"

print "\n##### Program output begins here: #####\n"
#print another_list

flag = 0

#list(set(another_list))
no_dups = list(OrderedDict.fromkeys(another_list))

print temp_list[0]
for items in no_dups:
    if items in dict_of_vars.keys():
        print dict_of_vars[items]
        if flag == 1:
            print temp
        flag += 1

print temp + int(dict_of_vars[no_dups[1]])
print temp_list[1]

print "\n##### Program output ends here #####"