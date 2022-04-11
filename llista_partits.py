

class Partits:
    llista_partits = {}

    def get_partits_to_print(self):
        txt = ""
        for index, partit in enumerate(self.llista_partits.keys()):
            txt += "\t" + str(index+1) + ". " + str(partit) + "\n"
        return txt

    def set_partits(self, partits):
        self.llista_partits = partits
