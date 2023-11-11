# [Codember 2023](https://codember.dev/)

## 01 - The Challenge
A spy is sending encrypted messages.

Your mission is to create a program that decodes the messages.

The messages are words separated by spaces like this:
 
```text
cat dog dog car Cat doG sun
```

We need the program to return the number of times each word appears in the message, regardless of whether it is in uppercase or lowercase.

The result will be a text string with the word and the number of times it appears in the message, in this format:

```text 
cat2dog3car1sun1
```

The words are sorted by their first appearance in the message!

### Examples

```text
keys house HOUSE house keys -> keys2house3
```

```text
cup te a cup -> cup2te1a1
```

```text
houses house housess -> houses1house1housess1
```

### Run solution

```bash
cat input_challenge_01.txt | python challenge_01.py
```


## 02 - Mini Compiler Challenge

In the world of espionage, a coding language is used with symbols that perform simple mathematical operations.

Your task is to create a mini compiler that interprets and executes programs written in this symbol language.

The operations of the language are as follows:

```text
"#" Increases the numeric value by 1.
"@" Decreases the numeric value by 1.
"*" Multiplies the numeric value by itself.
"&" Prints the current numeric value.
```

The initial numeric value is 0 and the operations should be applied in the order in which they appear in the string of symbols.

### Examples
```text
Input: "##*&"
Expected Output: "4"
Explanation: Increment (1), increment (2), multiply (4), print (4).
```

```text
Input: "&##&*&@&"
Expected Output: "0243"
Explanation: Print (0), increment (1), increment (2), print (2), multiply (4), print (4), decrement (3), print (3).
```

### Run solution

```bash
cat input_challenge_02.txt | python challenge_02.py
```