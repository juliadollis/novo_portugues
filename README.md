# new_portugues
São necessários alguns requisitos para execução:
1- Python instalado

2- Biblioteca Pandas
```bash
pip install pandas
```
3- Chave API que pode ser criada em: https://platform.openai.com/account/api-keys

Para executar o codigo use a linha de comando modificando o arquivo de entrada, o nome da planilha e da coluna que se deseja traduzir. Além de definir o nome do arquivo de saída e sua chave API
```bash
python translate.py --input dev.xlsx --output dev_att.xlsx --api_key CHAVEAPI --sheet Sheet1 --column transcript
```
