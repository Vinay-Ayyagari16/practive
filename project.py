# Imports
import numpy as np
import pandas as pd
from datetime import datetime

#CounterApp Class
class CounterApp:
    def __init__(self):
        self.count = 0
        self.log = []
        
    #Increment Method
    def increment(self, step=1):
        self.count += step
        self._log_change("increment", step)
        
    #Decrement Method
    def decrement(self, step=1):
        self.count -= step
        self._log_change("decrement", step)
        
    #Random Increment
    def random_increment(self, max_step=10):
        step = np.random.randint(1, max_step + 1)
        self.increment(step)
        
    #Internal Logging Method
    def _log_change(self, action, step):
        self.log.append({
            "timestamp": datetime.now(),
            "action": action,
            "step": step,
            "new_count": self.count
        })
        
    #Show Log
    def show_log(self):
        df = pd.DataFrame(self.log)
        print(df)
        
    #Export Log to CSV
    def export_log(self, filename="counter_log.csv"):
        df = pd.DataFrame(self.log)
        df.to_csv(filename, index=False)
        print(f"Log exported to {filename}")

    # Demo usage(main block) 
app=CounterApp()
app.increment()
app.random_increment()
app.decrement(2)
app.show_log()
app.export_log()
