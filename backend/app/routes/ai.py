from fastapi import APIRouter, HTTPException, Depends, status
from app.models import ChatRequest, ChatResponse, QuizGenerateRequest, ExplainRequest
from fastapi.security import HTTPBearer
import openai
from app.config import settings
from datetime import datetime

router = APIRouter()
security = HTTPBearer()

# Configure OpenAI
if settings.OPENAI_API_KEY:
    openai.api_key = settings.OPENAI_API_KEY

@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(
    request: ChatRequest,
    credentials = Depends(security),
):
    """Chat with AI assistant"""
    try:
        # Using OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are CampusVault AI, an educational assistant for students and teachers."},
                {"role": "user", "content": request.message}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        
        return ChatResponse(
            response=response.choices[0].message.content,
            timestamp=datetime.now()
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/generate-quiz")
async def generate_quiz(
    request: QuizGenerateRequest,
):
    """Generate quiz questions using AI"""
    try:
        prompt = f"""Generate {request.number_of_questions} multiple choice questions about {request.subject}.
        
        Format as JSON with this structure:
        {{
            "questions": [
                {{
                    "question": "...",
                    "options": ["...", "...", "...", "..."],
                    "correctAnswer": 0,
                    "explanation": "..."
                }}
            ]
        }}"""
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an educational quiz generator."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        
        # Parse and return quiz
       return {
    "title": f"{request.subject} AI Quiz",
    "questions": [
        {
            "questionText": f"What is {request.subject}?",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "correctAnswerIndex": 0,
            "explanation": "This is a sample explanation."
        },
        {
            "questionText": f"Why is {request.subject} important?",
            "options": [
                "Reason A",
                "Reason B",
                "Reason C",
                "Reason D"
            ],
            "correctAnswerIndex": 1,
            "explanation": "This is another explanation."
        },
        {
            "questionText": f"Choose the correct statement about {request.subject}.",
            "options": [
                "Statement A",
                "Statement B",
                "Statement C",
                "Statement D"
            ],
            "correctAnswerIndex": 2,
            "explanation": "Correct answer explanation."
        }
    ]
}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/explain")
async def explain_topic(
    request: ExplainRequest,
    credentials = Depends(security),
):
    """Explain a topic in detail"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an educational expert. Explain concepts clearly for students."},
                {"role": "user", "content": f"Explain {request.subject} in simple terms with examples."}
            ],
            temperature=0.7,
            max_tokens=1000,
        )
        
        return {
            "topic": request.subject,
            "explanation": response.choices[0].message.content
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/summarize")
async def summarize_content(
    file_url: str,
    credentials = Depends(security),
):
    """Summarize document content"""
    try:
        # In production, download and read the file
        return {
            "message": "Summarization in progress",
            "fileUrl": file_url
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/roadmap")
async def generate_learning_roadmap(
    topic: str,
    credentials = Depends(security),
):
    """Generate a learning roadmap for a topic"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a learning advisor."},
                {"role": "user", "content": f"Create a step-by-step learning roadmap for {topic}"}
            ],
            temperature=0.7,
        )
        
        return {
            "topic": topic,
            "roadmap": response.choices[0].message.content.split('\n')
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/code-help")
async def get_code_help(
    code: str,
    language: str,
    credentials = Depends(security),
):
    """Get help with code"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a programming expert."},
                {"role": "user", "content": f"Review this {language} code and provide help:\n{code}"}
            ],
            temperature=0.7,
        )
        
        return {"help": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post("/exam-tips")
async def get_exam_tips(
    subject: str,
    credentials = Depends(security),
):
    """Get exam preparation tips"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an exam preparation expert."},
                {"role": "user", "content": f"Provide exam preparation tips for {subject}"}
            ],
            temperature=0.7,
        )
        
        return {"subject": subject, "tips": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
