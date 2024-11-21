java = $(wildcard *.java)
javacompile = $(patsubst %.java, %.class, $(java))


$(javacompile): $(java)
	javac $(java)
