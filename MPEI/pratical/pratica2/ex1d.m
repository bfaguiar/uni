

N = 1000; % numero de experiencias
nFilhos = 2;
p = 0.5; %probabilidade de sair cada filho.

amostras = rand(nFilhos, N) < p; % gera uma matriz 2 linhas (nFilhos) por 1000 colunas (de numeros aleatorios entre 0.0 e 1.0)


A = amostras(1,:) == 1; % array do primeiro caso
B = amostras(2,:) == 1; % array do segundo caso

AB = A&B;

somaA = sum(A);
somaB = sum(B);
somaAB = sum(AB);

pA = somaA / N;
pB = somaB / N;


probabilidadeSabendoQue = somaAB / somaB
