def make_predictions(model, data):
    probabilities = model.predict_proba(data)
    classes = model.classes_
    predictions = [dict(zip(classes, prob)) for prob in probabilities]
    return predictions
