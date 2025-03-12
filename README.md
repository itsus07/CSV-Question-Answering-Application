This Gradio-based application allows users to upload a CSV file, ask questions about its contents, and generate visualizations. The app leverages the Ollama framework for LLM-based question answering and includes robust CSV parsing and graph plotting capabilities.

🚀Features:

•	CSV File Upload: Easily upload CSV files with automatic error handling.
•	Question Answering System: Ask both numerical and textual queries about the CSV data.
•	Graph Plotting: Generate Line, Bar, and Scatter plots directly within the Gradio interface.
•	LLM Integration: Uses Ollama with the LLaMA 3 model for intelligent query processing.
•	User-Friendly Interface: Simple yet powerful interface built with Gradio.


▶️Usage:

1. Install required libraries using command prompt :- pip install gradio pandas ollama pydantic matplotlib seaborn
2. Start the ollama server :- ollama start  (## Ensure ollama is ruuning before starting the application otherwise it won't work ##)
3. Run the application :- python app.py
4. Open the provided Gradio link in your browser (e.g., http://localhost:7860).
5. You can now upload a CSV file on your gradio based web application and ask any question about the data and plot graph according to your requirements.


📂Project Structure:
app.py                # Main Gradio application
file_handler.py       # CSV file handling logic
query_processor.py    # Question-answering system using Ollama
graph_plotter.py      # Graph plotting logic
