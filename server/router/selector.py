def select_model(task_type):
    # اگه task_type برابر "code" بود → مدل deepseek-coder رو برگردون
    if task_type == "code":
        return "deepseek-coder"
    # اگه "fast" بود → llama-3.1-8b برگردون
    elif task_type == "fast":
        return "llama-3.1-8b"
    # اگه "reasoning" بود → gemini-flash
    elif task_type == "reasoning":
        return "gemini-flash"
    # اگه "creative" بود → mixtral
    elif task_type == "creative":
        return "mixtral"
    # در غیر این صورت (else) → یه مدل پیش‌فرض: gemini-flash
    else:
        return "gemini-flash"
