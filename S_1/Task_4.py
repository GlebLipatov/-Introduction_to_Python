def calculator_crains(crains_total):
    crains_Petr = crains_total // 3 // 2
    crains_Sergey = crains_Petr
    crains_Kate = crains_total - crains_Petr * 2

    print(f'Петр сделал {crains_Petr} журавликов.')
    print(f'Катя сделал {crains_Kate} журавликов.')
    print(f'Сергей сделал {crains_Sergey} журавликов.\n')


crains_total_1 = 6
crains_total_2 = 24
crains_total_3 = 60

calculator_crains(crains_total_1)
calculator_crains(crains_total_2)
calculator_crains(crains_total_3)
