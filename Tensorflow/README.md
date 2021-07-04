## Study for Tensorflow

I have studied Machine Learning and Deep Learning using tensorflow. 


I take a lecture https://hunkim.github.io/ml/


I did the practice based on the file used in the lecture and upload my practice file.




## Regression with Tensorflow
#### It must have equal type between node.


#### We can build Graph 2 ways
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
