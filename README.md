# 🎛️ Painel de LEDs Interativo com ESP32-S2

Este projeto consiste em um sistema interativo de controle de iluminação desenvolvido em **MicroPython** para a placa **ESP32-S2**. Utilizando três botões e três LEDs (Vermelho, Verde e Azul), o usuário pode disparar diferentes modos de animação e sequências luminosas temporizadas.

O projeto foi estruturado e testado utilizando o simulador eletrônico **Wokwi**.

imagem

Abaixo estão listados os componentes utilizados no circuito:

* **Placa Principal:** ESP32-S2 DevKitM-1
* **LEDs:**
    * `led1`: Vermelho (Conectado ao pino **GPIO 14**)
    * `led2`: Verde (Conectado ao pino **GPIO 12**)
    * `led3`: Azul (Conectado ao pino **GPIO 13**)
* **Componentes de Entrada e Proteção:**
    * 3 Botões do tipo Pushbutton (Conectados com resistor interno de *Pull-Up*)
    * 3 Resistores de $65\ \Omega$ para limitação de corrente dos LEDs.

### Mapeamento de Pinos (GPIOs)

| Componente | Pino ESP32-S2 | Função no Código |
| :--- | :--- | :--- |
| **Botão 1 (Vermelho)** | GPIO 21 | Ativa a Sequência Temporizada (Semáforo) |
| **Botão 2 (Verde)** | GPIO 26 | Ativa a Sequência Cumulativa Rápida |
| **Botão 3 (Azul)** | GPIO 33 | Ativa o Modo Pisca-Pisca Geral (Strobo) |
| **LED 1 (Vermelho)** | GPIO 14 | Saída Digital |
| **LED 2 (Verde)** | GPIO 12 | Saída Digital |
| **LED 3 (Azul)** | GPIO 13 | Saída Digital |

---

## 🕹️ Modos de Operação (`main.py`)

O código roda em um loop contínuo e monitora o pressionamento dos botões (nível lógico `0` / `LOW` devido ao Pull-Up). Cada botão ativa um comportamento diferente:

### 🔴 Botão 1: Modo Sequência Temporizada (Estilo Semáforo)
Enquanto o botão estiver pressionado, executa um ciclo rígido de temporização:
1. Acende apenas o **LED Vermelho** por **3 segundos**.
2. Acende apenas o **LED Verde** por **5 segundos**.
3. Acende apenas o **LED Azul** por **1 segundo**.

### 🟢 Botão 2: Modo Sequência Cumulativa Rápida
Gera um efeito de preenchimento e esvaziamento rápido:
1. Acende o **LED Vermelho**.
2. Mantém o anterior e acende também o **LED Verde** (após 0.5s).
3. Mantém os anteriores e acende o **LED Azul** (após mais 0.5s).
4. Apaga todos os LEDs por 0.5 segundos antes de reiniciar o ciclo.

### 🔵 Botão 3: Modo Strobo Geral
Faz todos os LEDs agirem em uníssono:
1. Acende o **LED Vermelho, Verde e Azul** simultaneamente por **2 segundos**.
2. Apaga todos os LEDs simultaneamente por **1 segundo**.

---
