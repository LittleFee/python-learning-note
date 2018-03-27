filename='pi_million_digits.txt'

with open(filename) as file_millons:
    string=file_millons.readlines()

pi_string=''
for line in string:
    pi_string+=line.strip()

# print(pi_string[:100])
# print(len(pi_string))
birthday=input('Tell me your birthday like mmddyy:')
if birthday in pi_string:
    print('Woo your birthday:'+birthday+' in the string')
else:
    print('Opps your birthday:' + birthday + ' not in the string')