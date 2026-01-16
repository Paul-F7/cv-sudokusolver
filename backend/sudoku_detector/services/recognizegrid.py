# will recognize grid from cells
CONF = 0.7

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
                digit = predicted if conf > CONF else 0
            else:
                digit = 0
            row_str += '?' if digit == 0 else str(digit)
        rows.append(row_str)
    return rows