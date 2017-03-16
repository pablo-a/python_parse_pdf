# coding=utf-8
import re


def special_generator(lst):
    for i in range(0, len(lst) - 1, 2):
        yield (lst[i], lst[i + 1])

def parse(data):#nul produit
    # pattern = r"^.*([A-Z]+)(.*)(\d,\d\d).*(([-+]\d+(,\d+)?)|(=))$"
    accented_char = "àèìòùÀÈÌÒÙáéíóúýÁÉÍÓÚÝâêîôûÂÊÎÔÛãñõÃÑÕäëïöüÿÄËÏÖÜŸçÇßØøÅåÆæœ"
    pattern = r"[\r]*([A-Z" + accented_char + r"]+)(.*)(\d,\d\d).*(([-+]\d+(,\d+)? %)|(=))"
    results = re.findall(pattern, data)
    print("nb result = %s" % len(results))
    for item in results:
        yield item
    #générateur spécial pour me doner les deux partie d'un résultat.
    # for product, price in special_generator(results):
    #     item = {}
    #     item.name = "aze"
    #     yield item



def some(path, database=None):
    with open(path, "r") as file:
        #print(type(file.read().decode('utf-8')))
        for item in parse(file.read()):
            #insert item in database.
            print(item)

some("pdfminer.txt")
