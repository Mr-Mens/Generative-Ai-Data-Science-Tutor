# System Role Definition
SYSTEM_PROMPT = "You are a highly knowledgeable data science tutor. Your job is to teach data science concepts in a clear, detailed, and engaging manner. Provide explanations using simple language, code examples, and, where necessary, visualizations. Always check if the user understands and offer further assistance if they need clarification. if user gives one word answer or question, ask them to elaborate."

# Topic-Specific Prompts
TOPIC_PROMPTS = {
    "python_basics": "Explain how to {concept} in Python. Provide a simple example and explain each part of the code.",
    "pandas": "Show the user how to {operation} using pandas. Explain each step and provide a code snippet with a sample DataFrame.",
    "machine_learning": "Describe the concept of {algorithm}. Explain its purpose, how it works, and provide a simple code example using scikit-learn.",
    "data_visualization": "Teach the user how to create a {chart_type} using {library}. Include code examples and explain how each part of the code contributes to building the visualization."
}

# Interactive Learning Prompts
INTERACTIVE_PROMPTS = {
    "understanding_check": "After explaining {concept}, ask the user: 'Do you understand this concept? If not, I can provide another example or explain it in a different way.'",
    "exercise": "Now that you’ve learned about {topic}, try this: {exercise}. I can check your code if you need help."
}

# Dynamic and Adaptive Prompts
ADAPTIVE_PROMPTS = {
    "progress_tracking": "It seems like you’re interested in {topic}. Would you like to go deeper and explore {related_concept} or do an exercise to practice?",
    "advanced_suggestion": "Great job! Since you’re comfortable with {basic_topic}, would you like to learn about {advanced_topic} next?"
}

# Error Handling and Clarification Prompts
ERROR_PROMPTS = {
    "clarification": "I’m not sure I understand. Are you asking about {interpretation_1} or {interpretation_2}? Could you please clarify?",
    "coding_error": "It looks like there might be an error in your code. {describe_error} Have you checked {solution_suggestion}?"
}

# Roadmap Prompt
ROADMAP_PROMPT = """
Provide a comprehensive roadmap for becoming a data scientist. Include the following:
1. Key programming languages (Python, SQL) and their importance.
2. Essential statistics and mathematics topics.
3. Machine learning algorithms and their applications.
4. Data visualization tools and libraries.
5. Practical projects and portfolio building.
6. Suggested learning paths, courses, and resources for each area.
Ensure the roadmap is structured in a way that a beginner can follow it step-by-step.
"""

# Function to get a prompt based on the category
def get_prompt(category, key=None, **kwargs):
    if category == "system":
        return SYSTEM_PROMPT
    elif category == "topic":
        prompt = TOPIC_PROMPTS.get(key, "")
    elif category == "interactive":
        prompt = INTERACTIVE_PROMPTS.get(key, "")
    elif category == "adaptive":
        prompt = ADAPTIVE_PROMPTS.get(key, "")
    elif category == "error":
        prompt = ERROR_PROMPTS.get(key, "")
    elif category == "roadmap":
        return ROADMAP_PROMPT
    else:
        prompt = ""

    return prompt.format(**kwargs)
