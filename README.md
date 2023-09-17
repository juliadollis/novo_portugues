# novo_portugues
São necessários alguns requisitos para execução:

1- Python instalado

2- Bibliotecas
```bash
pip install pandas openpyxl openai argparse

```
3- Chave API que pode ser criada em: https://platform.openai.com/account/api-keys

obs.: o sleep pode ser alterado de acordo com as limitações da API

Para executar o codigo use a linha de comando modificando o arquivo de entrada, o nome da planilha e da coluna que se deseja traduzir. Além de definir o nome do arquivo de saída e sua chave API
```bash
python translate.py --input dev.xlsx --output dev_att.xlsx --api_key CHAVEAPI --sheet Sheet1 --column transcript
```
