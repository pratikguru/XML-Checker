import time
import os


stack = []


class Lexon:
    def __init__(self, key, type_, opening, count):
        self.key = key
        self.type = type_
        self.opening = opening
        self.count = count

    def printLexon(self):
        print("-------------------------")
        print("Key: " + str(self.key))
        print("Type: " + str(self.type))
        print("opening: " + str(self.opening))
        print("-------------------------")


atoms = ["<note>", "<date>", "dfdfdfdf", "</date>", "<hour>", "03:34",
         "</hour>", "<to>", "someone", "</note>", "</note>"]


class XMLChecker:
    def __init__(self):
        self.stack = []
        self.count = 0
        self.DEBUG = False
        self.CRITICAL = False

    def check(self, atoms):

        for x in atoms:
            self.count = self.count + 1
            if x[0: 2] == '</' and x[-1] == '>':
                if x[2: -1].isdecimal():
                    raise Exception(
                        "Incorrect syntax: Unruly naming scheme " + str(self.count) + "=>\t" + str(x))

                if self.stack:
                    popped_element = self.stack.pop().key
                    if self.DEBUG:
                        print("Current stack size: " +
                              str(len(self.stack)))
                    if x[2:-1] == popped_element:
                        if self.DEBUG:
                            print("Popping:\t" + str(x))
                        else:
                            pass
                    else:
                        raise Exception(
                            "Incorrect syntax: Unbalanced scheme =>\t" + str(popped_element) + " and " + str(x))
                else:
                    raise Exception(
                        "Incorrect syntax: Premature closing encountered.")

            elif x[0] == '<' and x[-1] == '>':
                if x[1:-1].isdecimal():
                    raise Exception(
                        "Incorrect syntax: Unruly naming scheme =>\t" + str(x))

                if self.DEBUG:
                    print("Inserting:\t" + str(x[1:-1]))

                newLexon = Lexon(x[1:-1], "opening", 1, self.count)
                self.stack.append(newLexon)

            elif x[0] != '<' and x[-1] != '>':
                if self.DEBUG:
                    print("Normal keyword:\t" + str(x))
                else:
                    pass
            else:
                raise Exception(
                    "Incorrect syntax: Unruly naming scheme => " + str(x))
            if self.CRITICAL:
                print("---------------------------------")
                for atoms in stack:
                    atoms.printLexon()
                print("---------------------------------")

        if len(self.stack) > 0:
            for leftover in self.stack:
                print("Found leftover: " + str(leftover.key))
            raise Exception(
                "Incorrect syntax: Stack residue found => " + str(len(self.stack)) + " slice(s).")

        else:
            if self.DEBUG:
                print("OK")
            else:
                pass


if __name__ == "__main__":
    checker = XMLChecker()
    checker.check(atoms)
