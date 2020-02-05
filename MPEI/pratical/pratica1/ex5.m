
N=1000000; % numero de experiencias
Pecas=5;
p=0.3;

amostras = rand(5, N) <= 0.3;

freql = sum(amostras);

% a)

def3=sum((freql)==3)/N

% b)

def2=sum((freql)<=2)/N

% c)

hist(freql,5)
