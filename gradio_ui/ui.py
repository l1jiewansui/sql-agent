import gradio as gr
import requests

def generate_sql(table_structure, query):
    response = requests.post("http://127.0.0.1:5000/generate_sql", json={
        "table_structure": table_structure,
        "query": query
    })
    return response.json().get('sql_query')

iface = gr.Interface(
    fn=generate_sql,
    inputs=["text", "text"],
    outputs="text",
    title="Text to SQL",
    description="Enter the table structure and your query to generate SQL."
)

iface.launch()
