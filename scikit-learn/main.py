import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

if __name__ == '__main__':
    col_names = ['chieu cao','tay','chan','than tren','than duoi','tong the','linh hoat','suc ben','can bang','toc do','mon']
    pima = pd.read_csv("scikit-learn/dataset.txt", header=None, names=col_names)

    feature_cols = ['chieu cao','tay','chan','than tren','than duoi','tong the','linh hoat','suc ben','can bang','toc do']
    X = pima[feature_cols]
    y = pima['mon']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier()

    # Train Decision Tree Classifer
    clf = clf.fit(X,y)

    #Predict the response for test dataset
    # y_pred = clf.predict(y_test)
    # y_pred = clf.predict(X_train)
    # print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    res = clf.predict([[0,0,0,0,1,1,1,1,0,1]])
    print(res)

# from sklearn.tree import export_graphviz
# from sklearn.externals.six import StringIO  
# from IPython.display import Image  
# import pydotplus

# dot_data = StringIO()
# export_graphviz(clf, out_file=dot_data,  
#                 filled=True, rounded=True,
#                 special_characters=True,feature_names = feature_cols,class_names=['0','1'])
# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# graph.write_png('scikit-learn/diabetes.png')
# Image(graph.create_png())