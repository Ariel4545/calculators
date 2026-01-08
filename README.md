# Egon Calculators

![My project-1 (1)(1)](https://user-images.githubusercontent.com/95249974/182220333-0305942e-f94e-4d2f-a8dc-610f376f8a65.png)

## 🔱 Purpose
The goal of this project is to provide a variety of calculators, each demonstrating different approaches to solving mathematical problems and UI design. Over time, these implementations have evolved to become more efficient and user-friendly.

## 🖩 Available Calculators

### 1. Basic Calculator
A robust standard calculator for everyday arithmetic.
- **Remastered Version (`EgonCalc-Remastered.py`):**
  - Modern UI with `customtkinter`.
  - **Themes:** Switch between Light and Dark modes.
  - **Resizable UI:** Choose from Small, Medium, or Big window sizes.
  - **Calculation Modes:** 
    - *One at a time*: Traditional step-by-step calculation.
    - *All at once*: Type the full expression and evaluate it.
- **Standard Version (`standards/EgonCalc.py`):**
  - Classic `tkinter` implementation.
  - Basic arithmetic operations.

### 2. Number Base Calculator
A specialized tool for programmers and computer science enthusiasts.
- **Remastered Version (`EgonBaseCalc-Remastered.py`):**
  - Supports **Decimal, Binary, Octal, and Hexadecimal** number systems.
  - **Base Conversion:** Automatically converts the current number when switching bases.
  - **Input Validation:** Restricts button inputs based on the selected base (e.g., only 0-1 for Binary).
  - Customizable appearance (Themes & Sizes).
- **Standard Version (`standards/EgonBaseCalc.py`):**
  - Classic `tkinter` implementation for base conversions.

### 3. Scientific Calculator
An advanced calculator for more complex mathematical needs.
- **Remastered Version (`EgonScientificCalc-Remastered.py`):**
  - **Trigonometry:** Sine, Cosine, Tangent.
  - **Advanced Math:** Square Root (√), Power (^), Exponential (exp), Factorial (!n), Absolute Value (|X|).
  - **Utilities:** Random Integer generator (randint).
  - Supports both immediate and expression-based calculation modes.
- **Standard Version (`standards/EgonScientificCalc.py`):**
  - Classic `tkinter` implementation with scientific functions.

![EC-preview](https://user-images.githubusercontent.com/95249974/198843916-a0348631-d197-49d0-9ad3-386d79ad5220.png)

## 🛠️ Built With
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /> 
<img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/CustomTkinter-UI-blue?style=for-the-badge" />

## 💻 Installation & Usage

1. **Prerequisites**: Ensure you have Python installed.
2. **Install Dependencies**: The remastered versions use `customtkinter` for the UI.
   ```bash
   pip install customtkinter
   ```
3. **Run**: Execute the python script for the calculator you wish to use.
   ```bash
   # For the remastered basic calculator
   python EgonCalc-Remastered.py
   
   # For the standard basic calculator
   python standards/EgonCalc.py
   ```

## 🧪 Tested On
<img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
