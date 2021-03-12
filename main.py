# Mandru Cosmina
# 333CB
import string
import sys

#functia genereaza un dictionar de forma {"prefix":"state"}
def compute_prefix(pattern):
    prefix = {}
    prefix['e'] = 0
    for i in range(1, len(pattern) + 1):
        one_prefix = pattern[:i]
        prefix[one_prefix] = i
    return prefix

#functia genereaza un dictionar de forma {"state":"prefix"}
def compute_prefix2(pattern):
    prefix = {}
    prefix[0] = 'e'
    for i in range(1, len(pattern) + 1):
        one_prefix = pattern[:i]
        prefix[i] = one_prefix
    return prefix

# functia primeste un string si returneaza starea celui mai lung prefix
def get_longest_prefix(prefix, dictOfprefix):
    temp = prefix
    while temp:
        if temp in dictOfprefix.keys():
            return dictOfprefix[temp]
        temp = temp[1:]
    return 0

def compute_delta(pattern):
    #numarul de stari
    state_number = len(pattern)
    
    #dictionarul de prefixe al pattern-ului {"prefix":"state"}
    dictOfprefix = compute_prefix(pattern)
    
    #lista pentru coloanele matricei (A-Z)
    col = list(string.ascii_uppercase)
    
    # un set cu literele din pattern
    s = set(pattern)
    
    #matricea delta
    delta = {}
    
    for i in dictOfprefix.keys(): #ex: delta = {'e':{}, 'L':{}, 'LF':{}, 'LFA':{}}
        delta[i] = {}
    
    # adaug pentru fiecare prefix intrari in dictionar pentru fiecare litera a alfabetului si
    # setez valoarea 0
    for i in delta.keys():
        for j in col:
            delta[i][j] = 0
    # parcurg fiecare prefix
    for i in delta.keys():
        for j in s:
            # realizez concatenarea dintre prefix si urmatorul caracter de citit
            if i == 'e':
                tmp = j
            else:
                tmp = i + j
            
            # completez matricea delta
            # daca am gasit un prefix intreg adaug starea corespunzatoare
            if tmp in dictOfprefix:
                delta[i][j] = dictOfprefix.get(tmp)
            # in caz contrat caut cel mai lung prefix
            else:
                delta[i][j] = get_longest_prefix(tmp, dictOfprefix)
    return delta


def automata_matcher(pattern, text, filename_out):
    output_file = open(filename_out, "w")
    q = 0;
    
    # dictionar de forma {"state":"prefix"}
    dictOfprefix = compute_prefix2(pattern)
    
    # calculez matricea delta
    delta = compute_delta(pattern);
    
    for i in range(0, len(text)):
        # prefixul corespondent starii date
        prefixFromState_q = dictOfprefix.get(q)
        q = delta[prefixFromState_q][text[i]]
        if q == len(pattern):
            output_file.write(str(i-(len(pattern))+1))
            output_file.write(str(" "))
    output_file.write(str("\n"))
    output_file.close()

def read_input(filename):
    input_file = open(filename, "r")
    lines = input_file.readlines()
    input_file.close()
    pattern = lines[0].rstrip()
    text = lines[1].rstrip()
    return pattern, text

if __name__ == '__main__':
    pattern, text = read_input(str(sys.argv[1]))
    automata_matcher(pattern, text, str(sys.argv[2]))
