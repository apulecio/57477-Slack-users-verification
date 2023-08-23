# User Duplication Checker

This Python program is designed to process a list of usernames and their corresponding statuses to identify usernames that appear twice with the "Member" status. It achieves this by performing two key functions:

1. `eliminar_numeros(lista)`: This function takes a list of strings as input and removes any numerical digits from each string using regular expressions.

2. `usuarios_repetidos_con_estado(username, status)`: This function takes two lists as input - a list of usernames and a list of statuses. It then counts how many times each user appears with the "Member" status and returns a list of usernames that appear twice with this status.

## Usage

To use this program, you can follow these steps:

1. Define your list of usernames and statuses.

```python
username = ['996589', 'anthony.vanwinkle', '997406']
states = ['Deactivated', 'Member', 'Deactivated']
username_without_numbers = eliminar_numeros(username)
result = usuarios_repetidos_con_estado(username_without_numbers, states)
print(result)
```

## Example
In the provided example, the program processes the username list, removes numerical digits, and then checks for usernames that repeat twice with the "Member" status. The results are printed to the console.

## Dependencies
This program uses the re module for regular expression operations. There are no external dependencies.