# 🎨 Gerador de PDF Profissional

Script para converter a apostila Markdown em PDF com layout bonito para impressão.

## ✨ Características

- **🎯 Layout Profissional:** Headers, footers, numeração de páginas
- **🔤 Fonte Montserrat:** Importada do Google Fonts 
- **🖼️ Capa Personalizada:** Com gradiente e imagem
- **📄 Formatação A4:** Otimizada para impressão
- **🎨 Design Moderno:** Cores, espaçamentos e tipografia cuidadosos

## 🚀 Como Usar

### 1. Instalar Dependências
```bash
chmod +x instalar_dependencias.sh
./instalar_dependencias.sh
```

### 2. Ativar Ambiente Virtual
```bash
source pdf_env/bin/activate
```

### 3. Gerar PDF
```bash
python gerar_pdf_bonito.py
```

### 4. Resultado
O arquivo `Apostila_Projeto_Rejuvenescimento_IMPRESSAO.pdf` será gerado na mesma pasta.

## 🎨 Elementos do Layout

### Capa
- **Imagem:** Logo/capa do projeto
- **Título:** "Projeto Rejuvenescimento" 
- **Subtítulo:** "Apostila Completa - Metodologia Psych-K®"
- **Autor:** Marco Fernandes - CEO DietFlow
- **Data:** Mês/Ano atual

### Headers & Footers
- **Header:** "Projeto Rejuvenescimento Psych-K®"
- **Footer Esquerdo:** Copyright
- **Footer Direito:** "Página X de Y"
- **Footer Centro:** Linha decorativa

### Tipografia
- **Fonte Principal:** Montserrat (Google Fonts)
- **Títulos:** Pesos 700-800, cores azuis
- **Texto:** Peso 400, justificado
- **Tamanho:** 11pt (10pt na impressão)

### Cores
- **Azul Principal:** #2c5282
- **Azul Claro:** #4299e1  
- **Cinza Escuro:** #2d3748
- **Cinza Médio:** #718096

## 🔧 Dependências

- **Python 3:** Linguagem base
- **markdown:** Conversão MD → HTML
- **weasyprint:** Conversão HTML → PDF (moderno e confiável)
- **FontConfiguration:** Renderização avançada de fontes

## 📁 Arquivos Gerados

- `Apostila_Projeto_Rejuvenescimento_IMPRESSAO.pdf` - PDF final
- `temp_apostila.html` - HTML temporário (removido automaticamente)

## 🎯 Configurações de Impressão

- **Formato:** A4
- **Margens:** 2cm (superior/lateral), 3cm (inferior)
- **DPI:** 300 (alta qualidade)
- **Quebras de página:** Automáticas e otimizadas
- **Órfãos/Viúvas:** Controlados para melhor legibilidade

---

*Desenvolvido por Marco Fernandes - CEO DietFlow* 