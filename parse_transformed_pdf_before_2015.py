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
    pattern = r"[\r]*([ A-Z" + accented_char + r"]+)(.*)(\d,\d\d).*([-+]\d+(,\d+)? %|=)"
    pattern2015 = r"[\r]*([A-Z" + accented_char + r"]+)(.*?)(\d\.\d\d|NC).*?(\d\.\d\d|NC).*?(\d\.\d\d|NC)"
    results = re.findall(pattern2015, data)

    day_reference = r".*(\d\d/\d\d/\d{4}).*\d\d/\d\d/\d{4}.*Semaine \d\d"
    date_res = re.findall(day_reference, data)
    try:
        final_date = re.sub(r"(\d\d)/(\d\d)/(\d{4})", r"\3\2\1", date_res[0])
    except IndexError:
        print("no date could be found")
        return


    for name, desc, price1, price2, price3 in results:
        if name == "BOEUF" or name == "VEAU" or name == "PORC" or name == "BAR" or name == "CABILLAUD":
            break
        item = {
            'date' : final_date,
            'name' : name,
            'desc' : desc.strip(),
            'price': price2,
        }
        print(item)
        yield item



def some(path):
    bdd = Pablo()
    # date = re.sub(r"text2015\\Rungis2015_(\d{2}).*", r"\1", path)
    # date = time.strftime("%Y%m%d", time.strptime(date, "%Y %m %d"))

    req = """INSERT INTO fruit_vegetable
            (product, description, price, date_extract, date_price, source)
            VALUES (%s, %s, %s, %s, %s, %s)"""
    with open(path, "rb") as file:
        print(path)
        #print(type(file.read().decode('utf-8')))
        for item in parse_fruits(file.read()):
            #insert item in database.
            params = (item['name'], item['desc'], item['price'],
                        time.strftime("%Y%m%d"), item['date'], u"Rungis")
            bdd.exec_req_with_args(req, params)

    bdd.commit()
    bdd.close()

files = [f for f in listdir("text2015")]
for f in files:
    some(u"text2015\\" + f)
