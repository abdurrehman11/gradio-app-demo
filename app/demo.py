import gradio as gr
from image_search import image_search


with gr.Blocks() as demo:
    gr.Markdown("# Search images in PDF docs")
    with gr.Row():
        with gr.Column():
            pdf_file = gr.File(
                file_count="single",
                file_types=[".pdf"],
                label="Upload PDF"
            )
            search_text = gr.Textbox(label="Input Text")
            btn_search = gr.Button("Search with Text")
        result_img = gr.Image(type="pil", label="Result")

    btn_search.click(
        fn=image_search,
        inputs=[pdf_file, search_text],
        outputs=[result_img]
    )

demo.queue().launch(
    share=False,
    favicon_path="../favicon.ico",
    server_name="0.0.0.0"
)
