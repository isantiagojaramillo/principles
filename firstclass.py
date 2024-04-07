print("HELLO WORLD");

# COMMMENT

'''
COMMENTS

'''

age = 34;
true = True;

print(age);

print("My age is: " , age, true);

input = input("Enter something: ");

print(input);

print(5+8);

age = 25;

if age > 18:
  print("YOU'RE OVER 18");
else:
  print("you're under 18");

A = 3 + 6 * 14;

print(A);

B = 12 + 3 * 7 + 5 * 4;

print(B);

C = 7 * 8 % 2 *7 + 9;

print(C);

D = 7 * (10-5) - 34 % 3 * 5 + 7;

print(D);

E = 12 * 4 / 2 + (15 - 3) * 5  + 7;

print(E);

F = -16 + 3 * 6 + 14 * 8;

print(F);

A=4;
B=5;
C=1;

X = B * A - B**2 / 4 * C;

print(X);

Y = A * B / 3**2;

print(Y);

Z = (((B+C)/2*A+10)*3*B)-6;

print(Z);

A=4;
B=5;
C=1;

P=A**(1/2)**B;
print(P);

R=A*B+A**(1/2);
print(R);

S=B*A-B**2/4*C;
print(S);

A = 4;
B = 3;

X = A < B;
print(X);

Y = (A - 2 ) < (B + 5);
print(Y);

Z = A*(12-5) > B * 3;
print(Z);

D = A + B > B**2;
print(D);

X = 3;
Y = 3;

A = X > Y;
print(A);

B = X < 6.5;
print(B);

C = X >= 8;
print(C);

D = Y <= X + 2;
print(D);

print(type("Hola Mundo"));
print(type([1, 10, 100]));
print(type(-25));
print(type(["Hola", "Mundo"]));
print(type(' '));
print(type(1.167));

a = 10;
b = -5;
c = "Hola ";
d = [1, 2, 3];

print(a * 5);
print(a - b);
print(c + "Mundo");
print(c * 2);
print(d[-1]);
print(d[1:]);
print(d + d);

numero_1 = 9;
numero_2 = 3;
numero_3 = 6;

media = numero_1 + numero_2 + numero_3 / 3;
print("La nota media es", media);

number1 = input("Enter first number: ")
number2 = input("Enter second number: ")

number1 = int(number1);
number2 = int(number2);


if number1 == number2:
  print("Son iguales");
elif number1 != number2:
  print("Son diferentes");
elif number1 > number2:
  print("El primer número es mayor que el segundo");
elif number2 >= number1:
  print("El segundo número es mayor o igual que el primer número");