# Data Science Tutor

Data Science Tutor is an interactive Generative AI web application designed to provide personalized data science guidance through a chatbot interface. It serves as a virtual tutor that helps users learn data science concepts, offers coding examples, and provides a step-by-step roadmap for becoming a data scientist.

## Features

- **Interactive Chat Interface**: Engage in conversations with the virtual tutor to learn about various data science topics.
- **Markdown Support**: The chatbot can render responses in a well-formatted manner using Markdown, ensuring information is easy to read and visually appealing.
- **Topic Selection**: Users can select predefined topics like Python Basics, Machine Learning, and Data Visualization for focused learning.
- **User and Bot Message Distinction**: Clear visual separation between user messages and tutor responses to enhance readability and user experience.
- **Dynamic Responses**: The chatbot adapts based on user inputs, providing relevant information and examples.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Python)
- **Styling**: Flexbox and CSS Grid for responsive design
- **Markdown Rendering**: Showdown.js library for converting Markdown responses to HTML
- **Rich Text Support**: TinyMCE integration for rich text editing and formatting
- **Deployment**: Parcel for bundling JavaScript and assets, npm for managing dependencies

## Getting Started

Follow these instructions to set up and run the Data Science Tutor locally.

### Prerequisites

Ensure you have the following installed:

- [Node.js](https://nodejs.org/) (npm is included)
- [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/)
- [Parcel](https://parceljs.org/) (for bundling assets)

## **Usage**
Type your questions into the input box, and click "Send" to interact with the tutor.
Select a topic from the footer to get information on a specific data science subject.
The tutor will respond with formatted content, providing code examples, visualizations, and step-by-step explanations.

## **Project Structure**
data-science-tutor/
│
├── tutor/
│   ├── static/tutor/
│   │   ├── css/          # CSS files for styling
│   │   ├── js/           # JavaScript files (e.g., script.js, main.js)
│   │   └── images/       # Static images (e.g., tutor image)
│   ├── templates/tutor/
│   │   └── index.html    # Main HTML file for the application
│   ├── views.py          # Django views for rendering templates
│   ├── models.py         # Django models for storing chat sessions/messages
│   └── urls.py           # URL configuration for routing
│
├── package.json          # Frontend dependencies and scripts
├── requirements.txt      # Backend dependencies
└── README.md             # Project documentation

## **Roadmap**
 - Add support for additional programming languages (e.g., R)
 - Integrate visualizations using Plotly or D3.js for a more interactive experience
 - Implement user authentication for personalized learning paths
 - Deploy the application on Heroku or AWS for broader access

## **License**
This project is licensed under the MIT License - see the LICENSE file for details.
