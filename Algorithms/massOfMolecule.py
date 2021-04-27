'''
A molecule can be defined as a sequence of atoms and represented by a checmical formula
    consisting of letters denoting these atoms. E.g. letter H denotes atom of hydrogen,
    C denotes atom of carbon, O denotes atom of oxygenm formula COOH represents molecule
    consisting of one atom of carbon, two atoms of oxygen and one atom of hydrogen.

To write some formulas efficiently, we use the following rules. Letters denoting some atoms
    can be grouped by enclosing in parentheses, e.g. formula CH(OH) contains group OH. Groups
    can be nested - a group can also contain other groups. To simplify a formula,
    consetive occurences of the same letter can be replaced with that letter followed
    by a number of these occurence. E.g. formula COOHHH can be written as CO2H3 and it
    represents a molecule consisting of one atom of carbon, two atoms of oxygen, and 
    three atoms of hydrogen.

Furthermore, consecutive occurrences of the same group can be replaced with that group
    followed by a number of these occurences. E.g. formula CH (CO2H) (CO2H) (CO2H)
    can be written as CH(CO2H)3 and molecule represented by both those formulas consists
    of four atoms of carbon, four atoms of hydrogen, and six atoms of oxygen.

A number written after a letter or a group is always greater than or equal to 2 and
    less than or equal to 9. A mass of a molecule is a sum of masses of all its
    atoms. One atoms of hydrogen has mass 1. One atom of carbon has mass 12 and one
    atom of oxygen has mass 16.
'''

# formula of a molecule whose mass needs to be determined
molecule = input()

mass_dict = {'H': 1, 'C': 12, 'O': 16}

stack = []

for symbol in molecule:
