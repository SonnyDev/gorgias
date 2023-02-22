# Cet algo permet de générer du code Gorgias
# définir la première règle pour chaque valeur de i
first_rule = 1

# Les i sont les numéros de règles qu'on préfère et les j celles qui ne sont pas préférés.
# Itérer sur chaque valeur de i de c33 à c56
for i in range(33, 57):
    # itérer sur chaque valeur de j de c9 à c16
    for j in range(9, 17):
        # générer la règle et l'afficher
        rule_id = f'd{first_rule}'
        rule = f'rule({rule_id}, prefer(c{i}, c{j}), []).'
        with open('res.txt', 'a') as f:
            f.write(rule + "\n")
        # incrémenter first_rule
        first_rule += 1
    # Itérer sur d'autres valeurs de j si nécessaires
    for j in range(25, 33):
        # générer la règle et l'afficher
        rule_id = f'd{first_rule}'
        rule = f'rule({rule_id}, prefer(c{i}, c{j}), []).'
        with open('res.txt', 'a') as f:
            f.write(rule + "\n")
        # incrémenter first_rule
        first_rule += 1
