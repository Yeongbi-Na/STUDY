## Study for Tensorflow

I have studied Machine Learning and Deep Learning using tensorflow. 


I take a lecture https://hunkim.github.io/ml/


I did the practice based on the file used in the lecture and upload my practice file.


.py format is provided as a practice file, but I am studying in a colab environment, so I upload it in .ipynb format.



## Regression with Tensorflow
#### It must have equal type between node.

#### sometimes we need to normalize data because values of cost have infinite values.

#### I have to consider the shape of y_data when I extract y_data(label). 
y_data = data[:, -1]  >> It would make error because the shape is (~, ) so I have to reshape y_data like y_data.reshape(-1,1)


y_data = data[:, [-1]] >> the shape (~, 1)

<br>

#### We can build Graph by 2 ways
1. Define training data in advance.
2. Using tf.placeholder - > After build graph, we can give feed_dict




#### Overal Process
1. Define node and build graph
2. Define cost function, optimizer and way to optimize
3. Define session and Run tf.global_variables_initializer()
4. Run cost, weights, train with feed_dict
5. After 4 steps, we can test out model 
   sess.run(hypothesis, feed_dict = { } )


* It is important to make graph with exact shape for W,b, x, y




