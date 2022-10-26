""" 
    Puzzle A*
"""
class Node:
    def __init__(self,data,level,fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ Gere nós filhos a partir do nó fornecido movendo o espaço em branco
            nas quatro direções {cima, baixo, esquerda, direita}  """
        x,y = self.find(self.data,'_')
        """ val_list contém valores de posição para mover o espaço em branco em qualquer um dos
            as 4 direções [cima, baixo, esquerda, direita], respectivamente. """
        val_list = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data,x,y,i[0],i[1])
            if child is not None:
                child_node = Node(child,self.level+1,0)
                children.append(child_node)
        return children
        
    def shuffle(self,puz,x1,y1,x2,y2):
        """ Mova o espaço em branco na direção dada e se o valor da posição estiver fora
            de limites o retorno Nenhum """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None
            

    def copy(self,root):
        """Função de cópia para criar uma matriz semelhante do nó fornecido"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp    
            
    def find(self,puz,x):
        """ Usado especificamente para encontrar a posição do espaço em branco """
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data)):
                if puz[i][j] == x:
                    return i,j


class Puzzle:
    def __init__(self,size):
        """ Inicialize o tamanho do quebra-cabeça pelo tamanho especificado, listas abertas e fechadas para esvaziar """
        self.n = size
        self.open = []
        self.closed = []

    def accept(self):
        """ Aceita o quebra-cabeça do usuário """
        puz = []
        for i in range(0,self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self,start,goal):
        """ Função heurística para calcular o valor heurístico f(x) = h(x) + g(x) """
        return self.h(start.data,goal)+start.level

    def h(self,start,goal):
        """ Calcula a diferença entre os quebra-cabeças fornecidos """
        temp = 0
        for i in range(0,self.n):
            for j in range(0,self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp
        

    def process(self):
        """Aceite o estado de início e quebra-cabeça de meta"""
        print("Insira a matriz de estado inicial \n")
        start = self.accept()
        print("Insira a matriz de estado da meta \n")        
        goal = self.accept()

        start = Node(start,0,0)
        start.fval = self.f(start,goal)
        """ Coloque o nó inicial na lista aberta"""
        self.open.append(start)
        print("\n\n")
        while True:
            cur = self.open[0]
            print("")
            print("  | ")
            print("  | ")
            print(" \\\'/ \n")
            for i in cur.data:
                for j in i:
                    print(j,end=" ")
                print("")
            """ Se a diferença entre o nó atual e o nó objetivo for 0, atingimos o nó objetivo"""
            if(self.h(cur.data,goal) == 0):
                break
            for i in cur.generate_child():
                i.fval = self.f(i,goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            """ ordena a lista aberta com base no valor f """
            self.open.sort(key = lambda x:x.fval,reverse=False)


puz = Puzzle(3)
puz.process()