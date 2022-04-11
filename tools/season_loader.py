import urllib.request
from html.parser import HTMLParser

class team_parser(HTMLParser):
    header = "https://www.basquetcatala.cat/"
    footer = "/0"
    competitions_links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and "competicions/resultats" in attr [1] and "basquetcatala" not in attr[1]:
                    print("Hem trobat la seguent competicio:", attr[1])
                    self.competitions_links.append(self.header + attr[1] + self.footer)
    def obtain_links(self):
        return self.competitions_links

class games_parser(HTMLParser):
    header = "https://www.basquetcatala.cat/"
    games_links_dict = {}
    team_identifier = False
    opponent = ""
    opponent_selected = False
    local_visitant = ""

    def __init__(self, team_id, idx_competition):
        self.team_id = team_id
        self.idx_competition = idx_competition
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and "estadistiques" in attr[1] and self.team_identifier:
                    self.games_links_dict[self.opponent] = attr[1]
                    self.team_identifier = False
                    self.opponent = ""
                elif attr[0] == "href" and "/equip/" in attr[1]:
                    if self.team_id in attr[1]:
                        self.team_identifier = True
                    else:
                        if self.team_identifier:
                            self.local_visitant = "L"
                        else:
                            self.local_visitant = "V"
                        self.opponent_selected = True


    def handle_data(self, data):
        if self.opponent_selected:
            self.opponent = str(self.idx_competition) + "-" + data.replace(" ", "_").replace("-","_") + "-" + self.local_visitant
            self.opponent_selected = False

    def obtain_links(self):
        return self.games_links_dict

class SeasonLoader:
    def load_season(self, team_link):

        team_id = team_link.split("/")[-1]

        contents = urllib.request.urlopen(team_link).read()
        parser = team_parser()
        parser.feed(contents.decode("utf-8"))


        for idx_competition,competition in enumerate(parser.competitions_links):
            contents = urllib.request.urlopen(competition).read()
            parser = games_parser(team_id, idx_competition)
            parser.feed(contents.decode("utf-8"))

        return parser.obtain_links()



