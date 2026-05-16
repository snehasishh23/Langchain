from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humans have achieved remarkable milestones.

These missions have not only expanded our knowledge of the universe but have also contributed to technological advancements on Earth.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)