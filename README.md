# novo_portugues
São necessários alguns requisitos para execução:

1- Python instalado

2- Bibliotecas
```bash
pip install pandas openpyxl openai argparse

```
3- Chave API que pode ser criada em: https://platform.openai.com/account/api-keys


Para executar o codigo use a linha de comando modificando o arquivo de entrada, o nome da planilha e da coluna que se deseja traduzir. Além de definir o nome do arquivo de saída e sua chave API
```bash
python translate.py --input dev.xlsx --output dev_att.xlsx --api_key CHAVEAPI --sheet Sheet1 --column COLUNA1 COLUNA2
```
Nomes das colunas do nosso dataset: transcript e transcript_wav2vec

Nomes dos nossos arquivos: test, train e dev (os arquivos originalmente estao em csv mas devido a problemas no encoding, estamos usando xlsx)

Nome original da plhanilha: Sheet1 (obs.: se ocorrer erro tente Planilha1)

obs.: o sleep pode ser alterado de acordo com as limitações da API
