import sys
import time

from compute_statistics import ComputeStatistics
from llista_partits import Partits


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

answer = ask_question("- Has actualitzat el fitxer llista_partits.py amb els links dels partits? Escriu 1 o 2.",
                      "\t 1. Si\n\t 2. No", 2)
if answer == 1:
    pass
elif answer == 2:
    print("Necessitaràs els links per a poder visualitzar el teu equip. Modifica el fitxer i torna a executar-me.\n")
    sys.exit(0)

print("Molt bé, llavors ja podem anar a veure el que ens interessa.\n\n")

answer_stats = ask_question("Actualment el programa permet visualitzar les següents opcions. Tria'n una:",
                            "\t1. Punts anotats i rebuts per 5s (acumulats i per partit)\n"
                            "\t2. Distribució de minuts dels jugadors (acumulats i per partit)\n"
                            "\t3. % us jugador  (acumulats i per partit)\n"
                            "\t4. % us jugador evolucio al llarg de partits", 4)

answer_accumulated = 0
game = "all"
if answer_stats != 4:
    answer_accumulated = ask_question("\nVols veure els resultats acumulats o només d'un partit?",
                                  "\t1. Acumulats\n"
                                  "\t2. Un sol partit", 2)

if answer_accumulated == 2:
    answer_game = ask_question("\nQuin partit vols visualitzar?", Partits().get_partits_to_print(),
                               len(Partits().llista_partits))
    game = list(Partits().llista_partits.keys())[answer_game - 1]

statistics_calculator = ComputeStatistics()
out_str = ""
if answer_stats == 1:
    out_str = statistics_calculator.get_scores_by_fives(game)
elif answer_stats == 2:
    out_str = statistics_calculator.get_minutes_distribution_in_game(game)
elif answer_stats == 3:
    out_str = statistics_calculator.get_player_usage(game)
elif answer_stats == 4:
    out_str = statistics_calculator.get_player_usage_evolution(game)

print("\n\n\n Les teves estadístiques són:\n\n")
print(out_str)
