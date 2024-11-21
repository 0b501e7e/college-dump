java = $(wildcard *.java)
javacompile = $(patsubst %.java, %.class, $(java))
classfile = $(wildcard *.class)

$(javacompile): $(java)
	javac $(java)

clean: $(classfile) 
	rm -f $(javacompile)

.PHONY: clean
