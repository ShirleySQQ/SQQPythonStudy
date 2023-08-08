"""
Write a code, which will:
1. create a list of random number of dicts (from 2 to 10)
dict's random numbers of keys should be letter,
dict's values should be a number (0-100),
example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:
if dicts have same key, we will take max value, and rename key with dict number with max value
if key is only in one dict - take it as is,
example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
Each line of code should be commented with description.
Commit script to git repository and provide link as home task result.
"""
import random
import string

dic_list = []
dict_sub = {}
# generate random number of dic items
len_size = random.randint(2, 11)
print('The number of item of this dic is: %i' % len_size)

# add generated random number items to this dic
for j in range(len_size):
    # print('j %i' % j)
    dict_sub = {}
    for i in range(len_size):
        # key is random ascii character
        key_v = random.choice(string.ascii_lowercase)
        # value is random number between 0 and 100
        value_v = random.randint(0, 100)
        # add the key:value to dic
        # python list does not support duplicate key
        dict_sub.update({key_v: value_v})
    dic_list.insert(i, dict_sub)
# print the generated list
print('The generated list is :\n', dic_list)
# print(dict_sub)

# this is a dic for the ultimate result: save the max value for the key
dic_max_ul = {}
# this is a temp dic for saving same key:value, the key is re-defined with its index+1 of original list
tmp_dic = {}
'''
if len_size == 1:
    remain_interval = 0
    dic_max_ul = dic_list[0]
'''
# this is a tmp list for find same keys
dic_conbine = dic_list
# for each key of sub-dic of the list, save them to tmp_dic,key will append with _(index+1)
# then find the max value
# then update dic_max_ul dic with the max value and its key
for i in range(len_size):
    for key, val in dic_conbine[i].items():
        tmp_dic = {}
        for j in range(len_size):
            for key_c, val_c in dic_conbine[j].items():
                if key == key_c:
                    tmp_dic.update({key + '_' + str(i + 1): val, key_c + '_' + str(j + 1): val_c})
        if (tmp_dic.__len__()) == 1:
            dic_max_ul.update({key: val})
        else:
            if (tmp_dic.__len__()) > 1:
                max_v = max(tmp_dic.values())
                for key_f in tmp_dic.keys():
                    if tmp_dic.get(key_f) == max_v:
                        max_key = key_f
                        dic_max_ul.update({max_key: max_v})
# print the max value dic, with its key_(index+1)
print('The dic with key\'s max value:\n', dic_max_ul)
