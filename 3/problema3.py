import os

class Solution:

    input_folder = os.path.join("soluzioni", "input", "3")
    output_folder = os.path.join("soluzioni", "output", "3")

    @staticmethod
    def solve(blueprint: list[str]) -> int:
        """
        Scrivi la tua soluzione qui.

        :param blueprint: blueprint
        """

        piastrella = "."
        limitatori = ["╗", "╔", "╝", "╚", "║", "═"]
        counter = 0
        
        lunghezzablueprint = len(blueprint)
        coun = 0
        for linea in blueprint:
        
            if(coun == lunghezzablueprint-1):
                break
            
            start = False
            lunghezza = len(linea)


            for i in range(0,lunghezza-1):
            
            

                if(linea[i] in limitatori and linea[i+1] in limitatori and not start):
                    i += 2
                    continue
                
                
                elif(linea[i] in limitatori and linea[i+1] in limitatori and start):
                    start = False

                else: 
                    if(linea[i] == piastrella and not start):
                        continue
                    
                    if(linea[i] in limitatori and not start):
                    
                    
                        #controllo se nei prossimi caratteri ci sono limitator
                        muro = False
                        for j in range(i+1, lunghezza):
                            if(linea[j] in limitatori):
                            

                                muro = True
                                break
                            
                        if(muro):
                            start = True
                    elif(linea[i] in limitatori and start):
                        start = False
                        continue
                    
                    
                    elif(linea[i] == piastrella and start):
                        counter += 1

            coun += 1

        return counter


                

                

    @staticmethod
    def load_input(i: int) -> list[str]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """

        # list dei file presenti nella cartella input
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            return [line.strip() for line in f.readlines()]

    @staticmethod
    def load_output(i: int) -> int:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.output_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.output_folder, files[i]), "r") as f:
            return int(f.read())
