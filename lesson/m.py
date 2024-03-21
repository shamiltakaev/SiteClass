class MinMaxWordFinder:
    def __init__(self):
        self.strokes = []

    def add_sentence(self, line):
        self.strokes.extend(line.split())

    def shortes_words(self):
        # if self.strokes:
        if self.strokes:
            mn = len(min(self.strokes, key=len))
        else:
            mn = 0
        return sorted([w for w in self.strokes if len(w) == mn])
    
    def longest_words(self):
        # if self.strokes:
        if self.strokes:
            mx = len(max(self.strokes, key=len))
        else:
            mx = 0
        # mx = set([word for word in self.strokes if len(word) == mx])
        return sorted([w for w in self.strokes if len(w) == mx])
        
finder = MinMaxWordFinder()
print("".join(finder.shortes_words()))
print("".join(finder.longest_words()))