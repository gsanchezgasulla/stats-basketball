import sys
import traceback

from compute_statistics import ComputeStatistics
from llista_partits import Partits
from tools.season_loader import SeasonLoader
from team_link import TeamLink


def ask_question(question, options_text, options):
    while True:
        print(question)
        text = input(options_text + "\n")

        try:
            if "," in text: # multioption selected
                resposta = []
                for split_text in text.split(","):
                    num = int(split_text)
                    if 0 < num > options:
                        print(" La opció seleccionada '" + split_text + "' no existeix!!")
                    else:
                        resposta.append(num)
                return resposta

            else:
                resposta = int(text)
                if 0 <= resposta > options:
                    print(" La opció seleccionada no existeix!!")
                else:
                    return resposta
        except ValueError:
            print("La opció seleccionada no és un número!!")


print("Welcome to GS stats!!")
print("El funcionament d'aquest programa és el seguent:")
print("\t El programa et farà unes preguntes que s'han de respondre de forma numèrica (triant 1, 2, 3, etc. ")
print("\t D'aquesta manera podràs seleccionar quin tipus d'estadística obtenir.")
print("\t Finalment, hauras d'enganxar les dades a un full d'excel (o drive) per a poder visualitzar-les correctament!")
print("Comencem...\n\n")

answer = ask_question("- Has actualitzat el fitxer team_link.py amb el link a l'equip que vols analitzar? Escriu 1 o 2.",
                      "\t 1. Si\n\t 2. No", 2)
if answer == 1:
    pass
elif answer == 2:
    print("Necessitaràs el link per a poder visualitzar el teu equip. Modifica el fitxer i torna a executar-me.\n")
    sys.exit(0)

print("Carregant els partits... \n")
season_loader = SeasonLoader()
season_games = season_loader.load_season(TeamLink.team_link)

partits = Partits()
partits.set_partits(season_games)
print("\n\nMolt bé, llavors ja podem anar a veure el que ens interessa.\n\n")

answer_stats = ask_question("Actualment el programa permet visualitzar les següents opcions. Tria'n una:",
                            "\t1. Punts anotats i rebuts per 5s (acumulats i per partit)\n"
                            "\t2. Distribució de minuts dels jugadors (acumulats i per partit)\n"
                            "\t3. % us jugador  (acumulats i per partit)\n"
                            "\t4. % us jugador evolucio al llarg de partits\n"
                            "\t5. evolució possessions per partit de l'equip.", 5)

answer_accumulated = 0

games_to_analyze =  {}
if answer_stats != 4 or answer_stats != 5:
    answer_accumulated = ask_question("\nVols veure els resultats acumulats o seleccionar per partit?",
                                  "\t1. Acumulats\n"
                                  "\t2. Escull els partits", 2)

if answer_accumulated == 2:
    answer_game = ask_question("\nQuin partit vols visualitzar? Pots posar una llista de números separada per comes "
                               "per si vols triar-ne de varies formes. Ex: 1,2,3,20,21\n", partits.get_partits_to_print(),
                               len(partits.llista_partits))
    if type(answer_game) != list:
        answer_game = [answer_game]
    for idx in answer_game:
        games_to_analyze[list(partits.llista_partits.keys())[idx-1]] = list(partits.llista_partits.values())[idx-1]

else:
    games_to_analyze = partits.llista_partits

statistics_calculator = ComputeStatistics(games_to_analyze)
out_str = ""
try:
    if answer_stats == 1:
        out_str = statistics_calculator.get_scores_by_fives()
    elif answer_stats == 2:
        out_str = statistics_calculator.get_minutes_distribution_in_game()
    elif answer_stats == 3:
        out_str = statistics_calculator.get_player_usage()
    elif answer_stats == 4:
        out_str = statistics_calculator.get_player_usage_evolution()
    elif answer_stats == 5:
        out_str = statistics_calculator.get_team_possessions_by_match()

except (Exception, BaseException) as e:
    out_str  = "There has been an error:\n\n"
    out_str += e.__str__()
    out_str += traceback.format_exc()
finally:
    with open("estadistiques.txt", "w+") as f_out:
        f_out.write(out_str)