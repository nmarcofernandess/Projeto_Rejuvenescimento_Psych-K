#!/usr/bin/env python3
"""
Script para converter Markdown em PDF com layout profissional
Usando Montserrat, headers/footers bonitos e design para impressão
Versão com WeasyPrint (mais moderna que wkhtmltopdf)
"""

import markdown
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import os
from datetime import datetime

def criar_css_bonito():
    """Cria CSS profissional com Montserrat e layout para impressão"""
    return """
    /* Importar Montserrat do Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700;800&display=swap');
    
    /* Reset e configurações básicas */
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* Configurações da página */
    @page {
        size: A4;
        margin: 2cm 2cm 3cm 2cm;
        
        /* Header */
        @top-center {
            content: "Projeto Rejuvenescimento Psych-K®";
            font-family: 'Montserrat', sans-serif;
            font-weight: 600;
            font-size: 10pt;
            color: #2c5282;
            border-bottom: 1px solid #e2e8f0;
            padding-bottom: 5pt;
            margin-bottom: 10pt;
        }
        
        /* Footer */
        @bottom-left {
            content: "© 2025 Marco Fernandes - CEO DietFlow";
            font-family: 'Montserrat', sans-serif;
            font-size: 8pt;
            color: #718096;
        }
        
        @bottom-right {
            content: "Página " counter(page) " de " counter(pages);
            font-family: 'Montserrat', sans-serif;
            font-size: 8pt;
            color: #718096;
        }
        
        @bottom-center {
            content: "";
            border-top: 1px solid #e2e8f0;
            width: 100%;
            margin-top: 5pt;
        }
    }
    
    /* Body principal */
    body {
        font-family: 'Montserrat', sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #2d3748;
        background: #ffffff;
    }
    
    /* Capa especial */
    .capa {
        page-break-after: always;
        text-align: center;
        padding-top: 4cm;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .capa img {
        max-width: 200px;
        margin-bottom: 2cm;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .capa h1 {
        font-size: 2.5em;
        font-weight: 800;
        margin-bottom: 0.5cm;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .capa .subtitulo {
        font-size: 1.2em;
        font-weight: 300;
        margin-bottom: 2cm;
        opacity: 0.9;
    }
    
    .capa .autor {
        font-size: 1em;
        font-weight: 500;
        margin-top: auto;
        padding-top: 2cm;
    }
    
    /* Títulos principais */
    h1 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        font-size: 1.8em;
        color: #2c5282;
        margin: 1.5em 0 0.8em 0;
        page-break-after: avoid;
        border-left: 4px solid #4299e1;
        padding-left: 15px;
    }
    
    h2 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: 1.4em;
        color: #2d3748;
        margin: 1.2em 0 0.6em 0;
        page-break-after: avoid;
    }
    
    h3 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        font-size: 1.2em;
        color: #4a5568;
        margin: 1em 0 0.5em 0;
        page-break-after: avoid;
    }
    
    h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        font-weight: 500;
        color: #718096;
        margin: 0.8em 0 0.4em 0;
    }
    
    /* Parágrafos */
    p {
        margin: 0.8em 0;
        text-align: justify;
        orphans: 3;
        widows: 3;
    }
    
    /* Listas */
    ul, ol {
        margin: 0.8em 0;
        padding-left: 1.5em;
    }
    
    li {
        margin: 0.3em 0;
        line-height: 1.5;
    }
    
    /* Citações */
    blockquote {
        background: #f7fafc;
        border-left: 4px solid #4299e1;
        margin: 1.2em 0;
        padding: 1em 1.5em;
        font-style: italic;
        page-break-inside: avoid;
    }
    
    /* Código */
    code {
        background: #edf2f7;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        font-size: 0.9em;
    }
    
    pre {
        background: #2d3748;
        color: #e2e8f0;
        padding: 1em;
        border-radius: 5px;
        overflow-x: auto;
        margin: 1em 0;
        page-break-inside: avoid;
    }
    
    /* Tabelas */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 1em 0;
        page-break-inside: avoid;
    }
    
    th, td {
        border: 1px solid #e2e8f0;
        padding: 8px 12px;
        text-align: left;
    }
    
    th {
        background: #edf2f7;
        font-weight: 600;
    }
    
    /* Links */
    a {
        color: #4299e1;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Elementos especiais */
    .destaque {
        background: #fef5e7;
        border: 1px solid #f6ad55;
        padding: 1em;
        border-radius: 5px;
        margin: 1em 0;
        page-break-inside: avoid;
    }
    
    .importante {
        background: #fed7d7;
        border: 1px solid #fc8181;
        padding: 1em;
        border-radius: 5px;
        margin: 1em 0;
        page-break-inside: avoid;
    }
    
    /* Quebras de página */
    .page-break {
        page-break-before: always;
    }
    
    /* Imagens */
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 1em auto;
        border-radius: 5px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Índice */
    .indice {
        page-break-after: always;
    }
    
    .indice ul {
        list-style: none;
        padding-left: 0;
    }
    
    .indice li {
        padding: 0.3em 0;
        border-bottom: 1px dotted #e2e8f0;
    }
    
    /* Ajustes para impressão */
    @media print {
        body {
            font-size: 10pt;
        }
        
        h1 { font-size: 1.6em; }
        h2 { font-size: 1.3em; }
        h3 { font-size: 1.1em; }
        
        .no-print {
            display: none;
        }
    }
    """

