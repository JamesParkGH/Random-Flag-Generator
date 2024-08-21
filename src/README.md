# Random Flag Generator (RFG) Source Code

The folders and files for this project are as follows:

Folders:
---

**.vs:** sqlite package files

**ImagesGUI:** image files for GUI elements; logos, buttons, etc.

**jka:** flag asset files for flag generation; low, mid and high resolution assets included

Source Code Files:
---

**DecisionUtilities.py:** A collection of modules used by HashToFlag to grind the hashcode and map decisions to arrays

**Display.py:** A dispay option to display the generated flag

**FlagAssetsLib.py:** A library of constants and symbol/design options

**FlagGenerator.py:** A module for generating the flag image using a given input string and hashing algorithm

**GUI.py:** A graphical user interface module uses all other modules to allow the user to communicate with the Random Flag Generator software

**Gallery.py:** A gallery to showcase all the generated flags

**HashGenerator.py:** A library module for getting the hexidecimal hash of a given string

**HashToFlag:** A module with functions for taking a given hashcode input and generating the options for the flag to be generated.

**Help.py:** A help option teach the user how to use the software and giving more information of it

**JKAReader.py:** A library module for parsing .jka files for use in generating flags

**Settings.py:** A settings option to select differnt flag size, set certain features, such as colour, symbols, stripes, and select different hash type


Testing Files:
---

**TestDecisionUtilities.py:** Tests implementation of the DecisionUtilities library helper functions

**TestFlagGenerator.py:** Tests implementation of FlagGenerator for generating flag image files from given input strings and hashing algorithm string names

**TestGUI.py:**

**TestHashGenerator.py:** Tests implementation of HashGenerator for generating hexidecimal hash digests from given input strings and hashing algorithms

**TestHashToFlag.py:** Tests implementation of the HashToFlag library helper functions

**TestJKAReader.py:** Tests implementation of JKAReader for parsing .jka flag asset files into a usable form for flag generation


Other Files:
---

**Makefile:** For running the Random Flag Generator (RFG) program, generating/cleaning up documentation

**doxConfig:** For configuring the doxygen commenting documentation generation
