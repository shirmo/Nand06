// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Sort.asm

// Sorts R[R[14]] decendingally, R14 stores the register of the array and R15 stores the length of the array.

// Put your code here.
	@R15
	D=M
	@n
	M=D // n = length(arr)
	@i
	M=1 // initializing loop index i=1 

 (LOOP1)
	@i
	D=M // D is index
	@n
	D=D-M
	@STOP1
	D;JGT 
	// id i>n goto STOP1
	
	@n
	D=M
	@i
	D=D-M
	@m
	M=D // initializing second loop length
	@j
	M=0 //init index 2
	
  (LOOP2)
	@j
	M=M+1 // incrementing index
	
	@j
	D=M // D is index
	@m
	D=D-M
	@STOP2
	D;JGT // if j>m goto STOP1
  
	@j
	D=M
	@R14
	D=D+M // The wanted arr index
	A=D-1
	D=M
	@left
	M=D
	
	@j
	D=M
	@R14
	D=D+M // The wanted arr index for comparison
	A=D
	D=M
	@right
	M=D
	
	//comparison
	@left 
	D=M
	@right
	D=D-M
	@LOOP2
	D;JGT 
	//if arr[j+place-1] > arr[j+place-1] don't do swap
	
	//SWAP
	@left
	D=M
	@temp
	M=D // temp = left
	
	@j
	D=M
	@R14
	D=D+M // The wanted arr index
	@indexL
	M=D-1
	
	@right
	D=M
	@indexL
	A=M
	M=D
	
	@j
	D=M
	@R14
	D=D+M // The wanted arr index for swaping
	@indexR
	M=D
	
	@temp
	D=M
	@indexR
	A=M
	M=D

	@LOOP2
	0;JMP 
	//return to loop2
	
  (STOP2)
	@i
	M=M+1 // incrementing index
	@LOOP1
	0;JMP
	
  (STOP1)
	
  (END)
	@END
	0;JMP
	