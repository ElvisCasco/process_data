from process_data import pred_auc_score

def test_pred_auc_score_basic():
    y_true = [0, 0, 1, 1]
    y_score = [0.1, 0.4, 0.35, 0.8]
    auc = pred_auc_score(y_true, y_score)
    assert 0.0 <= float(auc) <= 1.0