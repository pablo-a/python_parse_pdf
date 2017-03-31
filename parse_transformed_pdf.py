# coding=utf-8
import re
from pablo import Pablo
import time
from os import listdir
from os.path import isfile, join

def parse_fruits(data):
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
            'desc' : desc.strip(),
            'price': re.sub(",", ".", price),
            'evolution' : evolution
        }
        print(item)
        yield item



def some(path):
    bdd = Pablo()
    date = re.sub(r"text_all_2016\\marche_rungis_(\d{2})-(\d{2})-(\d{4}).*", r"\3\2\1", path)
    # date = time.strftime("%Y%m%d", time.strptime(date, "%Y %m %d"))
    print(date)
    req = """INSERT INTO fruit_vegetable
            (product, description, price, evolution, date_extract, date_price, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    with open(path, "rb") as file:
        #print(type(file.read().decode('utf-8')))
        for item in parse_fruits(file.read()):
            #insert item in database.
            params = (item['name'], item['desc'], item['price'],
                        item['evolution'], time.strftime("%Y%m%d"), date, u"Rungis")
            bdd.exec_req_with_args(req, params)

    bdd.commit()
    bdd.close()

files = [f for f in listdir("text_all_2016")]
for f in files:
    some(u"text_all_2016\\" + f)
