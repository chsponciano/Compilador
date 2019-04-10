class LexicoConstants:
	EPSILON = 0
	DOLLAR	= 1
	t_identificador = 2
	t_cons_inteira = 3
	t_cons_real = 4
	t_cons_string = 5
	t_cons_caracter = 6
	t_comentario_linha = 7
	t_comentario_bloco = 8
	t_and = 9
	t_begin = 10
	t_bool = 11
	t_char = 12
	t_end = 13
	t_false = 14
	t_float = 15
	t_forward = 16
	t_iffalsedo = 17
	t_iftruedo = 18
	t_int = 19
	t_main = 20
	t_module = 21
	t_not = 22
	t_or = 23
	t_read = 24
	t_string = 25
	t_true = 26
	t_void = 27
	t_whilefalsedo = 28
	t_whiletruedo = 29
	t_write = 30
	t_TOKEN_31 = 31
	t_TOKEN_32 = 32
	t_TOKEN_33 = 33
	t_TOKEN_34 = 34
	t_TOKEN_35 = 35
	t_TOKEN_36 = 36
	t_TOKEN_37 = 37
	t_TOKEN_38 = 38
	t_TOKEN_39 = 39
	t_TOKEN_40 = 40
	t_TOKEN_41 = 41
	t_TOKEN_42 = 42
	t_TOKEN_43 = 43
	t_TOKEN_44 = 44
	t_TOKEN_45 = 45
	t_TOKEN_46 = 46
	t_TOKEN_47 = 47

	CLASS_LEXEME = ["IDENTIFICADOR", "CONSTANTE INTEIRA", "CONSTANTE REAL",
					"CONSTANTE STRING", "CONSTANTE CARACTERE", "PALAVRA RESERVADA",
					"SIMBOLO ESPECIAL"]
					
	TOKEN_STATE = [-1, 0, -1, -1, -1, 31, 32, 41, 39, 43, 40, 44, 42, 
					3, 3, 46, 45, 35, 47, 37, 7, 2, -1, 2, 34, 5, -1, 
					-1, 36, 33, 38, 7, 2, 6, 2, -1, 4, 2, -1, -1, -1, 
					8]

	SPECIAL_CASES_INDEXES = [0, 0, 0, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
							 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
							 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
							 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 
							 22, 22, 22, 22]

	SPECIAL_CASES_KEYS = ["and", "begin", "bool", "char", "end", "false", 
						  "float", "forward", "ifFalseDo", "ifTrueDo", "int", 
						  "main", "module", "not", "or", "read", "string", 
						  "true", "void", "whileFalseDo", "whileTrueDo", "write"]

	SPECIAL_CASES_VALUES = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
							22, 23, 24, 25, 26, 27, 28, 29, 30]	

	SCANNER_ERROR = [ "Símbolo Inválido", "", "", 
					  "Constate String Inválida", "Comentário de bloco inválido ou não finalizado", 
					  "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
					  "Constate Caractere Inválida", "", "", "", 
					  "Comentário de bloco inválido ou não finalizado", "Constate Real Inválida", 
					  "", "", "", "", "", "", "", "Comentário de bloco inválido ou não finalizado", "", 
					  "", "Comentário de bloco inválido ou não finalizado", 
					  "Comentário de bloco inválido ou não finalizado", "Constate Real Inválida", ""]			  

	SCANNER_TABLE_INDEXES = [0, 83, 83, 84, 275, 276, 276, 276, 276, 
							 276, 276, 276, 276, 276, 277, 288, 288, 
							 288, 289, 290, 291, 484, 521, 524, 587, 
							 587, 587, 778, 788, 788, 788, 788, 788, 
							 851, 851, 888, 1081, 1091, 1154, 1346, 
							 1538, 1548, 1548]

	SCANNER_TABLE = [ [9, 1], [10, 1], [32, 1], [33, 2], [34, 3], [35, 4], 
					 [40, 5], [41, 6], [42, 7], [43, 8], [44, 9], [45, 10], 
					 [46, 11], [47, 12], [48, 13], [49, 14], [50, 14], [51, 14], 
					 [52, 14], [53, 14], [54, 14], [55, 14], [56, 14], [57, 14], 
					 [58, 15], [59, 16], [60, 17], [61, 18], [62, 19], [63, 20], 
					 [65, 21], [66, 21], [67, 21], [68, 21], [69, 21], [70, 21], 
					 [71, 21], [72, 21], [73, 21], [74, 21], [75, 21], [76, 21], 
					 [77, 21], [78, 21], [79, 21], [80, 21], [81, 21], [82, 21], 
					 [83, 21], [84, 21], [85, 21], [86, 21], [87, 21], [88, 21], 
					 [89, 21], [90, 21], [92, 22], [97, 23], [98, 23], [99, 23], 
					 [100, 23], [101, 23], [102, 23], [103, 23], [104, 23], 
					 [105, 23], [106, 23], [107, 23], [108, 23], [109, 23], 
					 [110, 23], [111, 23], [112, 23], [113, 23], [114, 23], 
					 [115, 23], [116, 23], [117, 23], [118, 23], [119, 23],
					 [120, 23], [121, 23], [122, 23], [61, 24], [9, 3], [13, 3], 
					 [32, 3], [33, 3], [34, 25], [35, 3], [36, 3], [37, 3], 
					 [38, 3], [39, 3], [40, 3], [41, 3], [42, 3], [43, 3], [44, 3], 
					 [45, 3], [46, 3], [47, 3], [48, 3], [49, 3], [50, 3], [51, 3], 
					 [52, 3], [53, 3], [54, 3], [55, 3], [56, 3], [57, 3], [58, 3], 
					 [59, 3], [60, 3], [61, 3], [62, 3], [63, 3], [64, 3], [65, 3], 
					 [66, 3], [67, 3], [68, 3], [69, 3], [70, 3], [71, 3], [72, 3], 
					 [73, 3], [74, 3], [75, 3], [76, 3], [77, 3], [78, 3], [79, 3], 
					 [80, 3], [81, 3], [82, 3], [83, 3], [84, 3], [85, 3], [86, 3], 
					 [87, 3], [88, 3], [89, 3], [90, 3], [91, 3], [93, 3], [94, 3], 
					 [95, 3], [96, 3], [97, 3], [98, 3], [99, 3], [100, 3], [101, 3], 
					 [102, 3], [103, 3], [104, 3], [105, 3], [106, 3], [107, 3], [108, 3], 
					 [109, 3], [110, 3], [111, 3], [112, 3], [113, 3], [114, 3], [115, 3], 
					 [116, 3], [117, 3], [118, 3], [119, 3], [120, 3], [121, 3], [122, 3], 
					 [123, 3], [124, 3], [125, 3], [126, 3], [161, 3], [162, 3], [163, 3], 
					 [164, 3], [165, 3], [166, 3], [167, 3], [168, 3], [169, 3], [170, 3], 
					 [171, 3], [172, 3], [173, 3], [174, 3], [175, 3], [176, 3], [177, 3], 
					 [178, 3], [179, 3], [180, 3], [181, 3], [182, 3], [183, 3], [184, 3],
					 [185, 3], [186, 3], [187, 3], [188, 3], [189, 3], [190, 3], [191, 3], 
					 [192, 3], [193, 3], [194, 3], [195, 3], [196, 3], [197, 3], [198, 3], 
					 [199, 3], [200, 3], [201, 3], [202, 3], [203, 3], [204, 3], [205, 3], 
					 [206, 3], [207, 3], [208, 3], [209, 3], [210, 3], [211, 3], [212, 3], 
					 [213, 3], [214, 3], [215, 3], [216, 3], [217, 3], [218, 3], [219, 3], 
					 [220, 3], [221, 3], [222, 3], [223, 3], [224, 3], [225, 3], [226, 3],
					 [227, 3], [228, 3], [229, 3], [230, 3], [231, 3], [232, 3], [233, 3], 
					 [234, 3], [235, 3], [236, 3], [237, 3], [238, 3], [239, 3], [240, 3], 
					 [241, 3], [242, 3], [243, 3], [244, 3], [245, 3], [246, 3], [247, 3], 
					 [248, 3], [249, 3], [250, 3], [251, 3], [252, 3], [253, 3], [254, 3], 
					 [255, 3], [124, 26], [46, 27], [46, 27], [48, 14], [49, 14], [50, 14], 
					 [51, 14], [52, 14], [53, 14], [54, 14], [55, 14], [56, 14], [57, 14], 
					 [61, 28], [61, 29], [61, 30], [9, 20], [10, 31], [13, 20], [32, 20], 
					 [33, 20], [34, 20], [35, 20], [36, 20], [37, 20], [38, 20], [39, 20], 
					 [40, 20], [41, 20], [42, 20], [43, 20], [44, 20], [45, 20], [46, 20], 
					 [47, 20], [48, 20], [49, 20], [50, 20], [51, 20], [52, 20], [53, 20], 
					 [54, 20], [55, 20], [56, 20], [57, 20], [58, 20], [59, 20], [60, 20], 
					 [61, 20], [62, 20], [63, 20], [64, 20], [65, 20], [66, 20], [67, 20], 
					 [68, 20], [69, 20], [70, 20], [71, 20], [72, 20], [73, 20], [74, 20], 
					 [75, 20], [76, 20], [77, 20], [78, 20], [79, 20], [80, 20], [81, 20], 
					 [82, 20], [83, 20], [84, 20], [85, 20], [86, 20], [87, 20], [88, 20], 
					 [89, 20], [90, 20], [91, 20], [92, 20], [93, 20], [94, 20], [95, 20],
					 [96, 20], [97, 20], [98, 20], [99, 20], [100, 20], [101, 20], [102, 20], 
					 [103, 20], [104, 20], [105, 20], [106, 20], [107, 20], [108, 20], [109, 20], 
					 [110, 20], [111, 20], [112, 20], [113, 20], [114, 20], [115, 20], [116, 20], 
					 [117, 20], [118, 20], [119, 20], [120, 20], [121, 20], [122, 20], [123, 20], 
					 [124, 20], [125, 20], [126, 20], [161, 20], [162, 20], [163, 20], [164, 20], 
					 [165, 20], [166, 20], [167, 20], [168, 20], [169, 20], [170, 20], [171, 20], 
					 [172, 20], [173, 20], [174, 20], [175, 20], [176, 20], [177, 20], [178, 20], 
					 [179, 20], [180, 20], [181, 20], [182, 20], [183, 20], [184, 20], [185, 20], 
					 [186, 20], [187, 20], [188, 20], [189, 20], [190, 20], [191, 20], [192, 20], 
					 [193, 20], [194, 20], [195, 20], [196, 20], [197, 20], [198, 20], [199, 20], 
					 [200, 20], [201, 20], [202, 20], [203, 20], [204, 20], [205, 20], [206, 20], 
					 [207, 20], [208, 20], [209, 20], [210, 20], [211, 20], [212, 20], [213, 20],
					 [214, 20], [215, 20], [216, 20], [217, 20], [218, 20], [219, 20], [220, 20], 
					 [221, 20], [222, 20], [223, 20], [224, 20], [225, 20], [226, 20], [227, 20], 
					 [228, 20], [229, 20], [230, 20], [231, 20], [232, 20], [233, 20], [234, 20], 
					 [235, 20], [236, 20], [237, 20], [238, 20], [239, 20], [240, 20], [241, 20], 
					 [242, 20], [243, 20], [244, 20], [245, 20], [246, 20], [247, 20], [248, 20], 
					 [249, 20], [250, 20], [251, 20], [252, 20], [253, 20], [254, 20], [255, 20], 
					 [48, 32], [49, 32], [50, 32], [51, 32], [52, 32], [53, 32], [54, 32], 
					 [55, 32], [56, 32], [57, 32], [95, 32], [97, 32], [98, 32], [99, 32], 
					 [100, 32], [101, 32], [102, 32], [103, 32], [104, 32], [105, 32], [106, 32], 
					 [107, 32], [108, 32], [109, 32], [110, 32], [111, 32], [112, 32], [113, 32], 
					 [114, 32], [115, 32], [116, 32], [117, 32], [118, 32], [119, 32], [120, 32], 
					 [121, 32], [122, 32], [110, 33], [115, 33], [116, 33], [48, 23], [49, 23], 
					 [50, 23], [51, 23], [52, 23], [53, 23], [54, 23], [55, 23], [56, 23], [57, 23], 
					 [65, 34], [66, 34], [67, 34], [68, 34], [69, 34], [70, 34], [71, 34], [72, 34], 
					 [73, 34], [74, 34], [75, 34], [76, 34], [77, 34], [78, 34], [79, 34], [80, 34], 
					 [81, 34], [82, 34], [83, 34], [84, 34], [85, 34], [86, 34], [87, 34], [88, 34], 
					 [89, 34], [90, 34], [95, 23], [97, 23], [98, 23], [99, 23], [100, 23], [101, 23], 
					 [102, 23], [103, 23], [104, 23], [105, 23], [106, 23], [107, 23], [108, 23], 
					 [109, 23], [110, 23], [111, 23], [112, 23], [113, 23], [114, 23], [115, 23], 
					 [116, 23], [117, 23], [118, 23], [119, 23], [120, 23], [121, 23], [122, 23], 
					 [9, 35], [10, 35], [13, 35], [32, 35], [33, 35], [34, 35], [36, 35], [37, 35], 
					 [38, 35], [39, 35], [40, 35], [41, 35], [42, 35], [43, 35], [44, 35], [45, 35], 
					 [46, 35], [47, 35], [48, 35], [49, 35], [50, 35], [51, 35], [52, 35], [53, 35], 
					 [54, 35], [55, 35], [56, 35], [57, 35], [58, 35], [59, 35], [60, 35], [61, 35], 
					 [62, 35], [63, 35], [64, 35], [65, 35], [66, 35], [67, 35], [68, 35], [69, 35], 
					 [70, 35], [71, 35], [72, 35], [73, 35], [74, 35], [75, 35], [76, 35], [77, 35], 
					 [78, 35], [79, 35], [80, 35], [81, 35], [82, 35], [83, 35], [84, 35], [85, 35], 
					 [86, 35], [87, 35], [88, 35], [89, 35], [90, 35], [91, 35], [92, 35], [93, 35], 
					 [94, 35], [95, 35], [96, 35], [97, 35], [98, 35], [99, 35], [100, 35], [101, 35], 
					 [102, 35], [103, 35], [104, 35], [105, 35], [106, 35], [107, 35], [108, 35], 
					 [109, 35], [110, 35], [111, 35], [112, 35], [113, 35], [114, 35], [115, 35], 
					 [116, 35], [117, 35], [118, 35], [119, 35], [120, 35], [121, 35], [122, 35], 
					 [123, 35], [125, 35], [126, 35], [161, 35], [162, 35], [163, 35], [164, 35], 
					 [165, 35], [166, 35], [167, 35], [168, 35], [169, 35], [170, 35], [171, 35], 
					 [172, 35], [173, 35], [174, 35], [175, 35], [176, 35], [177, 35], [178, 35], 
					 [179, 35], [180, 35], [181, 35], [182, 35], [183, 35], [184, 35], [185, 35], 
					 [186, 35], [187, 35], [188, 35], [189, 35], [190, 35], [191, 35], [192, 35], 
					 [193, 35], [194, 35], [195, 35], [196, 35], [197, 35], [198, 35], [199, 35], 
					 [200, 35], [201, 35], [202, 35], [203, 35], [204, 35], [205, 35], [206, 35], 
					 [207, 35], [208, 35], [209, 35], [210, 35], [211, 35], [212, 35], [213, 35], 
					 [214, 35], [215, 35], [216, 35], [217, 35], [218, 35], [219, 35], [220, 35], 
					 [221, 35], [222, 35], [223, 35], [224, 35], [225, 35], [226, 35], [227, 35], 
					 [228, 35], [229, 35], [230, 35], [231, 35], [232, 35], [233, 35], [234, 35], 
					 [235, 35], [236, 35], [237, 35], [238, 35], [239, 35], [240, 35], [241, 35], 
					 [242, 35], [243, 35], [244, 35], [245, 35], [246, 35], [247, 35], [248, 35], 
					 [249, 35], [250, 35], [251, 35], [252, 35], [253, 35], [254, 35], [255, 35], 
					 [48, 36], [49, 36], [50, 36], [51, 36], [52, 36], [53, 36], [54, 36], [55, 36], 
					 [56, 36], [57, 36], [48, 32], [49, 32], [50, 32], [51, 32], [52, 32], [53, 32], 
					 [54, 32], [55, 32], [56, 32], [57, 32], [65, 21], [66, 21], [67, 21], [68, 21], 
					 [69, 21], [70, 21], [71, 21], [72, 21], [73, 21], [74, 21], [75, 21], [76, 21], 
					 [77, 21], [78, 21], [79, 21], [80, 21], [81, 21], [82, 21], [83, 21], [84, 21], 
					 [85, 21], [86, 21], [87, 21], [88, 21], [89, 21], [90, 21], [95, 32], [97, 32], 
					 [98, 32], [99, 32], [100, 32], [101, 32], [102, 32], [103, 32], [104, 32], 
					 [105, 32], [106, 32], [107, 32], [108, 32], [109, 32], [110, 32], [111, 32], 
					 [112, 32], [113, 32], [114, 32], [115, 32], [116, 32], [117, 32], [118, 32], 
					 [119, 32], [120, 32], [121, 32], [122, 32], [48, 37], [49, 37], [50, 37], [51, 37], 
					 [52, 37], [53, 37], [54, 37], [55, 37], [56, 37], [57, 37], [95, 37], [97, 37], 
					 [98, 37], [99, 37], [100, 37], [101, 37], [102, 37], [103, 37], [104, 37], 
					 [105, 37], [106, 37], [107, 37], [108, 37], [109, 37], [110, 37], [111, 37], 
					 [112, 37], [113, 37], [114, 37], [115, 37], [116, 37], [117, 37], [118, 37], 
					 [119, 37], [120, 37], [121, 37], [122, 37], [9, 35], [10, 35], [13, 35], [32, 35], 
					 [33, 35], [34, 35], [35, 38], [36, 35], [37, 35], [38, 35], [39, 35], [40, 35], 
					 [41, 35], [42, 35], [43, 35], [44, 35], [45, 35], [46, 35], [47, 35], [48, 35], 
					 [49, 35], [50, 35], [51, 35], [52, 35], [53, 35], [54, 35], [55, 35], [56, 35], 
					 [57, 35], [58, 35], [59, 35], [60, 35], [61, 35], [62, 35], [63, 35], [64, 35], 
					 [65, 35], [66, 35], [67, 35], [68, 35], [69, 35], [70, 35], [71, 35], [72, 35], 
					 [73, 35], [74, 35], [75, 35], [76, 35], [77, 35], [78, 35], [79, 35], [80, 35], 
					 [81, 35], [82, 35], [83, 35], [84, 35], [85, 35], [86, 35], [87, 35], [88, 35], 
					 [89, 35], [90, 35], [91, 35], [92, 35], [93, 35], [94, 35], [95, 35], [96, 35],
					 [97, 35], [98, 35], [99, 35], [100, 35], [101, 35], [102, 35], [103, 35], [104, 35], 
					 [105, 35], [106, 35], [107, 35], [108, 35], [109, 35], [110, 35], [111, 35], [112, 35], 
					 [113, 35], [114, 35], [115, 35], [116, 35], [117, 35], [118, 35], [119, 35], [120, 35], 
					 [121, 35], [122, 35], [123, 35], [124, 39], [125, 35], [126, 35], [161, 35], [162, 35], 
					 [163, 35], [164, 35], [165, 35], [166, 35], [167, 35], [168, 35], [169, 35], [170, 35], 
					 [171, 35], [172, 35], [173, 35], [174, 35], [175, 35], [176, 35], [177, 35], [178, 35], 
					 [179, 35], [180, 35], [181, 35], [182, 35], [183, 35], [184, 35], [185, 35], [186, 35], 
					 [187, 35], [188, 35], [189, 35], [190, 35], [191, 35], [192, 35], [193, 35], [194, 35], 
					 [195, 35], [196, 35], [197, 35], [198, 35], [199, 35], [200, 35], [201, 35], [202, 35], 
					 [203, 35], [204, 35], [205, 35], [206, 35], [207, 35], [208, 35], [209, 35], [210, 35], 
					 [211, 35], [212, 35], [213, 35], [214, 35], [215, 35], [216, 35], [217, 35], [218, 35], 
					 [219, 35], [220, 35], [221, 35], [222, 35], [223, 35], [224, 35], [225, 35], [226, 35], 
					 [227, 35], [228, 35], [229, 35], [230, 35], [231, 35], [232, 35], [233, 35], [234, 35], 
					 [235, 35], [236, 35], [237, 35], [238, 35], [239, 35], [240, 35], [241, 35], [242, 35], 
					 [243, 35], [244, 35], [245, 35], [246, 35], [247, 35], [248, 35], [249, 35], [250, 35], 
					 [251, 35], [252, 35], [253, 35], [254, 35], [255, 35], [48, 40], [49, 36], [50, 36], 
					 [51, 36], [52, 36], [53, 36], [54, 36], [55, 36], [56, 36], [57, 36], [48, 37], [49, 37], 
					 [50, 37], [51, 37], [52, 37], [53, 37], [54, 37], [55, 37], [56, 37], [57, 37], [65, 34], 
					 [66, 34], [67, 34], [68, 34], [69, 34], [70, 34], [71, 34], [72, 34], [73, 34], [74, 34], 
					 [75, 34], [76, 34], [77, 34], [78, 34], [79, 34], [80, 34], [81, 34], [82, 34], [83, 34], 
					 [84, 34], [85, 34], [86, 34], [87, 34], [88, 34], [89, 34], [90, 34], [95, 37], [97, 37], 
					 [98, 37], [99, 37], [100, 37], [101, 37], [102, 37], [103, 37], [104, 37], [105, 37], 
					 [106, 37], [107, 37], [108, 37], [109, 37], [110, 37], [111, 37], [112, 37], [113, 37], 
					 [114, 37], [115, 37], [116, 37], [117, 37], [118, 37], [119, 37], [120, 37], [121, 37], 
					 [122, 37], [9, 35], [10, 35], [13, 35], [32, 35], [33, 35], [34, 35], [35, 38], [36, 35], 
					 [37, 35], [38, 35], [39, 35], [40, 35], [41, 35], [42, 35], [43, 35], [44, 35], [45, 35],
					 [46, 35], [47, 35], [48, 35], [49, 35], [50, 35], [51, 35], [52, 35], [53, 35], [54, 35], 
					 [55, 35], [56, 35], [57, 35], [58, 35], [59, 35], [60, 35], [61, 35], [62, 35], [63, 35], 
					 [64, 35], [65, 35], [66, 35], [67, 35], [68, 35], [69, 35], [70, 35], [71, 35], [72, 35], 
					 [73, 35], [74, 35], [75, 35], [76, 35], [77, 35], [78, 35], [79, 35], [80, 35], [81, 35], 
					 [82, 35], [83, 35], [84, 35], [85, 35], [86, 35], [87, 35], [88, 35], [89, 35], [90, 35], 
					 [91, 35], [92, 35], [93, 35], [94, 35], [95, 35], [96, 35], [97, 35], [98, 35], [99, 35], 
					 [100, 35], [101, 35], [102, 35], [103, 35], [104, 35], [105, 35], [106, 35], [107, 35], 
					 [108, 35], [109, 35], [110, 35], [111, 35], [112, 35], [113, 35], [114, 35], [115, 35], 
					 [116, 35], [117, 35], [118, 35], [119, 35], [120, 35], [121, 35], [122, 35], [123, 35], 
					 [125, 35], [126, 35], [161, 35], [162, 35], [163, 35], [164, 35], [165, 35], [166, 35], 
					 [167, 35], [168, 35], [169, 35], [170, 35], [171, 35], [172, 35], [173, 35], [174, 35], 
					 [175, 35], [176, 35], [177, 35], [178, 35], [179, 35], [180, 35], [181, 35], [182, 35], 
					 [183, 35], [184, 35], [185, 35], [186, 35], [187, 35], [188, 35], [189, 35], [190, 35], 
					 [191, 35], [192, 35], [193, 35], [194, 35], [195, 35], [196, 35], [197, 35], [198, 35], 
					 [199, 35], [200, 35], [201, 35], [202, 35], [203, 35], [204, 35], [205, 35], [206, 35], 
					 [207, 35], [208, 35], [209, 35], [210, 35], [211, 35], [212, 35], [213, 35], [214, 35], 
					 [215, 35], [216, 35], [217, 35], [218, 35], [219, 35], [220, 35], [221, 35], [222, 35], 
					 [223, 35], [224, 35], [225, 35], [226, 35], [227, 35], [228, 35], [229, 35], [230, 35], 
					 [231, 35], [232, 35], [233, 35], [234, 35], [235, 35], [236, 35], [237, 35], [238, 35], 
					 [239, 35], [240, 35], [241, 35], [242, 35], [243, 35], [244, 35], [245, 35], [246, 35], 
					 [247, 35], [248, 35], [249, 35], [250, 35], [251, 35], [252, 35], [253, 35], [254, 35], 
					 [255, 35], [9, 35], [10, 35], [13, 35], [32, 35], [33, 35], [34, 35], [35, 41], [36, 35], 
					 [37, 35], [38, 35], [39, 35], [40, 35], [41, 35], [42, 35], [43, 35], [44, 35], [45, 35], 
					 [46, 35], [47, 35], [48, 35], [49, 35], [50, 35], [51, 35], [52, 35], [53, 35], [54, 35], 
					 [55, 35], [56, 35], [57, 35], [58, 35], [59, 35], [60, 35], [61, 35], [62, 35], [63, 35], 
					 [64, 35], [65, 35], [66, 35], [67, 35], [68, 35], [69, 35], [70, 35], [71, 35], [72, 35], 
					 [73, 35], [74, 35], [75, 35], [76, 35], [77, 35], [78, 35], [79, 35], [80, 35], [81, 35], 
					 [82, 35], [83, 35], [84, 35], [85, 35], [86, 35], [87, 35], [88, 35], [89, 35], [90, 35], 
					 [91, 35], [92, 35], [93, 35], [94, 35], [95, 35], [96, 35], [97, 35], [98, 35], [99, 35], 
					 [100, 35], [101, 35], [102, 35], [103, 35], [104, 35], [105, 35], [106, 35], [107, 35], 
					 [108, 35], [109, 35], [110, 35], [111, 35], [112, 35], [113, 35], [114, 35], [115, 35], 
					 [116, 35], [117, 35], [118, 35], [119, 35], [120, 35], [121, 35], [122, 35], [123, 35], 
					 [125, 35], [126, 35], [161, 35], [162, 35], [163, 35], [164, 35], [165, 35], [166, 35], 
					 [167, 35], [168, 35], [169, 35], [170, 35], [171, 35], [172, 35], [173, 35], [174, 35], 
					 [175, 35], [176, 35], [177, 35], [178, 35], [179, 35], [180, 35], [181, 35], [182, 35], 
					 [183, 35], [184, 35], [185, 35], [186, 35], [187, 35], [188, 35], [189, 35], [190, 35], 
					 [191, 35], [192, 35], [193, 35], [194, 35], [195, 35], [196, 35], [197, 35], [198, 35],
					 [199, 35], [200, 35], [201, 35], [202, 35], [203, 35], [204, 35], [205, 35], [206, 35], 
					 [207, 35], [208, 35], [209, 35], [210, 35], [211, 35], [212, 35], [213, 35], [214, 35], 
					 [215, 35], [216, 35], [217, 35], [218, 35], [219, 35], [220, 35], [221, 35], [222, 35], 
					 [223, 35], [224, 35], [225, 35], [226, 35], [227, 35], [228, 35], [229, 35], [230, 35], 
					 [231, 35], [232, 35], [233, 35], [234, 35], [235, 35], [236, 35], [237, 35], [238, 35], 
					 [239, 35], [240, 35], [241, 35], [242, 35], [243, 35], [244, 35], [245, 35], [246, 35], 
					 [247, 35], [248, 35], [249, 35], [250, 35], [251, 35], [252, 35], [253, 35], [254, 35], 
					 [255, 35], [48, 40], [49, 36], [50, 36], [51, 36], [52, 36], [53, 36], [54, 36], [55, 36], 
					 [56, 36], [57, 36] ]

