from googletrans import Translator
import time
import random

translator = Translator()


def trans_list(str_array):
    print("Starting Translator!")
    print()

#     res = []
    res = translator.translate(str_array, dest='bn')

#     str_len = 0

#     for txt in str_array:
#         str_len = str_len + len(txt)



#     if (str_len >= 15000):
#         print('Too big!!! 15k Max!')
        
#         return

#     else:
#     res.append(translator.translate(str_array, dest='bn'))



    # Wait for 5 seconds
    randy = random.randint(1, 5)

    print("Waiting for " + str(randy) + " seconds.")

    time.sleep(randy)
    
    return res



def conc_tag_txt_lst(tag_text_list):
    '''
    tag_text_list = 
    [['title', 'What Every Child Needs For Good Mental Health'],
     ['p', 'Basics for a child’s good physical health:'],
     ]
    '''
    magic_lst = []

    str_len = 0

    for _ in tag_text_list:
        if(str_len >= 15000):
            break

        str_len = str_len + len(_[1])
#         print(_[1])
        magic_lst.append(_[1])
        
    return magic_lst
