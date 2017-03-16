# coding=utf-8
import re
from pablo import Pablo
import time
import os

def parse_fruits(data):#nul produit
    # group 1 is FRUITS
    # group 2 is description
    # group 3 is price
    # group 4 is evolution
    accented_char = "àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇßØøÅåÆæœ"
    pattern = r"[\r]*([A-Z" + accented_char + r"]+)(.*)(\d,\d\d).*([-+]\d+(,\d+)? %|=)"
    results = re.findall(pattern, data)

    for name, desc, price, evolution, rest in results:
        if name == "BOEUF" or name == "VEAU" or name == "PORC":
            break
        item = {
            'name' : name,
            'desc' : desc,
            'price': price,
            'evolution' : evolution
        }
        yield item



def some(path):
    bdd = Pablo()
    date = re.sub(r".*(\d{8}).*", r"\1", path)
    print(date)
    req = """INSERT INTO fruit_vegetable
            (product, description, price, evolution, date_extract, date_price)
            VALUES (%s, %s, %s, %s, %s, %s)"""
    with open(path, "r") as file:
        #print(type(file.read().decode('utf-8')))
        for item in parse_fruits(file.read()):
            #insert item in database.
            params = (item['name'], item['desc'], item['price'],
                        item['evolution'], time.strftime("%Y%m%d"), date)
            #bdd.exec_req_with_args(req, params)

    bdd.commit()
    bdd.close()


some("pdfminer20170315.txt")
