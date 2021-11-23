from chefboost import Chefboost as chef
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("dataset.txt")
    # print(df.head())
    config = {'algorithm': 'ID3'}
    model = chef.fit(df, config = config, target_label = 'mon')
    chef.save_model(model, 'model.pkl')