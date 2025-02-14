def brians_Dead():
    return """

yo dude, y’know they killed the uh, the dog on Family Guy
THE DOG BRIAN? yeah, Brian. MAN STOP PLAYING FR. Nah man, I’m not playing. BRIAN’S DEAD…? Yeah.
UUAUUUAUAAUAUAUAUAAAAAAGGGGHHHHH! SHOOOOOOOOOOOTTTT!!!

*bangs table* BRIIIIIANNNNSSS DEEEAAAAAAD!

AAAAAAGHHH- AGHHHHHHH- *goes silent* DAAAAAH!
"""

def recursive(n):
    if (n == 0):
        return
    print(n)
    recursive(n - 1)

print(brians_Dead())
recursive(10)
