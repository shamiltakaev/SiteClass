class Table:
    def __init__(self, n_rows, n_cols):
        self.n_rows_ = n_rows
        self.n_cols_ = n_cols
        self.tab = [[0] * n_cols for _ in range(n_rows)]

    def n_rows(self):
        return self.n_rows_

    def n_cols(self):
        return self.n_cols_

    def set_value(self, row, col, value):
        self.tab[row][col] = value

    def get_value(self, row, col):
        if (row < 0 or row >= self.n_rows_
                or col < 0 or col >= self.n_cols_):
            return None
        return self.tab[row][col]

    def add_row(self, row):
        self.tab.insert(row, [0] * self.n_cols_)
        self.n_rows_ += 1

    def delete_row(self, row):
        self.tab.pop(row)
        self.n_rows_ -= 1

    def add_col(self, col):
        for r in range(self.n_rows_):
            self.tab[r].insert(col, 0)
        self.n_cols_ += 1

    def delete_col(self, col):
        for r in range(self.n_rows_):
            self.tab[r].pop(col)
        self.n_cols_ -= 1
