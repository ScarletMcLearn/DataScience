def get_article_title(soup):
    return soup.find("h1", {"class": "title"}).get_text()
    
    


def tag_text_list_gen(body, tag_text_list):
    '''Give list object containing bs tags'''
    
#     tag_text_list = []

    for itm in body:
        try:
#             print()
#             print(itm.name)
#             print(itm.text)
#             print()
#             print(itm)
#             print()
            tag_text_list.append([itm.name, itm.text])
        except:
            continue
            
    return(tag_text_list)