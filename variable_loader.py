from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()
endpoint = os.getenv("azure_endpoint")
azure_api_key = os.getenv("azure_api_key")
deployment_name=os.getenv("deployment_gpt")
font_folder_path=os.getenv("font_folder_path")
version=os.getenv("version_gpt")
version_embedding=os.getenv('version_embedding')
deployment_embedding=os.getenv("deployment_embedding")
folder_path_cv = os.getenv("folder_path_cv")
font_name = os.getenv("thai_font_name")


llm_global = AzureChatOpenAI(azure_endpoint=endpoint, api_key=azure_api_key,api_version=version, deployment_name=deployment_name, temperature=0)
embeddings = AzureOpenAIEmbeddings(azure_deployment=deployment_embedding,azure_endpoint=endpoint,api_key=azure_api_key,api_version=version_embedding,chunk_size=100,show_progress_bar=True)