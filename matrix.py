class Matrix:

    def __init__(self,m,n=None):
        if n is None:
            if len(m)==0 or len(m[0])==0:
                raise ValueError()
            self.strock=len(m)
            self.stolbcov=len(m[0])
            self.value=m
        elif type(n)==int and type(m)==int:
            if n<=0 or m<=0:
                raise ValueError()
            self.strock=m
            self.stolbcov=n
            self.value=[[0]*n for i in range(m)]
        else:
            raise ValueError()



    def __add__(self,other):
        if self.stolbcov!=other.stolbcov or self.strock!=other.strock:
            raise ValueError()
        b=[[0]*self.stolbcov for i in range(self.strock)]
        for i in range(self.strock):
            for j in range(self.stolbcov):
                b[i][j]=self.value[i][j]+other.value[i][j]
        return Matrix(b)



    #def determinant(self):
            #FIXME



    def __eq__(self, other):
        if self.stolbcov!=other.stolbcov or self.strock!=other.strock:
            raise RuntimeError()
        else:
            for i in range(self.strock):
                for j in range(self.stolbcov):
                    if self.value[i][j]!=other.value[i][j]:
                        return False
            return True



    def get(self,i,j):
        if i>self.strock or j>self.stolbcov:
            raise ValueError()
        return self.value[i][j]



    def get_m(self):
        return self.strock



    def get_n(self):
        return self.stolbcov



    def get_size(self):
        return self.strock,self.stolbcov


    #def invert(self):
        #FIXME


    def __mul__(self,other):
        if type(other)==float or type(other)==int:
            b=[[0]*self.stolbcov for i in range(self.strock)]
            for i in range(self.strock):
                for j in range(self.stolbcov):
                    print(self.value[i][j],type(self.value[i][j]),other,type(other))
                    b[i][j]=self.value[i][j]*other
            return Matrix(b)
        if self.stolbcov!=other.strock:
            raise RuntimeError
        else:
            b=[[0]*self.strock for i in range(self.stolbcov)]
            for i in range(self.strock):
                for j in range(other.stolbcov):
                    for k in range(self.stolbcov):
                        b[i][j]+=self.value[i][k]+other.value[k][j]
            return Matrix(b)




    def set(self,i,j,value):
        if i>self.strock or j>self.stolbcov or i<0 or j<0:
            raise ValueError()
        if type(value)!=int:
            raise ValueError()
        self.value[i][j]=value



    def __sub__(self,other):
        if self.stolbcov!=other.stolbcov or self.strock!=other.strock:
            raise ValueError()
        b=[[0]*self.stolbcov for i in range(self.strock)]
        for i in range(self.strock):
            for j in range(self.stolbcov):
                b[i][j]=self.value[i][j]-other.value[i][j]
        return Matrix(b)



    #def transpose(self):
        #FIXME




    def __truediv__(self, other):
        if other==0:
            raise ZeroDivisionError()
        else:
            b=[[0]*self.stolbcov for i in range(self.strock)]
            for i in range(self.strock):
                for j in range(self.stolbcov):
                    print(self.value[i][j],type(self.value[i][j]),other,type(other))
                    b[i][j]=self.value[i][j]/other
            return Matrix(b)





