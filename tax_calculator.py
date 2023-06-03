import gradio as gr

def tax_calculator(income):
    tax = 0

    if income < 500000:
        tax = 0
    elif income >= 500000 and income < 1000000:
        tax = int(income * 0.2)
    else:
        tax = int(income * 0.3)

    return tax

income_input = gr.inputs.Number(label="Your income is")
output = gr.outputs.Textbox(label="Your tax is")

gr.Interface(fn=tax_calculator, inputs=income_input, outputs=output, title="Tax Calculator").launch()
