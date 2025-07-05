#!/bin/bash

echo "🎬 Gerador de PDF - Projeto Rejuvenescimento"
echo "=" * 45

# Verificar se ambiente virtual existe
if [ ! -d "pdf_env" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "💡 Execute primeiro: ./instalar_dependencias.sh"
    exit 1
fi

# Ativar ambiente virtual
echo "⚡ Ativando ambiente virtual..."
source pdf_env/bin/activate

# Verificar se arquivo MD existe
if [ ! -f "Apostila_Projeto_Rejuvenescimento_Refinada.md" ]; then
    echo "❌ Arquivo Markdown não encontrado!"
    echo "💡 Certifique-se de estar na pasta Apostila/"
    exit 1
fi

# Executar gerador
echo "🚀 Iniciando geração do PDF..."
python gerar_pdf_bonito.py

# Verificar resultado
if [ -f "Apostila_Projeto_Rejuvenescimento_IMPRESSAO.pdf" ]; then
    echo ""
    echo "🎉 PDF gerado com sucesso!"
    echo "📁 Arquivo: Apostila_Projeto_Rejuvenescimento_IMPRESSAO.pdf"
    echo "📊 Tamanho: $(du -h Apostila_Projeto_Rejuvenescimento_IMPRESSAO.pdf | cut -f1)"
    echo "🖨️  Pronto para impressão!"
else
    echo "❌ Erro na geração do PDF"
    exit 1
fi 