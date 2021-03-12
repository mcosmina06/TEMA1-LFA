Mandru Cosmina
333CB

				Tema 1 - LFA

	Codul se imparte in 2 functii principale: compute_delta si automata_matcher, cea
din urma fiind prezentata la curs. 
	compute_delta: Cu ajutorul functiei compute_prefix generez dictionarul de prefixe
conform patternului de forma {"prefix":"state"}. Matricea delta am reprezentat-o ca pe
un dictionar de dictionare, ex: delta = {'e':{}, 'L':{}, 'LF':{}, 'LFA':{}}. Creez un
dictionar delta si adaug cate un dictionar vid pentru cheile reprezentate de fiecare 
prefix generat anterior. Apoi, pentru fiecare prefix, in dictionarul corespunzator,
adaug intrari reprezentate de literele din alfabet si valoare 0. Urmeaza completarea
matrice: parcurg fiecare prefix si pentru fiecare litera a alfabetului realizez concatenarea
intre prefix si litera curenta. Daca aceasta concatenare exista in dictionarul de prefixe,
completez matricea cu stare corespunzatoare pe pozitia curenta, in caz contrat ma folosesc
de functia get_longest_prefix ce imi intoarce starea corespunzatoare celui mai lung prefix
gasit in concatenare. Functia get_longest_prefix parcurge concatenarea data pana la gasirea
unei intrari in dictionarul de prefixe, la fiecare ciclu stergandu-se primul caracter.
	automata_matcher: am preluat implementarea oferita la curs.
	
	