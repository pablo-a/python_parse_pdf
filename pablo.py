# coding=utf-8
import MySQLdb
dbName = "pablo"
user = "root"
passwd = ""
host = "localhost"
port = 3306


class Pablo:


    def __init__(self):
        "Etablissement connexion et creation curseur"
        try:
            self.bdd = MySQLdb.connect(db=dbName, user=user, passwd=passwd, host=host, port=port)
            self.cursor = self.bdd.cursor()
        except Exception as e:
            self.fail_connect = 1
            print("Connexion Error : %s", e)
        else:
            self.fail_connect = 0
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def executerReq(self, req):
        "Exécution de la requête <req>, avec détection d'erreur éventuelle"
        try:
            self.cursor.execute(req)
        except Exception, err:
            # afficher la requête et le message d'erreur système :
            print "Requête SQL incorrecte :\n%s\nErreur détectée :\n%s" % (req, repr(err))
            return 0
        else:
            return 1

    def resultatReq(self):
        "renvoie le résultat de la requête précédente (un tuple de tuples)"
        return self.cursor.fetchall()

    def commit(self):
        if self.bdd:
            self.bdd.commit()         # transfert curseur -> disque

    def close(self):
        if self.bdd:
            self.bdd.close()

    def exec_req_with_args(self, req, args):
        try:
            self.cursor.execute(req, args)
        except Exception, err:
            print "Requête SQL incorrecte :\n%s\nErreur détectée :\n%s" % (req, repr(err))
            return 0
        else:
            return 1
