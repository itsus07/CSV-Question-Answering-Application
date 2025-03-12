import gradio as gr
from file_handler import load_csv
from query_processor import QueryProcessor, QueryRequest
from graph_plotter import plot_graph

query_processor = QueryProcessor()

def process_csv(file, question, x_col, y_col, graph_type):
    df = load_csv(file)
    if isinstance(df, str):  
        return df, None

    query_request = QueryRequest(question=question, data=df.to_dict())
    answer = query_processor.answer_question(query_request)

    graph = plot_graph(df, x_col, y_col, graph_type)
    
    return answer, graph

interface = gr.Interface(
    fn=process_csv,
    inputs=[
        gr.File(label="Upload CSV"),
        gr.Textbox(label="Ask a Question"),
        gr.Textbox(label="X-axis Column"),
        gr.Textbox(label="Y-axis Column"),
        gr.Radio(["Line", "Bar", "Scatter"], label="Graph Type")
    ],
    outputs=[
        gr.Textbox(label="Answer"),
        gr.Plot(label="Generated Graph")
    ],
    title="CSV Question Answering & Visualization App"
)

interface.launch()
