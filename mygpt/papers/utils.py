from gpt.utils import get_completion


def translate(input_text: str, lang: str):
    prompt = f"""You will receive a piece of text wrapped in triple quotes. If the content is in English, please translate it into Chinese, and if the text is in Chinese, please translate it into English. Please be as accurate as possible.

'''
{input_text}
'''
"""
    return get_completion(prompt)

def modify(input_text: str, lang: str):

    prompt = f"""Please follow these steps to modify the content wrapped in tripe quotes.You have to give me the modified content in {lang} without any other content.
1. Please delete the redundant content to make the content more compact;
2. Please add or modify the transitional content between sentences to make the content more smooth;
3. Please identify and correct typos and grammatical errors in the content;
4. If necessary, adjust the order of statements to make the content more logical;
5. Please find out where the content is not clear and use more explicit language to clarify.

'''
{input_text}
'''

"""

    return get_completion(prompt)
