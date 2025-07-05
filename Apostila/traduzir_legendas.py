#!/usr/bin/env python3
"""
Script para traduzir todas as legendas .vtt de inglês para português.
Mantém a estrutura original (timestamps, numeração) e traduz apenas o texto.
"""

import os
import re
import time
from pathlib import Path
from deep_translator import GoogleTranslator

def traduzir_arquivo_vtt(arquivo_path):
    """Traduz um arquivo VTT específico."""
    
    print(f"🔄 Traduzindo: {arquivo_path.name}")
    
    try:
        # Ler arquivo original
        with open(arquivo_path, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        # Inicializar tradutor
        translator = GoogleTranslator(source='en', target='pt')
        
        # Processar linhas
        linhas_traduzidas = []
        i = 0
        
        while i < len(linhas):
            linha = linhas[i].strip()
            
            # Cabeçalho WEBVTT
            if linha == "WEBVTT":
                linhas_traduzidas.append("WEBVTT\n")
                i += 1
                continue
            
            # Linha vazia
            if not linha:
                linhas_traduzidas.append("\n")
                i += 1
                continue
            
            # Número do bloco (só números)
            if linha.isdigit():
                linhas_traduzidas.append(linha + "\n")
                i += 1
                continue
            
            # Timestamp (formato: 00:00:00.000 --> 00:00:00.000)
            if "-->" in linha:
                linhas_traduzidas.append(linha + "\n")
                i += 1
                
                # Próximas linhas são texto até linha vazia ou fim
                texto_bloco = []
                while i < len(linhas) and linhas[i].strip():
                    texto_bloco.append(linhas[i].strip())
                    i += 1
                
                # Traduzir texto do bloco
                if texto_bloco:
                    texto_completo = " ".join(texto_bloco)
                    
                    try:
                        # Traduzir com retry em caso de erro
                        for tentativa in range(3):
                            try:
                                texto_traduzido = translator.translate(texto_completo)
                                break
                            except Exception as e:
                                if tentativa == 2:
                                    print(f"⚠️  Erro ao traduzir '{texto_completo}': {e}")
                                    texto_traduzido = texto_completo  # Manter original
                                else:
                                    time.sleep(1)  # Aguardar antes de tentar novamente
                        
                        linhas_traduzidas.append(texto_traduzido + "\n")
                        
                    except Exception as e:
                        print(f"⚠️  Erro ao traduzir: {e}")
                        linhas_traduzidas.append(texto_completo + "\n")
                
                continue
            
            # Linha não identificada, manter original
            linhas_traduzidas.append(linha + "\n")
            i += 1
        
        # Escrever arquivo traduzido
        with open(arquivo_path, 'w', encoding='utf-8') as f:
            f.writelines(linhas_traduzidas)
        
        print(f"✅ Traduzido: {arquivo_path.name}")
        
    except Exception as e:
        print(f"❌ Erro ao processar {arquivo_path.name}: {e}")

def traduzir_todas_legendas():
    """Traduz todas as legendas nas pastas video_XX/"""
    
    base_dir = Path.cwd()
    pastas_video = []
    
    # Encontrar todas as pastas video_XX
    for pasta in base_dir.glob("video_*"):
        if pasta.is_dir():
            match = re.search(r'video_(\d+)', pasta.name)
            if match:
                numero = int(match.group(1))
                pastas_video.append((numero, pasta))
    
    pastas_video.sort()  # Ordenar por número
    
    print(f"🎯 Encontradas {len(pastas_video)} pastas de vídeo")
    print("🌍 Iniciando tradução de inglês → português...\n")
    
    # Processar cada pasta
    for numero, pasta in pastas_video:
        print(f"📁 Pasta: {pasta.name}")
        
        # Procurar arquivo .vtt na pasta
        arquivos_vtt = list(pasta.glob("*.vtt"))
        
        if arquivos_vtt:
            for arquivo_vtt in arquivos_vtt:
                traduzir_arquivo_vtt(arquivo_vtt)
                time.sleep(0.5)  # Pausa para não sobrecarregar a API
        else:
            print(f"⚠️  Nenhum arquivo .vtt encontrado em {pasta.name}")
        
        print()  # Linha em branco entre pastas
    
    print("🎉 Tradução de todas as legendas concluída!")

if __name__ == "__main__":
    traduzir_todas_legendas() 