def processar_markdown(arquivo_md):
    """Processa arquivo markdown e adiciona elementos especiais"""
    with open(arquivo_md, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Converter markdown para HTML
    md = markdown.Markdown(extensions=[
        'extra',
        'codehilite',
        'toc',
        'tables',
        'fenced_code'
    ])
    
    html_content = md.convert(conteudo)
    
    # Criar capa personalizada
    capa_html = f"""
    <div class="capa">
        <img src="capa-rejuvenescimento.png" alt="Capa do Projeto">
        <h1>Projeto Rejuvenescimento</h1>
        <div class="subtitulo">Apostila Completa - Metodologia Psych-K®</div>
        <div class="autor">
            <strong>Marco Fernandes</strong><br>
            CEO DietFlow<br>
            {datetime.now().strftime('%B %Y')}
        </div>
    </div>
    """
    
    # Template HTML completo
    html_completo = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Projeto Rejuvenescimento - Apostila Completa</title>
        <style>
            {criar_css_bonito()}
        </style>
    </head>
    <body>
        {capa_html}
        <div class="conteudo">
            {html_content}
        </div>
    </body>
    </html>
    """
    
    return html_completo

def gerar_pdf(arquivo_md, arquivo_pdf):
    """Gera PDF com WeasyPrint - mais moderno e confiável"""
    
    print("🎨 Processando markdown...")
    html_content = processar_markdown(arquivo_md)
    
    # Salvar HTML temporário para debug
    with open('temp_apostila.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("📄 Configurando WeasyPrint...")
    
    # Configuração de fontes para melhor renderização
    font_config = FontConfiguration()
    
    print("🔥 Gerando PDF com WeasyPrint...")
    try:
        # Criar objeto HTML
        html_doc = HTML(string=html_content, base_url='.')
        
        # CSS adicional para WeasyPrint
        css_doc = CSS(string=criar_css_bonito(), font_config=font_config)
        
        # Gerar PDF
        html_doc.write_pdf(
            arquivo_pdf, 
            stylesheets=[css_doc],
            font_config=font_config
        )
        
        print(f"✅ PDF gerado com sucesso: {arquivo_pdf}")
        
        # Limpar arquivo temporário
        if os.path.exists('temp_apostila.html'):
            os.remove('temp_apostila.html')
            
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        print("💡 Verifique se todas as dependências estão instaladas:")
        print("   pip install weasyprint markdown")

def main():
    """Função principal"""
    print("🎬 Gerador de PDF Profissional - Projeto Rejuvenescimento")
    print("📚 Usando WeasyPrint para renderização moderna")
    print("=" * 60)
    
    # Arquivos
    arquivo_md = "Apostila_Projeto_Rejuvenescimento_Refinada.md"
    arquivo_pdf = "Apostila_Projeto_Rejuvenescimento_IMPRESSAO.pdf"
    
    # Verificar se arquivo MD existe
    if not os.path.exists(arquivo_md):
        print(f"❌ Arquivo não encontrado: {arquivo_md}")
        return
    
    # Gerar PDF
    gerar_pdf(arquivo_md, arquivo_pdf)
    
    print("\n🎯 Processo concluído!")
    print(f"📁 Arquivo gerado: {arquivo_pdf}")
    print("🖨️  Pronto para impressão em alta qualidade!")
    print("\n💡 Dica: Abra o PDF e verifique o resultado antes de imprimir")

if __name__ == "__main__":
    main() 