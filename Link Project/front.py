import pandas as pd


df = pd.read_json('data.json').set_index('New link')

class Link:
    def __init__(self,original_link):
        self.original_link = original_link  
        self.create_new_link()
        self.open_new_link()
        
    def create_new_link(self):
        self.new_suffix=  ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5)) 
        df.append({'New link':self.new_suffix ,'Original link':self.original_link ,'Counter':0},ignore_index=True).to_json('data.json')
        print("Your new link is:",f"http://127.0.0.1:5000/{self.new_suffix}")
        # return f"http://127.0.0.1:5000/{self.new_suffix}"
    
    def open_new_link(self):
        # webbrowser.open(self.dict_links[self.new_suffix][0])
        pass
    

link = input("Enter your URL:")
Link(link)