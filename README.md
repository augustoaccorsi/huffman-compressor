# Compressão e decompressão de arquivos utilizando a abordagem de codificação Huffman

## Teoria da Informação - Unisinos - Ciência da Computação

* O trabalho consiste comprimir e decomprimir dois arquivos providos pelo [corpus de Canterbury](corpus.canterbury.ac.nz/descriptions/#cantrbry) sum e alice26.txt

* Trabalho relizado na plataforma Windows

* O algoritimo irá utilizar a codificação de Huffman para comprimir ambos os arquivos, criando um árvore para cada uma deles e um dicionário de frequência de símbolos, que serão utilizados para a decompressão dos mesmos

### Execução do programa

`python Huffman.py files\alice29.txt` para comprimir e descombrimir o arquivo alice.29.txt

`python Huffman.py files\sum` para comprimir e descombrimir o arquivo sum

* Uma vez que o algoritmo é executado, ele cria dois arquivos novos na mesma pasta do arquivo que foi passado parametro. Um arquivo binário comprimido, e um arquivo, do mesmo formato do inicial, descomprimido
