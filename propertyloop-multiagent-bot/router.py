def route_input(user_text, has_image=False):
    if has_image:
        return "agent_1"
    
    tenancy_keywords = ["tenant", "landlord", "rent", "deposit", "notice", "eviction"]
    if any(word in user_text.lower() for word in tenancy_keywords):
        return "agent_2"
    
    return "clarify"

