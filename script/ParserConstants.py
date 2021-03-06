class ParserConstants():
    START_SYMBOL = 49
    FIRST_NON_TERMINAL = 49
    FIRST_SEMANTIC_ACTION = 92

    PARSER_TABLE = [[ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1,  2, -1, -1, -1, -1,  1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, 23, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 24, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 26, -1, -1, -1, -1, -1, -1, 26, 26, -1, -1, 26, -1, -1, -1, 26, -1, -1, -1, -1, 26, 26, -1, -1, -1, -1, 26, 26, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 26 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,  3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1,  6,  7, -1, -1,  5, -1, -1, -1,  4, -1, -1, -1, -1, -1,  8, -1,  9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, 11, 11, -1, -1, 11, -1, -1, -1, 11, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, 14, 14, -1, -1, 14, -1, -1, -1, 14, -1, -1, -1, -1, -1, 14, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, 17, 18, -1, -1, 16, -1, -1, -1, 15, -1, -1, -1, -1, -1, 19, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 20, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 25, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 27, -1, -1, -1, -1, -1, -1, 28, 28, -1, -1, 28, -1, -1, -1, 28, -1, -1, -1, -1, 27, 28, -1, -1, -1, -1, 27, 27, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 27 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, 29, 29, -1, -1, 29, -1, -1, -1, 29, -1, -1, -1, -1, -1, 29, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 30, -1, -1, -1, -1, -1, 30, 30, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 30 ],
                    [ -1, 33, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 34, -1, -1, -1, -1, -1, 35, 36, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 37 ],
                    [ -1, 40, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 42, 43, -1, -1, -1, -1, -1, -1, -1, -1, 41, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 44, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 45, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 46, 46, 46, 46, 46, -1, -1, -1, -1, -1, 46, -1, -1, -1, -1, -1, -1, -1, 46, -1, -1, -1, 46, -1, -1, -1, -1, 46, -1, -1, -1, -1, -1, -1, -1, -1, -1, 46, 46, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 49, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 51, -1, -1, -1, 50, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 52, 52, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 54, 53, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 55 ],
                    [ -1, 56, 56, 56, 56, 56, -1, -1, -1, -1, -1, 56, -1, -1, -1, -1, -1, -1, -1, 56, -1, -1, -1, 56, -1, -1, -1, -1, 56, -1, -1, -1, -1, -1, -1, -1, -1, -1, 56, 56, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, 57, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 58, -1, -1, -1, -1, -1, -1, -1, -1, 59, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 59, 59, -1, -1, -1, -1 ],
                    [ -1, 60, 60, 60, 60, 60, -1, -1, -1, -1, -1, 62, -1, -1, -1, -1, -1, -1, -1, 63, -1, -1, -1, 61, -1, -1, -1, -1, 60, -1, -1, -1, -1, -1, -1, -1, -1, -1, 60, 60, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 64, 64, 64, 64, 64, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 64, -1, -1, -1, -1, -1, -1, -1, -1, -1, 64, 64, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 67, 68, 69, 70, 71, 72, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, 73, 73, 73, 73, 73, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 73, -1, -1, -1, -1, -1, -1, -1, -1, -1, 73, 73, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, 76, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 76, -1, -1, -1, -1, -1, -1, -1, -1, 76, 76, 76, 76, 76, 76, 76, -1, -1, 74, 75, -1, -1, 76, 76, -1, -1, -1, -1 ],
                    [ -1, 77, 77, 77, 77, 77, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 77, -1, -1, -1, -1, -1, -1, -1, -1, -1, 77, 77, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 80, -1, -1, -1, -1, -1, -1, -1, -1, 80, 80, 80, 80, 80, 80, 80, -1, -1, 80, 80, 78, 79, 80, 80, -1, -1, -1, -1 ],
                    [ -1, 81, 82, 83, 84, 85, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 86, -1, -1, -1, -1, -1, -1, -1, -1, -1, 87, 88, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 22, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 21, 22, 22, -1, -1, -1 ],
                    [ -1, 31, -1, -1, -1, -1, -1, -1, -1, -1, 32, -1, -1, -1, 32, -1, -1, -1, -1, -1, -1, 31, -1, -1, -1, -1, -1, 31, 31, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 31 ],
                    [ -1, -1, -1, -1, -1, -1, 66, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 66, -1, -1, -1, -1, -1, -1, -1, -1, 66, 65, 65, 65, 65, 65, 65, -1, -1, -1, -1, -1, -1, 66, 66, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, 90, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 90, -1, -1, -1, -1, -1, -1, -1, 89, 90, 90, 90, 90, 90, 90, 90, -1, -1, 90, 90, 90, 90, 90, 90, -1, -1, -1, -1 ],
                    [ -1, 91, 91, 91, 91, 91, -1, -1, -1, -1, -1, 91, -1, -1, -1, -1, -1, -1, -1, 91, -1, -1, -1, 91, -1, -1, -1, -1, 91, 92, -1, -1, -1, -1, -1, -1, -1, -1, 91, 91, -1, -1, -1, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 48, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 47, -1, -1, -1, -1, -1 ],
                    [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 38, -1, -1, -1, -1, -1, -1, -1, -1, -1, 39, 39, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1 ]]

    PRODUCTIONS = [ [ 107,  18,  50,  51, 108,   8,  52,  11, 109 ],
                    [   0 ],
                    [  53,  50 ],
                    [  14,  19,  54,   2,  29,  55,  30 ],
                    [  17 ],
                    [  13 ],
                    [   9 ],
                    [  10 ],
                    [  23 ],
                    [  25 ],
                    [   0 ],
                    [  56,  57 ],
                    [   0 ],
                    [  45,  56,  57 ],
                    [  58,  46,  59 ],
                    [  17 ],
                    [  13 ],
                    [   9 ],
                    [  10 ],
                    [  23 ],
                    [   2, 124,  85 ],
                    [  43,  59 ],
                    [   0 ],
                    [   0 ],
                    [  60,  51 ],
                    [  19,   2,   8,  52,  11 ],
                    [  61,  63 ],
                    [   0 ],
                    [  62,  61 ],
                    [  58, 122,  46,  59, 123,  44 ],
                    [  64,  44,  86 ],
                    [  63 ],
                    [   0 ],
                    [  65 ],
                    [  67 ],
                    [  68 ],
                    [ 129,  29,  75,  30,  91 ],
                    [  74 ],
                    [  70 ],
                    [  72 ],
                    [   2, 124,  66, 128,  75, 126 ],
                    [  47 ],
                    [  37 ],
                    [  38 ],
                    [  22,  29,  59, 127,  30 ],
                    [  28,  29,  69,  30 ],
                    [  75, 106,  90 ],
                    [  43,  69 ],
                    [   0 ],
                    [  16, 130,  63,  71,  11, 131 ],
                    [ 132,  15,  63 ],
                    [   0 ],
                    [  73, 133,  63,  11, 134 ],
                    [  27 ],
                    [  26 ],
                    [  48,  75 ],
                    [  77,  76 ],
                    [   7,  77, 110,  76 ],
                    [  21,  77, 111,  76 ],
                    [   0 ],
                    [  78 ],
                    [  24, 103 ],
                    [  12, 104 ],
                    [  20,  77, 105 ],
                    [  80,  87 ],
                    [  79, 101,  80, 102 ],
                    [   0 ],
                    [  31 ],
                    [  32 ],
                    [  33 ],
                    [  34 ],
                    [  35 ],
                    [  36 ],
                    [  82,  81 ],
                    [  39,  82,  93,  81 ],
                    [  40,  82,  94,  81 ],
                    [   0 ],
                    [  84,  83 ],
                    [  41,  84,  95,  83 ],
                    [  42,  84,  96,  83 ],
                    [   0 ],
                    [   2, 125,  88 ],
                    [   3,  97 ],
                    [   4,  98 ],
                    [   5, 113 ],
                    [   6, 112 ],
                    [  29,  75,  30 ],
                    [  39,  84,  99 ],
                    [  40,  84, 100 ],
                    [  29,  89,  30 ],
                    [   0 ],
                    [  69 ],
                    [   0 ]]

    PARSER_ERROR = [ "",
                    "esperado fim de arquivo",
                    "esperado identificador",
                    "esperado constante int",
                    "esperado constante float",
                    "esperado constante string",
                    "esperado constante caracter",
                    "esperado and",
                    "esperado begin",
                    "esperado bool",
                    "esperado char",
                    "esperado end",
                    "esperado false",
                    "esperado float",
                    "esperado forward",
                    "esperado IfFalseDo",
                    "esperado IfTrueDo",
                    "esperado int",
                    "esperado main",
                    "esperado module",
                    "esperado not",
                    "esperado or",
                    "esperado read",
                    "esperado string",
                    "esperado true",
                    "esperado void",
                    "esperado WhileFalseDo",
                    "esperado WhileTrueDo",
                    "esperado write",
                    "esperado (",
                    "esperado )",
                    "esperado ==",
                    "esperado !=",
                    "esperado <",
                    "esperado <=",
                    "esperado >",
                    "esperado >=",
                    "esperado +=",
                    "esperado -=",
                    "esperado +",
                    "esperado -",
                    "esperado *",
                    "esperado /",
                    "esperado ,",
                    "esperado .",
                    "esperado ;",
                    "esperado :",
                    "esperado =",
                    "esperado ^",
                    "esperado main",                                                    # "<programa> invalido",
                    "esperado begin forward module",                                    # "<declaracao> invalido",
                    "esperado begin module",                                            # "<modulo> invalido",
                    "esperado identificador tipo read write ( ^",                       # "<corpo> invalido", # ver com a professora por causa do void
                    "esperado forward",                                                 # "<especificacoes_declaracao> invalido",
                    "esperado tipo",                                                    # "<tipo_modulo> invalido",
                    "esperado tipo )",                                                  # "<parametros_formais> invalido",
                    "esperado tipo",                                                    # "<parametros> invalido",
                    "esperado ) ;",                                                     # "<lista_de_parametros> invalido",
                    "esperado tipo",                                                    # "<tipo> invalido",
                    "esperado identificador",                                           # "<lista_de_identificadores> invalido",
                    "esperado module",                                                  # "<especificacoes_modulo> invalido",
                    "esperado identificador tipo write read ( ^",                       # "<declaracao_de_variaveis> invalido",
                    "esperado tipo",                                                    # "<variavel> invalido",
                    "esperado identificador read write ( ^",                            # "<lista_de_comandos> invalido",
                    "esperado identificador read write ( ^",                            # "<comando> invalido",
                    "esperado identificador",                                           # "<comando_atribuicao> invalido",
                    "esperado += -= =",                                                 # "<operador_de_atribuicao> invalido",
                    "esperado read",                                                    # "<comando_entrada> invalido",
                    "esperado write",                                                   # "<comando_saida> invalido",
                    "esperado expressão",                                               # "<lista_de_expressoes> invalido",
                    "esperado IfTrueDo",                                                # "<comando_selecao> invalido",
                    "esperado end IfFalseDo",                                           # "<selecao_opcional> invalido",
                    "esperado WhileFalseDo WhileTrueDo",                                # "<comando_repeticao> invalido",
                    "esperado WhileFalseDo WhileTrueDo",                                # "<tipo_de_repeticao> invalido",
                    "esperado ^",                                                       # "<comando_retorno> invalido",
                    "esperado expressão",                                               # "<expressao> invalido",
                    "esperado expressão",                                               # "<expressao_I> invalido",
                    "esperado expressão",                                               # "<elemento> invalido",
                    "esperado expressão",                                               # "<relacional> invalido",
                    "esperado expressão",                                               # "<operador_relacional> invalido",
                    "esperado expressão",                                               # "<aritmetica> invalido",
                    "esperado expressão",                                               # "<aritmetica_I> invalido",
                    "esperado expressão",                                               # "<termo> invalido",
                    "esperado expressão",                                               # "<termo_I> invalido",
                    "esperado expressão",                                               # "<fator> invalido",
                    "esperado ) , . ;",                                                 # "<lista_de_identificadores_I> invalido",
                    "esperado identificador end IfFalseDo read write ( ^",              # "<lista_de_comandos_I> invalido",
                    "esperado expressão",                                               # "<relacional_I> invalido",
                    "esperado expressão",                                               # "<fator_I> invalido",
                    "esperado expressão",                                               # "<fator_II> invalido",
                    "esperado )",                                                       # "<lista_de_expressoes_I> invalido",
                    "esperado IfTrueDo WhileFalseDo WhileTrueDo"                        # "<comando_dirigido> invalido" 
                    ]