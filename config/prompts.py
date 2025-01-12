eval_math_prompts = """
I will give you two answers of a same math problem. The first one is the groundtruth and the second one is a student's answer.
Groundtruth Answer:
{groundtruth_answer}
Student's Answer:
{generated_answer}
Your duty is to give judgements on whether the student's answer is correct. Note that:
1) If the student's answer is correct, reply ANSWER_CORRECT. If the student's answer is wrong, reply ANSWER_WRONG.
2) If the final answer format of groundtruth answer and generated answer is different(for example, decimal and fractional), you should validate whether they are equal. If they are equal, you should also reply ANSWER_CORRECT.
3) You must include ANSWER_CORRECT or ANSWER_WRONG in your reply.
"""