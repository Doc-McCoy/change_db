import os, re
from tkinter import filedialog

def saveConfig():

	pathV1 = filedialog.askopenfilename(title="Selecione o arquvo config.ini do V1")
	pathV2 = filedialog.askopenfilename(title="Selecione o arquvo config.ini do V2")

	if pathV1 and pathV2:

		fileSave = open("config.txt", "w")
		fileSave.write(pathV1 + "\n")
		fileSave.write(pathV2 + "\n")
		fileSave.close()

		return {"V1" : pathV1, "V2" : pathV2}

	else:
		print("Informe os caminhos de ambos os sistemas.")

		return False

def loadConfig():

	file = open("config.txt", "r")
	pathV1 = file.readline().rstrip() # rstrip para tirar o "\n" do final da string
	pathV2 = file.readline().rstrip() # rstrip para tirar o "\n" do final da string
	file.close()

	return {"V1" : pathV1, "V2" : pathV2}

def replace(paths):
	# Função que faz a substituição das linhas nos arquivos.

	banco = input("Digite o nome do banco que deseja alterar:\ngpd_")

	# Carregar os config.ini do V1 e V2
	configV1 = open(paths["V1"], "r", encoding="ISO8859-1")
	configV2 = open(paths["V2"], "r", encoding="ISO8859-1")
	
	# Ler os config.ini
	conteudoV1 = configV1.readlines()
	conteudoV2 = configV2.readlines()

	# Fechar os arquivos
	configV1.close()
	configV2.close()

	# Abrir novamente os configs, sobreescrevendo-os
	novoConfigV1 = open(paths["V1"], "w", encoding="ISO8859-1")
	novoConfigV2 = open(paths["V2"], "w", encoding="ISO8859-1")

	# Novos conteudos de ambos os configs
	novoConteudoV1 = []
	novoConteudoV2 = []

	# Procurar e fazer a substituicao no V1
	for linha in conteudoV1:
		# print(linha, end="") # end="" faz com que nao pule uma linha no print
		resultado = re.match("^db=g", linha)
		if resultado:
			novoConteudoV1.append("db=gpd_{};\n".format(banco))
		else:
			novoConteudoV1.append(linha)

	# Procurar e fazer a substituicao no V2
	for linha in conteudoV2:
		# print(linha, end="") # end="" faz com que nao pule uma linha no print
		resultado = re.match("^db=g", linha)
		if resultado:
			novoConteudoV2.append("db=gpd_{};\n".format(banco))
		else:
			novoConteudoV2.append(linha)

	# Escreve o novo conteudo gerado nos config.ini abertos
	novoConfigV1.writelines(novoConteudoV1)
	novoConfigV2.writelines(novoConteudoV2)

	# Fecha os arquivos
	novoConfigV1.close()
	novoConfigV2.close()

def main():

	# If ternario maroto do python, feio pra cacete
	# Criar o config caso esse não exista ainda, ou ler ele caso ja exista
	paths = loadConfig() if os.path.isfile("config.txt") else saveConfig()

	# Fazer a substituicao
	replace(paths)

# Roda a porra toda
if __name__ == '__main__':
	main()