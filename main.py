import tkinter as tk
from tkinter import ttk, scrolledtext, Button


class Application:
    def main(self):
        window = tk.Tk()
        window.title("Generador de Palabras")
        window.geometry("810x570")
        window.resizable(False, False)

        tabControl = ttk.Notebook(window)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)

        tabControl.add(tab1, text='Parejas')
        tabControl.add(tab2, text='Duplicados')
        tabControl.pack(expand=1, fill="both")

        # Title Label
        ttk.Label(tab1,
                  text="Introduce las palabras en el bloque izquierdo, una por línea, sin separar por comas ni ningún símbolo y luego pulsa el botón 'Crear Parejas'",
                  background='green', foreground="white").grid(column=1, row=1, columnspan=3, pady=10)

        # Words Textarea
        self.text_areaPairs = scrolledtext.ScrolledText(tab1, wrap=tk.WORD, width=40, height=30)
        self.text_areaPairs.grid(column=1, padx=10, pady=10, row=2)
        self.text_areaPairs.focus()

        # Pairs Textarea result
        self.text_area_resultPairs = scrolledtext.ScrolledText(tab1, wrap=tk.WORD, width=40, height=30, state='disabled')
        self.text_area_resultPairs.grid(column=3, padx=25, row=2)

        # Submit Button
        self.submitPairs = Button(tab1, text='Crear Parejas', command=self.executePairs)
        self.submitPairs.grid(column=2, row=2, pady=10)

        # Title Label
        ttk.Label(tab2,
                  text="Introduce las palabras en el bloque izquierdo, una por línea, sin separar por comas ni ningún símbolo y luego pulsa el botón 'Crear Gemelos'",
                  background='green', foreground="white").grid(column=1, row=1, columnspan=3, pady=10)
        # Words Textarea Twins
        self.text_areaTwins = scrolledtext.ScrolledText(tab2, wrap=tk.WORD, width=40, height=30)
        self.text_areaTwins.grid(column=1, padx=10, pady=10, row=2)
        self.text_areaTwins.focus()

        # Pairs Textarea result
        self.text_area_resultTwins = scrolledtext.ScrolledText(tab2, wrap=tk.WORD, width=40, height=30, state='disabled')
        self.text_area_resultTwins.grid(column=3, padx=25, row=2)

        # Submit Button
        self.submitTwins = Button(tab2, text='Crear gemelos', command=self.executeTwins)
        self.submitTwins.grid(column=2, row=2, pady=10)


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
        alreadyProcessed = []
        result = ""

        for first in array:
            result += first+":"+first+"\r\n"
        return result


if __name__ == "__main__":
    app = Application()
    app.main()
