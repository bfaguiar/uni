

paises = {'Portugal','Estados Unidos da America','Reino Unido', 'Australia'};

paisesAdd = {'Portugal','Estados Unidos da America','Franca'};

BFSize = 100;

key = 3;

bloom = inicializarBF(BFSize);

for i = 1:length(paises)
    bloom = inserirElemento(bloom, key, paises{i});
end

for i = 1:length(paisesAdd)
    ok = elementoPertence(bloom, key, paisesAdd{i});
    if ok == 1
       fprintf('%s percence ao set de paises!\n', paisesAdd{i})
    else
       fprintf('%s nao percentence ao set de paises! :( \n', paisesAdd{i})
    end
end
