import retrieve_data
import plot
import sort

def main():
    attackers_list, defenders_list = retrieve_data.retrieve_data()
    sort.sort(attackers_list)
    sort.sort(defenders_list)
    plot.plot_operators(attackers_list, defenders_list)

if __name__ == '__main__':
    main()
