
# from fastapi import APIRouter
# from transformers import BlenderbotForConditionalGeneration, BlenderbotTokenizer

# # Create a new router
# router = APIRouter()

# # Load the model and tokenizer
# model_name = "facebook/blenderbot-400M-distill"
# model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BlenderbotTokenizer.from_pretrained(model_name)

# def generate_response(user_input):
#     """
#     Generate response for the given user input using the loaded model and tokenizer.

#     Args:
#     - user_input (str): The input provided by the user.

#     Returns:
#     - str: The response generated by the model.
#     """
#     # Generate response
#     input_ids = tokenizer(user_input, return_tensors="pt").input_ids
#     response_ids = model.generate(input_ids)[0]
#     response = tokenizer.decode(response_ids, skip_special_tokens=True)

#     return response

# # Define the route handler for the chatbot endpoint
# @router.get("/chatbot")
# async def chatbot_response(title: str):
#     response = generate_response(title)
#     return {"result": response}
