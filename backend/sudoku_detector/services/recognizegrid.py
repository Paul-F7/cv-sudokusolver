# will recognize grid from cells
#CONF = 0.85
CONF = {
    0: 0.85,  # empty
    1: 0.85,
    2: 0.85,
    3: 0.85,
    4: 0.85,
    5: 0.85,
    6: 0.6,   # lower threshold for 6 as it had trouble with it
    7: 0.85,
    8: 0.85,
    9: 0.85,
}

def recognize_grid(cells, model):
    rows = []
    for row in range(9):
        row_str = ""
        for col in range(9):
            cell_img = cells[row][col]

            results = model.predict(cell_img, verbose=False)

            # Get the predicted class (digit) from results specific to degit
            if results[0].probs is not None:
                predicted = int(results[0].probs.top1)
                conf = results[0].probs.top1conf
                threshold = CONF.get(predicted, 0.85)
                digit = predicted if conf > threshold else 0
            else:
                digit = 0
            row_str += '?' if digit == 0 else str(digit)
        rows.append(row_str)
    return rows