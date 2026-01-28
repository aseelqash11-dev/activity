"""
Day 5 Activity: JSON + File Handling mini workflow.
Tasks:
1) Load training config from JSON
2) Simulate training results (dict)
3) Save results to JSON safely
"""

import json
#from pathlib import Path
#
config={
   "model": {"name": "LogisticRegression"},
   "training": {
       "batch_size": 32,
       "epochs": 10,
       "learning_rate": 0.001
   }
}
with open("config.json","w") as f :
    json.dump(config,f ,indent=4)
# 1. Load Configuration
with open("config.json","r") as f:
    config=json.load(f)
print(config)
#2. Training Process (simplified)
results={
    "accuracy": 0.9,
    "loss": 0.1
}
# 3. Save Results
try:
    with open("results.json","w") as f:
        json.dump(results,f,indent=4)
        print("results saved")
except Exception as e:
    print(f"Error saving results: {e}")
