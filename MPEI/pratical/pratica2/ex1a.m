

N = 1000; % numero de experiencias
nFilhos = 2;
p = 0.5; %probabilidade de sair cada filho.

amostras = rand(nFilhos, N) <= p; % gera uma matriz 2 linhas (nFilhos) por 1000 colunas (de numeros aleatorios entre 0.0 e 1.0)
%se a condicao " <= p" for falsa, ele mete zeros, se for verdadeira, ele mete uns.

%ex.1: 1 0 1 0 0 1 1
%      0 1 1 0 1 1 0

freq = sum(amostras); % soma os numeros de cada coluna da matriz e cria um array com cada soma.

%ex.1: 1 1 2 0 1 2 1


def3 = sum((freq)>=1)/N % soma na matriz 1 e 2 porque o zero ´e s´o raparigas