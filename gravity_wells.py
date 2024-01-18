def TransformTransform(A, N):

    # трансформирующая трансформация S массива A
    def transformative_transformation(a):
        B = [] # выходной массив/список B 
        for i in range(N - 1):
            for j in range(N - i - 1):
                k = a[i] + a[j]
                maxx = max(a[j:k])
                B.append(maxx)
        return(B)
    
    # ключевой ключ
    def key_key(b):
        return sum(b)
    
    # двойная трансформация
    t_second = transformative_transformation(transformative_transformation(A))

    # проверка на четность
    if key_key(t_second) % 2 == 0:
        return True
    if key_key(t_second) % 2 != 0:
        return False
