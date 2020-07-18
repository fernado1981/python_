from letters import letters


class lettersAction:
    letter = ["F", "E", "R", "N", "A", "N", "D", "O"]

    letra = letters(letter)
    letra.addLetter("M")
    letra.addLetter("A")
    letra.addLetter("N")
    letra.showLetters()
    letra.delLetter("A")
    letra.showLetters()
    letra.countRepitChar("A")
    letra.mayLetter()
    letra.showLetters()
    letra.minLetter()
    letra.showLetters()
    letra.volteoLetter()
    letra.setLetter()
    letra.showLetters()
    letra.arrLetter()
    letra.showLetters()
