#
#                                     J5~
#                  .:^~!7?JYY555555YYJY##?.
#            .^!?Y5PGGBBBBBBBBGBBBB####BB#G5J!:
#         .7YGB###BBGGGGGBGGGGBBBBB###########BPJ~.
#        :5BB###BBGGGGBBBGGGBBBBBBBBBB############BY!.
#      :JPGBB###BBGBBGGBBBB#######BBBBBBBB###########BY~
#     !GBGGBBBBBBBBBGGB##&&&&&&&&&&&&&&&################G?:
#    .G#BGGBBB###BBGB##&&&&&&&&&&&&&&&&&&&&&&&&&#########&#5~
#    .P#BGGBBBBBBBB##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#5^
#     !BBBGGBBB###&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&J
#      !BBBGB#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@Y
#       ~GBGB##&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@#:
#        ?GGB##&&&&&####BBBG#BBB####&&&@@&&@&&&&&&&&&&&&&&&&&&&&&^
#        ^GBB#BG5Y#5!!!!!~~~5J~!!!!!77?JYBBG#&&@@@@@&&&&&&&&&&@@#.
#         7B#Y7Y~~Y5~~~~~~~~J#?~~~~~~~~~~G7~!!7J5G#&@@@&&&&@@@@@J
#         :&P~!?~~75~~~~~~~~755?~~!~~~~~!Y~~~~~~~~!7Y#&@@@@@@@@Y          .
#         ^@Y~!~~!!?!~~~~~~~!!!P7~!~~~~!!!~~~~~~~~~~Y?J#&@@@&P!        :~77!~.
#         ^@5~~~~~!~~~~~~~~~~~~?7~~~~!!~~~~~~~~~~~~~7!G5#B7^:        .~!!~77?7.
#         :&G~~~!~!!~~~~!~~!~~!~~!~~!~~~~~~~~~~~~!!~~5YG@?          :~!7?YYJ?7:
#          G&!~~!~~~~~~~~~~~~~~~!~~~~~!~~~~~~~~~~~!~!?Y@G:         :^!JYYYJ?7~
#          ?@Y~~!~~!?JJJ7!~~~~~~~~~!!~!~~~7JJJ?7~~~!!!#&7         :!7?JJ777!!:
#          ^@B~~~!5BGG&@@#5!~!~~~~~~!~~~JBBPB@@&BJ~!~Y@5.       .^~!7!!!!!!7~
#           G@7~!B@7  ?@@@@B!~~~!~!~~~~J@#: .B@@@@J~~B&!       .^~~!7?JJ?77!.
#           ~@5~7&@#PP#&&@@&7~!~~!~~~~~P@@G5G&&@@@P~7@G:      .^!7??????77!.
#            G#!~Y&@@@&7G@&Y~~~~~~~~~~~7B@@@@P?@@#7~5@J      .^!~~!!7?J?77:
#            ~@J~~75B#####BGBBG5?!?5GBBGPGBB##BGJ!~!##~     .~!^^~7JYJ??7^
#             P#!7Y!~!?P#&@@@@@@&#&@@@@@@@#P?!~!Y?~5@Y.    .^~^~??JYJ??!^
#             .P#JP&B#&@@@@@@@@@@&@@@@@@@@@@&#B&G!5&Y:     :^^!7???JJ?7~.
#               ?#BG#&@@@@@@@&BP?!?PB&@@@@@@@&B5JGG7.     :^:^!?7!!?J?7:
#             .Y55PGGP5555YJ?!~~~~~~~!7JYY55Y5PGP7.      :^!7?7!:^7???^
#             .G&PYJY5PBYJYJ????777????JJY5BBBPG#~      .~777~~^!?JJ?~
#             :B&GGPGBG?!~PP777YG5G5??75#J?JBGGB?.     .~7~^!7?J5YJJ!.
#              :~~:!#5~~~?G!~~~~!G?~~~~!GJ777Y@Y      .~~:^~?Y55YYJ7.
#                 ?#5??YJPP~~~~~~57~~~~~YBY?!~?BY~!!~.^^:~?Y55YYYJ7:
#                5B?5P7!!P5J?7J?75J77JJ?5P?J?5?Y&B5BB~:^7?JJYYYYJ?^
#            JY7Y@77Y57~5B77JP7!!!7?JP?!?B5??P7P?B#?^:^^!7?JJJYYJ!
#            JG5#JYY!?Y7&Y77?P7!~!!7?P~~?B&?~J7?Y7&Y:^^~7??!7JYY?.
#             Y&J~BJ~!5G@PYJ?YJJ?!!!J7??5J@B75!!J~YJ~!!77!~?Y55J:
#             PG~~J?~~P@@P557!7YJ775Y??JJ!&@57~~~~!!!~~!!!Y555Y^
#            :&?~!7J~~5@#77?555?!!!7BY?JYY&@5~!!~~7!^^~7?55PPY^
#             YGJYYJ75#&&J~~Y!~7#&B?J!~~J?&&&J7P7!~^~~7YPPPPY^
#              :?5P5YY75&J?J57JY&@#YYJ7?JY#P75PGP!^~7JY55PPY:
#                      YB~77??7~#@G~YY777~GG.    .^~!?Y5PP?.
#                      5#7J!!J!?&@#7YY!!?Y&P.     :~7YPPY~
#                      :Y5P55P5P5!?5PPPPPP5~       .^!~:
#
#
# Je suis Groot
#

from decimal import Decimal


def polyderiv(p: list[Decimal]) -> list[Decimal]:
    """Computes the derivative of the given polynomial"""
    return [k * a for k, a in enumerate(p)][1:]


def polyeval(p, x):
    """Computes p(x)"""
    if len(p) == 1:
        return p[0]
    result = p[0] + x * p[1]
    xk = x
    for a in p[2:]:
        xk *= x
        result += xk * a
    return result


def poly_rootfind(
    p: list[Decimal], lb: Decimal | float, ub: Decimal | float, tol: Decimal | float
) -> list[Decimal]:
    """Numerically computes the roots of the given polynomial `p` using
    a sequence of bisection methods. Assumes all of the roots are real,
    and lie in the range `(lb,ub)`.

    The true values (at the current decimal accuracy) will be within a
    distance `tol` of the given values.

    Args:
        p (list[Decimal]): the list of coefficients of p in increasing degree.
            Assumes p[-1] != 0.
        lb (Decimal): Lower bound of roots to find
        ub (Decimal): Upper bound of roots to find
        tol (Decimal): the tolerance for the roots

    Returns:
        list[Decimal]: the list of roots of p, in increasing value
    """
    degree = len(p) - 1
    if degree == 2:
        vert = -p[1] / (2 * p[2])
        off = (p[1] ** 2 - 4 * p[2] * p[0]).sqrt() / (2 * p[2])
        return [vert - off, vert + off]

    if degree == 1:
        return [p[0] / p[1]]

    deriv = polyderiv(p)
    # since roots are all real and unique, derivative roots lie between each root.
    root_bounds = [lb, *poly_rootfind(deriv, lb, ub, tol), ub]

    roots = []
    for i in range(degree):
        # bisection method: assume one root falls between a and b
        # therefore (p(a)*p(b) < 0)
        a = root_bounds[i]
        b = root_bounds[i + 1]

        pa = polyeval(p, a)

        while True:
            c = (a + b) / 2
            if c - a < tol:
                break
            pc = polyeval(p, c)
            if pa * pc < 0:
                # root is between a and c
                b = c
            else:
                # root is between c and b
                a = c

        roots.append((a + b) / 2)

    return roots
