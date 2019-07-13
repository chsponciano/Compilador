from SemanticError import SemanticError
from Constants import Constants
from ConstantsType import ConstantsType
from Stack import Stack


class Semantic(Constants):

    def __init__(self):
        self._stack = Stack()
        self._labels = Stack()
        self._counter_labels = 0
        self._code_out = ''
        self._operator = None
        self._type_var = None
        self._ts = dict()
        self._list_id = []
        self._actions = {
            1: self.action01,
            2: self.action02,
            3: self.action03,
            4: self.action04,
            5: self.action05,
            6: self.action06,
            7: self.action07,
            8: self.action08,
            9: self.action09,
            10: self.action10,
            11: self.action11,
            12: self.action12,
            13: self.action13,
            14: self.action14,
            15: self.action15,
            16: self.action16,
            17: self.action17,
            18: self.action18,
            19: self.action19,
            20: self.action20,
            21: self.action21,
            30: self.action30,
            31: self.action31,
            32: self.action32,
            33: self.action33,
            34: self.action34,
            35: self.action35,
            36: self.action36,
            37: self.action37,
            38: self.action38,
            39: self.action39,
            40: self.action40,
            41: self.action41,
            42: self.action42
        }

    def get_code_out(self):
        return self._code_out

    def execute_action(self, action, token, line):
        self._actions[action](token, line)

    def arithmetic_validation(self, is_div, line):
        l_type = [self._stack.pop(), self._stack.pop()]

        if any(value in ConstantsType.list_not_number64 for value in l_type):
            raise SemanticError('Tipos incompatíveis em expressão aritmética', line)

        if is_div:
            if l_type[0] == l_type[1]:
                self._stack.push(l_type[0])
        else:
            self._stack.push(
                ConstantsType.c_float64 if ConstantsType.c_float64 in l_type else ConstantsType.c_int64)

    def numerical_type_validation(self, v_type, line):
        if v_type in ConstantsType.list_not_number64:
            raise SemanticError('Tipos incompatíveis em expressão aritmética', line)
        self._stack.push(v_type)

    def next_label(self):
        self._counter_labels += 1
        return 'label' + str(self._counter_labels)

    def action01(self, token, line):
        self.arithmetic_validation(False, line)
        self._code_out += '     add\n'

    def action02(self, token, line):
        self.arithmetic_validation(False, line)
        self._code_out += '     sub\n'

    def action03(self, token, line):
        self.arithmetic_validation(False, line)
        self._code_out += '     mul\n'

    def action04(self, token, line):
        self.arithmetic_validation(True, line)
        self._code_out += '     div\n'

    def action05(self, token, line):
        self._code_out += '     ldc.i8 ' + token.lexeme + '\n'
        self._code_out += '     conv.r8\n'
        self._stack.push(ConstantsType.c_int64)

    def action06(self, token, line):
        self._stack.push(ConstantsType.c_float64)
        self._code_out += '     ldc.r8 ' + token.lexeme + '\n'

    def action07(self, token, line):
        v_type = self._stack.pop()
        self.numerical_type_validation(v_type, line)

    def action08(self, token, line):
        v_type = self._stack.pop()
        self.numerical_type_validation(v_type, line)
        self._code_out += '     ldc.i8 -1\n'

        if v_type == ConstantsType.c_int64:
            self._code_out += '     conv.r8\n'

        self._code_out += '     mul\n'

    def action09(self, token, line):
        self._operator = token.lexeme

    def action10(self, token, line):
        v_type_one = self._stack.pop()
        v_type_two = self._stack.pop()

        if v_type_one != v_type_two:
            raise SemanticError('Tipos incompatíveis em expressão aritmética', line)

        self._stack.push(ConstantsType.c_bool)

        if self._operator == '>':
            self._code_out += '     cgt\n'
        elif self._operator == '<':
            self._code_out += '     clt\n'
        elif self._operator in ['=', '==']:
            self._code_out += '     ceq\n'
        elif self._operator == '!=':
            self._code_out += '     ceq\nldc.i4 0\nceq\n'
        elif self._operator == '<=':
            self._code_out += '     clt\nldc.i4 0\nceq\n'
        elif self._operator == '>=':
            self._code_out += '     cgt\nldc.i4 0\nceq\n'

    def action11(self, tokne, line):
        self._stack.push(ConstantsType.c_bool)
        self._code_out += '     ldc.i4.1\n'

    def action12(self, tokne, line):
        self._stack.push(ConstantsType.c_bool)
        self._code_out += '     ldc.i4.0\n'

    def action13(self, tokne, line):
        v_type = self._stack.pop()

        if v_type != ConstantsType.c_bool:
            raise SemanticError('Tipos incompatíveis em expressão lógica', line)

        self._stack.push(v_type)
        self._code_out += '     ldc.i4.1\n'
        self._code_out += '     xor\n'

    def action14(self, token, line):
        v_type = self._stack.pop()
        if v_type == ConstantsType.c_int64:
            self._code_out += '     conv.i8\n'

        self._code_out += '     call void [mscorlib]System.Console::Write(' + \
            v_type + ')\n'

    def action15(self, token, line):
        self._code_out += '.assembly extern mscorlib {}\n'
        self._code_out += '.assembly _codigo_objeto{}\n'
        self._code_out += '.module   _codigo_objeto.exe\n'
        self._code_out += '\n.class public _UNICA {\n'

    def action16(self, token, line):
        self._code_out += '.method static public void _principal() {\n'
        self._code_out += '     .entrypoint\n'

    def action17(self, token, line):
        self._code_out += '     ret\n'
        self._code_out += '     }\n'
        self._code_out += '}'

    def action18(self, token, line):
        v_type = self._stack.pop()

        if v_type != ConstantsType.c_bool:
            raise SemanticError('Tipos incompatíveis em expressão lógica', line)

        self._stack.push(v_type)
        self._code_out += '     ldc.i4.1\n'
        self._code_out += '     and\n'

    def action19(self, token, line):
        v_type = self._stack.pop()

        if v_type != ConstantsType.c_bool:
            raise SemanticError('Tipos incompatíveis em expressão lógica', line)

        self._stack.push(v_type)
        self._code_out += '     ldc.i4.1\n'
        self._code_out += '     or\n'

    def action20(self, token, line):
        self._code_out += '     ldstr "' + token.lexeme + '"\n'
        self._stack.push(ConstantsType.c_string)

    def action21(self, token, line):
        self._code_out += '     ldstr ' + token.lexeme + '\n'
        self._stack.push(ConstantsType.c_string)

    def action30(self, token, line):
        if token.lexeme == 'int':
            self._type_var = ConstantsType.c_int64
        elif token.lexeme == 'float':
            self._type_var = ConstantsType.c_float64

    def action31(self, token, line):
        l_locals = []
        for idx in self._list_id:

            if self._ts.get(idx) is not None:
                raise SemanticError(f'{idx} já declarado', line)

            self._ts[idx] = self._type_var
            l_locals.append(self._type_var + ' ' + idx)
        
        self._code_out += '     .locals(' + ', '.join(l_locals) + ')\n'
            
        self._list_id.clear()

    def action32(self, token, line):
        self._list_id.append(token.lexeme)

    def action33(self, token, line):
        idx = token.lexeme
        if self._ts.get(idx) is None:
            raise SemanticError(f'{idx} não declarado', line)
        
        type_idx = self._ts.get(idx)

        self._code_out += '     ldloc ' + idx + '\n'
        if type_idx == ConstantsType.c_int64:
            self._code_out += '     conv.r8\n'

        self._stack.push(type_idx)

    def action34(self, token, line):
        idx = self._list_id.pop(-1)

        if self._ts.get(idx) is None:
            raise SemanticError(f'{idx} não declarado', line)
        
        type_idx = self._ts.get(idx)
        type_exp = self._stack.pop()

        if type_idx != type_exp:
            raise SemanticError('Tipos incompatíveis em expressão aritmética', line)

        if self._operator == '=':
            if type_idx == ConstantsType.c_int64:
                self._code_out += '     conv.i8\n'
            self._code_out += '     stloc ' + idx + '\n'
        else:
            if self._operator == '+=':
                self._code_out += '     add\n'
            elif self._operator == '-=':
                self._code_out += '     sub\n'

            if type_idx == ConstantsType.c_int64:
                self._code_out += '     conv.i8\n'
            self._code_out += '     stloc ' + idx + '\n'

    def action35(self, token, line):
        for idx in self._list_id:

            if self._ts.get(idx) is None:
                raise SemanticError(f'{idx} não declarado', line)

            type_idx = self._ts.get(idx)
            class_idx = None

            if type_idx == ConstantsType.c_int64:
                class_idx = 'Int64'
            elif type_idx == ConstantsType.c_float64:
                class_idx = 'Double'

            self._code_out += '     call string [mscorlib]System.Console::ReadLine()\n'
            self._code_out += '     call ' + type_idx + \
                              ' [mscorlib]System.' + class_idx + '::Parse(string)\n'
            self._code_out += '     stloc ' + idx + '\n'

        self._list_id.clear()

    def action36(self, token, line):
        self._operator = token.lexeme  

        if self._operator in ['+=', '-=']:
            idx = self._list_id.pop(-1)
            type_idx = self._ts.get(idx)
            self._code_out += '     ldloc ' + idx + '\n'
            
            if type_idx == ConstantsType.c_int64:
                self._code_out += '     conv.r8\n'   
            
            self._list_id.append(idx)

    def action37(self, token, line):
        labels = self.next_label()
        self._labels.push(labels)
        self._code_out += '     ' + labels + ':\n'

    def action38(self, token, line):
        labels = self.next_label()
        self._labels.push(labels)
        self._code_out += '     brfalse ' + labels + '\n'

    def action39(self, token, line):
        labels = self._labels.pop()
        self._code_out += '     ' + labels + ':\n'        

    def action40(self, token, line):
        labels_br = self.next_label()
        self._code_out += '     br ' + labels_br + '\n'

        labels = self._labels.pop()
        self._code_out += '     ' + labels + ':\n'
        
        self._labels.push(labels_br)
        
    def action41(self, token, line):
        labels = self.next_label()
        self._code_out += ('     brfalse ' if token.lexeme != 'whileFalseDo' else '     brtrue ') + labels + '\n'
        self._labels.push(labels)

    def action42(self, token, line):
        label_br = self._labels.pop()
        label = self._labels.pop()
    
        self._code_out += '     br ' + label + '\n'
        self._code_out += '     ' + label_br + ':\n'