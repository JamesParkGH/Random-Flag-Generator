PY = python3
PYFLAGS = 
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = doxConfig

SRC = HashGenerator.py
SRCRUN = GUI.py

.PHONY: all prog doc clean

run:    
	$(PY) $(PYFLAGS) $(SRCRUN)

prog: 
	$(PY) $(PYFLAGS) $(SRC)

doc: 
	$(DOC) $(DOCFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: prog doc

clean:
	rm -rf html
	rm -rf latex
