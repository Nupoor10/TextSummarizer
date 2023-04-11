# TEXT SUMMARIZER

The text summarizer app summarizes long texts into short and concise summaries. Users can upload a txt file or paste their text in the text box to get the summary.

## 💻 GUI

The GUI of this application was built using HTML, CSS and JavaScript

📌 Landing Screen 

![Landing Screen](https://i.ibb.co/ZBj56Kw/landing.png)

📌 How it Works

![Working Screen](https://i.ibb.co/CKKZLtg/working.png)

📌 User Input Screen

![Input Screen](https://i.ibb.co/1vxVH12/input.png)

📌 Output Summary 

![Output Screen](https://i.ibb.co/BB2Pxmd/output.png)

📌 Contact Us 

![Contact Screen](https://i.ibb.co/f0QgZ8K/contact.png)

## 💻Built With : 

- ➡ HTML
- ➡ CSS
- ➡ JavaScript
- ➡ NLTK 
- ➡ Flask

## 💻 How it Works : 

- The web app takes the user input and flask provides the input to the text summarizer function. 
- The text summarizer function tokenizes the input string into words, removes the stop words and creates a dictionary of word frequency
- The article is then tokenized into sentences and the sentence weight is calculated according to the word frequency table
- The sentence weight value is then divided by the sentence length to get average sentence score
- Finally the sentences having the score above a certain threshold are included in the summary
- The output of the function is served by the flask app to the frontend and the user can see the original text and the summarized text along with the word count