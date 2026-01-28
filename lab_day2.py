"""
Day 2 Activity: Build a utility library with reusable functions.
Required functions:
1) calculate_statistics(data)
2) normalize_data(data, method)
3) remove_outliers(data, threshold)
4) train_test_split(data, ratio)
5) encode_labels(labels)
"""




from typing import List, Dict, Tuple

def calculate_statistics(data:List[float]) -> Dict[str, float]:
  return {"mean":sum(data)/len(data),"min":min(data),"max":max(data)}




def normalize_data(data: List[float], method= "minmax") -> List[float]:
  if method == "minmax":
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data
print(normalize_data(cat_a))

def remove_outliers(data: List[float], threshold: float) -> List[float]:
  return [x for x in data if abs(x) < threshold]
  
print(remove_outliers([35,34,36,31,56],50))


def train_test_split(data: List[float], ratio: float = 0.8) -> Tuple[List[float], List[float]]:
  split_index = int(len(data) * ratio)
  train_data = data[:split_index]
  test_data = data[split_index:]
  return train_data , test_data
print(train_test_split(cat_a))


d=["dana","fatmah","nassab","maria"]

def encode_labels(labels: List[str]) -> Dict[str, int]:
  unique_labels = list(set(labels))
  label_encoding = {label: i for i, label in enumerate(unique_labels)}
  return label_encoding
print(encode_labels(d))