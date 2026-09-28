jmeno = input('Zadejte vaše jméno: ')
styl = input('Zvolte styl pozdravu (1 = neformální, 2 = formální): ')

if styl == '1':
    print(f'Zdarec, {jmeno}!')
else:
    print(f'Vazeny pane, {jmeno}!')