"""
This file you have to run seperately using this command this fille push the seleted file into the seleted repository dataset

```
python push_to_huggingface.py
```

"""
import os
from datasets import Dataset
from dotenv import load_dotenv
from huggingface_hub import login


load_dotenv()

file_path = "./temp/frappeframework.jsonl"

repo_id = "antony-pk/frappeframework-demo-1"

# Login To the huggingface
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')
login(HUGGINGFACEHUB_API_TOKEN)

dataset = Dataset.from_json(file_path)


# Print the first few examples to verify
print(dataset[0])

# Upload the dataset to the Hugging Face Hub
print(dataset.push_to_hub(repo_id))

print("Pushed Successfully")
