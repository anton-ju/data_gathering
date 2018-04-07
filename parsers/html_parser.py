import logging
from parsers.parser import Parser

logger = logging.getLogger(__name__)
fh = logging.FileHandler('data_gathering1.log')
fh.setLevel(logging.INFO)

from bs4 import BeautifulSoup  # You can use any other library
import re

class HtmlParser(Parser):

    def parse(self, data):
        """
        Parses html text and extracts field values
        :param data: html text (page)
        :return: a dictionary where key is one
        of defined fields and value is this field's value
        """
        soup = BeautifulSoup(data, "lxml")
        
        table1 = soup.find_all(attrs={'class':'item-description-title-link'})
        table2 = soup.find_all(attrs={'class':'about'})
        
        item_list = []
        pattern = '(^.*?),\s?(\d{4})\s*(.*)руб.\s*(.*)км.*(\d\.\d).*(AT|MT).*\((\d*).*?(\w+),\s+?(\w+),\s+?(\w+)\s+?'
        
        
        li1 = [_.text for _ in table1]
        li2 = [_.text for _ in table2]
        
        for i in range(len(li1)):
            broken= False
            if li2[i].find('Битый') :
                broken = True
                li2[i] = li2[i].replace('Битый,', '')
            
            str_to_parse= li1[i]+li2[i]
            
            result = re.findall(pattern, str_to_parse, re.DOTALL)

            if result :
                result = list(result[0] + tuple([broken.__str__()]))
              
                res_dict = dict(
                            model = result[0],
                            year= result[1],
                            price= int(str(result[2]).replace(' ','')),
                            distance= int(str(result[3]).replace(' ','')),
                            volume= result[4],
                            transmission= result[5],
                            power= result[6],
                            carcase= result[7],
                            drive_unit= result[8],
                            fuel= result[9],
                            broken= result[10])
                
    

                item_list.append(res_dict)
        
        return item_list
