import requests
from bs4 import BeautifulSoup
import pickle

class BQScraper:
    '''Scrapes BQ for links, images and quotes.'''
    base_url = 'https://www.brainyquote.com/topics'
    
    def get_catagory_bq(self):
        name_2_link = {}
        try:
            base_site = requests.get(self.base_url)
        except requests.ConnectionError:
            print('Connection Error(s) occured. :( : ' + requests.ConnectionError)
            return

        soup = BeautifulSoup(base_site.content, 'html5lib')

        for div in soup.findAll('div', attrs={'class' : 'row bq_left'}):
            temp_res_1 = (div.findAll('div', attrs={'class':'bqLn'}))

        for item in temp_res_1:
            temp_link = item.find('div', attrs={'class':'bqLn'})
            temp_name = item.find('span', attrs={'class':'topicContentName'})

            name = ""
            link = ""

            if(temp_name):

                name = temp_name.text

            if(temp_link):
                if temp_link.find('a', href=True):
                    link = (temp_link.find('a').get('href'))
                    name_2_link[name] = self.base_url+link   
        return name_2_link
    
    
    def txt_img_extract(self, res_page):
        txt_img_dic = {}
        try:
            res_pg = requests.get(res_page)


        except requests.ConnectionError:
            print('Connection Error(s) occured. :( : ' + requests.ConnectionError)

        res_page_soup = BeautifulSoup(res_pg.content, 'html5lib')

        img_box = res_page_soup.findAll('div', {'class':'m-brick grid-item boxy bqQt'})

        for itm in img_box:
            try:
                img_t = itm.find('img')['alt']
                img_l = 'https://www.brainyquote.com' + itm.find('img')['src'].replace('.jpg', '-2x.jpg')

                txt_img_dic[img_t] = img_l
            except:
                pass

        return txt_img_dic
    
    
    def txt_img_d2l(self, dict_t_i):
        img_lst = []
        for i in range(len(dict_t_i)):
            img_lst.append([list(dict_t_i.keys())[i], list(dict_t_i.values())[i]])
        return img_lst 
    
    def complete_img_l(self, img_lst):
        for i in range(len(img_lst)):
            frm_2 = img_lst[i][1].replace('1-2x.jpg', '2-2x.jpg')
            frm_3 = img_lst[i][1].replace('1-2x.jpg', '3-2x.jpg')
            frm_4 = img_lst[i][1].replace('1-2x.jpg', '4-2x.jpg')
            frm_5 = img_lst[i][1].replace('1-2x.jpg', '5-2x.jpg')

            img_lst[i].append(frm_2)
            img_lst[i].append(frm_3)
            img_lst[i].append(frm_4)
            img_lst[i].append(frm_5)

        return img_lst
    
    
    def picklify_lst(self, lst, fn):
        with open(fn+".txt", "wb") as fp:   #Pickling
            pickle.dump(lst, fp)
        print('Completed Picklifying.\n\n')

    def pickle_loader(self, fn):
        with open(fn, "rb") as fp:   # Unpickling
            b = pickle.load(fp)
        print('Completed Loading.\n\n')
        return b