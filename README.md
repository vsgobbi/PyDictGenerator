
# PyDicGenerator
### Licensa GPLv3.0
Desenvolvido por Ongui, vitorsgobbi@hotmail.com
Gerador de lista de dicionario em Python 2.7 

ADICIONAR E EDITAR:
#Repo: https://github.com/vsgobbi/PyDictGenerator.git
```
$git clone https://github.com/vsgobbi/PyDictGenerator.git .
```

COMO UTILIZAR: 

### REQUISITOS :
#### Utilizar em ambiente virtual Python2.7
#### Criar ambiente virtual virtualenv 
```
$virtualenv -p /usr/bin/python2.7 venv
```
#Ativar ambiente
```
$source venv/bin/activate
```
#Conferir versão python
```
$python --version
```
#Chamando o script corretamente:
```
python 'local/do/arquivo/onguiDictSortGenerator.py' [inputText.txt] [onguiWordList.txt]
```        
#Ou:
```
chmod 755 "seed.txt" #Deve criar um pwdlist a partir de um arquivo fonte

chmod +x onguiDictSortGenerator.py

./onguiDictSortGenerator.py "seed.txt" "listagerada.txt"
```
