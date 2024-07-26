name1 = input('Enter your name? ')
name2 = input('Enter his/her name? ')

concat = (name1 + name2).lower()

t = concat.count('t')
r = concat.count('r')
u = concat.count('u')
e = concat.count('e')
true = t + r + u + e

l = concat.count('l')
o = concat.count('o')
v = concat.count('v')
e = concat.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f'Your love score is {love_score}% \n You guys go together like coke and mentos')
elif love_score >=40 and love_score <= 50:
    print(f'Your love score is {love_score}% \n You guys are good together')
else:
    print(f'Your love score is {love_score}%')

