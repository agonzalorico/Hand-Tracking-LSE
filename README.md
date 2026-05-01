# ✋ Hand Gesture Alphabet Recognition (Spanish Sign Language - LSE)

> ⚠️ This project is based on **Spanish Sign Language (Lengua de Signos Española, LSE)**

---

## 🇬🇧 English

### 📌 Description

This project uses OpenCV for computer vision and MediaPipe to track hand landmarks and identify signs of the Spanish Sign Language (LSE) alphabet.
Currently it can detect every letter that is signed with a static gesture (no movement during the sign), except the letter T due to limitations in the MediaPipe ability to propertly detect the hand during that position.
Current letters available: A, B, C, D, E, F, G, I, K, L, M, N, O, P, Q, R, S, U, W
Missing letters: H, J, LL, RR, T, V, X, Y, Z


### 🧠 How it works

* When the program detects a hand onscreen MediaPipe extracts 21 hand landmarks (x, y, z)
* Using the relative position of these landmarks the program tries to assign that gesture to a letter using the LSE alphabet
--- 

### 🚀 Features

* Real-time hand tracking
* Landmark visualization (points and connections)
* Static gesture recognition

---

### ⚠️ Project Status

🚧 Work in progress

The program now is a first prototype, with some bugs and a lot of work needed, next I will indicate what are the plans for the future of this program.

**Planned:**

* Improve the robustness of each letter, adjust landmarks so that when a different gesture is detected the program will not assign it to an incorrect letter
* Try aplying Machine learning for the most challenging letters, like the T and the ones that require dynamic sings.
* Improve the code
* Full LSE alphabet support
* Improved UI and feedback system
* Add a function in which the user can spell a word using LSE and the program writes it.

---

### 🛠️ Installation

```bash
pip install -r requirements.txt
```

---

### ▶️ Usage

```bash
python LSE_video.py
```

---


### 🤝 Contributing

Contributions, ideas, and feedback are welcome!

---

## 🇪🇸 Español

### 📌 Descripción

Este proyecto utiliza vision artificial con OpenCV y MediaPipe para rastrear puntos de referencia en la mano e identificar signos del alfabeto dactilologico la Lengua de Signos Española (LSE).

Actualmente puede detectar todas las letras que se signan con un gesto estático (no se requiere movimiento para signar), excepto la letra T debido a limitaciones de MediaPipe a la hora de identificar de forma adecuada los puntos de referencia de la mano para ese gesto.

Letras disponibles actualmente: A, B, C, D, E, F, G, I, K, L, M, N, O, P, Q, R, S, U, W
Letras aún sin añadir: H, J, LL, RR, Ñ, T, V, X, Y, Z

### 🧠 Como funciona

* Cuando el program detecta una mano en la pantalla Mediapipe obtiene 21 puntos de referencia (x,y,z)
* Usando la posición relativa de estos puntos de referencia el programa intenta asignar al gesto obtenido una letra usando el alfabeto dactilologico del LSE.
--- 
### 🚀 Características

* Seguimiento de manos en tiempo real
* Visualización de puntos y conexiones
* Reconocimiento de gestos estáticos

---

### ⚠️ Estado del proyecto

🚧 En desarrollo

El programa es actualmente un primer prototipo, con algunos errores y mucho trabajo por realizar, a continuación indicaré los planes para el futuro de este proyecto

**Planificado:**

* Mejorar la robustez de cada letra, ajustar los puntos de referencia para que no se asignen letras incorrectas
* Mejorar el código
* Intentar utilizar modelos de machine learning para letras más complicadas como la T y las que requieren signos dinámicos.
* Mejorar la interfaz
* Conseguir poder analizar todas las letras del alfabeto dactilologico.
* Añadir una función para que el usuario pueda deletrear una palabra y el programa la escriba


### 🛠️ Instalación

```bash
pip install -r requirements.txt
```

---

---

### 🤝 Contribuciones

¡Se aceptan ideas, sugerencias y contribuciones!

---

