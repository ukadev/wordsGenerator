import tkinter as tk
from tkinter import ttk, scrolledtext, Button


class Application:
    def main(self):
        window = tk.Tk()
        window.title("Generador de Palabras")
        window.geometry("830x570")
        window.resizable(False, False)

        tabControl = ttk.Notebook(window)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Parejas')
        tabControl.add(tab2, text='Gemelos')
        tabControl.add(tab3, text='Gemelos Únicos')
        tabControl.pack(expand=1, fill="both")

        # Title Label
        ttk.Label(tab1,
                  text="Introduce las palabras en el bloque izquierdo, una por línea, sin separar por comas ni ningún símbolo y luego pulsa el botón 'Crear Parejas'",
                  background='green', foreground="white").grid(column=1, row=1, columnspan=3, pady=10)

        # Words Textarea
        self.text_areaPairs = scrolledtext.ScrolledText(tab1, wrap=tk.WORD, width=40, height=30)
        self.text_areaPairs.grid(column=1, padx=10, pady=10, row=2, rowspan=2)
        self.text_areaPairs.focus()

        # Pairs Textarea result
        self.text_area_resultPairs = scrolledtext.ScrolledText(tab1, wrap=tk.WORD, width=40, height=30, state='disabled')
        self.text_area_resultPairs.grid(column=3, padx=25, row=2, rowspan=2)

        # Submit Button
        self.submitPairs = Button(tab1, text='Crear Parejas', command=self.executePairs)
        self.submitPairs.grid(column=2, row=2, pady=10)

        # Copy Button Pairs
        self.copyPairs = Button(tab1, text='Copiar Resultado', command=self.copyPairs)
        self.copyPairs.grid(column=2, row=3, pady=10)

        # Title Label
        ttk.Label(tab2,
                  text="Introduce las palabras en el bloque izquierdo, una por línea, sin separar por comas ni ningún símbolo y luego pulsa el botón 'Crear Gemelos'",
                  background='green', foreground="white").grid(column=1, row=1, columnspan=3, pady=10)

        # Words Textarea Twins
        self.text_areaTwins = scrolledtext.ScrolledText(tab2, wrap=tk.WORD, width=40, height=30)
        self.text_areaTwins.grid(column=1, padx=10, pady=10, row=2, rowspan=2)
        self.text_areaTwins.focus()

        # Pairs Textarea result
        self.text_area_resultTwins = scrolledtext.ScrolledText(tab2, wrap=tk.WORD, width=40, height=30, state='disabled')
        self.text_area_resultTwins.grid(column=3, padx=25, row=2, rowspan=2)

        # Submit Button
        self.submitTwins = Button(tab2, text='Crear gemelos', command=self.executeTwins)
        self.submitTwins.grid(column=2, row=2, pady=10)

        # Copy Button Twins
        self.copyTwins = Button(tab2, text='Copiar Resultado', command=self.copyTwins)
        self.copyTwins.grid(column=2, row=3, pady=10)

        # Title Label
        ttk.Label(tab3,
                  text="Introduce las palabras en el bloque izquierdo, una por línea, sin separar por comas ni ningún símbolo y luego pulsa el botón 'Crear Gemelos Únicos'",
                  background='green', foreground="white").grid(column=1, row=1, columnspan=3, pady=10)

        # Words Textarea Unique Twins
        self.text_areaUniqueTwins = scrolledtext.ScrolledText(tab3, wrap=tk.WORD, width=40, height=30)
        self.text_areaUniqueTwins.grid(column=1, padx=10, pady=10, row=2, rowspan=2)
        self.text_areaUniqueTwins.focus()

        # Unique twins Textarea result
        self.text_area_resultUniqueTwins = scrolledtext.ScrolledText(tab3, wrap=tk.WORD, width=40, height=30, state='disabled')
        self.text_area_resultUniqueTwins.grid(column=3, padx=25, row=2, rowspan=2)

        # Submit Unique Twins Button
        self.submitUniqueTwins = Button(tab3, text='Crear gemelos únicos', command=self.executeUniqueTwins)
        self.submitUniqueTwins.grid(column=2, row=2, pady=10)

        # Copy Button Twins
        self.copyUniqueTwins = Button(tab3, text='Copiar Resultado', command=self.copyUniqueTwins)
        self.copyUniqueTwins.grid(column=2, row=3, pady=10)

        tabControl.bind("<1>", self.clearTextAreas())

        window.mainloop()

    def executePairs(self):
        words = self.text_areaPairs.get("1.0", "end")
        wordsArray = list(filter(None, words.splitlines()))
        pairs = self.generatePairs(wordsArray)

        self.text_area_resultPairs.config(state="normal")
        self.text_area_resultPairs.delete('1.0', "end")
        self.text_area_resultPairs.insert("insert", pairs)
        self.text_area_resultPairs.config(state="disabled")

    def executeTwins(self):
        words = self.text_areaTwins.get("1.0", "end")
        wordsArray = list(filter(None, words.splitlines()))
        twins = self.generateTwins(wordsArray)

        self.text_area_resultTwins.config(state="normal")
        self.text_area_resultTwins.delete('1.0', "end")
        self.text_area_resultTwins.insert("insert", twins)
        self.text_area_resultTwins.config(state="disabled")

    def executeUniqueTwins(self):
        words = self.text_areaUniqueTwins.get("1.0", "end")
        wordsArray = list(filter(None, words.splitlines()))
        uniqueTwins = self.generateUniqueTwins(wordsArray)

        self.text_area_resultUniqueTwins.config(state="normal")
        self.text_area_resultUniqueTwins.delete('1.0', "end")
        self.text_area_resultUniqueTwins.insert("insert", uniqueTwins)
        self.text_area_resultUniqueTwins.config(state="disabled")


    def generatePairs(self, array):
        alreadyProcessed = []
        result = ""

        for first in array:
            for second in array:
                combination = [first, second]
                if(first == second):
                    continue
                result += first+":"+second+"\r\n"
                alreadyProcessed.append(combination)
        return result

    def generateTwins(self, array):
        result = ""

        for first in array:
            result += first+":"+first+"\r\n"
        return result


    def generateUniqueTwins(self, array):
        result = ""
        loaded = []
        for first in array:
            if first in loaded:
                continue
            result += first+":"+first+"\r\n"
            loaded.append(first)
        return result

    def clearTextAreas(self):
        self.text_area_resultTwins.config(state="normal")
        self.text_area_resultTwins.delete('1.0', "end")
        self.text_area_resultTwins.config(state="disabled")
        self.text_areaTwins.delete('1.0', "end")
        self.text_area_resultUniqueTwins.config(state="normal")
        self.text_area_resultUniqueTwins.delete('1.0', "end")
        self.text_area_resultUniqueTwins.config(state="disabled")
        self.text_areaTwins.delete('1.0', "end")
        self.text_area_resultPairs.config(state="normal")
        self.text_area_resultPairs.delete('1.0', "end")
        self.text_area_resultPairs.config(state="disabled")
        self.text_areaPairs.delete('1.0', "end")

    def copyPairs(self):
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.text_area_resultPairs.get("1.0", "end"))
        clip.destroy()

    def copyTwins(self):
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.text_area_resultTwins.get("1.0", "end"))
        clip.destroy()

    def copyUniqueTwins(self):
        clip = tk.Tk()
        clip.withdraw()
        clip.clipboard_clear()
        clip.clipboard_append(self.text_area_resultUniqueTwins.get("1.0", "end"))
        clip.destroy()

if __name__ == "__main__":
    app = Application()
    app.main()
