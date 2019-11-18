// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.\
	@R2
	M=0 // initializing space in memory
	@R0
	D=M // D = 	RAM[0]
	@n
	M=D // n = RAM[0]
	@i
	M=1 // initializing loop index i=1 
	@mult
	M=0 // mult = 0
 (LOOP)
	@i
	D=M // D is index
	@n
	D=D-M
	@STOP
	D;JGT // id i>n goto STOP
	
	@mult
	D=M
	@R1
	D=D+M
	@mult
	M=D // mult = mult + R1
	@i
	M=M+1 // incrementing index
	@LOOP
	0;JMP
	
  (STOP)
	@mult
	D=M
	@R2
	M=D // puting result in R2 - RAM[2] = mult
	
  (END)
	@END
	0;JMP
	