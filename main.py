import retrieve_data_operators
import retrieve_data_general
import plot
import sort

version = '0.1.1'

def main():
    winrate, time_played = retrieve_data_general.retrieve()
    attackers_list, defenders_list = retrieve_data_operators.retrieve_data()
    sort.sort(attackers_list)
    sort.sort(defenders_list)
    plot.plot_operators(attackers_list, defenders_list, winrate, time_played, version)

if __name__ == '__main__':
    main()
