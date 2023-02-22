# Cet algo permet de générer du code Gorgias
# définir la première règle pour chaque valeur de i
first_rule = 1
# itérer sur chaque valeur de i de c514 à c576
for i in range(33, 57):
    # itérer sur chaque valeur de j de c321 à c384
    for j in range(9, 17):
        # générer la règle et l'afficher
        rule_id = f'd{first_rule}'
        rule = f'rule({rule_id}, prefer(c{i}, c{j}), []).'
        with open('res.txt', 'a') as f:
            f.write(rule + "\n")
        # incrémenter first_rule
        first_rule += 1
    for j in range(25, 33):
        # générer la règle et l'afficher
        rule_id = f'd{first_rule}'
        rule = f'rule({rule_id}, prefer(c{i}, c{j}), []).'
        with open('res.txt', 'a') as f:
            f.write(rule + "\n")
        # incrémenter first_rule
        first_rule += 1
