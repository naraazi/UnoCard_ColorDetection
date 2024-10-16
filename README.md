# Detecção de Cores com OpenCV
Este script detecta as cores vermelho, amarelo, verde e azul em uma imagem capturada pela câmera e exibe a cor predominante na tela. Ele pode ser usado para identificar cartas de Uno e realizar ações com um Arduino com base na cor detectada.

## Requisitos
* Python 3.10.x
* OpenCV
* NumPy
* PySerial (opcional, usado para conexão Python + Arduino)
* PlaySound (opcional, não possui uso no código básico, apenas no uso com Arduino)

Você pode instalar as dependências necessárias com:
```bash
pip install -r requirements.txt
```

## Como usar
1. **Configurar Tradução das Cores:** Para traduzir os nomes das cores para português, edite o dicionário color_ranges no início do código.

    Exemplo:
```python
color_ranges = {
    "vermelho": [(0, 100, 100), (10, 255, 255)],
    "amarelo": [(20, 150, 150), (30, 255, 255)],
    "verde": [(40, 100, 100), (80, 255, 255)],
    "azul": [(90, 100, 100), (130, 255, 255)]
}
```
O mesmo pode ser dito para as linhas:
```python
return result, "Todas as cores!"
```
e
```python
return result, "Nenhuma cor!"
```

2. **Executar o Script:** Conecte sua câmera e execute o script com o comando:
```bash
python nome_do_arquivo.py
```

Caso algum problema ocorra, pode ser o endereçamento da sua câmera. A alteração pode ser feita aqui:
```python
cap = cv2.VideoCapture(0)
```
Se estiver em um notebook, "0" é o endereço da câmera imbutida do aparelho. Se outra câmera for usada, o endereço dela pode mudar para "1" (ou "2" ou "3"...)

3. **Interagir com a Janela**: O vídeo da câmera será exibido em uma janela chamada "Window". A cor predominante (ou a ausência de cores) ou a mensagem "Todas as cores!" (caso todas as cores sejam detectadas) deverá ser exibida na tela.

4. **Finalizar:** Para parar a execução do script, pressione a tecla 'q'.

# Detecção de Cores com Arduino + Python
No projeto, há um diretório chamado "serial_version"

Nele, o scrip foi alterado para mandar caracteres em serial para um Arduino. O objetivo é fazer um led da mesma cor identificada acender, enquanto essa cor é narrada.

# Como usar
Acomode os terminais... (há um erro no playsound)

## Licença
Este projeto é distribuído sob a [Licença MIT](LICENSE).