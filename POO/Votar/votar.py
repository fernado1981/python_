from prueb import Votar


class votar:
    name = input("Dime tu nombre: ")
    print(name)
    edad = int(input("Dime tu edad: "))

    vote = Votar(name, edad)
    #vote.couldVote()
    #vote.seeVote()
    vote.suma([2, 3, 4, 5, 7, 1, 2])
    vote.multiplica()
