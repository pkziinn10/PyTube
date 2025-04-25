# 🎬 YouTube Video Downloader com Python e yt-dlp

Este projeto oferece uma solução simples e eficiente para baixar vídeos do YouTube diretamente pelo terminal, utilizando Python e a biblioteca `yt-dlp`. Ideal para quem busca automatizar downloads ou integrar essa funcionalidade em outros sistemas.

---

## 🧰 Funcionalidades

- Download de vídeos na melhor qualidade disponível.
- Suporte a milhares de sites além do YouTube.
- Extração de áudio de vídeos (modo somente áudio).
- Personalização do diretório de saída.
- Integração com `ffmpeg` para pós-processamento.

---

## 📁 Estrutura do Projeto

- **`download_video.py`**: Script principal para realizar os downloads.
- **`requirements.txt`**: Lista de dependências do projeto.
- **`README.md`**: Este arquivo de documentação.

---

## 🚀 Instalação

### Pré-requisitos

- Python 3.6 ou superior.
- `ffmpeg` instalado no sistema (necessário para fusão de vídeo e áudio).

### Passos

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/yt-downloader.git
   cd yt-downloader
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

   Ative o ambiente virtual:

   - **Linux/macOS**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Como Usar

Execute o script passando a URL do vídeo e, opcionalmente, o caminho de destino:

```bash
python download_video.py "https://www.youtube.com/watch?v=ABC123" --path "/caminho/para/salvar"
```

Parâmetros:

- **`url`**: URL do vídeo no YouTube.
- **`--path` ou `-p`**: Diretório onde o vídeo será salvo (padrão: diretório atual).

---

## 🛠️ Personalização

O script pode ser adaptado para:

- Baixar apenas o áudio dos vídeos.
- Selecionar a qualidade específica do vídeo.
- Baixar playlists inteiras.
- Adicionar metadados ou legendas.

Consulte a [documentação oficial do yt-dlp](https://github.com/yt-dlp/yt-dlp#readme) para explorar todas as opções disponíveis.

---

## 🧪 Exemplo de Uso

Baixar um vídeo específico:

```bash
python download_video.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --path "./videos"
```

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

Com este `README.md`, seu projeto estará bem documentado e atrativo para outros desenvolvedores. Se desejar adicionar badges de status, instruções para Docker ou suporte a outras plataformas, posso ajudá-lo a expandir este arquivo.
