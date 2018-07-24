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

		return [pathV1, pathV2]

	else:
		print("Informe os caminhos de ambos os sistemas.")

		return False

def loadConfig():

	file = open("config.txt", "r")
	pathV1 = file.readline().rstrip() # rstrip para tirar o "\n" do final da string
	pathV2 = file.readline().rstrip() # rstrip para tirar o "\n" do final da string
	file.close()

	return [pathV1, pathV2]

def replace(paths, banco):

	conteudos = []
	novosConfigs  =[]
	
	# Carregar os config.ini do V1 e V2
	for file in paths:
		config = open(file, "r", encoding="ISO8859-1")
		conteudos.append(config.readlines())
		config.close()
		# Abrir novamente os configs para serem sobreescritos
		novosConfigs.append(open(file, "w", encoding="ISO8859-1"))

	indice = 0

	for conteudo in conteudos:
		novoConteudo = []
		for linha in conteudo:
			resultado = re.match("^db=g", linha)
			if resultado:
				novoConteudo.append("db=gpd_{};\n".format(banco))
			else:
				novoConteudo.append(linha)
		# Escreve o novo conteudo gerado nos config.ini abertos
		novosConfigs[indice].writelines(novoConteudo)
		# Fecha os arquivos
		novosConfigs[indice].close()
		indice += 1

def main():

	# If ternario maroto do python, feio pra cacete
	# Criar o config caso esse não exista ainda, ou ler ele caso ja exista
	paths = loadConfig() if os.path.isfile("config.txt") else saveConfig()

	banco = input("Digite o nome do banco que deseja alterar:\ngpd_")

	# Fazer a substituicao
	replace(paths, banco)

# Roda a porra toda
if __name__ == '__main__':
	main()