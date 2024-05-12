import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "4")
    output_folder = os.path.join("soluzioni", "output", "4")

    @staticmethod
    def solve(wall: list[list[int]]) -> int:
        """
        Scrivi la tua soluzione qui.

        :param wall: griglia che rappresenta le macchie di muffa sul muro
        """
        max_area = 0  # Inizializza l'area massima a 0

        # Funzione per eseguire una DFS e trovare l'area di 1 contigua
        def DFS(r, c):
            # Verifica i limiti della griglia e se il valore è 0 o già visitato
            if r < 0 or r >= len(wall) or c < 0 or c >= len(wall[0]) or wall[r][c] == 0:
                return 0
            # Imposta il punto corrente a 0 per segnalarlo come visitato
            wall[r][c] = 0
            # Calcola l'area corrente e somma le aree adiacenti
            area = 1 + DFS(r+1, c) + DFS(r-1, c) + DFS(r, c+1) + DFS(r, c-1)
            return area

        # Scansiona la griglia per trovare l'area massima
        for r in range(len(wall)):
            for c in range(len(wall[0])):
                # Se il punto corrente è 1, esegui una DFS per trovare l'area adiacente
                if wall[r][c] == 1:
                    max_area = max(max_area, DFS(r, c))

        return max_area

    @staticmethod
    def load_input(i: int) -> list[list[int]]:
        """
        Carica il file di input i-esimo, contenuto all'interno della cartella dei file input.
        Questo metodo deve restituire il valore da passare al metodo solve.
        """

        # list dei file presenti nella cartella input
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            lines = f.readlines()
            return [list(map(int, line.strip().split())) for line in lines]

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

