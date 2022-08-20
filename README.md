This is a fun hobby project during my teaching days, which also saved my colleagues a great deal of time in sorting A Level physics questions into topics. It is a Python Flask webapp with trained AI model to classify H2 A Level physics questions into their respective topics.

Machine learning is trained separately in Python using many A Level tutorial physics questions from the school in which I taught (I cannot share the question papers here unfortunately). The classifier model is imported in the .pkl file. tfidf vectorizer used to vectorized the words is also imported in .pkl to vectorize the words from user input before classifying it.

Deployed live on https://physicsquestion.herokuapp.com/

Feel free to try it out! You can enter questions or phrases like like "find the speed of ball..." or "an alpha particle..."

The full app which requires the user to upload many physics papers in pdf to have all of them sorted is deployed here: https://physicsquestionsorter.herokuapp.com/. The The app returns a zipped folder of separate pdf files of the sorted questions, one for each topic.
