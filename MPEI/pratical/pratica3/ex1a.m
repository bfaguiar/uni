N = 10000;
lados = 6;
dados = 1;
 
px=floor(rand(dados,N)*(lados+1));
 
%Funcao probabilidade massa
prob=[sum(px==1)/N,sum(px==2)/N,sum(px==3)/N,sum(px==4)/N,sum(px==5)/N,sum(px==6)/N];
 
stem(1:lados, prob)

%Funcao distribuicao acumulada
acum=[0 cumsum(probabilidade)];
 
stairs(0:6,acum)

printf("ola mundo")