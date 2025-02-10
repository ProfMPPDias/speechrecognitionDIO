# Speech Recognition Python IA - DIO

## Demonstração

### Clique para Assistir a Demonstração
[![Assistir ao vídeo](https://i.imgur.com/GAXwUBi.png)](https://drive.google.com/file/d/1BIr6ssOFuJXhCZkhaJZ1gvkFs11K31iR/view)


Este é um assistente virtual baseado em reconhecimento de fala e síntese de voz desenvolvido em Python. O projeto permite que o usuário dê comandos de voz para abrir o YouTube, Google Maps ou pesquisar no Wikipedia.

## Tecnologias Utilizadas
- Python 3
- `speech_recognition` para reconhecimento de fala
- `pyttsx3` para síntese de voz (text-to-speech)
- `webbrowser` para abrir páginas da web

## Instalação
Certifique-se de ter o Python 3 instalado. Em seguida, instale as dependências necessárias:
```sh
pip install speechrecognition pyttsx3 pyaudio requests
```

## Como Usar
Execute o script Python para iniciar o assistente virtual:
```sh
python3 main.py
```

Ao executar o programa, o assistente irá perguntar como pode ajudar. Você pode utilizar os seguintes comandos:

- **"Wiki <termo>"**: Abre a página do Wikipedia para o termo especificado.
- **"Youtube"**: Abre o YouTube.
- **"Google Maps"**: Abre o Google Maps.
- **"Sair" ou "Parar"**: Encerra o assistente.

## Funcionamento
1. O assistente inicia e sauda o usuário.
2. O programa escuta e interpreta comandos de voz.
3. Se o comando for reconhecido, a ação correspondente é executada.
4. Caso o comando não seja identificado, o assistente pede que o usuário repita.
5. O loop continua até que o usuário diga "sair" ou "parar".

## Autor
Este projeto foi desenvolvido como parte do curso da Digital Innovation One (DIO).

## Licença
Este projeto é de livre uso e distribuído sob a licença MIT.
