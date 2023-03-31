#naturaal arvude hulk 1 .. 10
natural_num_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#hääletuse tulemuste hulk
vote_result_set = {('P', 76.69), ('G', 11.77), ('J', 5.65), ('S', 1.68), ('Y', 1.05), ('T', 0.76), ('S', 0.68), ('B', 0.65)}

#tühja hulga loomine
friend_list = set()

#muu andmetüüpi hulgaks muteerimine
strange_app = set('TikTok')
print(strange_app)

#elementide lisamine
natural_num_set.add(11)
print(natural_num_set)

#hulka "puhtaks" tegemine
vote_result_set.clear()
print(vote_result_set)

#elementi kustutamine hulgast (veateadega)
natural_num_set.remove(11)
print(natural_num_set)
#elementi kustutamine hulgast (ei anna viga, kui elementi ei ole)
natural_num_set.discard(11)
print(natural_num_set)
#hulgast suvalise elemendi kustutamine ja selle tagastamine
print(strange_app.pop())
print(strange_app)

for element in natural_num_set:
    print(element)

#kas mingi element on hulga sees
print('a' in strange_app)
print(len(natural_num_set))

#kui on vaja sorteerida
some_digits = {1, 55, 34, 2, 12, 14, -4}
print(sorted(some_digits))
print(some_digits)

input()