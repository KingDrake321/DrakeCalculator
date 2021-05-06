#welcome screen

print("Drake's Calculator 2.0 ")
print("")
langu = input("English or Espanol: ")



if (langu == "English"):
    print("English Selected")
    EngOper = input("What Operator: |/|*|-|+|  ")
    num1Eng = float(input("What is First Number:  "))
    num2Eng = float(input("What is Second Number:   "))
    if (EngOper == "/"):
        print("Division")
        print(num1Eng / num2Eng)
    
    if (EngOper == "*"):
        print("Multiplcation")
        print(num1Eng * num2Eng)
    
    if (EngOper == "-"):
        print("Subtraction")
        print(num1Eng - num2Eng)
        
    if (EngOper == "+"):
        print("Addition")
        print(num1Eng + num2Eng)
        
        
if (langu == "Espanol"):
    print("Español Seleccionado")
    SpanOper = input("Que Operador: |/|*|-|+|  ")
    num1Span = float(input("Cual Es El Primer Numero:  "))
    num2Span = float(input("Cual Es El Segundo Numero:   "))
    if (SpanOper == "/"):
        print("División")
        print(num1Span / num2Span)
    
    if (SpanOper == "*"):
        print("Multiplicación")
        print(num1Span * num2Span)
    
    if (SpanOper == "-"):
        print("Sustracción")
        print(num1Span - num2Span)
        
    if (SpanOper == "+"):
        print("Adición")
        print(num1Span + num2Span)
        
    
    
#operator assingment

    
