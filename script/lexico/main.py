from Lexico import Lexico
from Token import Token
from LexicalError import LexicalError


try:
	l = Lexico("@")
	t = l.nextToken()
	print("Linha	Classe				Lexeme")
	while t is not None:
		if(t.classLexeme == -1):
			continue

		print(t)
		t = l.nextToken()

except LexicalError as e:
	print(e.mensagem_error())