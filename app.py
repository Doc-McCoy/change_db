import os, re
from tkinter import *
from tkinter import filedialog, messagebox

class App:

    def __init__(self, root):

        self.pathV1 = str()
        self.pathV2 = str()
        
        root.title("Change Batabase")
        root.resizable(0, 0)

        self.base = Frame(root)
        self.base.pack()
        # Botões de configuração
        # Botão do v1
        self.setV1 = Button(
            self.base,
            text="Configurar caminho V1",
            command=lambda:self.setPath(1),
            width=50,
        )
        self.setV1.pack()
        # Botão do v2
        self.setV2 = Button(
            self.base,
            text="Configurar caminho V2",
            command=lambda:self.setPath(2),
            width=50,
        )
        self.setV2.pack()
        # Botão salvar
        self.save = Button(
            self.base,
            text="Salvar",
            command=self.savePathInFile,
            width=50,
        )
        self.save.pack()

    def setPath(self, v):
        ''' Define a variável de path do v1 e do v2. '''
        if v == 1:
            self.pathV1 = filedialog.askopenfilename(title="Selecione o arquvo config.ini do V1")
        elif v == 2:
            self.pathV2 = filedialog.askopenfilename(title="Selecione o arquvo config.ini do V2")

    def savePathInFile(self):
        ''' Salva os paths em um arquivo. '''
        if self.pathV1 and self.pathV2:
            filePath = open("path", "w")
            for path in content:
                filePath.write(path + '\n')
            filePath.close()
        else:
            messagebox.showinfo("Atenção", "Ambos os paths precisam estar setados para salvar.")
            return False
        self.reloadButtons()

    def reloadButtons(self):
        ''' Recarrega a interface gráfica. '''
        pass

def main():
    root = Tk()
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()