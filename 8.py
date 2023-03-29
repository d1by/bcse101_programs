import re

hair = input("Enter hair sample DNA: ").upper()
person = input("Enter suspect DNA: ").upper()

if(re.findall("^[AGCT]*$", hair) and re.findall("^[AGCT]*$", person)):
    hairseq = re.findall("AGCT", hair)
    personseq = re.findall("AGCT", person)

    if(len(hairseq)==len(personseq)):
        print("MATCH")
    else:
        print("MISMATCH")

else:
    print("Incorrect DNA")