# HW3 notes

Answer each question in a few sentences. Be specific: name the function, the error or the command.

## What did you try?
I worked on walks and test_my_walks to handle row filtering, safe file saving, report generation, and unit tests for parse_walk.
## What broke, and how did you fix it?
When I ran pytest on good_walks, the tests failed with because a bad row had an empty steps field and my loop was either letting int() fail or raising ValueError instead of skipping bad rows. I fixed it by wrapping the row parsing in a try...except ValueError block with continue so invalid rows are skipped and valid Walk objects keep yielding.
## What would you do differently next time?
I would check how parse_walk handles bad inputs right from the start instead of duplicating validation checks in good_walks, and run  pytest earlier while building my test cases so edge cases like 0 steps, whitespace, and empty strings are checked right away.