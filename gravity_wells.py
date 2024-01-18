def TransformTransform(A, N):

    # трансформирующая трансформация S массива A
    def transformative_transformation(a):
        B = [] # выходной массив/список B 
        for i in range(len(a)):
            for j in range(len(a) - i):
                k = i + j
                maxx = max(a[j:k+1])
                B.append(maxx)
        return(B)
    
    # ключевой ключ
    def key_key(b):
        return sum(b)
    
    # двойная трансформация
    t_second = transformative_transformation(transformative_transformation(A))

    # проверка на четность
    otv = key_key(t_second)
    if otv % 2 == 0:
        return True
    if otv % 2 != 0:
        return False
