brainbolt_project/
├── README.md                   # Project documentation
├── backend/                    # Contains all backend logic
│   ├── api/                    # Backend API code for GPT service and document parsing
│   │   ├── __init__.py         # Package initializer for the API
│   │   ├── gpt_service.py      # Module to handle GPT API calls
│   │   └── document_parser.py  # Module to parse user-uploaded documents
│   ├── models/                 # Data models for handling and validating user inputs
│   │   ├── __init__.py         # Package initializer for models
│   │   └── user_inputs.py      # Model for user input (prompt, documents)
│   └── __init__.py             # Package initializer for the backend
├── frontend/                   # Frontend components (HTML, CSS, etc.)
│   ├── templates/              # HTML templates (if using Flask)
│   │   └── index.html          # The main HTML form for user input
│   └── static/                 # Static files (CSS, JS, images)
│       └── css/
│           └── styles.css      # CSS styles for the frontend
├── app.py                      # Main application file for routing and server setup
├── requirements.txt            # Python dependencies
├── tests/                      # Unit and integration tests
│   ├── __init__.py             # Test package initializer
│   ├── test_api.py             # Tests for API endpoints
│   └── test_models.py          # Tests for data models and validation
├── .gitignore                  # Specifies which files to ignore in Git version control
└── .env                        # Environment variables (e.g., API keys)
