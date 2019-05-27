from Lexico import Lexico
from Token import Token
from LexicalError import LexicalError
import sys
sys.stdout.reconfigure(encoding='utf-8')

code = sys.argv[1]

try:
	lexico = Lexico(str(code))
	token = lexico.nextToken()
	maxLine = 0
	out = str("Linha".ljust(8) + "Classe".ljust(20) + "Lexeme" + "\n")

	while token is not None:
		if(token.classLexeme is not None):
			if len(str(token.__repr__())) > maxLine:
				maxLine = len(str(token.__repr__()))

			out += str(token.__repr__() + "\n")
			
		token = lexico.nextToken()

	out += "\n" + "Programa compilado com sucesso!".center(maxLine)

	print(out)

except LexicalError as e:
	print(e.mensagem_error())


sys.stdout.flush()