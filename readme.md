
# Problem definition
**Purpose**

This project aims to develop a web-based application that indexes and ranks multiple other web pages in terms of similarity according to the web page content at a given URL. Thus, through this project, it is aimed to gain knowledge about web indexing methods and to develop web-based application writing skills.

# Requirements

## Calculating Frequencies of Words on a Page
**For a given URL:**

Find how many times each word occurs (frequency) in the URL content (in the page content the URL points to).

**Output:**

On a page on the project's website (eg: asama1.php, asama1.asp) a field to enter the URL will be created. Afterwards, the number of times each word in the text of this URL entered will be calculated and printed.

## Keyword Extraction
**For a given URL:**

- Identify the most important words (the set of words that describe the content features of the page and reflect the categorical features) from the words in the URL text and extract the keywords.
- For example, selecting the 5 words with the highest frequency.

## Similarity Scoring Between Two Pages
**For the 2 given URLs:**

- In the second part, define a similarity score formula based on the number of keywords obtained for URL 1 included in the content of URL 2.
- For example, let's denote the keywords in Url 1 with a, b, c, d and e. Let a, c and e be the ones used in the 2nd Url text of these keywords. Let's show the repeating numbers (frequencies) of these 3 keywords in the 2nd Url with , and . Let's define an example similarity score formula based on common keywords (a, c, and e) in both URLs:
- Print all keywords of the 1st URL and the number (frequency) of occurrences in the 1st URL content, the similarity score for these two URLs, all the keywords in the 2nd URL and their frequencies in the 2nd URL content (2nd and 2nd URL) 3. Results should be printed for sections on a single web page (eg: asama23.php, asama23.asp,…).

**And lastly develop a website for the application**

# Ease of Use 

- To run the project, go to its folder and run "python manage.py runserver"

- Go to the html address in the output

- There is no homepage, add "asama1" and "asama23" to the end of the address and go to the stage you want

- All you have to do is enter the url and press the submit button.

