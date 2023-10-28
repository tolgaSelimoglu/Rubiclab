"""
    inputs:
        cubestring :
            The cube color positions obtained by processing the captured images should be
             in the following format: 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
            U : Up
            R : Right
            F : Front
            D : Down
            L : Left
            B : Back
        t:
            Time to solve the cube, if could not find a solution on time find the closest time (seconds)
        m:
            Exact number of moves to solve the cube, enter 0 for the shortest maneuver found in this time t


        example of usage:

            cubestring = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
            t = 2
            m = 19
            sv.solve(cubestring, m, t)

    --------------------------------------------------------------------------------------------------------

    output:
        String that contains the moves to solve the cube and at the end the number of moves.

        example of output:

            >>> L3 U1 B1 R2 F3 L1 F3 U2 L1 U3 B3 U2 B1 L2 F1 U2 R2 L2 B2 (19f)

            The algorithm output is given as the face to be rotated and
             the number of degrees to be rotated clockwise divided by 90.


    some cube examples:

        FFDFUUBBDRBFLRRLUURDBFFUBBBURDBDFFDLULURLDDLLLRRUBDFLR (16 moves in 5 seconds)
        FDDLURBFDRFRLRDFBRLDBRFFBBLURDBDLLFBUUDDLUFULFBRLBRUUU (18 moves in 5 seconds)
        BLRBUDDLBUFULRUURBBDLDFBDLLLUFUDFRURRRLDLBFRFFFUBBRDFD (18 moves in 5 seconds)
        DULDULDDLFUBDRFBBRRRDDFBURLFUURDLRBUFLBLLFBBLDFRRBFFUU (19 moves in 5 seconds)
        DBDBUFURUBLFBRLFFLFDRRFUBLDDDRBDURUUBDLDLFULRLRLUBFBRF (20 moves in 5 seconds)
        RBBRURRDLDFLLRUUFDDLBFFFRDLUBFBDUFBFBDFRLDRUBULDLBULRU (19 moves in 5 seconds)
        UDLRURDBBDFUBRLFDRBLRBFUFLURULRDBFDUBDLFLRLUDBFRFBUFLD (18 moves in 5 seconds)
        BRFRULFUBUFLLRBBRRULLLFBBDDDFLBDULRFRDRULDFURDFUDBFDBU (19 moves in 5 seconds)
        FUBFUBBBDRLDFRFBDRURBBFUUDUFLRUDRFFURLLULDLRLLBDRBLFDD (19 moves in 5 seconds)
        BRLLUFLDRBUUURLDUFURDDFBLLFDFLLDRRFRRUFBLFFBBBBUDBDURD (20 moves in 5 seconds)

"""

import twophase.solver as sv

cubestring = 'Cube to Solve'
t = 5
m = 0

solution = sv.solve(cubestring, m, t)

print(solution)
