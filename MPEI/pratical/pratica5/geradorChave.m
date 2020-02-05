function [chave] = geradorChave(compMax, compMin, strng)
  compDif = compMax - compMin;
  comprimento = ceil((rand()*compDif) + compMin);
  chaveAux = ceil((rand(1, comprimento)*(length(strng)-1))+1);
  chave = strng(chaveAux);
endfunction
