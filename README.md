# Part 11 - Starter

This part builds on your Part 10 solution. In Part 10, you created a class that contains the search logic and the 
combination of multiple `SearchResult` instances to create the final, displayed `SearchResult`. 

You now find a class `Searcher` that does the same thing but based on a positional index (class `Index`), that you also 
find in `models.py`. Before you begin, make yourself comfortable with the code and try to understand how the positional 
index is implemented to have a rough idea.

Your task is to complete the positional index. There are two todos in the `Index` and one todo in the `Searcher` class.
Fill the gaps for things to work. See the ToDos and their description in `models.py` to get a better idea of what the
concrete tasks are.

## Run the app

``` bash
python -m part11.app
```

## What to implement (ToDos)

Your ToDos are all located in `part11/models.py`, but you are free to move classes and functions around or create
new modules.
0.  If you came up with a solution to de-duplicate the settings code (highlight, search-mode, hl-mode), move it from 
    Part 10.
1.  Add an `id` to the `Sonnet` class, which we will need for the index. It must be unique. It's best to use the existing id 
    in the title of the sonnet. We will call this the document ID or the sonnet ID.
2.  In this task use the already existent methods `tokenize` and `_add_token` to fill the `Index` with data. There is 
    already a loop going through the sonnets, your job is to use `tokenize` to get individual tokens for
    the `title` and the individual `lines` of each sonnet and add them to the index. Use `None` as the line
    number for tokens from the `title` of the sonnet.
3.  Then, complete the `search_for` method of the `Index` class. Again, there is already loop code to get the postings
    for a given search string, the `token`. Your task is to use the information in the `Posting` to create a 
    corresponding `SearchResult` instance for display. Remember, that a `line_no` in `Posting` means that this a 
    posting from the title of the sonnet.
4.  The final todo is complete the `search` method in the `Searcher` class. The task is described in detail in the code! 
