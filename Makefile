##
## EPITECH PROJECT, 2020
## math
## File description:
## Makefile
##

SRC	    =	./src/main.py
TARGET  =   the_father

all:
	@ cp $(SRC) $(TARGET)
	@ chmod +x $(TARGET)

clean:
	@ $(RM) $(TARGET)

re: clean all