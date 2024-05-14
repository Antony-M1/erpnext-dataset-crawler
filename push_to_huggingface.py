"""
This file you have to run seperately using this command this fille push the seleted file into the seleted repository dataset

```
python push_to_huggingface.py
```

"""
import os
import traceback
from datasets import Dataset
from dotenv import load_dotenv
from huggingface_hub import login, delete_repo
import sys


load_dotenv()

file_path = "./temp/frappeframework.jsonl"

repo_id = "antony-pk/erpnext-docs-ds"

# Login To the huggingface
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')
login(HUGGINGFACEHUB_API_TOKEN)

dataset = Dataset.from_json(file_path)


# Print the first few examples to verify
print(dataset[0])

# Upload the dataset to the Hugging Face Hub
print(dataset.push_to_hub(repo_id))

print("Pushed Successfully")



def delete_hf_repo(repo_id):
    try:
        delete_repo(repo_id)
    except:
        traceback.print_exc()
        raise(f"Check the repo_id : {repo_id}")


# if __name__ == "__main__":
    
#     try:
#         funtion_name = sys.argv[1]
        
#         if funtion_name == "delete_hf_repo":
#             delete_hf_repo(sys.argv[2])
#         else:
#             raise("Invalid Function Name")
#     except:
#         traceback.print_exc()