import pickle

model = pickle.load(open("model.pkl", "rb"))

print("Model type:", type(model))
print("Has class_count_:", hasattr(model, "class_count_"))

if hasattr(model, "class_count_"):
    print("Model is FITTED ")
else:
    print("Model is NOT FITTED ")
