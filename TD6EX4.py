def est_sous_chaine():
    a = True
    while a :
        try:
            b = list(ch2,'.')
            ch1 = input("doner chaine 1 ")
            ch2 = input("donner chaine 2 ") 
            pos=0
            assert type(ch1) == str
            assert type(ch1) == str
            assert type(pos) == int 
            assert len(ch1) < len(ch2)
            pos = ch2.find(ch1)
            print(pos)
            assert pos == 0 or pos <= (len(ch2)-len(ch1))
            a = False
        except AssertionError as err :
            print(err)
            a = True

est_sous_chaine()