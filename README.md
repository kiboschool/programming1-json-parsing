# JSON Data Parsing

In this exercise, you'll use Python's json library to read JSON-formatted files
into your program, process the data, and print out JSON-formatted results.

## Data

In `posts.json` are sample posts generated from
https://jsonplaceholder.typicode.com/. You'll practice loading the posts data
into Python, analyzing it, and printing out results.

There are 100 posts. Each post has a `userId`, an `id`, a `title`, and a `body`.

## Instructions

In `main.py` are a set of functions (mostly written) that do some analysis,
based on a list of posts. You need to

* import the `json` module
* open the posts.json file for reading
* parse the JSON-formatted data into a Python list
* pass the list into the `analyze` function
* print out the results

## Expected Results

There are no automated tests for this exercise.

If you parse the file correctly and pass the list into the analyze function, the
result should be like this:

```json
{
  "count": 100,
  "by_user": {
    "1": 10,
    "2": 10,
    "3": 10,
    "4": 10,
    "5": 10, 
    "6": 10,
    "7": 10, 
    "8": 10, 
    "9": 10,
    "10": 10
  },
  "longest": 225,
  "average_title": 39.52
}
```

The spacing may be different, but these should be the values.

> Note: You shouldn't need to change the analysis functions.
