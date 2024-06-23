import cohere

# Initialize the cohere client with your API key
co = cohere.Client(api_key='CfPKJpnLJ2gKQDGlE8craNF0r05A9FXKlDtllcFv')

# Sample input text
input_text = """
The rapid advancement of technology has significantly transformed various sectors, including healthcare, education, and finance. In healthcare, technological innovations such as telemedicine, wearable devices, and artificial intelligence have improved patient care and operational efficiency. Education has been revolutionized by e-learning platforms, digital resources, and virtual classrooms, making education more accessible and flexible. The finance sector has also seen a substantial shift with the rise of digital banking, cryptocurrencies, and fintech solutions, enhancing the convenience and security of financial transactions. These advancements have collectively contributed to increased productivity and better quality of life.
"""

# Create the message with the input text
message = f"""
## Instructions
Summarize the text below.

## Input Text
{input_text}
"""

# Get model response
response = co.chat(
  message=message,
  model="command-r-plus",
  temperature=0.3
)

# Print the summarized text
print(response.text)
