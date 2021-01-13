# Quiz-Game
#100DaysOfCode - Day: 17 

Intermediate Python Programming

Covered: OOP topics

### Question and Answer Data Generation

Using Open Trivia platform [Click here](https://opentdb.com/api_config.php) 
we can generate API tat contain the questions and answers in JSON format.

In `data.py` contain list of all questions and answers set.

### Other details

Run `main.py` file

In `quiz_brain.py` ontain the main logic of the game.In this file `question_number`, `question_list`, `socre` are the attributes and

`check_answer`, `stll_has_questions`, `nex_question` are the main methods.

`still_has_questions` will return either True or False if still have questions
 
 `nex_question` It will show all the uestions from `question_list` and allow users to select True or False.
 
 Method `check_answer` is called to verify the user entered answer right or wrong.
 
 Points will be awarded for the each right answers.
