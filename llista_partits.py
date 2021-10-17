

class Partits:
    llista_partits = {}
    llista_partits["lima_V"] = "https://www.basquetcatala.cat/estadistiques/2021/613ca346a4d427060f7943cc"
    llista_partits["granollers_L"] = "https://www.basquetcatala.cat/estadistiques/2021/6145db96a4d4270610364080"
    llista_partits["cornella_L"] = "https://www.basquetcatala.cat/estadistiques/2021/614f43d7a4d4270613252d6d"
    llista_partits["tgn_V"] = "https://www.basquetcatala.cat/estadistiques/2021/6158af70a4d427060de72f55"
    llista_partits["cnt_L"] = "https://www.basquetcatala.cat/estadistiques/2021/6162bf52a4d427061954512c"
    llista_partits["lima_L"] = "https://www.basquetcatala.cat/estadistiques/2021/6165cb51a4d427061b7d00f1"
    llista_partits["granollers_V"] = "https://www.basquetcatala.cat/estadistiques/2021/616b2705a4d4270628db9c1b"
    llista_partits["manresa_V"] = "https://www.basquetcatala.cat/estadistiques/2021/6165cb86a4d427061b7d0109"

    def get_partits_to_print(self):
        txt = ""
        for index, partit in enumerate(self.llista_partits.keys()):
            txt += "\t" + str(index+1) + ". " + str(partit) + "\n"
        return txt

