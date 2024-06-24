
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/4ch7gob74uo7/101/workflows/workflow-12d8a1"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="d12e43acbfb64ff78a0c8a7da3bfb85f"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
