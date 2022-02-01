
I ran 3 models:
    Naive-Bayes (unoptimized) - Accuracy:  0.39683238011438626
    KNN - Accuracy:  0.5327760668719753
    SVM - Accuracy:  0.5644522657281126

Then found a tutorial on Google colab and ran:
    Simple MLP - Validation accuracy: 0.6159260869026184, loss: 1.0084409713745117
    sepCNN - alidation accuracy: 0.2498900145292282, loss: 1.5990124940872192

Repeated KNN with NGRAMS and further data input cleaning:
    KNN (11 neighbors from previous optimization)- Accuracy:  0.2833260008798944

This resulted in a huge drop in accuracy.

Tried KNN again with new optimization for n-neighbors:
    This time it decided optimal was 1 neighbor and resulted in:
    Accuracy:  0.33040035195776507

I think the root issue is the lack of good human labelling (collection choice).
To improve this:
    - Could use unsupervised clustering 
    - Could add additional feature of related scripture
    - Could classify entire devotional vs. individual devotional days

    


