Membros = {'Espanha','Portugal','Italia'};
Teste = {'Italia','Polonia','Fran�a'};
m=100;
k=3;
B=inicializar(m);
for(i=1:length(Membros)
  B=incluirMembro(B,k,Membros{i});
end
for i=1:length(Teste)
  ok=pertenceMembro(B,k,Teste{i});
  if ok==1
     fprintf('%s Pertence\n', Teste{i})
  else
     fprintf('%s N�o Pertence\n', Teste{i})
  end
end
