%% Codigo 2

% Gerar uma matriz com 3 linhas e 10000 colunas de numeros aleatorios entre 0.0 e 1.0 
%(ou seja, cada coluna representa uma experiˆencia): experiencias = rand(3,10000);

% Gerar uma matriz com 3 linhas e 10000 colunas com o valor 1 se o valor da matriz anterior for superior a 0.5 (ou seja, se saiu cara) 
%ou com o valor 0 caso contrario (ou seja, saiu coroa):lancamentos = experiencias > 0.5;

% Gerar um vetor linha com 10000 elementos com a soma dos valores de cada coluna da matriz anterior 
%(ou seja, o n´umero de caras de cada experiˆencia): resultados= sum(lancamentos);

% Gerar um vetor linha com 10000 elementos com o valor 1 quando o valor do vetor anterior e' 2 
%(ou seja, se a experiˆencia deu 2 caras) ou 0 quando e' diferente de 2: sucessos= resultados==2;

% Determinar o resultado final dividindo o n´umero de experiˆencias com 2 caras pelo n´umero total de experiˆencias: 

%probSimulacao= sum(sucessos)/10000

N = 1e5; % numero de experiencias
p = 0.5; % probabilidade de cara
k = 2;   % numero de caras
n = 3;   % numero de lancamentos

lancamentos = rand(n, N) > p;
sucessos = sum(lancamentos) == k;
probSimulacao = sum(sucessos)

% se nao metermos ";" ele imprimenos o resultado.