from chefboost import Chefboost as chef

if __name__ == '__main__':
    model = chef.load_model("model.pkl")
    res = chef.predict(model, ['thap','ngan','ngan','yeu','yeu','yeu','kem','kem','kem','cham'])
    print(res)