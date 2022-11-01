# https://www.codewars.com/kata/62dabb2225ea8e00293da513

def pass_or_fail(harmony):
    chords = [chord.split() for chord in harmony]
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(3):
                if chords[k][i] == chords[k][j] and chords[k+1][i] == chords[k+1][j] and chords[k][i] != chords[k+1][i]:
                    return "Fail"
    return "Pass"