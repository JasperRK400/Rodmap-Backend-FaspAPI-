def roadmap_prompt(goal, level, months):
    return f"""
Create a learning roadmap.

Goal: {goal}
Level: {level}
Timeline: {months} months

Return JSON with:
title
overview
phases
"""
