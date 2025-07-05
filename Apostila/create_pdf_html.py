import re

def clean_text(text):
    """Remove emojis e limpa formatação para PDF"""
    # Remove emojis
    text = re.sub(r'[^\w\s\-\.,\!\?\:\;\(\)\"\'\/\>\<]+', ' ', text)
    # Limpa espaços duplos
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def process_markdown_to_html():
    # Ler o arquivo markdown refinado
    with open('Apostila_Projeto_Rejuvenescimento_Refinada.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extrair seções dos vídeos
    video_sections = re.findall(r'## (Vídeo \d+:.*?)(?=## Vídeo|\Z)', content, re.DOTALL)

    html_videos = ''
    
    for i, section in enumerate(video_sections, 1):
        lines = section.strip().split('\n')
        title = clean_text(lines[0].replace('## ', ''))
        
        html_videos += f'''
<!-- VÍDEO {i:02d} -->
<div class="video-chapter">
    <h2 class="video-title">{title}</h2>
'''
        
        in_list = False
        list_type = ''
        
        for line in lines[1:]:
            line = line.strip()
            if not line:
                if in_list:
                    html_videos += f'    </{list_type}>\n'
                    in_list = False
                continue
                
            # Títulos h3
            if line.startswith('### '):
                if in_list:
                    html_videos += f'    </{list_type}>\n'
                    in_list = False
                clean_title = clean_text(line[4:])
                html_videos += f'    <h3>{clean_title}</h3>\n'
            
            # Citações
            elif line.startswith('> '):
                if in_list:
                    html_videos += f'    </{list_type}>\n'
                    in_list = False
                quote_text = clean_text(line[2:])
                quote_text = quote_text.replace('**', '<strong>').replace('**', '</strong>')
                html_videos += f'    <blockquote>{quote_text}</blockquote>\n'
            
            # Listas com marcadores
            elif line.startswith('- ') or line.startswith('* '):
                if not in_list:
                    html_videos += '    <ul>\n'
                    in_list = True
                    list_type = 'ul'
                item_text = clean_text(line[2:])
                item_text = item_text.replace('**', '<strong>').replace('**', '</strong>')
                html_videos += f'        <li>{item_text}</li>\n'
            
            # Listas numeradas
            elif re.match(r'^\d+\.', line):
                if not in_list:
                    html_videos += '    <ol class="step-list">\n'
                    in_list = True
                    list_type = 'ol'
                item_text = re.sub(r'^\d+\.\s*', '', line)
                item_text = clean_text(item_text)
                item_text = item_text.replace('**', '<strong>').replace('**', '</strong>')
                html_videos += f'        <li>{item_text}</li>\n'
            
            # Caixas de destaque (detectar por palavras-chave)
            elif any(keyword in line for keyword in ['IMPORTANTE:', 'NÃO', 'Essenciais:', 'Lembre-se:']):
                if in_list:
                    html_videos += f'    </{list_type}>\n'
                    in_list = False
                clean_line = clean_text(line)
                clean_line = clean_line.replace('**', '<strong>').replace('**', '</strong>')
                if 'NÃO' in line or 'IMPORTANTE' in line:
                    html_videos += f'    <div class="warning-box"><strong>{clean_line}</strong></div>\n'
                else:
                    html_videos += f'    <div class="highlight-box">{clean_line}</div>\n'
            
            # Parágrafos normais
            else:
                if in_list:
                    html_videos += f'    </{list_type}>\n'
                    in_list = False
                clean_line = clean_text(line)
                clean_line = clean_line.replace('**', '<strong>').replace('**', '</strong>')
                clean_line = clean_line.replace('*', '<em>').replace('*', '</em>')
                if clean_line.strip():
                    html_videos += f'    <p>{clean_line}</p>\n'
        
        if in_list:
            html_videos += f'    </{list_type}>\n'
        
        html_videos += '</div>\n'

    return html_videos

# Processar o conteúdo
video_content = process_markdown_to_html()

# HTML base
html_base = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto Rejuvenescimento - Apostila Completa</title>
    <style>
        @page {
            size: A4;
            margin: 2.5cm 2cm 2cm 2cm;
        }

        body {
            font-family: 'Georgia', 'Times New Roman', serif;
            font-size: 11pt;
            line-height: 1.6;
            color: #333;
            background: #fff;
        }

        .cover-page {
            page-break-after: always;
            text-align: center;
            padding: 4cm 2cm;
            border: 3px solid #8e44ad;
            border-radius: 15px;
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }

        .cover-title {
            font-size: 36pt;
            font-weight: bold;
            color: #8e44ad;
            margin-bottom: 1cm;
            font-family: 'Arial', sans-serif;
        }

        .cover-subtitle {
            font-size: 16pt;
            color: #555;
            margin-bottom: 2cm;
            font-style: italic;
        }

        .cover-description {
            font-size: 14pt;
            color: #666;
            max-width: 80%;
            margin: 0 auto 2cm auto;
            line-height: 1.8;
        }

        .video-chapter {
            page-break-before: always;
            margin-bottom: 2cm;
        }

        .video-title {
            font-size: 18pt;
            color: #8e44ad;
            margin-bottom: 0.5cm;
            padding: 15px 20px;
            background-color: #f8f9fa;
            border-left: 5px solid #8e44ad;
            border-radius: 5px;
        }

        h3 {
            font-size: 14pt;
            color: #2c3e50;
            margin: 1cm 0 0.5cm 0;
            padding-left: 15px;
            border-left: 4px solid #8e44ad;
            background-color: #f8f9fa;
            padding: 10px 15px;
        }

        p {
            margin-bottom: 0.5cm;
            text-align: justify;
            text-indent: 1cm;
        }

        ul, ol {
            margin: 0.5cm 0 0.5cm 1.5cm;
        }

        li {
            margin-bottom: 0.3cm;
            line-height: 1.5;
        }

        blockquote {
            background-color: #f0f0f0;
            border-left: 5px solid #8e44ad;
            padding: 15px 20px;
            margin: 1cm 0;
            font-style: italic;
            border-radius: 5px;
        }

        .highlight-box {
            background-color: #e3f2fd;
            border: 2px solid #2196f3;
            padding: 15px;
            margin: 0.5cm 0;
            border-radius: 8px;
        }

        .warning-box {
            background-color: #fff3cd;
            border: 2px solid #ffc107;
            padding: 15px;
            margin: 0.5cm 0;
            border-radius: 8px;
        }

        strong {
            color: #8e44ad;
            font-weight: bold;
        }

        .step-list {
            counter-reset: step-counter;
            list-style: none;
            padding-left: 0;
        }

        .step-list li {
            counter-increment: step-counter;
            margin-bottom: 0.5cm;
            padding-left: 2cm;
            position: relative;
        }

        .step-list li::before {
            content: counter(step-counter);
            position: absolute;
            left: 0;
            top: 0;
            background-color: #8e44ad;
            color: white;
            width: 1.5cm;
            height: 1.5cm;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 12pt;
        }
    </style>
</head>
<body>

<!-- CAPA -->
<div class="cover-page">
    <h1 class="cover-title">PROJETO<br>REJUVENESCIMENTO</h1>
    <p class="cover-subtitle">Apostila Completa</p>
    <p class="cover-description">
        Material didático baseado na série de 30 vídeos sobre rejuvenescimento através da metodologia PSYCH-K®
    </p>
    <div style="margin-top: auto;">
        <p><strong>Uma jornada espiritual para lembrar quem você realmente é:<br>
        Um ser espiritual tendo uma experiência humana</strong></p>
    </div>
</div>

'''

# Montar HTML final
final_html = html_base + video_content + '\n</body>\n</html>'

# Salvar arquivo
with open('Apostila_Projeto_Rejuvenescimento_PDF.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Arquivo HTML para PDF criado com sucesso!")
print("Para gerar o PDF:")
print("1. Abra o arquivo 'Apostila_Projeto_Rejuvenescimento_PDF.html' no navegador")
print("2. Pressione Ctrl+P (ou Cmd+P no Mac)")
print("3. Selecione 'Salvar como PDF'")
print("4. Ajuste as configurações para 'Mais configurações' > 'Gráficos de fundo'") 