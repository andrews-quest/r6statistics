import matplotlib.pyplot as plt
import matplotlib.style

def plot_operators(attackers_list, defenders_list, winrate, time_played, version):
    attackers_x = []
    attackers_time_y = []
    attackers_time_lable = []
    defenders_x = []
    defenders_time_y = []
    defenders_time_lable = []

    for a in attackers_list:
        attackers_x.append(a[0])
        attackers_time_lable.append(a[1])
        attackers_time_y.append(a[2])

    for d in defenders_list:
        defenders_x.append(d[0])
        defenders_time_lable.append(d[1])
        defenders_time_y.append(d[2])

    figure = plt.figure('RAINBOW SIX: SIEGE OPERATOR STATISTICS', figsize=(14,7))
    axis1 = figure.add_subplot(211)
    axis2 = figure.add_subplot(212, sharex=axis1)

    axis1.set_title('v' + version + '\nTIME PLAYED: ' + str(time_played[0]) + 'h\nWINRATE: ' + str(winrate[0]) + '%\nATTACKERS', loc='left')
    #axis1.set_xlabel('HOURS')
    axis1.grid(axis='x')

    axis2.set_title('DEFENDERS', loc='left')
    #axis2.set_xlabel('HOURS')
    axis2.grid(axis='x')

    plt.xticks(rotation=0)
    plt.yticks()
    matplotlib.style.use('fivethirtyeight')

    #plt.tight_layout()
    plt.subplots_adjust(left=0.15)

    #window position for this backend
    thismanager = plt.get_current_fig_manager()
    thismanager.window.wm_geometry("+0+0")

    bars1 = axis1.barh(attackers_x, attackers_time_y)
    bars2 = axis2.barh(defenders_x, defenders_time_y)

    #def autolable():
    counter = 0
    for bar in bars2:
        hours = defenders_time_lable[counter] // 60
        minutes = defenders_time_lable[counter] % 60
        if hours != 0:
            plt.annotate(str(hours) + 'h ' +  str(minutes) + 'm', xy=(bar.get_x() + bar.get_width(), bar.get_y()))
        else:
            plt.annotate(str(minutes) + 'm', xy=(bar.get_x() + bar.get_width(), bar.get_y()))
        counter = counter + 1

    counter = 0
    for bar in bars1:
        plt.annotate(attackers_time_lable[counter], xy=(bar.get_x(), bar.get_y() + 20))
        counter = counter + 1

    plt.show()