#!/bin/bash

echo "🎬 Instalando dependências para geração de PDF..."
echo "=" * 50

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instale o Python primeiro."
    exit 1
fi

# Criar ambiente virtual (recomendado)
echo "🐍 Criando ambiente virtual..."
python3 -m venv pdf_env

# Ativar ambiente virtual
echo "⚡ Ativando ambiente virtual..."
source pdf_env/bin/activate

# Instalar dependências Python modernas
echo "📦 Instalando dependências Python..."
pip install markdown weasyprint

echo "✅ Instalação concluída!"
echo "🚀 Para usar o gerador:"
echo "   1. source pdf_env/bin/activate"
echo "   2. python gerar_pdf_bonito.py"
echo ""
echo "💡 WeasyPrint é mais moderno que wkhtmltopdf (descontinuado)" 