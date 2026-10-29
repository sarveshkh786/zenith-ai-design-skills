"""
Zenith AI Design Skills
Author: Sarvesh Zenith (Sarvesh Khandelwal) - Dayal Infotech Services
"""

from typing import Dict, Any, List

class AgentPersona:
    def __init__(self, name: str, domain: str, role_description: str = ""):
        self.name = name
        self.domain = domain
        self.role_description = role_description or f"Expert AI Agent specializing in {domain}."

class SkillRegistry:
    def __init__(self):
        self.skills: Dict[str, str] = {}

    def register_skill(self, skill_name: str, prompt_template: str):
        self.skills[skill_name] = prompt_template

    def format_prompt(self, persona: AgentPersona, skill_name: str = None) -> str:
        base_prompt = f"System Persona: {persona.name}\nDomain: {persona.domain}\nDescription: {persona.role_description}\n"
        if skill_name and skill_name in self.skills:
            base_prompt += f"\nActive Skill Directive:\n{self.skills[skill_name]}"
        return base_prompt

if __name__ == "__main__":
    registry = SkillRegistry()
    registry.register_skill(
        "structured_json", 
        "Always output strictly valid JSON matching the provided JSON Schema with no conversational preamble."
    )
    architect = AgentPersona(name="Zenith-Architect", domain="AI Systems Architecture & Cloud Security")
    print(registry.format_prompt(architect, "structured_json"))
