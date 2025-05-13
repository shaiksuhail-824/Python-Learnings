#Write a program to print all alphabets from a to z.
for i in range(97,123):
    print(chr(i),end=" ")
print()
for x in range(122,96,-1):
    print(chr(x),end=' ')
print()
for x in range(65,91):
    print(chr(x),end=' ')
print()
for x in range(90,64,-1):
    print(chr(x),end=' ')
#output
'''a b c d e f g h i j k l m n o p q r s t u v w x y z 
z y x w v u t s r q p o n m l k j i h g f e d c b a 
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
Z Y X W V U T S R Q P O N M L K J I H G F E D C B A'''