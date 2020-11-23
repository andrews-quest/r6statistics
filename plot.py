import matplotlib.pyplot as plt
import matplotlib.style

def plot_operators(attackers_list, defenders_list):
    attackers_x = []
    attackers_time_y = []
    defenders_x = []
    defenders_time_y = []

    for a in attackers_list:
        attackers_x.append(a[0])
        attackers_time_y.append(a[2])

    for d in defenders_list:
        defenders_x.append(d[0])
        defenders_time_y.append(d[2])

    figure = plt.figure('RAINBOW SIX: SIEGE OPERATOR STATISTICS', figsize=(14,7))
    axis1 = figure.add_subplot(211)
    axis2 = figure.add_subplot(212, sharex=axis1)

    axis1.set_title('ATTACKERS', loc='left')
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

    axis1.barh(attackers_x, attackers_time_y)
    axis2.barh(defenders_x, defenders_time_y)

    plt.show()