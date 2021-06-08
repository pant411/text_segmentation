from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score

testt = ["ประยุทธ"]
pre = ["xประยุทธ์"]
print(precision_score(testt, pre))
print(recall_score(testt, pre))
print(f1_score(testt, pre))