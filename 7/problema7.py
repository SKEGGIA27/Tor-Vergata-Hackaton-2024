import os


class Solution:

    input_folder = os.path.join("soluzioni", "input", "7")
    output_folder = os.path.join("soluzioni", "output", "7")

    @staticmethod
    def solve(X: list[int], Y: list[int]) -> tuple[int, int]:
        peso_totale_x=sum(X)
        peso_totale_y=sum(Y)

        array_Y=[]

        for y in range(len(Y)):
           array_Y.append((Y[y],y))
    
        Solution.MergeSort(array_Y,0,len(array_Y)-1)

        differenza_peso=abs(peso_totale_x-peso_totale_y)
        if differenza_peso % 2 !=0:
           return None  
    
        for x in range(len(X)):
           y=Solution.BinSearch(array_Y,X[x],0,len(array_Y)-1,differenza_peso)
           if y != -1:
              return (x,y[1])
        return None
    
    @staticmethod 
    def MergeSort(L: list, start: int, end: int) -> None:
       if start < end:
         medium = (start + end) // 2
         Solution.MergeSort(L, start, medium)
         Solution.MergeSort(L, medium + 1, end)
         Solution.Merge(L, start, medium, end)

    @staticmethod
    def Merge(L: list, start: int, end_1: int, end_2: int) -> None:
       X = [0] * (end_2 - start + 1)

       i = 0
       s1 = start
       s2 = end_1 + 1

       while s1 <= end_1 and s2 <= end_2:
         if L[s1][0] <= L[s2][0]:
            X[i] = L[s1]
            s1 += 1
         else:
            X[i] = L[s2]
            s2 += 1
         i += 1

       while s1 <= end_1:
        X[i] = L[s1]
        s1 += 1
        i += 1

       while s2 <= end_2:
         X[i] = L[s2]
         s2 += 1
         i += 1

       for i in range(start, end_2 + 1):
        L[i] = X[i - start]
    
    @staticmethod
    def BinSearch(a,x,i,j,differenza_peso):
        if(i>j):
            return -1
        m=(i+j)//2
        if abs(x-a[m][0]) == differenza_peso // 2:
            return a[m]
        if(abs(x-a[m][0]) < differenza_peso // 2):
            return Solution.BinSearch(a,x,m+1,j,differenza_peso)
        else:
            return Solution.BinSearch(a,x,i,m-1,differenza_peso)
        
        

    @staticmethod
    def load_input(i: int) -> tuple[list[int], list[int]]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.input_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.input_folder, files[i]), "r") as f:
            X = list(map(int, f.readline().split()))
            Y = list(map(int, f.readline().split()))
            return X, Y

    @staticmethod
    def load_output(i: int) -> tuple[int, int]:
        """
        Carica il file di output i-esimo, contenuto all'interno della cartella dei file output.
        Questo metodo deve restituire il valore presente nel file di output.
        """

        # list dei file presenti nella cartella output
        files = os.listdir(Solution.output_folder)
        files.sort()

        # load file i-esimo
        with open(os.path.join(Solution.output_folder, files[i]), "r") as f:
            i, j = map(int, f.readline().split())
            return i, j

    @staticmethod
    def evaluate_solution(istance_number: int, solution: tuple[int, int]) -> int:
        X, Y = Solution.load_input(istance_number)
        i, j = solution

        assert 0 <= i < len(X)
        assert 0 <= j < len(Y)

        if sum(X) - X[i] + Y[j] == sum(Y) - Y[j] + X[i]:
            return 10
        else:
            return 0

