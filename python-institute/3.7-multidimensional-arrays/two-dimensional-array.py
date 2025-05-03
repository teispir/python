# A four-column/four-row table ‒ a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)

print("0,0",table[0][0])  # outputs: ':('
print("0,1",table[0][1])  # outputs: ':)'
print("0,2",table[0][2])  # outputs: ':('
print("0,3",table[0][3])  # outputs: ':)'

print("1,0",table[1][0])  # outputs: ':)'
print("1,1",table[1][1])  # outputs: ':('
print("1,2",table[1][2])  # outputs: ':)'
print("1,3",table[1][3])  # outputs: ':)'

print("2,0",table[2][0])  # outputs: ':('
print("2,1",table[2][1])  # outputs: ':)'
print("2,2",table[2][2])  # outputs: ':)'
print("2,3",table[2][3])  # outputs: ':('

print("3,0",table[3][0])  # outputs: ':)'
print("3,1",table[3][1])  # outputs: ':)'
print("3,2",table[3][2])  # outputs: ':)'
print("3,3",table[3][3])  # outputs: ':('