from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from langchain_community.document_loaders import DirectoryLoader

def main():
    # Initialize OpenAI models (You need to have OpenAI API key)    
    data_generation_model = ChatOpenAI(model='gpt-4o-mini')
    critic_model = ChatOpenAI(model='gpt-4o')

    # Initialize OpenAI Embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002",  # Change with your model if needed
        chunk_size=1000
    )

    # Load documents
    path = "Sample_Docs_Markdown/"
    loader = DirectoryLoader(path, glob="**/*.md")
    documents = loader.load()

    # Initialize the generator
    generator = TestsetGenerator.from_langchain(
        data_generation_model,
        critic_model,
        embeddings
    )

    # Define distribution of question types, feel free to adjust the values as needed
    distributions = {
        simple: 0.4,
        multi_context: 0.4,
        reasoning: 0.2
    }

    # Generate test set
    testset = generator.generate_with_langchain_docs(documents, 10, distributions)

    # Convert to pandas DataFrame
    test_df = testset.to_pandas()
    test_df.to_csv('generated_testset.csv', index=False)

if __name__ == "__main__":
    main()
