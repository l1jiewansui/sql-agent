import openai

def generate_sql(table_structure, user_query):
    # 调用OpenAI API进行自然语言处理
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Table structure: {table_structure}\nUser query: {user_query}\nSQL query:",
        max_tokens=150
    )
    sql_query = response.choices[0].text.strip()
    return sql_query
