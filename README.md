## Detecting Similarities Between Copora of Text: 

### Calculating the Containment : 

In order to detect the similarities between two corpus of text we first calculate the ngrams for both of the sentences and then find the normalized 
sum of ngram counts. 
The formula for calculating the containment is following:

![Calculating Containments](https://raw.github.com/username/repo/master/images/figure 1-1.png "Figure 1-1")

### Calculating the Longest Common Subsequence:

We calculate the Longest Common Subsequence between two corpus of text using **Dynamic Programming** approach, or, basically the **Tabular Approach** where we create a matrix of the words obtained from the sentences of the corpus of the text using **.split()** method and if the words in both dimensions match we diagonally add up 1 to the current value of the matrix and if it doesn't we add the maximum value between the very left or the very top of the current cell of the matrix. In this way we can efficiently calculate the **LCS** for large number of sentences and words. We obtain the **LCS** from the very last cell(bottom right) of the matrix and normalize it by the number of words in the answer text. 

## To run the project type in the following command in a configured SageMaker Session.

```
cd SageMaker
https://github.com/swastiknath/pyt_SM_plg_det.git
```
Now Open the Jupyter Notebooks. 
