# Importación de librerias
import subprocess

import tkinter as tk
from tkinter import filedialog, messagebox

from antlr4 import *
from MiLenguajeLexer import MiLenguajeLexer
from MiLenguajeParser import MiLenguajeParser

# Definir la clase MiLenguajeListener que actúa como un listener del árbol de análisis
class MiLenguajeListener(ParseTreeListener):
    def __init__(self, output_file):
        self.output_file = output_file
        self.translation = ""
        self.inside_if = False
        self.indentation_level = 0

    # Método llamado al entrar en un Statement
    def enterStatement(self, ctx: MiLenguajeParser.StatementContext):
        # Comprobación de IF = SI
        if ctx.IF() is not None:
            condition = ctx.condition().getText()
            self.translation += f"{'    ' * self.indentation_level}if {condition}:\n"
            self.indentation_level += 1

        # Comprobación de ELIF = SWITCH
        elif ctx.ELIF() is not None:
            condition = ctx.condition().getText()
            self.translation += f"{'    ' * (self.indentation_level - 1)}elif {condition}:\n"

        # Comprobación de ELSE = SINO
        elif ctx.ELSE() is not None:
            self.indentation_level -= 1
            self.translation += f"{'    ' * self.indentation_level}else:\n"
            self.indentation_level += 1

        # Comprobación de FOR = PARA
        elif ctx.FOR() is not None:
            variable = ctx.variable().getText()
            start = ctx.expression(0).getText()
            end = ctx.expression(1).getText()
            self.translation += f"{'    ' * self.indentation_level}for {variable} in range({start}, {end} + 1):\n"
            self.indentation_level += 1

        # Comprobación de WHILE = MIENTRAS
        elif ctx.WHILE() is not None:
            condition = ctx.condition().getText()
            self.translation += f"{'    ' * self.indentation_level}while {condition}:\n"
            self.indentation_level += 1

        # Comprobación si es una declaración de variable
        elif ctx.variableDeclaration() is not None:
            declaration = ctx.variableDeclaration()
            variable = declaration.LETTER()[0].getText()
            expression = declaration.expression()
            if expression is not None:
                expression_text = expression.getText()
                self.translation += f"{'    ' * self.indentation_level}{variable} = {expression_text}\n"
            else:
                self.translation += f"{'    ' * self.indentation_level}{variable} = \n"

        # Comprobación si es una asignación de variable
        elif ctx.assignment() is not None:
            assignment = ctx.assignment()
            variable = assignment.variable().getText()
            expression = assignment.expression().getText()
            self.translation += f"{'    ' * self.indentation_level}{variable} = {expression}\n"

    # Método llamado al salir de un Statement
    def exitStatement(self, ctx: MiLenguajeParser.StatementContext):
        # Comprobar si es un FOR o WHILE para reducir el nivel de indentación
        if ctx.FOR() is not None or ctx.WHILE() is not None:
            self.indentation_level -= 1

        # Comprobar si es un ELSE para reducir el nivel de indentacion y agregar una línea en blanco
        if ctx.ELSE() is not None:
            self.indentation_level -= 1
            self.translation += f"{'    ' * self.indentation_level}\n"

    # Método llamado al entrar en un Action
    def enterAction(self, ctx: MiLenguajeParser.ActionContext):
        # Comprobar si es un PRINT
        if ctx.PRINT() is not None:
            # Comprobar si hay una expresión asociada al PRINT
            if ctx.expression() is not None:
                expression = ctx.expression().getText()
                indentation = "    " * self.indentation_level
                if self.inside_if:
                    self.translation += f"{indentation}print({expression})\n"
                else:
                    self.translation += f"{indentation}print({expression})\n"
            # Comprobar si hay una expresión_print asociada al PRINT
            elif ctx.expression_print() is not None:
                expression = ctx.expression_print().getText()[1:-1]
                indentation = "    " * self.indentation_level
                if self.inside_if:
                    self.translation += f'{indentation}print("{expression}")\n'
                else:
                    self.translation += f'{indentation}print("{expression}")\n'

    # Método llamado al salir del Start
    def exitStart(self, ctx: MiLenguajeParser.StartContext):
        # Escribir la traducción en el archivo de salida
        with open(self.output_file, "w") as file:
            file.write(self.translation)

    # Función para verificar si la traducción y compilado del archivo se llevaron a cabo de manera correcta
    def translate_and_evaluate(self, input_text):
        input_stream = InputStream(input_text)
        lexer = MiLenguajeLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MiLenguajeParser(token_stream)
        tree = parser.start()

        if parser.getNumberOfSyntaxErrors() == 0:
            listener = MiLenguajeListener(self.output_file)
            walker = ParseTreeWalker()
            walker.walk(listener, tree)

            print("")
            print("Compilación exitosa el archivo se compiló correctamente.")
            print("")
            print("ParseTree")
            print(tree.toStringTree(recog=parser))
            print("")
            print(f"Traducción guardada en: {self.output_file}")
            messagebox.showinfo("Chomin Messagge", "El archivo se compiló correctamente.")

            # Abrir el archivo en cmd
            print("")
            print("Ejecución del código compilado: ")
            subprocess.Popen(['cmd', '/c', self.output_file], shell=True)

        else:
            print("")
            print("Error de compilación el archivo no se compiló correctamente.")
            messagebox.showinfo("Chomin Messagge", "El archivo no se compiló correctamente.")

# Función para seleccionar el archivo de entrada
def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        file_name = file_path.split("/")[-1]
        label.config(text="Nombre del archivo seleccionado: " + file_name)
        global input_text
        with open(file_path, "r") as file:
            input_text = file.read()

# Función para compilar el archivo seleccionado
def compile_file():
    output_file = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if output_file:
        listener = MiLenguajeListener(output_file)
        listener.translate_and_evaluate(input_text)

        # Mostrar el archivo .py compilado en la pantalla
        with open(output_file, "r") as file:
            compiled_code = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, compiled_code)

# Interfaz gráfica del compilador
root = tk.Tk()
root.title("ChominCompiler_py")
root.geometry("400x500")

# Titulo de la interfaz
labelTitle = tk.Label(root, text="Chomin Compiler - Python", font=("Arial", 20), fg="black")
labelTitle.pack(pady=20)

# Botón para seleccionar el archivo
select_button = tk.Button(root, text="Seleccionar archivo", font=("Arial", 12), command=select_file, fg="white", bg="gray")
select_button.pack()

# Botón para compilar el archivo
compile_button = tk.Button(root, text="Compilar", font=("Arial", 12), command=compile_file, fg="white", bg="green")
compile_button.pack(pady=10)

# Etiqueta para mostrar el nombre del archivo seleccionado
label = tk.Label(root, text=" ", font=("Arial", 10), fg="black")
label.pack(pady=20)

# Área de texto para mostrar el archivo .py compilado
text_area = tk.Text(root, width=60)
text_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()