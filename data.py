
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.sentiment.vader import  SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()
def analyze(sentence):
    
    score = analyzer.polarity_scores(sentence)
    if score['compound'] >= 0.05 and score['pos'] - score['neg'] >= 0.1:
        return 'pos'  

    elif score['compound'] <= -0.05 and score['neg'] - score['pos'] >= 0.1:
        return 'neg'

    else:
        return 'neu'

# x = input()
# print(analyze(x ))

# pos_count = 0
# pos_correct = 0
# with open("pos.txt","r") as f:
#     for line in f.read().split('\n'):
#         if analyze(line) == 'pos':
#             pos_correct+=1
#         pos_count+=1
# neg_count = 0
# neg_correct = 0
# with open("neg.txt","r") as f:
#     for line in f.read().split('\n'):
#         if analyze(line) == 'neg':
#             neg_correct+=1
#         neg_count+=1



# print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
# print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))

# analyzer = SentimentIntensityAnalyzer()

# pos_count = 0
# pos_correct = 0

# file= open("wrong-pos.txt",'w')
# with open("pos.txt","r") as f:
#     for line in f.read().split('\n'):
#         vs = analyzer.polarity_scores(line)
#         if vs['compound'] >= 0.05:
#             pos_correct += 1
#         else:
#             line += '\n'
#             file.write(line )
#         pos_count +=1


# neg_count = 0
# neg_correct = 0
# file= open("wrong-neg.txt",'w')
# with open("neg.txt","r") as f:
#     for line in f.read().split('\n'):
#         vs = analyzer.polarity_scores(line)
       
#         if vs['compound'] <= -0.05:
#             neg_correct += 1
#         else:
#             line += '\n'
#             file.write(line )
#         neg_count +=1

# print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
# print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))