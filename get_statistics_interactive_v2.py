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
game = "all"
if answer_stats != 4 or answer_stats != 5:
    answer_accumulated = ask_question("\nVols veure els resultats acumulats o només d'un partit?",
                                  "\t1. Acumulats\n"
                                  "\t2. Un sol partit", 2)

if answer_accumulated == 2:
    answer_game = ask_question("\nQuin partit vols visualitzar?", Partits().get_partits_to_print(),
                               len(Partits().llista_partits))
    game = list(Partits().llista_partits.keys())[answer_game - 1]

statistics_calculator = ComputeStatistics(partits.llista_partits)
out_str = ""
try:
    if answer_stats == 1:
        out_str = statistics_calculator.get_scores_by_fives(game)
    elif answer_stats == 2:
        out_str = statistics_calculator.get_minutes_distribution_in_game(game)
    elif answer_stats == 3:
        out_str = statistics_calculator.get_player_usage(game)
    elif answer_stats == 4:
        out_str = statistics_calculator.get_player_usage_evolution(game)
    elif answer_stats == 5:
        out_str = statistics_calculator.get_team_possessions_by_match(game)

except (Exception, BaseException) as e:
    out_str  = "There has been an error:\n\n"
    out_str += e.__str__()
    out_str += traceback.format_exc()
finally:
    with open("estadistiques.txt", "w+") as f_out:
        f_out.write(out_str)