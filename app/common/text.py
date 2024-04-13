class Text: 
    def __init__(self):
        pass 
    
    def prompt_tools(self):
        MLOPS_TOOL = """
        This specialized MLOps tool serves as your expert assistant for managing machine learning operations. 
        It provides support by answering questions and guiding best practices for implementing 
        and scaling ML models efficiently in production environments.
        """
        DATA_ENGINEERING_TOOL = """
        Designed as an expert in data engineering, 
        this tool offers guidance on efficient data management. 
        It answers questions and assists in developing optimized data pipelines, 
        facilitating effective data collection, integration, and processing
        """
        ML_ENGINEERING_TOOL = """
        This tool specializes in machine learning engineering, 
        supporting you from model design to evaluation. 
        It answers questions about algorithm selection, hyperparameter tuning, 
        and more, ensuring the development of efficient and effective ML solutions.
        """
        DATA_SCIENCE_TOOL = """
        Acting as a data science expert, this tool helps you navigate through data analysis, 
        machine learning, and statistical modeling. 
        It responds to inquiries, providing insights to transform raw data into 
        strategic decisions through advanced analysis and visualization techniques.
        """
        return {
            'MLOps Tool': MLOPS_TOOL,
            'Data Engineering Tool': DATA_ENGINEERING_TOOL,
            'ML Engineering Tool': ML_ENGINEERING_TOOL,
            'Data Science Tool': DATA_SCIENCE_TOOL
        }
    
    def prompt_agent():
        AGENT = """
        You are a highly skilled agent tasked with the mission of educating and inspiring others in the field of data. 
        Your objective is to promote the study of data-related subjects, teach essential concepts, and provide answers to pertinent questions. 
        Your arsenal includes specialized tools such as the Data Engineering Tool, Machine Learning Engineering Tool, Data Science Tool, 
        and MLOps Tool, reflecting the areas where you possess the most expertise. You can use emojis and it should be as friendly as possible.
        """
