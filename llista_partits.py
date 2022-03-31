

class Partits:
    llista_partits = {}
    llista_partits["1-MANRESA_V"] = "https://www.basquetcatala.cat/estadistiques/613dedc3a4d427060f79470b"
    llista_partits["1-JET_L"] = "https://www.basquetcatala.cat/estadistiques/61460a25a4d4270610364163"
    # llista_partits["1-LLEIDA_L"] = "https://www.basquetcatala.cat/estadistiques/61504b39a4d427061325498f"
    # llista_partits["1-UESC_V"] = "https://www.basquetcatala.cat/estadistiques/61587bcfa4d427060de71656"
    # llista_partits["1-JAC_L"] = "https://www.basquetcatala.cat/estadistiques/6161b8fda4d427061954317c"
    # llista_partits["1-MANRESA_L"] = "https://www.basquetcatala.cat/estadistiques/61657074a4d427061b7cfde5"
    # llista_partits["1-JET_V"] = "https://www.basquetcatala.cat/estadistiques/616c5e56a4d4270628dbc6b0"
    # llista_partits["1-LLEIDA_V"] = "https://www.basquetcatala.cat/estadistiques/61755278a4d42706105a4632"
    # llista_partits["1-UESC_L"] = "https://www.basquetcatala.cat/estadistiques/617d65b0a4d427060526c70f"
    # llista_partits["1-JAC_V"] = "https://www.basquetcatala.cat/estadistiques/6186ca76a4d42706074d38f1"
    # llista_partits["2-TGN_L"] = "https://www.basquetcatala.cat/estadistiques/61ec32c2a9a1f903094e018e"
    # llista_partits["2-UESC_V"] = "https://www.basquetcatala.cat/estadistiques/61e2f1eaa9a1f90322762315"


    def get_partits_to_print(self):
        txt = ""
        for index, partit in enumerate(self.llista_partits.keys()):
            txt += "\t" + str(index+1) + ". " + str(partit) + "\n"
        return txt

# TODO
# - fer-ho executable a doble-click
# poss per partit i evolució en temps -> per treure en V-D
#