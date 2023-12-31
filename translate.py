import os
import pandas as pd
import openai
import time
import argparse


def translate_to_modern_portuguese(text, api_key):
    print(f"Texto para tradução: {text}")
    print("Traduzindo...")
    openai.api_key = api_key
    prompt = [{"role": "user",
               "content": f"corrija a grafia da seguinte frase do portugues antigo para o portugues atual, corrigindo "
                          f"numerais e numeros por numeros em extenso, corrigindo a acentuação e abreviações,  retorne apenas a "
                          f"frase corrigida, sem adições: {text}"}]
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=prompt, temperature=0.2, max_tokens=200)
    texto_traduzido = response['choices'][0]['message']['content'].strip()
    print(f"Texto traduzido: {texto_traduzido}")
    time.sleep(21)
    return texto_traduzido


def batch_translate(df, column_names, api_key):
    translated_texts = {col: [] for col in column_names}
    for index, row in df.iterrows():
        for col in column_names:
            text = row[col]
            translated_text = translate_to_modern_portuguese(text, api_key)
            translated_texts[col].append(translated_text)
    return translated_texts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tradução de texto')
    parser.add_argument('--input', required=True, help='Nome do arquivo Excel de entrada')
    parser.add_argument('--sheet', required=True, help='Nome da planilha do arquivo Excel')
    parser.add_argument('--columns', required=True, nargs='+',
                        help='Nomes das colunas contendo os textos para traduzir')
    parser.add_argument('--output', required=True, help='Nome do arquivo Excel de saída')
    parser.add_argument('--api_key', required=True, help='Chave da API da OpenAI')

    args = parser.parse_args()

    df = pd.read_excel(args.input, engine='openpyxl', sheet_name=args.sheet)

    if df.empty:
        print("O DataFrame está vazio. Nada para traduzir.")
    else:
        df.dropna(subset=args.columns, inplace=True)
        translated_texts = batch_translate(df, args.columns, args.api_key)

        for col, texts in translated_texts.items():
            df[col] = texts

        df.to_excel(args.output, engine='openpyxl', index=False)
        print("O arquivo Excel foi salvo com sucesso!")
