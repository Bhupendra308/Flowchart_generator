def generate_mermaid_code(input_data):
    # Initialize the mermaid code variable
    mermaid_code = ''

    # Helper function to extract Mermaid code from a section of text
    def extract_mermaid_from_section(section):
        # Mermaid flowchart and graph types commonly used
        start_phrases = ['graph TD', 'graph LR', 'flowchart TD', 'flowchart LR', 'flowchart TB']
        for phrase in start_phrases:
            if phrase in section:
                # Return phrase with the code content after it
                return f"{phrase}\n{section.split(phrase, 1)[1].strip()}"
        return ''

    # Verify 'result' exists in input_data and proceed if it does
    if 'result' in input_data:
        # Remove any unexpected null characters in the input string
        result = input_data['result'].replace('\x00', '')

        # Case 1: Check if there's a step-by-step guide without Mermaid code blocks
        if result.startswith("I can provide a text-based step-by-step guide"):
            steps = result.split('\n\n')
            mermaid_code = "flowchart TB\n"
            previous_step = None
            for step in steps:
                if step.startswith("**"):  # Recognize steps starting with markdown-like "**"
                    # Generate a node for each step
                    step_number = step.split(":")[0].replace("**", "").strip().replace(" ", "_")
                    step_description = step.split(":")[1].strip().replace("\n", " - ").replace("**", "")
                    step_node = f'{step_number}["{step_description}"]'
                    if previous_step:
                        # Link the previous step to the current step
                        mermaid_code += f"    {previous_step} --> {step_node}\n"
                    else:
                        # If it's the first step, just add the node
                        mermaid_code += f"    {step_node}\n"
                    previous_step = step_number

        # Case 2: Check for Mermaid code blocks denoted by ```
        if '```' in result:
            # Split by triple backticks and look for Mermaid code within
            mermaid_section = result.split('```')[1].strip()
            # Extract Mermaid code if valid graph type phrase is present
            extracted_code = extract_mermaid_from_section(mermaid_section)
            if extracted_code:
                mermaid_code = extracted_code

        # Case 3: If no backticks, try extracting Mermaid code directly from the entire text
        if not mermaid_code:
            extracted_code = extract_mermaid_from_section(result)
            if extracted_code:
                mermaid_code = extracted_code

    # Final cleanup of arrows and other Mermaid-specific adjustments
    mermaid_code = mermaid_code.replace(' -> ', ' --> ').replace(' -- ', ' --> ')

    # Trim content after 'classDef' for cleaner output
    index_class_def = mermaid_code.find('classDef')
    if index_class_def != -1:
        mermaid_code = mermaid_code[:index_class_def].strip()

    # Return the final extracted Mermaid code
    return mermaid_code

