# Python Interview Tasks Repository

This repository contains a collection of Python interview tasks categorized into **Junior**, **Mid**, and **Senior** levels. Each level is further divided into various sections covering different aspects of Python programming.

## Table of Contents

- [File Structure](#file-structure)
- [Junior Level](#junior-level)
  - [Core Python Tasks](#core-python-tasks)
  - [Data Structures and Algorithms](#data-structures-and-algorithms)
  - [File Handling and Data Manipulation](#file-handling-and-data-manipulation)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
  - [Real-World Applications](#real-world-applications)
  - [Basic Testing and Debugging](#basic-testing-and-debugging)
- [Mid Level](#mid-level)
  - [Core Python Tasks](#core-python-tasks-1)
  - [Data Structures and Algorithms](#data-structures-and-algorithms-1)
  - [Object-Oriented Programming](#object-oriented-programming)
  - [File Handling and Data Manipulation](#file-handling-and-data-manipulation-1)
  - [Real-World Applications](#real-world-applications-1)
  - [Testing and Debugging](#testing-and-debugging)
- [Senior Level](#senior-level)
  - [Advanced Core Python and System Design](#advanced-core-python-and-system-design)
  - [Concurrency and Asynchronous Programming](#concurrency-and-asynchronous-programming)
  - [Data Structures, Algorithms, and Big Data](#data-structures-algorithms-and-big-data)
  - [Software Engineering, Architecture, and System Design](#software-engineering-architecture-and-system-design)
  - [Bonus: System Monitoring, Security, and Testing](#bonus-system-monitoring-security-and-testing)

---

## File Structure

The repository is organized as follows:

```
├── junior/
│   ├── core_python_tasks/
│   │   ├── task1_largest_number.py
│   │   ├── task2_palindrome_check.py
│   │   ├── task11_sum_of_evens.py
│   │   ├── ...
│   ├── data_structures_and_algorithms/
│   │   ├── task1_anagram_check.py
│   │   ├── task2_even_numbers.py
│   │   ├── task11_merge_sorted_lists.py
│   │   ├── ...
│   ├── file_handling_and_data_manipulation/
│   │   ├── task1_file_copy.py
│   │   ├── task2_read_csv.py
│   │   ├── task11_read_every_other_line.py
│   │   ├── ...
│   ├── object_oriented_programming/
│   │   ├── task1_car_class.py
│   │   ├── task2_bank_account.py
│   │   ├── task6_rectangle_class.py
│   │   ├── ...
│   ├── real_world_applications/
│   │   ├── task1_todo_list_cli.py
│   │   ├── task2_api_fetch.py
│   │   ├── ...
│   └── basic_testing_and_debugging/
│       ├── task1_unit_tests.py
│       ├── task2_custom_exception.py
│       ├── ...
├── mid/
│   ├── core_python_tasks/
│   │   ├── task1_character_count.py
│   │   ├── task2_context_manager.py
│   │   ├── ...
│   ├── data_structures_and_algorithms/
│   │   ├── task1_binary_search.py
│   │   ├── task2_detect_cycle.py
│   │   ├── ...
│   ├── object_oriented_programming/
│   │   ├── task1_animal_hierarchy.py
│   │   ├── task2_singleton_pattern.py
│   │   ├── ...
│   ├── file_handling_and_data_manipulation/
│   │   ├── task1_csv_to_dict.py
│   │   ├── task2_top_words.py
│   │   ├── ...
│   ├── real_world_applications/
│   │   ├── task1_send_email.py
│   │   ├── task2_download_urls.py
│   │   ├── ...
│   └── testing_and_debugging/
│       ├── task1_unit_tests.py
│       ├── task2_api_test_suite.py
│       ├── ...
├── senior/
│   ├── advanced_core_python_and_system_design/
│   │   ├── task1_distributed_cache.py
│   │   ├── task2_thread_safe_singleton.py
│   │   ├── ...
│   ├── concurrency_and_asynchronous_programming/
│   │   ├── task1_scalable_web_scraper.py
│   │   ├── task2_sha256_parallel.py
│   │   ├── ...
│   ├── data_structures_algorithms_and_big_data/
│   │   ├── task1_trie_implementation.py
│   │   ├── task2_a_star_search.py
│   │   ├── ...
│   ├── software_engineering_architecture_and_system_design/
│   │   ├── task1_soa_design.py
│   │   ├── task2_consistent_hashing.py
│   │   ├── ...
│   └── bonus_system_monitoring_security_and_testing/
│       ├── task1_real_time_monitoring.py
│       ├── task2_security_module.py
│       ├── ...
└── README.md
```

---

## Junior Level

### Core Python Tasks

1. **Write a Python function that takes a list of numbers and returns the largest number.**
   - [Solution](junior/core_python_tasks/task1_largest_number.py)

2. **Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).**
   - [Solution](junior/core_python_tasks/task2_palindrome_check.py)

3. **Create a Python script that reads a text file and counts the number of lines, words, and characters in it.**
   - [Solution](junior/core_python_tasks/task3_file_statistics.py)

4. **Write a function that removes duplicates from a list while preserving the order.**
   - [Solution](junior/core_python_tasks/task4_remove_duplicates.py)

5. **Write a Python function that reverses the words in a given sentence.**
   - [Solution](junior/core_python_tasks/task5_reverse_sentence.py)

6. **Write a function that takes two lists and returns their intersection (common elements).**
   - [Solution](junior/core_python_tasks/task6_list_intersection.py)

7. **Create a Python function that finds the factorial of a number using both recursion and iteration.**
   - [Solution](junior/core_python_tasks/task7_factorial.py)

8. **Write a program that generates the first `n` numbers in the Fibonacci sequence.**
   - [Solution](junior/core_python_tasks/task8_fibonacci_sequence.py)

9. **Create a function that converts a string to title case (the first letter of each word is capitalized).**
   - [Solution](junior/core_python_tasks/task9_title_case.py)

10. **Write a Python script that calculates the sum of the digits of a given integer.**
    - [Solution](junior/core_python_tasks/task10_sum_of_digits.py)

11. **Write a Python function that returns the sum of all even numbers in a list.**
    - [Solution](junior/core_python_tasks/task11_sum_of_evens.py)

12. **Write a Python function that converts a list of integers to a list of their squares.**
    - [Solution](junior/core_python_tasks/task12_list_of_squares.py)

13. **Create a Python function that finds the maximum difference between any two elements in a list.**
    - [Solution](junior/core_python_tasks/task13_max_difference.py)

14. **Write a function that rotates a list to the right by `n` positions.**
    - [Solution](junior/core_python_tasks/task14_rotate_list.py)

15. **Write a function that takes a string and returns the number of vowels in the string.**
    - [Solution](junior/core_python_tasks/task15_count_vowels.py)

16. **Write a function that takes a list of strings and returns the longest string.**
    - [Solution](junior/core_python_tasks/task16_longest_string.py)

17. **Write a Python function that reverses a string without using built-in reverse functions.**
    - [Solution](junior/core_python_tasks/task17_reverse_string.py)

18. **Write a function to check if a number is a perfect square.**
    - [Solution](junior/core_python_tasks/task18_perfect_square.py)

19. **Write a function that takes a sentence and removes all the punctuation.**
    - [Solution](junior/core_python_tasks/task19_remove_punctuation.py)

20. **Create a function that counts how many times a character appears in a string.**
    - [Solution](junior/core_python_tasks/task20_character_frequency.py)

---

### Data Structures and Algorithms

1. **Write a Python function to check if two strings are anagrams (contain the same characters in a different order).**
   - [Solution](junior/data_structures_and_algorithms/task1_anagram_check.py)

2. **Write a function that takes a list of integers and returns a list of even numbers.**
   - [Solution](junior/data_structures_and_algorithms/task2_even_numbers.py)

3. **Implement bubble sort in Python to sort a list of numbers in ascending order.**
   - [Solution](junior/data_structures_and_algorithms/task3_bubble_sort.py)

4. **Write a function that finds the second largest number in a list.**
   - [Solution](junior/data_structures_and_algorithms/task4_second_largest.py)

5. **Create a Python function that checks if a number is prime.**
   - [Solution](junior/data_structures_and_algorithms/task5_prime_check.py)

6. **Write a function to find the GCD (Greatest Common Divisor) of two numbers using recursion.**
   - [Solution](junior/data_structures_and_algorithms/task6_gcd.py)

7. **Implement binary search in Python to search for an element in a sorted list.**
   - [Solution](junior/data_structures_and_algorithms/task7_binary_search.py)

8. **Write a function that returns the first non-repeating character in a string.**
   - [Solution](junior/data_structures_and_algorithms/task8_first_non_repeating.py)

9. **Create a function that generates all permutations of a given string.**
   - [Solution](junior/data_structures_and_algorithms/task9_string_permutations.py)

10. **Write a function that calculates the sum of all elements in a nested list (list of lists).**
    - [Solution](junior/data_structures_and_algorithms/task10_nested_list_sum.py)

11. **Write a function that merges two sorted lists into one sorted list without using the built-in sort function.**
    - [Solution](junior/data_structures_and_algorithms/task11_merge_sorted_lists.py)

12. **Implement the selection sort algorithm in Python to sort a list of numbers.**
    - [Solution](junior/data_structures_and_algorithms/task12_selection_sort.py)

13. **Write a function to check if a string contains only unique characters.**
    - [Solution](junior/data_structures_and_algorithms/task13_unique_characters.py)

14. **Write a function that removes the nth element from a list.**
    - [Solution](junior/data_structures_and_algorithms/task14_remove_nth_element.py)

15. **Implement the insertion sort algorithm in Python to sort a list of numbers.**
    - [Solution](junior/data_structures_and_algorithms/task15_insertion_sort.py)

16. **Write a Python function that rotates a matrix (2D list) by 90 degrees.**
    - [Solution](junior/data_structures_and_algorithms/task16_rotate_matrix.py)

17. **Write a function that checks whether a string has balanced brackets (parentheses, curly braces, etc.).**
    - [Solution](junior/data_structures_and_algorithms/task17_balanced_brackets.py)

18. **Write a Python function that merges two dictionaries, combining values for matching keys.**
    - [Solution](junior/data_structures_and_algorithms/task18_merge_dictionaries.py)

19. **Write a function to find the middle element of a linked list (you can use a list to simulate this).**
    - [Solution](junior/data_structures_and_algorithms/task19_middle_element.py)

20. **Write a function that returns the maximum depth (or height) of a binary tree (use nested lists to simulate this).**
    - [Solution](junior/data_structures_and_algorithms/task20_binary_tree_depth.py)

---

### File Handling and Data Manipulation

1. **Write a Python script to copy the contents of one file to another.**
   - [Solution](junior/file_handling_and_data_manipulation/task1_file_copy.py)

2. **Write a function that reads a CSV file and prints its content row by row.**
   - [Solution](junior/file_handling_and_data_manipulation/task2_read_csv.py)

3. **Create a Python function that renames all files in a directory by adding a suffix to their names.**
   - [Solution](junior/file_handling_and_data_manipulation/task3_rename_files.py)

4. **Write a function that reads a file and counts the frequency of each word.**
   - [Solution](junior/file_handling_and_data_manipulation/task4_word_frequency.py)

5. **Write a script that reads a log file and extracts lines containing a specific keyword.**
   - [Solution](junior/file_handling_and_data_manipulation/task5_extract_keyword_lines.py)

6. **Create a Python script that lists all files and subdirectories in a given directory.**
   - [Solution](junior/file_handling_and_data_manipulation/task6_list_directory.py)

7. **Write a function that takes a list of dictionaries and writes it to a CSV file.**
   - [Solution](junior/file_handling_and_data_manipulation/task7_dict_to_csv.py)

8. **Write a function that reads a JSON file and prints the data in a formatted way (pretty-printing).**
   - [Solution](junior/file_handling_and_data_manipulation/task8_pretty_print_json.py)

9. **Create a Python function to find and replace a word in a text file.**
   - [Solution](junior/file_handling_and_data_manipulation/task9_find_replace.py)

10. **Write a function that reads multiple text files and concatenates them into a single file.**
    - [Solution](junior/file_handling_and_data_manipulation/task10_concatenate_files.py)

11. **Write a Python script that reads a text file and prints every other line.**
    - [Solution](junior/file_handling_and_data_manipulation/task11_read_every_other_line.py)

12. **Write a function that reads a text file and removes all blank lines.**
    - [Solution](junior/file_handling_and_data_manipulation/task12_remove_blank_lines.py)

13. **Create a Python function that counts the frequency of each letter in a file and prints the top 5 most common letters.**
    - [Solution](junior/file_handling_and_data_manipulation/task13_letter_frequency.py)

14. **Write a Python function that reads a file and converts its contents to uppercase and writes it to a new file.**
    - [Solution](junior/file_handling_and_data_manipulation/task14_uppercase_contents.py)

15. **Write a function that reads a CSV file and prints out the rows that meet a specific condition (e.g., all rows where age > 30).**
    - [Solution](junior/file_handling_and_data_manipulation/task15_filter_csv.py)

16. **Write a script that reads a JSON file, adds a new key-value pair to each entry, and writes the result to a new file.**
    - [Solution](junior/file_handling_and_data_manipulation/task16_modify_json.py)

17. **Write a function that reads a text file and replaces all occurrences of a given word with another word.**
    - [Solution](junior/file_handling_and_data_manipulation/task17_replace_word.py)

18. **Create a script that reads an image file (e.g., JPEG) and converts it to grayscale (you can use PIL for this).**
    - [Solution](junior/file_handling_and_data_manipulation/task18_image_to_grayscale.py)

19. **Write a script that reads a CSV file and converts it into a list of dictionaries.**
    - [Solution](junior/file_handling_and_data_manipulation/task19_csv_to_list_of_dicts.py)

20. **Write a Python function that appends text to an existing file, creating the file if it doesn’t exist.**
    - [Solution](junior/file_handling_and_data_manipulation/task20_append_text.py)

---

### Object-Oriented Programming (OOP)

1. **Create a class `Car` that has attributes like `make`, `model`, and `year` and a method to display its information.**
   - [Solution](junior/object_oriented_programming/task1_car_class.py)

2. **Write a class `BankAccount` with methods to `deposit`, `withdraw`, and check the balance.**
   - [Solution](junior/object_oriented_programming/task2_bank_account.py)

3. **Create a class hierarchy with a base class `Animal` and derived classes like `Dog` and `Cat` that override the `speak()` method.**
   - [Solution](junior/object_oriented_programming/task3_animal_hierarchy.py)

4. **Write a class `Circle` that takes a radius as input and has methods to calculate the area and circumference.**
   - [Solution](junior/object_oriented_programming/task4_circle_class.py)

5. **Write a Python class that implements a simple stack with push and pop operations.**
   - [Solution](junior/object_oriented_programming/task5_stack_class.py)

6. **Create a class `Rectangle` with methods to calculate the area and perimeter of a rectangle.**
   - [Solution](junior/object_oriented_programming/task6_rectangle_class.py)

7. **Write a class `Student` that has attributes `name` and `age` and a method that prints the student’s information.**
   - [Solution](junior/object_oriented_programming/task7_student_class.py)

8. **Create a class hierarchy for geometric shapes: `Shape` (base class), `Square`, and `Triangle` (derived classes), and implement an `area()` method for each.**
   - [Solution](junior/object_oriented_programming/task8_shape_hierarchy.py)

9. **Write a class `ShoppingCart` that allows adding, removing, and viewing items in the cart, along with calculating the total price.**
   - [Solution](junior/object_oriented_programming/task9_shopping_cart.py)

10. **Write a class `Employee` with attributes `name`, `salary`, and `department`, and methods to update and print employee details.**
    - [Solution](junior/object_oriented_programming/task10_employee_class.py)

---

### Real-World Applications

1. **Create a simple command-line to-do list application that allows the user to add, delete, and view tasks.**
   - [Solution](junior/real_world_applications/task1_todo_list_cli.py)

2. **Write a Python script to fetch data from a public API (like weather data) and display it in a readable format.**
   - [Solution](junior/real_world_applications/task2_api_fetch.py)

3. **Create a basic web scraper using `requests` and `BeautifulSoup` to extract headlines from a news website.**
   - [Solution](junior/real_world_applications/task3_web_scraper.py)

4. **Write a Python program that simulates a simple calculator with basic operations like addition, subtraction, multiplication, and division.**
   - [Solution](junior/real_world_applications/task4_calculator.py)

5. **Build a simple CLI tool that generates a random password of a given length.**
   - [Solution](junior/real_world_applications/task5_password_generator.py)

6. **Write a Python script to send an email with an attachment using `smtplib`.**
   - [Solution](junior/real_world_applications/task6_send_email.py)

7. **Create a Python program that accepts a list of URLs and downloads the content from each one (use `requests`).**
   - [Solution](junior/real_world_applications/task7_download_urls.py)

8. **Write a Python script that extracts and prints all email addresses from a text file using regular expressions.**
   - [Solution](junior/real_world_applications/task8_extract_emails.py)

9. **Create a Python function that checks if a website is online by sending an HTTP request and analyzing the status code.**
   - [Solution](junior/real_world_applications/task9_website_status.py)

10. **Create a simple command-line calculator that supports addition, subtraction, multiplication, and division.**
    - [Solution](junior/real_world_applications/task10_cli_calculator.py)

---

### Basic Testing and Debugging

1. **Write a few unit tests for a Python function using `unittest`.**
   - [Solution](junior/basic_testing_and_debugging/task1_unit_tests.py)

2. **Write a function that raises a custom exception when invalid input is provided and handle that exception.**
   - [Solution](junior/basic_testing_and_debugging/task2_custom_exception.py)

3. **Use Python’s logging module to log errors and information in a script that processes data.**
   - [Solution](junior/basic_testing_and_debugging/task3_logging.py)

4. **Write a Python program that demonstrates the use of try-except to handle file I/O errors.**
   - [Solution](junior/basic_testing_and_debugging/task4_try_except.py)

5. **Use `pdb` (Python Debugger) to debug a Python script and trace through function calls.**
   - [Instructions](junior/basic_testing_and_debugging/task5_pdb_debugging.md)

---

## Mid Level

### Core Python Tasks

1. **Create a function that takes a string and returns a dictionary with the count of each character.**
   - [Solution](mid/core_python_tasks/task1_character_count.py)

2. **Implement a class-based context manager for opening and closing a file.**
   - [Solution](mid/core_python_tasks/task2_context_manager.py)

3. **Write a decorator that logs the execution time of a function.**
   - [Solution](mid/core_python_tasks/task3_execution_time_decorator.py)

4. **Write a function to flatten a nested list, e.g., `[[1,2,[3]],4] -> [1,2,3,4]`.**
   - [Solution](mid/core_python_tasks/task4_flatten_list.py)

5. **Create a generator function that yields the Fibonacci sequence.**
   - [Solution](mid/core_python_tasks/task5_fibonacci_generator.py)

6. **Write a function to merge two sorted lists into one sorted list without using built-in sort functions.**
   - [Solution](mid/core_python_tasks/task6_merge_sorted_lists.py)

7. **Explain and implement memoization in a recursive function for calculating factorials.**
   - [Solution](mid/core_python_tasks/task7_memoization_factorial.py)

8. **Create a thread-safe counter using Python’s `threading` library.**
   - [Solution](mid/core_python_tasks/task8_thread_safe_counter.py)

9. **Implement an LRU cache from scratch using a dictionary and a doubly linked list.**
   - [Solution](mid/core_python_tasks/task9_lru_cache.py)

10. **Write a function to validate if a given string is a valid IPv4 address.**
    - [Solution](mid/core_python_tasks/task10_validate_ipv4.py)

---

### Data Structures and Algorithms

1. **Implement a binary search algorithm for a sorted list.**
   - [Solution](mid/data_structures_and_algorithms/task1_binary_search.py)

2. **Write a function to detect a cycle in a linked list.**
   - [Solution](mid/data_structures_and_algorithms/task2_detect_cycle.py)

3. **Design and implement a min-heap in Python.**
   - [Solution](mid/data_structures_and_algorithms/task3_min_heap.py)

4. **Write a function that reverses a singly linked list.**
   - [Solution](mid/data_structures_and_algorithms/task4_reverse_linked_list.py)

5. **Write a function to determine if a string has balanced parentheses.**
   - [Solution](mid/data_structures_and_algorithms/task5_balanced_parentheses.py)

6. **Implement a function to find the longest common prefix in an array of strings.**
   - [Solution](mid/data_structures_and_algorithms/task6_longest_common_prefix.py)

7. **Implement a binary tree traversal (in-order, pre-order, and post-order).**
   - [Solution](mid/data_structures_and_algorithms/task7_binary_tree_traversal.py)

8. **Write a function to perform matrix multiplication for two 2D lists.**
   - [Solution](mid/data_structures_and_algorithms/task8_matrix_multiplication.py)

9. **Implement Dijkstra's algorithm for the shortest path in a weighted graph.**
   - [Solution](mid/data_structures_and_algorithms/task9_dijkstras_algorithm.py)

10. **Write a function to find all subsets (the power set) of a given list.**
    - [Solution](mid/data_structures_and_algorithms/task10_power_set.py)

---

### Object-Oriented Programming

1. **Design a class hierarchy for animals with a base class `Animal` and subclasses like `Mammal`, `Bird`, etc., with appropriate methods and properties.**
   - [Solution](mid/object_oriented_programming/task1_animal_hierarchy.py)

2. **Write an implementation of the Singleton design pattern in Python.**
   - [Solution](mid/object_oriented_programming/task2_singleton_pattern.py)

3. **Create an interface for a shape class and implement classes for `Circle`, `Rectangle`, and `Square` that inherit and override the methods.**
   - [Solution](mid/object_oriented_programming/task3_shape_interface.py)

4. **Write a function to serialize and deserialize a tree structure using JSON.**
   - [Solution](mid/object_oriented_programming/task4_serialize_tree.py)

5. **Create a class that implements a stack (with push, pop, peek methods) and supports a `get_min` method to retrieve the minimum element in O(1) time.**
   - [Solution](mid/object_oriented_programming/task5_min_stack.py)

---

### File Handling and Data Manipulation

1. **Write a Python script to read and parse a CSV file into a list of dictionaries.**
   - [Solution](mid/file_handling_and_data_manipulation/task1_csv_to_dict.py)

2. **Create a function that reads a large file and returns the top 10 most frequent words in the file.**
   - [Solution](mid/file_handling_and_data_manipulation/task2_top_words.py)

3. **Write a function that compresses and decompresses a file using `gzip` or `zipfile` libraries.**
   - [Solution](mid/file_handling_and_data_manipulation/task3_compress_decompress.py)

4. **Create a function to find and replace a word in a file without loading the whole file into memory.**
   - [Solution](mid/file_handling_and_data_manipulation/task4_inplace_replace.py)

5. **Write a script that lists all files in a directory, filters for a specific extension (e.g., `.py`), and outputs their sizes.**
   - [Solution](mid/file_handling_and_data_manipulation/task5_list_files.py)

---

### Real-World Applications

1. **Write a Python script to send an email with an attachment using `smtplib`.**
   - [Solution](mid/real_world_applications/task1_send_email.py)

2. **Create a Python program that accepts a list of URLs and downloads the content from each one (use `requests`).**
   - [Solution](mid/real_world_applications/task2_download_urls.py)

3. **Write a Python script that extracts and prints all email addresses from a text file using regular expressions.**
   - [Solution](mid/real_world_applications/task3_extract_emails.py)

4. **Create a Python function that checks if a website is online by sending an HTTP request and analyzing the status code.**
   - [Solution](mid/real_world_applications/task4_website_status.py)

5. **Create a simple command-line calculator that supports addition, subtraction, multiplication, and division.**
   - [Solution](mid/real_world_applications/task5_cli_calculator.py)

---

### Testing and Debugging

1. **Write unit tests for a Python class using `unittest` or `pytest`, including edge cases.**
   - [Solution](mid/testing_and_debugging/task1_unit_tests.py)

2. **Write a test suite for a REST API using `pytest` or `requests`, including tests for valid and invalid inputs.**
   - [Solution](mid/testing_and_debugging/task2_api_test_suite.py)

3. **Implement a function that raises a custom exception when invalid input is provided and write test cases to handle it.**
   - [Solution](mid/testing_and_debugging/task3_custom_exception_tests.py)

4. **Use `pdb` or another Python debugger to step through a script and inspect variable values at runtime.**
   - [Instructions](mid/testing_and_debugging/task4_debugging_instructions.md)

5. **Write a Python script that profiles the performance of a function using `cProfile` and optimizes the code based on the results.**
   - [Solution](mid/testing_and_debugging/task5_performance_profiling.py)

---

## Senior Level

### Advanced Core Python and System Design

1. **Design and implement a distributed cache in Python using `Redis` or `Memcached`, ensuring fault tolerance and data consistency.**
   - [Solution](senior/advanced_core_python_and_system_design/task1_distributed_cache.py)

2. **Implement a thread-safe singleton class that works across multiple processes, using locks or multiprocessing primitives.**
   - [Solution](senior/advanced_core_python_and_system_design/task2_thread_safe_singleton.py)

3. **Write a decorator that memoizes a function’s output and stores the results in a database or file for future retrieval across different runs.**
   - [Solution](senior/advanced_core_python_and_system_design/task3_persistent_memoization.py)

4. **Implement a robust retry mechanism with exponential backoff for handling intermittent API failures.**
   - [Solution](senior/advanced_core_python_and_system_design/task4_retry_mechanism.py)

5. **Design a plugin-based architecture where functionality can be extended at runtime by adding new plugins, without modifying the core codebase.**
   - [Solution](senior/advanced_core_python_and_system_design/task5_plugin_architecture.py)

6. **Create a dynamic dispatch mechanism for resolving function calls at runtime using custom logic (e.g., based on types or conditions).**
   - [Solution](senior/advanced_core_python_and_system_design/task6_dynamic_dispatch.py)

7. **Implement an interpreter pattern to parse and evaluate expressions provided as strings (e.g., arithmetic, logical, or domain-specific language).**
   - [Solution](senior/advanced_core_python_and_system_design/task7_expression_interpreter.py)

8. **Design and implement an event-driven system using message queues (like RabbitMQ or Kafka) and Python's `asyncio`.**
   - [Solution](senior/advanced_core_python_and_system_design/task8_event_driven_system.py)

9. **Write a Python function to parse and execute complex SQL queries on a custom data structure, mimicking basic SQL functionality (joins, aggregations, etc.).**
   - [Solution](senior/advanced_core_python_and_system_design/task9_sql_engine.py)

10. **Create a framework for managing microservices communication in a Python-based microservice architecture, using `gRPC` or `REST` API, including error handling and resilience.**
    - [Solution](senior/advanced_core_python_and_system_design/task10_microservices_framework.py)

---

### Concurrency and Asynchronous Programming

1. **Implement a highly scalable web scraper using `asyncio`, `aiohttp`, and `concurrent.futures` to concurrently scrape multiple pages, process them, and store results in a database.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task1_scalable_web_scraper.py)

2. **Write a Python program to calculate the SHA-256 hash of a large file in parallel, splitting the file into chunks and calculating partial hashes concurrently.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task2_sha256_parallel.py)

3. **Design and implement a rate-limiting algorithm (e.g., token bucket, leaky bucket) for an API service using `asyncio`.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task3_rate_limiting.py)

4. **Optimize a data processing pipeline in Python for a large dataset using multiprocessing, multithreading, or vectorized operations (NumPy/Pandas).**
   - [Solution](senior/concurrency_and_asynchronous_programming/task4_data_pipeline_optimization.py)

5. **Implement a Python application that uses `ZeroMQ` or `Kafka` to handle high-throughput message processing between distributed services.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task5_message_processing.py)

6. **Create an efficient parallelized solution for matrix multiplication using Python’s `multiprocessing` and `shared_memory`.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task6_parallel_matrix_multiplication.py)

7. **Write a performance-critical Python function in Cython or use `cffi` to call C/C++ functions from Python.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task7_cython_performance.py)

8. **Design a load-balancer in Python that distributes tasks to multiple worker processes/threads, with health checks and failover mechanisms.**
   - [Solution](senior/concurrency_and_asynchronous_programming/task8_load_balancer.py)

---

### Data Structures, Algorithms, and Big Data

1. **Implement a highly efficient Trie (Prefix Tree) for searching through a large dictionary of words, ensuring it uses minimal memory.**
   - [Solution](senior/data_structures_algorithms_and_big_data/task1_trie_implementation.py)

2. **Write a Python function to find the shortest path in a large-scale graph using A* search, optimizing for both time and space complexity.**
   - [Solution](senior/data_structures_algorithms_and_big_data/task2_a_star_search.py)

3. **Design a scalable solution for counting the number of distinct elements in a stream of data using probabilistic data structures like HyperLogLog.**
   - [Solution](senior/data_structures_algorithms_and_big_data/task3_hyperloglog.py)

4. **Implement a distributed MapReduce in Python to process large datasets, simulating how Hadoop or Spark works under the hood.**
   - [Solution](senior/data_structures_algorithms_and_big_data/task4_mapreduce.py)

5. **Write an efficient algorithm for topological sorting of a directed acyclic graph (DAG) and ensure it can handle millions of nodes.**
   - [Solution](senior/data_structures_algorithms_and_big_data/task5_topological_sort.py)

6. **Optimize a slow-performing algorithm by profiling its memory and CPU usage and refactoring the code using efficient data structures.**
   - [Solution](senior/data_structures_algorithms_and_big_data/task6_algorithm_optimization.py)

---

### Software Engineering, Architecture, and System Design

1. **Design and implement a service-oriented architecture (SOA) for a complex web application in Python, explaining how you'd handle service discovery, monitoring, and scaling.**
   - [Solution](senior/software_engineering_architecture_and_system_design/task1_soa_design.py)

2. **Write a Python program that implements a consistent hashing mechanism to distribute load across a set of servers.**
   - [Solution](senior/software_engineering_architecture_and_system_design/task2_consistent_hashing.py)

3. **Design and implement a scalable REST API with proper pagination, filtering, and sorting for large datasets. Add rate-limiting and authentication using OAuth2 or JWT.**
   - [Solution](senior/software_engineering_architecture_and_system_design/task3_scalable_rest_api.py)

4. **Develop a fault-tolerant distributed system using Python and `ZooKeeper` for managing leader elections and coordination between multiple nodes in a cluster.**
   - [Solution](senior/software_engineering_architecture_and_system_design/task4_distributed_system.py)

5. **Create a microservices architecture for a social media platform in Python, using Docker for containerization, Kubernetes for orchestration, and `RabbitMQ` for messaging between services.**
   - [Solution](senior/software_engineering_architecture_and_system_design/task5_microservices_architecture.py)

6. **Write a Python framework for data validation and transformation, supporting custom validators, pipeline-based transformations, and type-safe operations.**
   - [Solution](senior/software_engineering_architecture_and_system_design/task6_data_validation_framework.py)

---

### Bonus: System Monitoring, Security, and Testing

1. **Set up real-time monitoring and logging for a Python application using `Prometheus` for metrics and `ELK Stack` (Elasticsearch, Logstash, Kibana) for logging, integrating alerts when issues occur.**
   - [Solution](senior/bonus_system_monitoring_security_and_testing/task1_real_time_monitoring.py)

2. **Write a security module in Python to encrypt/decrypt sensitive data using AES encryption and integrate it with a system that stores encrypted user data in a database.**
   - [Solution](senior/bonus_system_monitoring_security_and_testing/task2_security_module.py)

3. **Design and implement an automated testing framework in Python that supports unit tests, integration tests, and end-to-end tests for a microservice-based application.**
   - [Solution](senior/bonus_system_monitoring_security_and_testing/task3_testing_framework.py)

4. **Implement a distributed tracing solution for tracking requests across a Python microservices architecture using tools like `Jaeger` or `OpenTelemetry`.**
   - [Solution](senior/bonus_system_monitoring_security_and_testing/task4_distributed_tracing.py)

