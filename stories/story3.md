Sure! Here's a simple "Hello, World!" console application written in COBOL:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO-WORLD.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 MESSAGE PIC X(13) VALUE 'Hello, World!'.

PROCEDURE DIVISION.
    DISPLAY MESSAGE.
    STOP RUN.
```

In this COBOL program, the **IDENTIFICATION DIVISION** specifies the program's identity, while the **DATA DIVISION** defines the data used in the program. In this case, we have a single working storage variable named MESSAGE that holds the message "Hello, World!".

The **PROCEDURE DIVISION** contains the actual instructions executed by the program. The **DISPLAY** statement outputs the value of **MESSAGE** to the console. The **STOP RUN** statement terminates the program.

To compile and run this COBOL program, you'll need a COBOL compiler and runtime environment. There are several options available, such as GNU COBOL (GnuCOBOL), OpenCOBOL, or Micro Focus COBOL. Once you have a COBOL compiler installed, you can use it to compile the program and execute the resulting binary.

Keep in mind that the specifics of setting up and running COBOL programs can vary depending on the compiler and platform you're using. Make sure to consult the documentation or resources specific to your environment for detailed instructions on compiling and executing COBOL code.
