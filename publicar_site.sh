#!/bin/bash
# Chama Diária · publica a página de privacidade e suporte no GitHub.
# Uso:  bash ~/Downloads/site_chama_diaria/publicar_site.sh
#
# Antes de rodar, crie em github.com/new um repositório PÚBLICO chamado
# chamadiaria, sem README, sem .gitignore e sem licença.
set -e
cd "$(dirname "$0")"

if [ -z "$(git config --global user.name)" ]; then
  git config --global user.name "Dalto Pastro"
fi
if [ -z "$(git config --global user.email)" ]; then
  git config --global user.email "daltopastro@hotmail.com"
fi

if [ ! -d .git ]; then
  git init -q
  git symbolic-ref HEAD refs/heads/main
  git remote add origin https://github.com/daltopastro/chamadiaria.git
  git add -A
  git commit -q -m "Página da Chama Diária: privacidade e suporte"
  if ! git push -q --force origin main; then
    echo ""
    echo "O GitHub recusou o envio. Confira se você criou o repositório PÚBLICO chamadiaria em github.com/new. Se criou, me mande uma foto desta tela."
    exit 1
  fi
else
  git add -A
  git commit -q -m "Atualização da página" >/dev/null 2>&1 || echo "Nada novo para salvar."
  git push -q origin main
fi
echo ""
echo "PRONTO. Agora ligue a publicação:"
echo "  1. Abra github.com/daltopastro/chamadiaria"
echo "  2. Settings  ->  Pages"
echo "  3. Em Source escolha 'Deploy from a branch', branch 'main', pasta '/ (root)' e salve"
echo "  4. Espere um ou dois minutos e abra:"
echo "     https://achamadiaria.com.br/"
echo ""
echo "Se a pagina ja estava publicada, nao precisa dos passos 1 a 3:"
echo "espere um ou dois minutos e recarregue com Cmd+Shift+R."
